import requests

headers = {
    "authority": "konto.onet.pl",
    "method": "POST",
    "path": "/newapi/oauth/email-user",
    "scheme": "https",
    "accept": "application/json, text/plain, */*",
    "accept-encoding": "gzip, deflate, br",
    "accept-language": "ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7",
    "content-length": "1024",
    "content-type": "application/json",
    "cookie": "_ga=GA1.2.779547852.1632044295; ea_uuid=202109191138153517105044; adpconsent=CPMxjJSPMxjJiEYACAENBrCsAP_AAH_AAB5YINNf_X__bX9n-_79__t0eY1f9_r_v-Qzjhfdt-8F2L_W_L0X_2E7NF36pq4KuR4ku3bBIQNtHMnUTUmxaolVrzPsak2Mr6NKJ7LkmnsZe2dYGHtPn91T-ZKZ7_7___f73z___9___9_3____________-_____9____________9_____wQaAJMNS8gC7EscGTaNKoUQIwrCQ6AUAFFAMLRNYAMDgp2VgEeoIWACE1ARgRAgxBRgwCAAQCAJCIgJACwQCIAiAQAAgBUgIQAETAILACwMAgAFANCxAigCECQgyOCo5TAgIkWignsrAEou9jTCEMssAKBR_RUYCJQggWBkJCwcxwBICXCgAAAA.cAAAD_gAAAAA; pubconsent=npa%3D0%26vendorListVersion%3D107%26cmpTid%3D1746213%26publicationVersion%3D467%26customVendorsConsent%3D1; leuconsent=CPMxjJSPMxjJiEYACAENBrCsAP_AAH_AAB5YINNf_X__bX9n-_79__t0eY1f9_r_v-Qzjhfdt-8F2L_W_L0X_2E7NF36pq4KuR4ku3bBIQNtHMnUTUmxaolVrzPsak2Mr6NKJ7LkmnsZe2dYGHtPn91T-ZKZ7_7___f73z___9___9_3____________-_____9____________9_____wQaAJMNS8gC7EscGTaNKoUQIwrCQ6AUAFFAMLRNYAMDgp2VgEeoIWACE1ARgRAgxBRgwCAAQCAJCIgJACwQCIAiAQAAgBUgIQAETAILACwMAgAFANCxAigCECQgyOCo5TAgIkWignsrAEou9jTCEMssAKBR_RUYCJQggWBkJCwcxwBICXCgAAAA.cAAAD_gAAAAA; lpubconsent=npa%3D0%26vendorListVersion%3D107%26cmpTid%3D1746213%26publicationVersion%3D467%26customVendorsConsent%3D1; _gcl_au=1.1.491846471.1632044301; onet_uoi=l%3DLilly_Aubrey938%40*.*%26n%3D233162281%26s%3D0%26k%3D0%26p%3D1%26z%3D0%26a%3D3163ad5360282f899109c36233817c03; acc_segment=95; _gid=GA1.2.1734714077.1633298621; _ga=GA1.3.779547852.1632044295; _gid=GA1.3.1734714077.1633298621; __gfp_64b=H0d8xQv_jFlTYO7HKn.R0gtUpmbd.U_wmWt9kxNcqUb.L7|1633298706; adp_dmp_dls=%7B%22nk%22%3A1635113107289%2C%22sso%22%3A1633903507289%2C%22sympatia%22%3A1633903507289%2C%22geo%22%3A1633903507290%2C%22dmp1px%22%3A1633385107290%7D; _fbp=fb.1.1633298707647.93707038; onet_adb=1633322089609; onet_nsess=cce54897800a40ebae7f77b6906406b127cd044f72924630ad57faa240c941a3; _dc_gtm_UA-21605888-22=1; _gat_UA-21605888-22=1",
    "origin": "https://konto.onet.pl",
    "referer": "https://konto.onet.pl/",
    "sec-ch-ua": 'Chromium";v="94", "Google Chrome";v="94", ";Not A Brand";v="99',
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "Windows",
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "same-origin",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.61 Safari/537.36"
}


agreements = [
  "1",
  "6",
  "21",
  "85"
]
browser_params = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.61 Safari/537.36"
captcha_response = "03AGdBq24BS7mYWZBbH4aaXRAo1jvvP0nzMxjRaA5gUzugov-U16s3gom3HZcdmLVDoznUH-Xz6tsewf6UK23x94SMVBPER5a80iHuMv7Evj0j5dRdDzyoWdE6M8Df-3fu6AotDNOEaM2SQbNWKD5xBENOCSIsmCG_-j0gDPRMyVqHzgcUDVizwfOVshMs7yTY35nbGWQe1-jXomxIkBcwPAF2FjzMV9PH4_0JSAAzSCtzJKWZuu7Tcbp5yay9cvMUpNd9NIRhEPSpnbePPdzQ2P4xTatf7bzIaSZCn9KyY_YcglYqonG0jfQOeO9wxzYkhNhSWB9TfK5Qb1e0rNLT1DffziVlaEgW2MVV_IjDU-dNh-qTCfJ2_Ot5vT9gCUM83GqLTNUm-4ccl8y6l8n7ipTVqM1QigV1k6uhDzXPCmCw7ObzNRGMeiYahcFXbnim1QlLe4OO0wcT"
client_id = "poczta.onet.pl.front.onetapi.pl"
date_of_birth = "1994-04-12"
domain = "vp.pl"
fingerprint =  "54fb99f00b4f8318dd9511bec1622d56"
guardian_email = ""
login = "asdasdasd"
name = "Vaele"
paid = 'false'
password = "asdQ@#ew23"
phone = "+48123123123"
phone_token = 'null'
place = 'null'
postal_code = 'null'
recoveryEmail = ""
save_phone = 'true'
sex = "K"
surname = "SSsdd"

data = f"agreements={agreements}&browser_params={browser_params}&captcha_response={captcha_response}&client_id={client_id}&" \
       f"date_of_birth={date_of_birth}&domain={domain}&fingerprint={fingerprint}&guardian_email={guardian_email}&" \
       f"login={login}&name={name}&paid={paid}&password={password}&phone={phone}&phone_token={phone_token}&" \
       f"&place={place}&postal_code={postal_code}&recoveryEmail={recoveryEmail}&save_phone={save_phone}&sex={sex}&" \
       f"surname={surname}"

response = requests.post('https://konto.onet.pl/newapi/oauth/email-user', headers=headers, data=data)

print(response.text)
print(response.status_code)
auth_cookies = response.cookies.get_dict()
