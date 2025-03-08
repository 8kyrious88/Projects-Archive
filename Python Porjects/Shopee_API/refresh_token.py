from Shopee_Orders import Shopee_Orders_Manager

so = Shopee_Orders_Manager()

#Refresh access token everyday before running this script, each access token only valid for 4 hours
so.refresh_access_token()