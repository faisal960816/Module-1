# take bill amount and calculate 18% GST
bill_amount=float(input("enter the bill amount:"))
GST=float(bill_amount/100)*18
print(f"total GST is:{GST}")
print(f"total bill with 18% gst{bill_amount + GST}")