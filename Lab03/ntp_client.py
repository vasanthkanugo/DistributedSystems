import socket
import time
from ntp_packet import NTPPacket
from ntp import NTP, NTPException
from time import ctime

class NTPStats(NTPPacket):
    """NTP statistics.

    Wrapper for NTPPacket, offering additional statistics like offset and
    delay, and timestamps converted to system time.
    """

    def __init__(self):
        """Constructor."""
        super(NTPStats, self).__init__()
        self.dest_timestamp = 0
        """destination timestamp"""

    @property
    def offset(self):
        """offset"""
        return ((self.recv_timestamp - self.orig_timestamp) +
                (self.tx_timestamp - self.dest_timestamp))/2

    @property
    def delay(self):
        """round-trip delay"""
        return ((self.dest_timestamp - self.orig_timestamp) -
                (self.tx_timestamp - self.recv_timestamp))

    @property
    def tx_time(self):
        """Transmit timestamp in system time."""
        return NTP.ntp_to_system_time(self.tx_timestamp)

    @property
    def recv_time(self):
        """Receive timestamp in system time."""
        return NTP.ntp_to_system_time(self.recv_timestamp)

    @property
    def orig_time(self):
        """Originate timestamp in system time."""
        return NTP.ntp_to_system_time(self.orig_timestamp)

    @property
    def ref_time(self):
        """Reference timestamp in system time."""
        return NTP.ntp_to_system_time(self.ref_timestamp)

    @property
    def dest_time(self):
        """Destination timestamp in system time."""
        return NTP.ntp_to_system_time(self.dest_timestamp)


class NTPClient(object):
    """NTP client session."""

    def __init__(self):
        """Constructor."""
        pass

    def request(self, host, version=2, port="ntp", timeout=5):
        """Query a NTP server.

        Parameters:
        host    -- server name/address
        version -- NTP version to use
        port    -- server port
        timeout -- timeout on socket operations

        Returns:
        NTPStats object
        """
        # lookup server address
        if host == 'localhost' or '127.0.0.1':
            addrinfo = socket.getaddrinfo(host, port)[0]
            family, sockaddr = addrinfo[0], addrinfo[4]
        else:
            family, sockaddr = socket.AF_INET, ('localhost',123)

        # create the socket
        s = socket.socket(family, socket.SOCK_DGRAM)

        try:
            s.settimeout(timeout)

            # create the request packet - mode 3 is client
            query_packet = NTPPacket(
                mode=3,
                version=version,
                tx_timestamp=NTP.system_to_ntp_time(time.time())
            )

            # send the request
            s.sendto(query_packet.to_data(), sockaddr)

            # wait for the response - check the source address
            src_addr = None,
            while src_addr[0] != sockaddr[0]:
                response_packet, src_addr = s.recvfrom(256)

            # build the destination timestamp
            dest_timestamp = NTP.system_to_ntp_time(time.time())
        except socket.timeout:
            raise NTPException("No response received from %s." % host)
        finally:
            s.close()

        # construct corresponding statistics
        stats = NTPStats()
        stats.from_data(response_packet)
        stats.dest_timestamp = dest_timestamp

        return stats

if __name__ == '__main__':
    c = NTPClient()
    response = c.request('127.0.0.1', version=3)
    print(response.offset)
    print(response.version)
    ctime(response.tx_time)
    NTP.leap_to_text(response.leap)
    print(response.root_delay)
    NTP.ref_id_to_text(response.ref_id)
