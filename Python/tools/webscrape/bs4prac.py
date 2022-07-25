from bs4 import BeautifulSoup as bs
from requests_html import HTMLSession
import requests
import pandas as pd

url = "https://www.accommodationforstudents.com/exeter" # Get Data with requests-html
r = HTMLSession().get(url, headers={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36"})

soup = bs(r.text, 'html.parser')  # Define Parser

lis = soup.find_all('li')  # Parse Text
print(lis[0].text)

image = soup.find('img', {'class': 'hero-location__image-mask-desktop'})  # Parse Image
print(image['src'])

link = soup.find_all('a')  # Parse link
print(link[2]['href'])

# JSON data - use Network tab and insomnia + cURL:

url2 = "https://www.sunglasshut.com/wcs/resources/plp/11352/byCategoryId/3074457345626651837"

querystring = {"isProductNeeded":"true","pageSize":"100","responseFormat":"json","isChanelCategory":"false","currency":"GBP","pageView":"image","viewTaskName":"CategoryDisplayView","beginIndex":"0","categoryId":"3074457345626651837","catalogId":"20603","langId":"-24","storeId":"11352","top":"Y","orderBy":"default","currentPage":"1"}
headers = {
    "cookie": "ak_bmsc=CAF9B311BFC86CB620D1511158021852~000000000000000000000000000000~YAAQD8NQaBkNZiyCAQAAC3EZNRAYfk7ingVqmfHkd/jER+yzIaGuMdKtwwrT9Cv0AjkI4VqlYqu0HtGFNART3ccUooGHPuB5XIvN1mD5p0+2c9oZUl09SgmoP/LWzLGDBk16T0Uy5VEi5MmMIMCiub690cRc7o5qvVVKR1xe+3gzLNjF58EKs0EGtUfIgfCvyNaFTlpor1g1yddIV9xApNH6+9eMPjnUHufKzJUrJQ00BXNqPpo7u1wZaezPgT8hgibm98QeMjv1qqWKCH4cDZdssCN+3UCpwe2nUt2rG88vVllLcHjaFIcDfrgsxFfbOio8udOMnZcT2Fhhd6NUYhMJvCgsLIAhnxytN/1ho5PaFPQ/tDHkn3TSDI3b+7BLfAQzrIKs28TIMG54Cw==; dtCookie=-13^; rxVisitor=1658748237681UES0BUA5MMJSMIV7T9F5JNEBRC46URRK; sgh-desktop-facet-state-search=; tealium_data2track_Tags_AdobeAnalytics_TrafficSourceMid_ThisHit=google.com/; tealium_data_tags_adobeAnalytics_trafficSourceMid_thisSession=google.com/; tealium_data_session_timeStamp=1658748238527; userToken=undefined; TrafficSource_Override=1; AMCVS_125138B3527845350A490D4C^%^40AdobeOrg=1; AMCV_125138B3527845350A490D4C^%^40AdobeOrg=-1303530583^%^7CMCIDTS^%^7C19199^%^7CMCMID^%^7C90164496688389623807519213133154679644^%^7CMCAID^%^7CNONE^%^7CMCOPTOUT-1658755438s^%^7CNONE^%^7CvVersion^%^7C3.3.0; s_cc=true; CONSENTMGR=consent:true^%^7Cts:1658748244561; SGPF=CT-2; aka-cc=GB; aka-ct=NEWTONABBOT; aka-zp=; cookiePolicy=true; rxvt=1658756400286^|1658754600286; _cs_mk=0.0703670546504549_1658754607906; s_sq=^%^5B^%^5BB^%^5D^%^5D; bm_mi=664FDC90EBE7C8FC37FED6A97CB58BAA~YAAQD8NQaLRlciyCAQAAsNF6NRBdr2qkR1FBPx+jUguXyjwPNqYeeZZv8qn4Skc/l1hJW1Rep8AouU0dWFhSUAE1TXhNS1xi6YAyTEwiWt4eX1jdi1IHGYeurNsmKE5ZRDrN9udj9M5G6Z6XxBdXfodSteucwkyX2U1YMWV97r2Cy7lV3KUyl2cqrpvv7Nd5JnlYFRJ9vcSmzoUu5EYgq1SsCH0sec4JnIAurIsi4baLBVQUZmXULabc/qwG0OvMt551z7Sa8Ye4TrgvkWvUn6My2WDxrRBrv6Ghdro7FLTGg+3z3doclw0b2m79LDpHXMAY7mT0by8KxO5v5hGtfpxJkg0=~1; bm_sv=9581140EFB7247BFD102516F31EF8BC3~YAAQD8NQaBdmciyCAQAAbdN6NRD1/ctA3Q0qApvuFGuRw/chEXVuT3CyaC+RsfO7LT9VTuJNDITs6shicku7svEN32tdmYNKRoQub7vvx56GzMJsH8oacB2bc3BoldlO1IGcorcKivp5LSn2+AG2mBpccshOpmnJpjbtjrITmx0JMnoD6tZRH/cJpJbV+AllfGc++O75nFj7GpKPwe3pmh42MSxsOhJjtAEw+YCWr7lHCjioHGwiUWFfFDc6MLGvyfi296Ic~1; dtPC=-13^-13^-13^-0e0; sgh-desktop-facet-state-plp=categoryid:undefined^|gender:true^|brands:partial^|polarized:true^|price:true^|frame-shape:partial^|color:true^|face-shape:false^|fit:false^|materials:false^|lens-treatment:false; tealium_data2track_Tags_AdobeAnalytics_TrafficSourceJid_ThisHit=207255REF; tealium_data_tags_adobeAnalytics_trafficSourceJid_stackingInSession=207251ORG-207252REF-207253REF-207254REF-207255REF; forterToken=b4b6499e07ef4f63bc6de2f2d1eeca7e_1658754619259_1275_UAL9_6; utag_main=v_id:018235197aaf001bacff28acefb20506f001e06700bd0^n:2^e:8^s:0^t:1658756445950^:sunglasshut.com^:2^:1658754601553^%^3Bexp-session^n:3^%^3Bexp-session^:3^%^3Bexp-session",
    "authority": "www.sunglasshut.com",
    "accept": "application/json, text/plain, */*",
    "accept-language": "en-GB,en-US;q=0.9,en;q=0.8",
    "referer": "https://www.sunglasshut.com/uk/mens-sunglasses",
    "sec-ch-ua": "^\^.Not/A",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "^\^Windows^^",
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "same-origin",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36"
}

response = requests.request("GET", url2, headers=headers, params=querystring)
data = response.json()

res = [] # Pooling product data into python list from JSON response
for p in data['plpView']['products']['products']['product']:
    res.append(p)
    
df = pd.json_normalize(res) # Pandas DF from res list
# df.to_csv('firstresults.csv')   Create CSV file from pandas DF
print(df)