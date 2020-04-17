#!/usr/bin/env python
import requests
import os

URL = "https://requests.readthedocs.io/en/master/#"

try:
    #   response = requests.HTTP-VERB(URL, <many many options here as needed>)
    response = requests.get(URL)
except requests.HTTPError as err:
    print(err)
else:
    if response.status_code == requests.codes.OK:  # 200
        # print(response.content) # bytes not str
        content = response.content.decode()  # convert bytes to str
        print(content)
        # could search with BeautifulSoup or just REs
        for name, value in response.headers.items():
            print(name, "==>", value)

PDF_URL = "https://www.bell.ca/Styles/common/all_languages/all_regions/pdfs/Bell_Terms_of_Service.pdf"

PDF_LOCAL_NAME = os.path.basename(PDF_URL)

try:
    #   response = requests.HTTP-VERB(URL, <many many options here as needed>)
    response = requests.get(PDF_URL, timeout=(10, 30))
except requests.HTTPError as err:
    print(err)
else:
    if response.status_code == requests.codes.OK:  # 200
        with open(PDF_LOCAL_NAME, "wb") as file_out:
            file_out.write(response.content)



