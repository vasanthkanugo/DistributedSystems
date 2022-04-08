import socket, time, threading
from util import Util
request_message_list, sequence_message_list, address_list,  stopFlag = {}, {}, [('127.0.0.1', 8888)], False


class request_message:
    def __init__(self, message_id, member_id, local_seq_number, body):
        self.message_id = message_id # message id
        self.member_id = member_id # sender id or member id; the id of the node
        self.local_seq_number = local_seq_number # local counter of the node
        self.body = body # request body

    def to_string(self):
        return Util.dict_to_json({'message_type':'request',
                                  'message': {'message_id': self.message_id,
                                  'member_id': self.member_id,
                                  'local_seq_number': self.local_seq_number,
                                  'body': self.body}
                                  })


class sequence_message:
    def __init__(self, global_seq_number, message_id, member_id, local_seq_number):
        self.global_seq_number = global_seq_number # global sequence
        self.message_id = message_id # message id to which the sequence number was assigned
        self.member_id = member_id
        self.local_seq_number = local_seq_number

    def to_string(self):
        return Util.dict_to_json({'message_type': 'sequence',
                                  'message': {
                                      'global_seq_number': self.global_seq_number,
                                      'message_id': self.message_id,
                                      'member_id': self.member_id,
                                      'local_seq_number': self.local_seq_number
                                    }
                                  })


class receive_request_thread(threading.Thread):

    def __init__(self, socket, member_id, nodes, broadcaster):
        threading.Thread.__init__(self)
        self.socket = socket
        self.member_id = member_id
        self.nodes = nodes
        self.broadcaster = broadcaster

    def run(self):
        global request_message_list, sequence_message_list, stopFlag
        while True:
            if stopFlag:
                print("receive request thread ended")
                break
            # client, address = self.socket.accept()
            message = self.socket.recv(2048)
            if not message:
                break
            payload = Util.json_to_dic(Util.bytes_to_json(message))
            #print(type(payload))
            if 'message_type' in payload:
                if payload['message_type'] == 'request':
                    message = payload['message']
                    key = str(message['message_id']) + ';'+str(message['member_id'])+';'+str(message['local_seq_number'])
                    request_message_list[key] = message
                else:
                    message = payload['message']
                    key = message['global_seq_number']
                    sequence_message_list[key] = str(message['message_id']) + ';'+str(message['member_id'])+';'+str(message['local_seq_number'])


