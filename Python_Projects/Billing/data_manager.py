import pandas

class Data_Manager:

    def __init__(self):
        self.df = pandas.read_excel(r"C:\Users\Ng ChunPing\Desktop\PDF Testing\Billing\BC Inventory Details.xlsx")
        self.df_1 = pandas.read_excel(r"C:\Users\Ng ChunPing\Desktop\PDF Testing\Billing\BC Sales Orders.xlsx")

    def calculate_base_uom_qty(self, sku_code, qty):
        try:
            fb_code = self.df[self.df["Parent Item No."] == sku_code]["No."].to_string(index=False)
            qty_per = int(self.df[self.df["Parent Item No."] == sku_code]["Quantity per"].to_string(index=False))
            base_uom = self.df[self.df["Parent Item No."] == sku_code]["Unit of Measure Code"].to_string(index=False)
        except ValueError:
            print(f"{sku_code} can't be found in BC inventory SKU list")
            return [sku_code,qty,""]
        else:
            qty_in_base_UOM = qty_per * qty
            return [fb_code, qty_in_base_UOM, base_uom]
        
    def check_order_discrepancy(self, BC_record:pandas.DataFrame, Shopee_income_breakdown:pandas.DataFrame):
        lst = []
        for (index, series) in Shopee_income_breakdown.iterrows():
            if series["Order ID"] in BC_record["External Document No."].to_list():
                pass
            else:
                lst.append(series)
        filtered_df = pandas.DataFrame(lst)
        # Use openpyxl engine to avoid overwriting the entire file
        with pandas.ExcelWriter(r"C:\Users\Ng ChunPing\Desktop\PDF Testing\Billing\BC Sales Orders.xlsx", engine='openpyxl', mode='a', if_sheet_exists='replace') as writer:
            # Save new_df to 'Sheet2' (or whichever sheet you want)
            filtered_df.to_excel(writer, sheet_name='Sheet2', index=False)
        
        




