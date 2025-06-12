import pandas
import time
import tkinter.filedialog

def create_Qoo10_import_file(date):
    input_file = rf"Z:\GJH Order\{date}\Qoo10\Qoo10 {date}.xlsx"  
    content = pandas.read_excel(input_file)

    local_time = time.localtime()
    today_date = f"{local_time.tm_mon}-{local_time.tm_mday}-{local_time.tm_year}"

    content["Deal Price"] = content["Payment"] / content["Qty."]
    content["Country"] = "SG"
    content["Discount Amount"] = 0
    content["Remark from buyer"] = ""
    content["Order Complete Time"] = ""
    content["Note"] = ""
    content["Order Paid Time"] = today_date

    new_content = content.rename(columns={"Order no.":"Order ID",
                            "Item":"Product Name",
                            "Seller code":"SKU Reference No.",
                            "Qty.":"Quantity",
                            "Customer":"Receiver Name",
                            "Customer mobile phone number":"Phone Number",
                            "Address":"Delivery Address",
                            "Postal code":"Zip Code"})

    data = pandas.DataFrame(new_content[["Order ID", "Order Paid Time", "Product Name","SKU Reference No.",
                                    "Deal Price","Quantity" ,"Discount Amount","Receiver Name",
                                    "Phone Number","Delivery Address", "Country", "Zip Code",
                                    "Remark from buyer","Order Complete Time","Note"]])


    data["Customer Code"] = "G035S"
    directory = tkinter.filedialog.askdirectory()
    data.to_excel(rf"Z:\GJH Order\{date}\BC import\BC_Import(Qoo10).xlsx")

