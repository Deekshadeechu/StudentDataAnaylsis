import requests
from bs4 import BeautifulSoup

products_to_track = [
    {
        "product_url": "https://www.amazon.in/Samsung-Galaxy-Space-Black-Storage/dp/B07HGJ7WLM/ref=pd_di_sccai_2?pd_rd_w=540cv&pf_rd_p=a477d781-9034-48be-b0b0-a72199c56506&pf_rd_r=KXSS6Y5Z5MH04W8Z9KBE&pd_rd_r=544c3bca-7734-4b35-b501-a298c825c454&pd_rd_wg=X8uw0&pd_rd_i=B07HGN617M&th=1",
        "name": "Samsung M31",
        "target_price": 16000
    },
    {
        "product_url": "https://www.amazon.in/Samsung-Galaxy-Midnight-Blue-Storage/dp/B07HGH88GL/ref=asc_df_B07HGJJ559/?tag=googleshopdes-21&linkCode=df0&hvadid=397083168716&hvpos=&hvnetw=g&hvrand=5876028060363236517&hvpone=&hvptwo=&hvqmt=&hvdev=c&hvdvcmdl=&hvlocint=&hvlocphy=1007772&hvtargid=pla-903950310453&ext_vrnc=hi&th=1",
        "name": "Samsung M2 6GB , 128GB ROM",
        "target_price": 15000
    },
    {
        "product_url": "https://www.amazon.in/Redmi-Note-Pro-Max-128GB/dp/B086993WBD/ref=sr_1_1?dchild=1&keywords=redmi+note+9+pro+max+6gb+128gb+black&qid=1613978011&s=electronics&sr=1-1",
        "name": "Redmi Note 9 Pro",
        "target_price": 16500
    },
    {
        "product_url": "https://www.amazon.in/NOKIA-105-2019-Dual-Black/dp/B07WXW8V4X?ref_=Oct_s9_apbd_orecs_hd_bw_b1W1uk3&pf_rd_r=SQS5B9ZMASA6F0D38WV8&pf_rd_p=ff99c2d8-5928-541a-9526-8dd3871ad289&pf_rd_s=merchandised-search-10&pf_rd_t=BROWSE&pf_rd_i=1389432031",
        "name": "Nokia 105 Dual Sim",
        "target_price": 1000
    },
    {
        "product_url": "https://www.amazon.in/HTC-Desire-12-Cool-Black/dp/B07DPD5FJ4/ref=asc_df_B07DPD5FJ4/?tag=googleshopdes-21&linkCode=df0&hvadid=397009354513&hvpos=&hvnetw=g&hvrand=2709335681046711092&hvpone=&hvptwo=&hvqmt=&hvdev=c&hvdvcmdl=&hvlocint=&hvlocphy=1007772&hvtargid=pla-482281313722&psc=1&ext_vrnc=hi",
        "name": "HTC Desire 12+",
        "target_price": 19000
    },
    {
        "product_url": "https://www.amazon.in/Mystery-Storage-Additional-Exchange-Offers/dp/B08444S68L/ref=gbph_img_s-3_30b3_1b74d144?smid=A14CZOWI0VEHLG&pf_rd_p=5dc0f0a2-b988-4b4e-8227-8b554c0430b3&pf_rd_s=slot-3&pf_rd_t=701&pf_rd_i=gb_main&pf_rd_m=A1VBAL9TL5WCBF&pf_rd_r=F35MGV3988XJF6561KEH&th=1",
        "name": "Oppo A31 6GB , 128GB ROM",
        "target_price": 13000
    }
]

def give_product_price(URL):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.182 Safari/537.36"
    }

    page = requests.get(URL, headers=headers)
    soup = BeautifulSoup(page.content, 'html.parser')

    product_price = soup.find(id="priceblock_dealprice")
    if (product_price == None):
        product_price = soup.find(id="priceblock_ourprice")

    return product_price.getText()
result_file = open('my_result_file.txt','w')

try:
    for every_product in products_to_track:
        product_price_returned = give_product_price(every_product.get("product_url"))
        print(product_price_returned + " - " + every_product.get("name"))

        my_product_price = product_price_returned[2:]
        my_product_price = my_product_price.replace(',', '')
        my_product_price = int(float(my_product_price))

        print(my_product_price)

        if my_product_price < every_product.get("target_price"):
            print("Available at your required price")
            result_file.write(every_product.get(
                "name") + ' - \t' + ' Available at target price ' + 'Current Price - ' + str(my_product_price) + '\n')
        else:
            print("Still at current price")
finally:
    result_file.close()
