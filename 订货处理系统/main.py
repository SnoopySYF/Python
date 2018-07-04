from MySql import(
    getAllCustomer, getAllProduct
) 

results = getAllProduct()
for row in results:
    print(row[0] + " " + row[1] + " " + row[2])