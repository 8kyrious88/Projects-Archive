import os, pypdf

# Path to the folder containing your PDF files
folder_path = r'C:\Users\Ng ChunPing\Desktop\PDF Testing'

# Initialize a PdfMerger object
merger = pypdf.PdfWriter()

# Get the list of PDF files in the folder
pdf_files = [f for f in os.listdir(folder_path) if f.endswith('.pdf')]

# Sort the files if necessary (e.g., by name)
pdf_files.sort()

# Merge all PDFs
for pdf in pdf_files:
    pdf_path = os.path.join(folder_path, pdf)
    merger.append(pdf_path)

# Output merged file path
output_path = os.path.join(folder_path, 'merged_output.pdf')

# Write the merged file to disk
with open(output_path, 'wb') as f_out:
    merger.write(f_out)

# Close the merger
merger.close()

print(f"Merged PDF saved to {output_path}")
