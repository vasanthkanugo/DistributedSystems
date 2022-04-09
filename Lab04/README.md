## Programming Assignment 02
**Goal** : Design and implement a rotating sequencer atomic broadcast protocol

**Contributors**: @arpita-ambavane(https://github.com/arpita-ambavane) and @vasanthkanugo(https://github.com/vasanthkanugo)

### System Design 
The consensus protocols are used to determine message ordering in the system.
The consensus protocol is implemented in 'grpc_s-erver.py' file before the query is committed to the data base
- RAFT implementation 
  - PSyncObj python RAFT implementation is used (https://github.com/bakwc/PySyncObj)
  - PSyncObj.ReplDict was modified to use a ordered dictionary object to maintain a synchronous message queue in the system4
- Rotating Sequencer atomic broadcast implementation
  - synchronous queues of request messages and sequence messages are used across different workers
  - workers: workers poll the synchronous queues
    - broadcaster worker -> worker broadcast messages across requests
    - accept request worker -> worker accept requests and saves them into global queue
    - consensus worker -> handles broadcast of sequence messages and delivery of request messages

### Current State of the System
- Implemented RAFT protocol
- Implemented a rotating sequencer atomic broadcast protocol
- Back end call to the database works with gRPC
- Architecture works over a local system in a kubernetes setup

### Performance Numbers
| Operation                                                                                                                                                                           | Performance Numbers |
|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------|
| Average response time for each client function when all replicas run normally (no failures)                                                                                         |                     |
| Average response time for each client function when one server-side sellers interface replica and one server-side buyers interface to which some of the clients are connected fail. |                     |
| Average response time for each client function when one product database replica (not the leader) fails                                                                             |                     |
| Average response time for each client function when the product database replica acting as leader fails                                                                             |                     |


