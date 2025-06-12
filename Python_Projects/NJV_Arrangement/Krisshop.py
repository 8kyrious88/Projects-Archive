import pymupdf, pandas, time, datetime, tkinter.filedialog
import pandas
import time
import datetime

def create_njv_delivery_KS():
    date = datetime.datetime.now()
    date = date.strftime("%d%m")

    local_time = time.localtime()
    today_date = f"{local_time.tm_mon}-{local_time.tm_mday}-{local_time.tm_year}"
    input_file = tkinter.filedialog.askopenfilename()
    with open (input_file, "r") as file:
        doc = pymupdf.open(file)
        orders = [page.get_textpage().extractText() for page in doc]
        
        #Split messy orders string 
        orders = orders[0].split("\n")

        #Get details
        name = orders[orders.index("Ship to") + 1]
        order_number = orders[orders.index("Order number") + 1]
        shipping_address = orders[orders.index("Ship to") + 2]
        contact_number = orders[orders.index("Email to") + 1]
        post_code = orders[orders.index("Ship to") + 3]

        #Create an anchor point to let pandas know how long an excel file is
        #Krisshop PDF only got 1 order, so index only need put 1 element inside
        data = {"Index": [1]}

        #Convert to DataFrame format
        df = pandas.DataFrame(data)

        df["REQUESTED TRACKING NUMBER"] = order_number.removesuffix("-2").removeprefix("PO_00")
        df["NAME"] = name
        df["ADDRESS 1"] = shipping_address
        df["PACKAGE TYPE"] = "Parcel"
        df["ADDRESS 2"] = ""
        df["EMAIL"] = ""
        df["CONTACT"] = contact_number.removeprefix("P: 65 ")
        df["POSTCODE"] = post_code.removeprefix("Singapore ")
        df["DELIVERY DATE"] = today_date
        df["DELIVERY TIME SLOT"] = "15:00-18:00"
        df["SIZE"] = "L"
        df["WEIGHT"] = 15
        df["DELIVERY TYPE"] = "Standard"
        df["SHIPPER ORDER NO"] = "Krisshop"
        df["INSTRUCTIONS"] = ""
        df["WEEKEND DELIVERY"] = "NO"
        df["PARCEL DESCRIPTION"] = "Food Product"
        df["IS DANGEROUS GOOD"] = "NO"
        df["CASH ON DELIVERY"] = 0
        df["INSURED VALUE"] = 0
        df["VOLUME"] = 0
        df["LENGTH"] = 0
        df["WIDTH"] = 0
        df["HEIGHT"] = 0
        
        df.to_csv(r"C:\Users\Ng ChunPing\Desktop\PDF Testing\NJV pickup.csv", index = False)
        

