# CashRegister.py

from Display import *
from TicketPrinter import *
from Keyboard import *
from Scanner import *
from ProductDB import *

class CashRegisterOut:
    def setCurrentProductUPC(UPCCode):
        return UPCCode

    #def getCurrentProductInfo:

def choiceout(choice):
    if choice == 1:
        scanned = int(input("Please choose what you want to scan: \n",
                           " 0: 0000 \n",
                           " 1: 0001 \n", 
                           " 2: 0002 \n", 
                           " 3: 0003 \n",
                           " 4: 0004 \n", 
                           " 5: 0005 \n",
                           " 6: 0006 \n"))
        return scanned
    else:
        out = 2

CashRegisterOut.setCurrentProductUPC(choiceout(int(input("1. Scan \n OR \n2. Keyboard \n"))))

#DisplayPrint.displayText("Test") ##
#TicketPrint.displayText("test") ##
#keyinput = KeyboardOut.setUPCCode(input("Keyboard Input (12): "))
#print(keyinput)

#scannd = ScannerOut.scannedUPCCode(input("Scanner: "))
#print(scannd)

#ProductDBOut.GetProductInfo(keyinput)

