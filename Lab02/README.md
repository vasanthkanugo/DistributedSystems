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

### RoundTrip Latency Numbers 
| Interface        | Operation              | RTT                   |
|------------------|------------------------|-----------------------|
| Seller Interface | Add item for Sale      | 0.0027799606323242188 |
| Seller Interface | Change Sale price      | 0.0005540847778320312 |
| Seller Interface | Remove item from Sale  | 0.0006127357482910156 |
| Seller Interface | Display items for Sale | 0.0005671977996826172 |
| Client Interface | Search item            | 0.0003330707550048828 |
| Client Interface | Add item to Cart       | 0.001811981201171875  |
| Client Interface | Remove item from Cart  | 0.0005340576171875    |
| Client Interface | Clear Cart             | 0.0004448890686035156 |
| Client Interface | Display Cart           | 0.0003330707550048828 |

