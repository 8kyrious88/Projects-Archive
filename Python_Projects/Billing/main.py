import pandas
from data_manager import Data_Manager

dm = Data_Manager()

df = pandas.read_excel(r"C:\Users\Ng ChunPing\Desktop\PDF Testing\Billing\SKU and Qty.xlsx")
Shopee_income_breakdown = pandas.read_excel(r"C:\Users\Ng ChunPing\Desktop\PDF Testing\Billing\Shopee Income Statment.xlsx", sheet_name=3)
BC_record = pandas.read_excel(r"C:\Users\Ng ChunPing\Desktop\PDF Testing\Billing\BC Sales Orders.xlsx")

columns_name = ["FB Code", "Qty", "UOM"]
lst = []

calculation_switch = False
fbs_orders_filter = False
price_discrepancy_checking = True


#Calculate the item used by FBS in FB_code format
if calculation_switch:
    for (index, series) in df.iterrows():
        calculation = dm.calculate_base_uom_qty(series["SKU"].upper(), series["Qty"])
        if any(calculation[0] in sublist for sublist in lst):
            for result in lst:
                if calculation[0] == result[0] and calculation[2] == result[2]:
                    result[1] += calculation[1]
        else:
            lst.append(calculation)

    pandas.DataFrame(data=lst, columns=columns_name).to_excel(r"C:\Users\Ng ChunPing\Desktop\PDF Testing\Billing\Calculation Result.xlsx")


#Filter out orders needed reimporting
if fbs_orders_filter:
    dm.check_order_discrepancy(Shopee_income_breakdown=Shopee_income_breakdown, BC_record=BC_record)


#Check price discrepancy
if price_discrepancy_checking:
    for (index, series) in Shopee_income_breakdown.iterrows():
        order_ID = series["Order ID"]
        statement_price = series["Product Price"]
        BC_price = float(BC_record[BC_record["External Document No."] == order_ID]["Amount Shipped Not Invoiced (LCY) Incl. VAT"].iloc[0])
        if statement_price != BC_price:
            print(order_ID, statement_price, BC_price)
        else:
            continue               

