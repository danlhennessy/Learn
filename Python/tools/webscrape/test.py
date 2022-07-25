from bs4 import BeautifulSoup as bs
import requests

url = "https://api.nike.com/cic/browse/v2"

querystring = {"queryid":"products","anonymousId":"A27B29617CE944975AC82C4165D2471D","country":"gb","endpoint":"/product_feed/rollup_threads/v2?filter=marketplace(GB)&filter=language(en-GB)&filter=employeePrice(true)&filter=attributeIds(0f64ecc7-d624-4e91-b171-b83a03dd8550,9b674c8e-25c9-45c3-8635-c284c07d3d17)&anchor=24&consumerChannelId=d9a5bc42-4b9c-4976-858a-f159cf99c647&count=24","language":"en-GB","localizedRangeStr":"{lowestPrice}—{highestPrice}"}

payload = ""
headers = {
    "cookie": "AMCV_F0935E09512D2C270A490D4D%40AdobeOrg=1994364360%7CMCMID%7C92210848905855433162441181068938129045%7CMCAID%7CNONE%7CvVersion%7C3.4.0; sq=3; anonymousId=A27B29617CE944975AC82C4165D2471D; NIKE_COMMERCE_COUNTRY=GB; NIKE_COMMERCE_LANG_LOCALE=en_GB; CONSUMERCHOICE=gb/en_gb; CONSUMERCHOICE_SESSION=t; guidS=9ea53cea-a412-41d1-d507-049a76be46d9; guidU=bed2e1a8-0adb-450f-f480-b69cf0566a31; AnalysisUserId=2.22.228.30.201921658443957277; geoloc=cc=GB,rc=EN,tp=vhigh,tz=GMT,la=50.53,lo=-3.60; bm_sz=5BE546F0F06F28FA9C0D7AC13EEBA844~YAAQPgUXAmFPNiSCAQAANAfSNRB1LmV6VtU1z6pv7mwdp6gxx5qA7H4rLYA1RCF16UdKrGqX4OKGbydihQ1hZx4iyS+AEJeGKlRJBXAp1ASJM2FjI2ZVGIclGrBs9hwjtSoSsn1jzpuzPVXzbKjD5oqAFs5Wa2WAG2nLP3UdBEFrJdzb4YYXGW60rpkuxQyQfFHgXqwRM+bjsdFmxahp39h0yLvBw6YAKD3V3KicbcoxTCTrf2YqQUOsr9V11QQaxMYrkaHoC5xGa4cPYLaTWTqbVlc7fe+Sb1Fy4x/17yZmoGzIagu68V+81sQ3Ae4PA+p1jZvLTPa5YUuKK6KxmrMEbkJlar3kABrsPV5IcK9R8c9VA2IakHVH1CDSjfJz5b/gFLXsfYReZMQtRS2HqnJlrOj4QSRLGDM=~3753525~3223856; AKA_A2=A; feature_enabled__as_nav_rollout=true; audience_segmentation_performed=true; ak_bmsc=3CB058313DFB5259E02F25233B410E64~000000000000000000000000000000~YAAQpsNQaKfiBR+CAQAASgzSNRDKt0AZCwq1bJrmGxk+WQnAkjmp0wAc48QUHPRC7MfdXKQDvjC0eaqpnOh2QMIppdc1kzz/yrFG3HzhEMGuEi4mcMc25l6QcfZJRyJpPh2akvXscD9kbBfuHmhmrzkC8tkgR/6DiDOgA5g8YP3gewk8SfNIPQdIzEeRuNDtey6j5v/qIoVPFwK/rPq0ShmcSnVVXcSA0RaTr5D+hRhqbllsv2LXa5WDfJxXHZLf0xcYMX8gBX6fsbwPLICJ7SY974Z94U0XgGF6wp8HfVaCWogV6UZ2FUp8sXM122oUf7KbWqgbITvCrF2PpwckPx22z/dWkC2n1k79Vd9PqRXwcX2y4mfzzV3tatsP9psoCEwdM/Ti; ppd=pw|nikecom>pw>men_hoodies%20&%20pullovers; bm_mi=256FADA8A56E3E237BAD9009FC3A03E1~YAAQksNQaPWHxiWCAQAAot3TNRDG+uBgbVQ8EEdVHcVXqiw2K+Udgg0rrj3J3jzdrX3F2Rrpe2l6LsoAutxssoRhIK4v8FokTFphKmeqVMDtcVT/RMql6RRyJKcZBnwL4C2NL3ZL2JsyP2mWA5mVImA2P8hB3Jguo7zacUA5nZoTmZLIswgcYnr79jFZtFpFP4ID+M6DnERl/Da7LTExk1H9VTSJ7uDImaHTc0mJ9gVRh5Q4aSDNlUtUDYgJFprAk2g5wqw0Kh0IivxMpxKEkn46tTjOO1DDeCtSC3bZUqFhyYl+vWGf1UPykCdsDif6blKOdsw7pQ==~1; ak_bmsc_nke-2.2-ssn=02AZVu4qud3XoetWi3y95s4Ei0NBm2DHlCUKmhnE5GUGuLZVlqn0Gw0GDaMU0iNLOmE1nQIAE76pCWaGd2nzm3Bqx48Wxjh1K9p4dWAxE7e3B3DPrTyPyhmwur5xeOPsJ2HLvUep1KDoFIUip4qz4dV; ak_bmsc_nke-2.2=02AZVu4qud3XoetWi3y95s4Ei0NBm2DHlCUKmhnE5GUGuLZVlqn0Gw0GDaMU0iNLOmE1nQIAE76pCWaGd2nzm3Bqx48Wxjh1K9p4dWAxE7e3B3DPrTyPyhmwur5xeOPsJ2HLvUep1KDoFIUip4qz4dV; bm_sv=A89A944360D96B06890324C05A02804A~YAAQDMNQaJS5hSCCAQAA/erTNRAPJNwua6G0p11mMs9jfpSxBs6PQSQIysWtIPCTzhOdiZQe6t3ibQQAbjXuDLKQjFywhPtS2jDBFf6AuiNZ65EOBILyIbJUljUSHYGkjoBxyPzzjdKcPOPO+08lkWsuugdpFqkdIRNTlcSvdVL2xjpuy4RjB6im48Nw7nPF7jvGMx1mrHpJWuUQ74rRTNB1M1BjCVySde6AB5J/7TX2/DtPeJSF8mGARIUyvQ==~1; _abck=898BE6C60462794D6EB026A84C1ECF4B~-1~YAAQCAUXAs+g3CuCAQAAOIjUNQgW/RDbJ/F89ogNiT4y1VtK9ZW+MEDDnDVRCfGuZbzX6ZWK82F5SzbNr05onBmH3vVOA6qtsZZrE4GWZQgf9CcysHRoECJ6Kgt5aB93u05VoE2uKrdl6UxXp2W8EY/OpJwa/JCItWyUfGe9NZy7tlkn49PEuke9b4rwQ6ZOYu2zcl86sI1KifwfOkCd9uUFHW8NxpUfp5HZjYYU9kT/qThRBw9Lh0URv8s8H+9qq8HPze0UkIgV8SXhAl7IbJyV41XJgqcq3rkgRYWh9sZDDpwxLCppGgV1HaNxigmZWMtkJMqUpabrPR3KtZOoH47J6S+2AUK7MQl0M7z5XIU1UN7T9ES6ir7eYh6yypYszrVjYLLL4TThtcL0BLqiRUtyltQlnr8CG8KopPiRzk8MzyiH52mRolmDttGr8cbIB5mJXK3vbVwPkGNaBH9uNLWtZrYEs93GCsRidb3dBWQUK0lO668p5jVO2djDZ87WjwPS0U/qgIBkfy/gV+frR0osEu4ivCA=~-1~-1~-1",
    "authority": "api.nike.com",
    "accept": "*/*",
    "accept-language": "en-GB,en-US;q=0.9,en;q=0.8",
    "origin": "https://www.nike.com",
    "referer": "https://www.nike.com/",
    "sec-ch-ua-mobile": "?0",
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "same-site",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36"
}

response = requests.request("GET", url, data=payload, headers=headers, params=querystring)

data = response.json()
for x in range(0,12):
    print(data["data"]["products"]["products"][x]["price"]["currentPrice"])