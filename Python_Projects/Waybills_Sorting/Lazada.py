from pypdf import PdfReader, PdfWriter
import tkinter.filedialog

def sorting_Lzd_waybills():
    # Extract item descriptions and their corresponding page numbers
    pdf_path = tkinter.filedialog.askopenfilename()
    item_page_map = {}
    with open(pdf_path, "rb") as file:
        reader = PdfReader(file)
        for page_num in range(len(reader.pages)):
            page = reader.pages[page_num]
            text = page.extract_text()
            lines = str(text.split('\n'))
            # Find the occurrence of "name" and consider text after it as the item description
            name_index = lines.find("Qty")
            if name_index != -1:
                item_description = lines[name_index + len("Qty"):].strip()
                item_page_map[item_description] = page_num
    
    # Sort item descriptions and reorder pages accordingly
    sorted_item_descriptions = sorted(item_page_map.keys())
    sorted_pages = [item_page_map[item_description] for item_description in sorted_item_descriptions]
    
    # Create a new PDF with sorted pages
    output_pdf = PdfWriter()
    with open(pdf_path, "rb") as file:
        reader = PdfReader(file)
        for page_num in sorted_pages:
            page = reader.pages[page_num]
            output_pdf.add_page(page)

    # Save the sorted PDF
    with open(pdf_path, "wb") as output_file:
        output_pdf.write(output_file)


