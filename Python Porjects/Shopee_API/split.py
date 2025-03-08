import pypdf
import datetime

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

with open (rf"C:\Users\Ng ChunPing\Desktop\PDF Testing\Shopee {today}24 (NDD).pdf", "wb") as file:
    NDD_file.write(file)

with open (rf"C:\Users\Ng ChunPing\Desktop\PDF Testing\Shopee {today}24 (SPX).pdf", "wb") as file:
    SPX_file.write(file)