import datetime
from Shopee import create_Shopee_import_file_pm

today = datetime.datetime.now().strftime("%d%m") + "25"


try:
    create_Shopee_import_file_pm(today)
except FileNotFoundError:
    print("No Shopee (pm) orders list found")