class consensus_thread(threading.Thread):

    def __init__(self, socket, member_id, nodes, broadcaster):
        threading.Thread.__init__(self)
        self.socket = socket
        self.global_seq_number = 0
        self.member_id = member_id
        self.nodes = nodes
        self.broadcaster = broadcaster


    def run(self):
        global request_message_list, sequence_message_list, stopFlag
        while True:
            #print("checking the lists")
            time.sleep(0.1) # polling the sequence and message_list for consensus
            print(request_message_list, sequence_message_list)
            # if request_message_list.__len__() != self.local_request_message_list.__len__() \
            #         or sequence_message_list.__len__() != self.local_request_message_list.__len__():
            #     print(f'New message received: {request_message_list};{self.local_request_message_list} , ' +
            #           f' {sequence_message_list};{self.local_sequence_message_list}')
            #     self.local_request_message_list, self.local_sequence_message_list = request_message_list.copy(), sequence_message_list.copy()
            if stopFlag:
                print("consensus_thread Ended")
                break

            # consensus logic to push the sequence numbers
            '''
                1> conditions to be checked. if its the turn of the current process -> 
                so global sequence number so far received should be noted {has_seen_max_sequence_number}
                2> check if all the global sequence numbers before the current number are received 
                and its corresponding messages are received {has_received_all_messages_for_sequence}
                3> check if all the messages for the given request message seq number are received 
                and assigned as global seq. number
            '''
            is_your_turn, has_seen_max_sequence_number, has_received_all_messages_for_global_sequence, has_received_all_messages_for_local_sequences = False, False, False, True
            sequence_numbers = list(sequence_message_list.keys()) # all the sequence number received
            if len(sequence_numbers) == 0:
                sequence_numbers = [self.global_seq_number]
            if len(sequence_numbers) >= 0 and max(max(sequence_numbers), self.global_seq_number) % self.nodes == self.member_id:
                print('its your turn')
                is_your_turn = True
            if len(sequence_numbers) != 0 and len(sequence_numbers) >= max(sequence_numbers): # check if all the numbers until k are received
                print(f' the largest sequence number is: {max(sequence_numbers)}')
                has_seen_max_sequence_number = True
            untagged_messages = []
            for request_key in request_message_list.keys():
                if request_key not in sequence_message_list.values():
                    print(f'message: {request_key} needs a global sequence number')
                    untagged_messages.append(request_message_list[request_key])
            print(untagged_messages)
            if len(untagged_messages) == 0 or len(untagged_messages)==1:
                has_received_all_messages_for_global_sequence  = True

            #create a map of all member messages
            member_local_message = {}
            for key, message in request_message_list.items():
                if message['member_id'] in member_local_message:
                    member_local_message[message['member_id']].add((key, message['local_seq_number']))
                else:
                    member_local_message[message['member_id']] = set([(key, message['local_seq_number'])])
            print(member_local_message)
            local_messages = []
            for member, value_set in member_local_message.items():
                max_local_seq_number = max([value for _, value in value_set])
                if len(value_set) <= max_local_seq_number:
                    print(f'message: havent received messages before {max_local_seq_number} for memberid - {member}')
                    local_messages.append((member, max_local_seq_number))

            if len(local_messages) == 0 or len(local_messages) == 1:
                has_received_all_messages_for_local_sequences = True

            print(f' is your turn: {is_your_turn} - has_seen_max_sequence_number:{has_seen_max_sequence_number} - '
                  f'has_received_all_messages_for_global_sequence: {has_received_all_messages_for_global_sequence} - '
                  f'has_received_all_messages_for_local_sequences:{has_received_all_messages_for_local_sequences}')
            if is_your_turn and has_seen_max_sequence_number and has_received_all_messages_for_global_sequence\
                    and has_received_all_messages_for_local_sequences and len(request_message_list)!=0:
                # send sequence message
                max_global_sequence_number = max(sequence_numbers)
                message = local_messages[0]
                message = self.broadcaster.get_sequence_message(max_global_sequence_number + 1, message[1], message[1], message[0])
                self.global_seq_number = max_global_sequence_number + 1
                self.broadcaster.broad_cast_message(message, False)
            # consensus logic to deliver the messages
            '''
                1> if all the messages before the current sequence number is delivered 
                2> also, check if majority of the group members have received the message 
                and corresponding sequence message
            '''

class accept_request:

    def __init__(self, member_id):
        self.member_id = member_id
        self.counter = 0
        self.local_seq_number = 0

    def get_request_message(self, query):
        message = request_message(self.counter, self.member_id, self.local_seq_number, query)
        return message.to_string()

    def get_sequence_message(self, global_seq_number, message_id, local_seq_number, member_id):
        message = sequence_message(global_seq_number, message_id, member_id, local_seq_number)
        return message.to_string()

    def broad_cast_message(self, message, is_request):
        global address_list
        if is_request:
            self.counter += 1
            self.local_seq_number += 1
        # send message to all the resources in the list
        for ip, port in address_list:
            soc = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            soc.connect((ip, port))
            soc.send(Util.dict_to_bytes(message))
            soc.close()
            print(f'{message} sent to {ip}:{port}')








if __name__ == '__main__':
    listenIp = "0.0.0.0"
    listenPort = 8888
    member_id, n_nodes = 0, 5
    broadcaster = accept_request(member_id)
    socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    socket.bind((listenIp, listenPort))
    print("local socket: ", socket.getsockname())
    rrt, ct,  = receive_request_thread(socket, member_id, n_nodes, broadcaster), consensus_thread(socket, member_id, n_nodes, broadcaster)
    rrt.start()
    ct.start()

    while True:
        try:
            time.sleep(0.5)
        except KeyboardInterrupt:
            print("Exiting...")
            stopFlag = True
            rrt.join()
            ct.join()
            # socket.close()
            print("Exited")
            break

