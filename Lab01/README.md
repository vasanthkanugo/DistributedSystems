## Programming Assignment 01
**Goal** : To review client-server programming using TCP/IP (using socket interface)

**Contributors**: @arpita-ambavane(https://github.com/arpita-ambavane) and @vasanthkanugo(https://github.com/vasanthkanugo)

### Interfaces Implemented
- Client Side Seller Interface
  -  Add an item for sale
  -  Update the sale price of an item
  -  Remove an item from sale
  -  Display items currently on sale

- Client Side Buyer Interface
  - Search item for sale
  - Add item to the shopping cart
  - Remove item from the shopping cart 
  - Clear the shopping cart
  - Display the shopping cart

### Current State of the System
- A TCP socket that is multithreaded to accept mulitple connections
- A local data store on the system (Implemented using pickle)
