import pandas
import time

def create_Tiktok_import_file(date):
    local_time = time.localtime()
    today_date = f"{local_time.tm_mon}-{local_time.tm_mday}-{local_time.tm_year}"

    input_file = rf"Z:\GJH Order\{date}\Tiktok\Tiktok {date}.xlsx"  
    content = pandas.read_excel(input_file)

    #Convert order ID to string
    order_ID_list = content["Order ID"].to_list()
    new_order_ID_list = [str(order) for order in order_ID_list]
    content["Order ID"] = new_order_ID_list

    #Convert Quantity to list
    quantity_list = content["Quantity"].to_list()
    quantity_list = [int(qty) for qty in quantity_list]


    #Convert price and discount amount to float
    price_list = content["SKU Subtotal Before Discount"].to_list()
    new_price_list = []
    for price in price_list:
        new_price_list.append(price.split(" ")[1])

    discount_list = content["SKU Seller Discount"].to_list()
    new_discount_list = []
    for discount in discount_list:
        new_discount_list.append(discount.split(" ")[1])

    #Minus price with discount
    deal_price_list = [float(new_price_list[num]) - float(new_discount_list[num]) for num in range(len(new_price_list))]
    deal_price_list = [deal_price_list[num] / quantity_list[num] for num in range(len(deal_price_list))]

    #Create template
    content["Country"] = "SG"
    content["Remark from buyer"] = ""
    content["Order Complete Time"] = ""
    content["Note"] = ""
    content["Order Paid Time"] = today_date
    content["Deal Price"] = deal_price_list
    content["Discount Amount"] = 0


    new_content = content.rename(columns={"Seller SKU":"SKU Reference No.",
                            "Recipient":"Receiver Name",
                            "Phone #":"Phone Number",
                            "Detail Address":"Delivery Address",
                            "Zipcode":"Zip Code"})

    data = pandas.DataFrame(new_content[["Order ID", "Order Paid Time", "Product Name","SKU Reference No.",
                                    "Deal Price","Quantity" ,"Discount Amount","Receiver Name",
                                    "Phone Number","Delivery Address", "Country", "Zip Code",
                                    "Remark from buyer","Order Complete Time","Note"]])


    data["Customer Code"] = "T066S"
    column_name = ["Customer Code","Order ID", "Order Paid Time", "Product Name",
                "SKU Reference No.", "Deal Price","Quantity" ,"Discount Amount",
                "Receiver Name", "Phone Number","Delivery Address", "Country",
                "Zip Code", "Remark from buyer","Order Complete Time","Note"]
    data = data[column_name]
    data.to_excel(rf"Z:\GJH Order\{date}\BC Import\BC_Import (Tiktok).xlsx", index=False)
