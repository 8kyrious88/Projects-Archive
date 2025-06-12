import pandas

df_1 = pandas.read_excel(r"C:\Users\Ng ChunPing\Desktop\PDF Testing\Shopee Income Statment.xlsx",sheet_name="Income")
df_2 = pandas.read_excel(r"C:\Users\Ng ChunPing\Desktop\PDF Testing\BC Sales Orders.xlsx")

for (index, series) in df_1.iterrows():
    order_ID = series["Order ID"]
    statement_price = series["Product Price"]
    BC_price = float(df_2[df_2["External Document No."] == order_ID]["Amount Shipped Not Invoiced (LCY) Incl. VAT"])
    if statement_price != BC_price:
        print(order_ID, statement_price, BC_price)
    else:
        continue               
