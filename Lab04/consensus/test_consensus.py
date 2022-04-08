import atomic_broadcast

ar = atomic_broadcast.accept_request(0)
request = ar.get_request_message('hello word')
ar.broad_cast_message(request, True)

request = ar.get_request_message('hello word 2')
ar.broad_cast_message(request, True)

# request = ar.get_sequence_message(1, 1, 1, 1)
# ar.broad_cast_message(request, False)
