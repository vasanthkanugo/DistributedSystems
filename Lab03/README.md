## Programming Assignment 02
**Goal** : Implement NTP protocol on both server and client

**Contributors**: @arpita-ambavane(https://github.com/arpita-ambavane) and @vasanthkanugo(https://github.com/vasanthkanugo)

### Interfaces Implemented
- NTP Client
  - UDP connections are established
  - NTP data format 
- NTP Server

### Current State of the System
- NTP server works   
- NTP Client works
  - Client works with public as well as local/remote server

### How to Test
- Server: ''easy-peasy'', python3 ntp_server.py to run the server
- Client: ''easy-peasy'', add the server ip/host name and port in the c.request() call at line 150,  ntp_client.py and run python3 ntp_client.py
