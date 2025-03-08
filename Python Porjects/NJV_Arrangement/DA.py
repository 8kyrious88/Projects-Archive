import pymupdf, pandas, time, tkinter.filedialog

def create_njv_delivery_DA():
    local_time = time.localtime()
    today_date = f"{local_time.tm_mon}-{local_time.tm_mday}-{local_time.tm_year}"
    input_file = tkinter.filedialog.askopenfilename()
    doc = pymupdf.open(input_file)
    for page_num in range(doc.page_count):
        page = doc.load_page(page_num).get_textpage().extractText()
        order = page.replace("\n","")
    name = order[order.index("Customer InformationName") + 24:order.index("Contact")]
    order_number = "Refer to email delivery ID"
    shipping_address = order[order.index("Address") + 7:order.index(", SG")]
    contact_number = order[order.index("Contact") + 10:order.index("DOB")]
    email = order[order.index("Email") + 5:order.index("Description")]
    post_code = order[order.index("SG") + 3:order.index("Email")]

    data = {"Index": [1]}

    #Convert to DataFrame format
    df = pandas.DataFrame(data)

    df["REQUESTED TRACKING NUMBER"] = order_number
    df["NAME"] = name
    df["ADDRESS 1"] = shipping_address
    df["PACKAGE TYPE"] = "Parcel"
    df["ADDRESS 2"] = ""
    df["EMAIL"] = email
    df["CONTACT"] = contact_number
    df["POSTCODE"] = post_code
    df["DELIVERY DATE"] = today_date
    df["DELIVERY TIME SLOT"] = "15:00-18:00"
    df["SIZE"] = "L"
    df["WEIGHT"] = 15
    df["DELIVERY TYPE"] = "Standard"
    df["SHIPPER ORDER NO"] = "Doctor Anywhere"
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

    df.to_csv(r"C:\Users\Ng ChunPing\Desktop\PDF Testing\NJV pickup(DA).csv", index = False)
