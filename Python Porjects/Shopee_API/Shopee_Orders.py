import dotenv, os, time, hmac, hashlib, requests, pypdf

dotenv.load_dotenv()

class Shopee_Orders_Manager:
    def __init__(self) -> None:
        self.host = "https://partner.shopeemobile.com"
        self.SHOPEE_ID = int(os.getenv("SHOPEE_ID"))
        self.LIVE_PARTNER_ID = int(os.getenv("LIVE_PARTNER_ID"))
        self.LIVE_PARTNER_KEY = os.getenv("LIVE_PARTNER_KEY")
        self.timestamp = int(time.time())
        self.CODE = os.getenv("CODE")
        self.access_token = os.getenv("ACCESS_TOKEN")
        self.refresh_token = os.getenv("REFRESH_TOKEN")
    
    def partial_sign(self, path):
        tmp_base_string = "%s%s%s" % (self.LIVE_PARTNER_ID, path, self.timestamp)
        base_string = tmp_base_string.encode()
        partner_key = self.LIVE_PARTNER_KEY.encode()
        sign = hmac.new(partner_key, base_string, hashlib.sha256).hexdigest()
        return sign
    
    def full_sign(self, path):
        tmp_base_string = "%s%s%s%s%s" % (self.LIVE_PARTNER_ID, path, self.timestamp,self.access_token,self.SHOPEE_ID)
        base_string = tmp_base_string.encode()
        partner_key = self.LIVE_PARTNER_KEY.encode()
        sign = hmac.new(partner_key, base_string, hashlib.sha256).hexdigest()
        return sign

    def get_token(self):
        path = "/api/v2/auth/token/get"
        sign = self.partial_sign(path)
        header = {"Content-Type": "application/json"}
        body = {"code": self.CODE, "shop_id": self.SHOPEE_ID, "partner_id": self.LIVE_PARTNER_ID}
        URL = self.host + path + "?partner_id=%s&timestamp=%s&sign=%s" % (self.LIVE_PARTNER_ID, self.timestamp, sign)
        response = requests.post(url=URL,json=body,headers=header)
        print(response.text)

    def refresh_access_token(self):
        path = "/api/v2/auth/access_token/get"
        sign = self.partial_sign(path)
        URL = self.host + path
        header = {"Content-Type": "application/json"}
        body = {
            "shop_id": self.SHOPEE_ID, 
            "refresh_token": self.refresh_token,
            "partner_id":self.LIVE_PARTNER_ID
        }
        parameters = {
            "partner_id":self.LIVE_PARTNER_ID,
            "timestamp":self.timestamp,
            "sign":sign
        }
        response = requests.post(url=URL,params=parameters,headers=header,json=body)
        result = response.json()
        new_access_token = result["access_token"]
        new_refresh_token = result["refresh_token"]
        env_file = r"C:\Users\Ng ChunPing\.vscode\python\Workspace\Shopee_API\.env"
        with open(env_file, "r") as file:
            lines = file.readlines()
        with open(env_file, "w") as file:
            for line in lines:
                if line.startswith("ACCESS_TOKEN ="):
                    file.write(f'ACCESS_TOKEN = "{new_access_token}"\n')
                elif line.startswith("REFRESH_TOKEN ="):
                    file.write(f'REFRESH_TOKEN = "{new_refresh_token}"\n')
                else:
                    file.write(line)
        self.access_token = os.getenv("ACCESS_TOKEN")
        self.refresh_token = os.getenv("REFRESH_TOKEN")
        print("Access token has been refreshed")
        
    def get_shipment_list(self):
        path = "/api/v2/order/get_shipment_list"
        sign = self.full_sign(path)
        URL = self.host + path
        parameters = {
            "partner_id":self.LIVE_PARTNER_ID,
            "timestamp":self.timestamp,
            "access_token":self.access_token,
            "shop_id":self.SHOPEE_ID,
            "sign":sign,
            "page_size":100
        }
        response = requests.get(url=URL, params=parameters)
        result = response.json()["response"]["order_list"]
        order_list = [order["order_sn"] for order in result]
        return order_list

    def get_shipping_parameter(self, order_list:list):
        path = "/api/v2/logistics/get_shipping_parameter"
        sign = self.full_sign(path)
        URL = self.host + path
        pickup_time_id_list = []
        print("Getting pickup time id")
        for order_number in order_list:
            parameters = {
                "partner_id":self.LIVE_PARTNER_ID,
                "timestamp":self.timestamp,
                "access_token":self.access_token,
                "shop_id":self.SHOPEE_ID,
                "sign":sign,
                "order_sn":order_number
            }
            response = requests.get(url=URL, params=parameters)
            result = response.json()["response"]["pickup"]["address_list"][0]["time_slot_list"][0]["pickup_time_id"]
            pickup_time_id_list.append(result)
        return pickup_time_id_list

    def ship_orders(self, order_list, pickup_time_id_list):
        path = "/api/v2/logistics/ship_order"
        sign = self.full_sign(path)
        URL = self.host + path
        body = {
            "partner_id":self.LIVE_PARTNER_ID,
            "timestamp":self.timestamp,
            "access_token":self.access_token,
            "shop_id":self.SHOPEE_ID,
            "sign":sign,        
            }
        
        print("Processing Orders")
        for num in range(len(order_list)):
            data = {
                "order_sn":order_list[num],
                "pickup": {
                    "address_id": int(4713173),
                    "pickup_time_id":pickup_time_id_list[num],
                    }
            }
            header = {"Content-Type": "application/json"}

            response = requests.post(url=URL,headers=header,params=body, json=data)
            response.raise_for_status()

    def get_tracking_number(self, order_list:list):
        path = "/api/v2/logistics/get_tracking_number"
        sign = self.full_sign(path)
        URL = self.host + path
        tracking_number_list = []
        for order_number in order_list:
            parameters = {
                "partner_id":self.LIVE_PARTNER_ID,
                "timestamp":self.timestamp,
                "access_token":self.access_token,
                "shop_id":self.SHOPEE_ID,
                "sign":sign,
                "order_sn":order_number
            }
            response = requests.get(url=URL, params=parameters)
            result = response.json()["response"]["tracking_number"]
            tracking_number_list.append(result)
        return tracking_number_list

    def create_waybills(self, order_list, tracking_number_list):
        path = "/api/v2/logistics/create_shipping_document"
        sign = self.full_sign(path)
        URL = self.host + path
        body = {
            "partner_id":self.LIVE_PARTNER_ID,
            "timestamp":self.timestamp,
            "access_token":self.access_token,
            "shop_id":self.SHOPEE_ID,
            "sign":sign,        
            }
        print("Creating Waybills")
        for num in range(len(order_list)):
            data = {
                "order_list":[{"order_sn":order_list[num], "tracking_number":tracking_number_list[num]}]
            }
            header = {"Content-Type": "application/json"}
            response = requests.post(url=URL,headers=header,params=body, json=data)
            print("Status Code:", response.status_code)
            

    def download_waybills(self, order_list):
        path = "/api/v2/logistics/download_shipping_document"
        sign = self.full_sign(path)
        URL = self.host + path
        body = {
            "partner_id":self.LIVE_PARTNER_ID,
            "timestamp":self.timestamp,
            "access_token":self.access_token,
            "shop_id":self.SHOPEE_ID,
            "sign":sign,        
            }
        header = {"Content-Type": "application/json"}
        pdf_writer = pypdf.PdfWriter()
        print("Downloading waybills")
        for order_number in order_list:
            data = {"order_list":[{"order_sn":order_number}]}
            response = requests.post(url=URL,headers=header,params=body, json=data)
            response.raise_for_status()
            print("Status Code:", response.status_code)
            print("Content-Type:", response.headers.get("Content-Type", "Unknown"))
            with open(r"C:\Users\Ng ChunPing\Desktop\PDF Testing\downloaded_file.pdf", "wb") as pdf_file:
                pdf_file.write(response.content)
            with open(r"C:\Users\Ng ChunPing\Desktop\PDF Testing\downloaded_file.pdf", "rb") as pdf_file:
                current_page = pypdf.PdfReader(pdf_file).pages[0]
                pdf_writer.add_page(current_page)
        with open(r"C:\Users\Ng ChunPing\Desktop\PDF Testing\downloaded_file.pdf", "wb") as pdf_file:
            pdf_writer.write(pdf_file)
