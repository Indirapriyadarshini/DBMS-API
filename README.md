# DBMS-API

ER Diagram has been added as jpg file.

# ERD.jpg


-> Each Product Refers to Stock. [Product: Stock is  1 : Many Relationship]
Rule0:     RX = Product ,  RY = Stock ;  PK(RX) = ProdId,  FK(RY) = prodId
Rule2:  (one - Many )
RAB(prodId, pname, price, quantity)
RB(depId, Prodid, quantity )
PK(RA) is PK(RB)[NULL] is unchanged
FK(Stock) = PK(Depot) = prodId
 
->Each Depot Refers to Stock. [Depot: Stock is 1 : Many Relationship]
Rule0:     RX = Depot ,  RY = Stock ;  PK(RX) = depId,  FK(RY) = depId 
Rule2:  (one - Many )
RAB(depId, addr, volume, quantity)
RB(depId, Prodid, quantity )
PK(RA) is PK(RB)[NULL] is unchanged
FK(Stock) = PK(Depot) = depId
