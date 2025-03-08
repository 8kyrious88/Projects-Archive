import pandas
import time, datetime

date = datetime.datetime.now()
date = date.strftime("%d%m")

def create_Ishop_import_file(date):
    input_file = rf"Z:\GJH Order\{date}\Ishop\Ishop {date}.xlsx"  
    content = pandas.read_excel(input_file)
    local_time = time.localtime()
    today_date = f"{local_time.tm_mon}-{local_time.tm_mday}-{local_time.tm_year}"

    content["Country"] = "SG"
    content["Discount Amount"] = 0
    content["Remark from buyer"] = ""
    content["Order Complete Time"] = ""
    content["Note"] = ""
    content["Order Paid Time"] = today_date

    new_content = content.rename(columns={"Order number":"Order ID",
                            "Details":"Product Name",
                            "SKU Code":"SKU Reference No.",
                            "Customer Name":"Receiver Name",
                            "Contact Number":"Phone Number",
                            "Shipping address street 1":"Delivery Address",
                            "Shipping Address Postcode":"Zip Code",
                            "Unit price":"Deal Price"})

    data = pandas.DataFrame(new_content[["Order ID", "Order Paid Time", "Product Name","SKU Reference No.",
                                    "Deal Price","Quantity" ,"Discount Amount","Receiver Name",
                                    "Phone Number","Delivery Address", "Country", "Zip Code",
                                    "Remark from buyer","Order Complete Time","Note"]])


    data["Customer Code"] = "C060S"
    column_name = ["Customer Code","Order ID", "Order Paid Time", "Product Name",
                "SKU Reference No.", "Deal Price","Quantity" ,"Discount Amount",
                "Receiver Name", "Phone Number","Delivery Address", "Country",
                "Zip Code", "Remark from buyer","Order Complete Time","Note"]
    data = data[column_name]
    data.to_excel(rf"Z:\GJH Order\{date}\BC Import\BC_Import (Ishop).xlsx", index=False)

