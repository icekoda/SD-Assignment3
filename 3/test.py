# CashRegister.py

from Display import *
from TicketPrinter import *
from Keyboard import *
from Scanner import *
from ProductDB import *

class CashRegisterOut:
    def setCurrentProductUPC(UPCCode):
        return UPCCode

    def getCurrentProductInfo(UPCCode):
        productinfo = ProductDBOut.GetProductInfo(UPCCode)

        # Outputs to Display
        DisplayPrint.displayText(productinfo)

        #Prints Ticket
        TicketPrint.displayText(productinfo)


print("Valid UPCs range from 0000 - 0006")
keyboardin = input("Keyboard - Please type UPC (XXXX): \n")
scannerin = input("Keyboard - Please type Scanned UPC (XXXX): \n")

keyboard = KeyboardOut.setUPCCode(keyboardin)
scanner = ScannerOut.scannedUPCCode(scannerin)


keyboardUPC = CashRegisterOut.setCurrentProductUPC(keyboard)
scannerUPC = CashRegisterOut.setCurrentProductUPC(scanner)

#Display
print("UPC: ", keyboardUPC)
CashRegisterOut.getCurrentProductInfo(keyboardUPC)
print("\n")

#Ticket
print("UPC: ", scannerUPC)
CashRegisterOut.getCurrentProductInfo(scannerUPC)


#DisplayPrint.displayText("Test") ##
#TicketPrint.displayText("test") ##
#keyinput = KeyboardOut.setUPCCode(input("Keyboard Input (12): "))
#print(keyinput)

#scannd = ScannerOut.scannedUPCCode(input("Scanner: "))
#print(scannd)

#ProductDBOut.GetProductInfo(keyinput)

