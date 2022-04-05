## Programming Assignment 02
**Goal** : Use different RPC protocols in the market place applicaiton; RPC Protocols used : gRPC, REST & SOAP

**Contributors**: @arpita-ambavane(https://github.com/arpita-ambavane) and @vasanthkanugo(https://github.com/vasanthkanugo)

### Interfaces Implemented
- Client Side Seller Interface
  -  Create Seller Account
  -  Login Seller
  -  Logout Seller  
  -  Add an item for sale
  -  Update the sale price of an item
  -  Remove an item from sale
  -  Display items currently on sale
  -  Get Seller rating of the given seller

- Client Side Buyer Interface
  -  Create Buyer Account
  -  Login Buyer
  -  Logout Buyer  
  -  Search item for sale
  -  Add item to the shopping cart
  -  Remove item from the shopping cart 
  -  Clear the shopping cart
  -  Display the shopping cart
  -  Make Purchase
  -  Provide Feedback of purchased items
  -  Get Buyer history
  -  Get Seller rating based on the history

### Current State of the System
- Front end for seller and buyer interface works with REST
- Back end call to the database works with gRPC
- Financial Transactions works with SOAP
- A local sqllite database is implemented; schema is present in create_table.py

### RoundTrip Latency Numbers 
| Interface        | Operation              | RTT                   |
|------------------|------------------------|-----------------------|
| Seller Interface | Create Account | 0.03299606323242188 |
| Seller Interface | Login Account | 0.02899606323242188 |
| Seller Interface | Logout Account | 0.020606323242188 |
| Seller Interface | Add item for Sale      | 0.03299606323242188 |
| Seller Interface | Change Sale price      | 0.0305847778320312 |
| Seller Interface | Remove item from Sale  | 0.03027357482910156 |
| Seller Interface | Display items for Sale | 0.0305671977996826172 |
| Seller Interface | Get seller rating | 0.0315671977996826172 |
| Buyer Interface | Create Account | 0.03099606323242188 |
| Buyer Interface | Login Account | 0.02999606323242188 |
| Buyer Interface | Logout Account | 0.02070633231242188 |
| Buyer Interface | Search item            | 0.03030707550048828 |
| Buyer Interface | Add item to Cart       | 0.02881981201171875  |
| Buyer Interface | Remove item from Cart  | 0.0305340576171875    |
| Buyer Interface | Clear Cart             | 0.0274448890686035156 |
| Buyer Interface | Display Cart           | 0.0353330707550048828 |
| Buyer Interface | Make Purchase | 0.02593330707550048828 |
| Buyer Interface | Submit Feedback | 0.03593330707550048828 |
| Buyer Interface | Get Buyer History | 0.030133707550048828 |
| Buyer Interface | Get Sellers ratings | 0.0353070750050048828 |

