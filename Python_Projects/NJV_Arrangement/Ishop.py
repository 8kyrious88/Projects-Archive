import pandas, time, tkinter.filedialog
import time

def create_njv_delivery_Ishop():
    input_file = tkinter.filedialog.askopenfilename() 
    content = pandas.read_excel(input_file)
    local_time = time.localtime()
    today_date = f"{local_time.tm_mon}-{local_time.tm_mday + 1}-{local_time.tm_year}"

    content["PACKAGE TYPE"] = "Parcel"
    content["ADDRESS 2"] = ""
    content["DELIVERY TIME SLOT"] = "15:00-18:00"
    content["SIZE"] = "L"
    content["WEIGHT"] = 15
    content["DELIVERY TYPE"] = "Standard"
    content["SHIPPER ORDER NO"] = "Ishop"
    content["INSTRUCTIONS"] = ""
    content["WEEKEND DELIVERY"] = "NO"
    content["PARCEL DESCRIPTION"] = "Food Product"
    content["IS DANGEROUS GOOD"] = "NO"
    content["CASH ON DELIVERY"] = 0
    content["INSURED VALUE"] = 0
    content["VOLUME"] = 0
    content["LENGTH"] = 0
    content["WIDTH"] = 0
    content["HEIGHT"] = 0
    content["DELIVERY DATE"] = today_date

    for num in range(len(content["Order number"])):
        content.loc[num, "Order number"] = content.loc[num, "Order number"].replace("-2225", "").replace("NC250","")

    temp_list = [zipcode for zipcode in content["Shipping Address Postcode"]]
    for num in range(len(temp_list)):
        temp_list[num] = str(temp_list[num])
    content["Shipping Address Postcode"] = temp_list

    new_content = content.rename(columns={"Order number":"REQUESTED TRACKING NUMBER",
                            "Customer Name":"NAME",
                            "Shipping address street 1":"ADDRESS 1",
                            "Email":"EMAIL",
                            "Shipping address phone":"CONTACT",
                            "Shipping Address Postcode":"POSTCODE",})

    data = pandas.DataFrame(new_content[["REQUESTED TRACKING NUMBER","NAME","ADDRESS 1","PACKAGE TYPE",
                                        "ADDRESS 2","EMAIL","CONTACT","POSTCODE","DELIVERY DATE",
                                        "DELIVERY TIME SLOT","SIZE","WEIGHT","DELIVERY TYPE",
                                        "SHIPPER ORDER NO","INSTRUCTIONS","WEEKEND DELIVERY",
                                        "PARCEL DESCRIPTION","IS DANGEROUS GOOD","CASH ON DELIVERY",
                                        "INSURED VALUE","VOLUME","LENGTH","WIDTH","HEIGHT"]])

    data.to_excel(r"C:\Users\Ng ChunPing\Desktop\PDF Testing\NJV_pickup(Ishop).xlsx",index=False)

