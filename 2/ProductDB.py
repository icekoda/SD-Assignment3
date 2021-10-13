# ProductDB.py

# Persistent storage of products and product info
# Will return a list of productinfo

class ProductDBOut:
   
    def GetProductInfo(UPCCode):
        products = [ 'cups','beer','apples','milk','juice','umbrella','lysol']
        price = [    4.99,   24.99,   1.99,  2.99,   2.50,    9.99,     5.99  ]
        productupc= ['0000', '0001', '0002', '0003', '0004', '0005',  '0006',]
        productinfo = []

        # Checks to see if the input is actually present
        if UPCCode in productupc:
            i = 0
            position = 0
            # Iterates over whole list to find position of UPC
            while i < len(productupc):
                if productupc[i] == UPCCode:
                    position = i
                    i = len(productupc)
                    productinfo = [productupc[position], products[position], price[position]]
                else:
                    i += 1
                    

        else:
            print("Product with UPC Code: ", UPCCode, " does not exist!")
        

        return productinfo
