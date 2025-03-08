import datetime, pandas, os
from Amazon import create_Amazon_import_file
from Fair_Price import create_Fairprice_import_file
from GJH_Eshop import create_GJH_Eshop_import_file
from Ishop import create_Ishop_import_file
from Lzd import create_Lzd_import_file, create_Lzd_import_file_pm
from Shopee import create_Shopee_import_file, create_Shopee_import_file_pm
from Tiktok import create_Tiktok_import_file



today = datetime.datetime.now().strftime("%d%m") + "25"

try:
    create_Amazon_import_file(today)
except FileNotFoundError:
    print("No Amazon orders list found")

try:
    create_Fairprice_import_file(today)
except FileNotFoundError:
    print("No Fair Price orders list found")

try:
    create_GJH_Eshop_import_file(today)
except FileNotFoundError:
    print("No GJH Eshop orders list found")

try:
    create_Ishop_import_file(today)
except FileNotFoundError:
    print("No Ishop orders list found")

try:
    create_Lzd_import_file(today)
except FileNotFoundError:
    print("No Lzd orders list found")

try:
    create_Lzd_import_file_pm(today)
except FileNotFoundError:
    print("No Lzd pm orders list found")

try:
    create_Shopee_import_file(today)
except FileNotFoundError:
    print("No Shopee orders list found")

try:
    create_Shopee_import_file_pm(today)
except FileNotFoundError:
    print("No Shopee (pm) orders list found")

try:
    create_Tiktok_import_file(today)
except FileNotFoundError:
    print("No Tiktok orders list found")

df = pandas.DataFrame()
folder_path = rf'Z:\GJH Order\{today}\BC Import'
file_list = [f for f in os.listdir(folder_path) if f.endswith(".xlsx")]

if file_list == []:
    print("No files in BC Import")
else:
    for i in file_list:
        temp_df = pandas.read_excel(rf"{folder_path}\{i}")
        df = pandas.concat([df,temp_df],ignore_index=True)
    df.to_excel(rf"Z:\GJH Order\{today}\BC Import\BC Import (Combined).xlsx",index=False)