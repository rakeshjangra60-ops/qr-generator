from fastapi import FastAPI, Query
from fastapi.responses import StreamingResponse
import pyqrcode
import io

app = FastAPI()

@app.get("/qr")
def generate_qr(pa: str = Query(...), am: str = Query(...), tn: str = Query(...)):
    upi_url = f"upi://pay?pa={pa}&pn=YourName&am={am}&cu=INR&tn={tn}"
    qr = pyqrcode.create(upi_url)
    buffer = io.BytesIO()
    qr.png(buffer, scale=6)
    buffer.seek(0)
    return StreamingResponse(buffer, media_type="image/png")
