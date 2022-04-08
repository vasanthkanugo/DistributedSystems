import threading
import time
from pysyncobj import SyncObj
from pysyncobj.batteries import ReplDict
from collections import OrderedDict

class raft_consensus(threading.Thread):
    def __init__(self, current_user, other_users):
        threading.Thread.__init__(self)
        self.data_store = ReplDict() # ordered dict
        self.syncObj = SyncObj(current_user, other_users, consumers=[self.data_store])
        self.current_user = current_user
        self.other_users = other_users
        self.post_requests = []
        self.request_dump = OrderedDict()

    def run(self):
        print(f"server is running on {self.current_user} - connected to {self.other_users}")
        while True:
            time.sleep(0.1) # wait every second and look for requests
            if len(self.post_requests) > 0: # if there are requests read the request and replicate
                print(f'{self.current_user} : found data base updates {self.post_requests}')
                for index, request in enumerate(self.post_requests.copy()):
                    self.data_store.set(request['key'], request['value'], sync=True) # Synchronous call to update others
                    del self.post_requests[index]

            if len(self.request_dump.items()) > 0:
                for key, value in self.data_store.items():
                    self.request_dump[key] = value
                    self.data_store.pop(key) # pop the element and get into local queue

    def poll_get(self):
        items = self.request_dump.items()
        self.request_dump = OrderedDict()
        return items

    def push_request(self, request):
        print(f'request: {request}')
        self.post_requests.append(request)

    def get_dictionary(self):
        return self.data_store.items()

if __name__ == '__main__':
    user_list = ['127.0.0.1:8888', '127.0.0.1:8889','127.0.0.1:8899']
    user_objects = []
    for index in range(len(user_list)):
        print(f'starting thread {index}: {user_list[index]}')
        obj = raft_consensus(user_list[index], user_list[:index]+user_list[index+1:])
        obj.start()
        user_objects.append(obj)
    print("Updating the dictionary ")
    for index in range(len(user_objects)):
        request = {'key': index * 2, 'value': index * 200}
        user_objects[index].push_request(request)
        for j_index in range(len(user_objects)):
            print(f'{j_index}: {user_objects[j_index].get_dictionary()}')
        time.sleep(1)
        for j_index in range(len(user_objects)):
            print(f'{j_index}: {user_objects[j_index].get_dictionary()}')\





