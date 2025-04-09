from fastapi import FastAPI, Request, Depends, HTTPException
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi.security import OAuth2PasswordBearer
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import Optional
import sap_integration
import database
import models

app = FastAPI(title="Dijital Tarım API", description="SAP Entegre Dijital Tarım Çözümü")

# Template ve static dosyalar için yapılandırma
app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

# CORS ayarları (mobil erişim için)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# JWT Authentication
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

# SAP Bağlantısı (entegrasyon yoksa None olacak)
try:
    sap_conn = sap_integration.SAPConnection()
except:
    sap_conn = None
    print("SAP entegrasyonu devre dışı")

@app.on_event("startup")
async def startup():
    await database.init_db()

@app.get("/", response_class=HTMLResponse)
async def root(request: Request):
    try:
        return templates.TemplateResponse("index.html", {"request": request})
    except Exception as e:
        return PlainTextResponse(f"Template error: {str(e)}", status_code=500)

@app.get("/api/fields")
async def get_fields(token: str = Depends(oauth2_scheme)):
    """Tarla bilgilerini getirir"""
    return await database.get_all_fields()

@app.get("/api/weather/{field_id}")
async def get_weather(field_id: int, token: str = Depends(oauth2_scheme)):
    """Tarlaya özel hava durumu bilgisi"""
    field = await database.get_field(field_id)
    if not field:
        raise HTTPException(status_code=404, detail="Tarla bulunamadı")
    # Hava durumu API'sinden veri çekme simülasyonu
    return {
        "field_id": field_id,
        "weather": "Güneşli",
        "temperature": 25,
        "humidity": 60
    }

@app.get("/api/sap/materials")
async def get_sap_materials(token: str = Depends(oauth2_scheme)):
    """SAP malzeme listesini getirir"""
    try:
        materials = sap_conn.get_materials()
        return {"materials": materials}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/api/sap/create_order")
async def create_sap_order(order_data: dict, token: str = Depends(oauth2_scheme)):
    """SAP'de üretim emri oluşturur"""
    try:
        result = sap_conn.create_production_order(order_data)
        return {"status": "success", "order_number": result}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
