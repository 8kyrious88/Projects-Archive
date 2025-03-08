import pandas
import time

def create_GJH_Eshop_import_file(date):
    input_file = rf"Z:\GJH Order\{date}\GJH\GJH {date}.xlsx"  
    content = pandas.read_excel(input_file)
    local_time = time.localtime()
    today_date = f"{local_time.tm_mon}-{local_time.tm_mday}-{local_time.tm_year}"

    content["Country"] = "SG"
    content["Discount Amount"] = 0
    content["Remark from buyer"] = ""
    content["Order Complete Time"] = ""
    content["Note"] = ""
    content["Order Paid Time"] = today_date

    new_content = content.rename(columns={"Order Number":"Order ID",
                            "Item Name":"Product Name",
                            "SKU":"SKU Reference No.",
                            "First Name (Billing)":"Receiver Name",
                            "Phone (Billing)":"Phone Number",
                            "Address 1&2 (Billing)":"Delivery Address",
                            "Postcode (Billing)":"Zip Code",
                            "Item Cost": "Deal Price"})

    data = pandas.DataFrame(new_content[["Order ID", "Order Paid Time", "Product Name","SKU Reference No.",
                                    "Deal Price","Quantity" ,"Discount Amount","Receiver Name",
                                    "Phone Number","Delivery Address", "Country", "Zip Code",
                                    "Remark from buyer","Order Complete Time","Note"]])


    data["Customer Code"] = "FBONLINE"
    column_name = ["Customer Code","Order ID", "Order Paid Time", "Product Name",
                "SKU Reference No.", "Deal Price","Quantity" ,"Discount Amount",
                "Receiver Name", "Phone Number","Delivery Address", "Country",
                "Zip Code", "Remark from buyer","Order Complete Time","Note"]
    data = data[column_name]
    data.to_excel(rf"Z:\GJH Order\{date}\BC import\BC_Import(GJH).xlsx",index=False)
