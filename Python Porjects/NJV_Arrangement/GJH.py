import pandas, time, tkinter.filedialog


def create_njv_delivery_GJH():
    input_file = tkinter.filedialog.askopenfilename()
    content = pandas.read_excel(input_file)
    local_time = time.localtime()
    today_date = f"{local_time.tm_mon}-{local_time.tm_mday + 2}-{local_time.tm_year}"

    content["PACKAGE TYPE"] = "Parcel"
    content["ADDRESS 2"] = ""
    content["DELIVERY TIME SLOT"] = "15:00-18:00"
    content["SIZE"] = "L"
    content["WEIGHT"] = 15
    content["DELIVERY TYPE"] = "Standard"
    content["SHIPPER ORDER NO"] = "GJH"
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

    for num in range(len(content["Order Number"])):
        content.loc[num, "Order Number"] = content.loc[num, "Order Number"].replace("-", "").replace("00","0")



    new_content = content.rename(columns={"Order Number":"REQUESTED TRACKING NUMBER",
                            "First Name (Shipping)":"NAME",
                            "Address 1&2 (Shipping)":"ADDRESS 1",
                            "Email (Shipping)":"EMAIL",
                            "Phone (Shipping)":"CONTACT",
                            "Postcode (Shipping)":"POSTCODE",})

    data = pandas.DataFrame(new_content[["REQUESTED TRACKING NUMBER","NAME","ADDRESS 1","PACKAGE TYPE",
                                        "ADDRESS 2","EMAIL","CONTACT","POSTCODE","DELIVERY DATE",
                                        "DELIVERY TIME SLOT","SIZE","WEIGHT","DELIVERY TYPE",
                                        "SHIPPER ORDER NO","INSTRUCTIONS","WEEKEND DELIVERY",
                                        "PARCEL DESCRIPTION","IS DANGEROUS GOOD","CASH ON DELIVERY",
                                        "INSURED VALUE","VOLUME","LENGTH","WIDTH","HEIGHT"]])

    data.to_excel(r"C:\Users\Ng ChunPing\Desktop\PDF Testing\NJV_pickup(GJH).xlsx",index=False)

