import requests as req
from bs4 import BeautifulSoup
import config
import re
import smtplib as smt

for item in config.items_list:
    response = req.get(item["url"], headers={"Accept-Language": config.lang,
                                             "User-Agent": config.user})

    response_text = response.text

    soup = BeautifulSoup(response_text, "html.parser")
    price = soup.select_one(selector=".a-price .a-offscreen").text[1:].split(".")[0]
    price = int(re.sub(r',+', '', price).strip())
    if price < 35000:
        with smt.SMTP("smtp.gmail.com", port=587) as connection:
            connection.starttls()  # tls = Transfer Layer Security
            connection.login(user=config.my_mail, password=config.password)
            connection.sendmail(from_addr=config.my_mail, to_addrs="saptarshinaruto@gmail.com",
                                msg=f"Subject:'LOW PRICE ALERT'\n\nThe price of {item['Item']} is {price} currently..")
