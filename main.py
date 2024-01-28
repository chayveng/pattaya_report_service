from typing import List

import requests
from fastapi import FastAPI, Response
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# Apply CORS middleware
app.add_middleware(CORSMiddleware)

@app.get("/")
def read_root():
    return {"message": "Hello, FastAPI"}

@app.get('/switch/{ip}')
async def get_switch_img(ip: str):
    url = f'http://localhost:18889/switch/{ip}'
    temp = requests.get(f'http://localhost:18889/switch/{ip}')
    temp.raise_for_status()
    return temp.json()

@app.get("/api/pty/customer_report/{report_name}")
async def get_monthly_report(report_name: str, ref_code: str, start: str, end: str, file_type: str, user_create: str):
    get_pdf_url = "http://10.4.5.32:18866/report-api/api/report/getreport"
    body = {
        "report_name": report_name,
        "ref_code": ref_code,
        "start": int(start),
        "end": int(end),
        "filetype": file_type,
        "user_create": user_create
    }
    try:
        res = requests.post(get_pdf_url, json=body, stream=True)
        data_bytes: bytes = res.content
        return Response(content=data_bytes, media_type=f"application/{file_type}")

    except requests.RequestException as e:
        return Response(content=f"Request failed: {str(e)}", media_type="text/plain")

@app.get("/api/pty/device_report/{report_name}")
async def get_monthly_report(report_name: str, ref_code: str, start: str, end: str, file_type: str, user_create: str, ip_switch: str, if_index: str=None, step: str=None):
    if_index_lst: List = []
    _step: str = ""
    if if_index is not None:
        if_index_lst = [int(i) for i in if_index.split(",")]
    if step is not None:
        _step = step
    get_pdf_url = "http://10.4.5.32:18866/report-api/api/report/getreport"
    body = {
        "report_name": str(report_name),
        "ref_code": str(ref_code),
        "start": int(start),
        "end": int(end),
        "filetype": str(file_type),
        "user_create": str(user_create),
        "ip_switch": str(ip_switch),
        "if_index": if_index_lst,
        "step": _step
    }
    print(body)

    try:
        res = requests.post(get_pdf_url, json=body, stream=True)
        res.raise_for_status()
        data_bytes: bytes = res.content
        return Response(content=data_bytes, media_type=f"application/{file_type}")

    except requests.RequestException as e:
        return Response(content=f"Request failed: {str(e)}", media_type="text/plain")


# app.add_middleware(
#     CORSMiddleware,
#     allow_origins=["*"],
#     allow_credentials=True,
#     allow_methods=["*"],
#     allow_headers=["*"],
# )