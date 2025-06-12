import os, pandas

df = pandas.DataFrame()
folder_path = r'C:\Users\Ng ChunPing\Desktop\PDF Testing\Krisshop'
file_list = [f for f in os.listdir(folder_path) if f.endswith(".xlsx")]
for i in file_list:
    temp_df = pandas.read_excel(rf"{folder_path}\{i}")
    df = pandas.concat([df,temp_df],ignore_index=True)
df.to_excel(r"C:\Users\Ng ChunPing\Desktop\PDF Testing\Krisshop\BC Import(Krisshop).xlsx")