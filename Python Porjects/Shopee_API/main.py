from Shopee_Orders import Shopee_Orders_Manager
import pypdf, datetime

som = Shopee_Orders_Manager()

order_list = som.get_shipment_list()
print(order_list)
pickup_time_id_list = som.get_shipping_parameter(order_list)
som.ship_orders(order_list,pickup_time_id_list)
tracking_number_list = som.get_tracking_number(order_list)
som.create_waybills(order_list,tracking_number_list)
som.download_waybills(order_list)

today = datetime.datetime.now().strftime("%d%m")
NDD_file = pypdf.PdfWriter()
SPX_file = pypdf.PdfWriter()
with open(r"C:\Users\Ng ChunPing\Desktop\PDF Testing\downloaded_file.pdf","rb") as pdf_file:
    reader = pypdf.PdfReader(pdf_file)
    for page_num in range(len(reader.pages)):
        page = reader.pages[page_num]
        text = page.extract_text()
        lines = text.replace("\n", "").replace(" ","")
        index = lines.find("NextDayDelivery")
        if index == -1:
            SPX_file.add_page(page)
        else:
            NDD_file.add_page(page)

with open (rf"C:\Users\Ng ChunPing\Desktop\PDF Testing\Shopee {today}25 (NDD).pdf", "wb") as file:
    NDD_file.write(file)

with open (rf"C:\Users\Ng ChunPing\Desktop\PDF Testing\Shopee {today}25 (SPX).pdf", "wb") as file:
    SPX_file.write(file)
        