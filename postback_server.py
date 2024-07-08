from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from database import SessionLocal, engine, get_db, Base
from models import Postback
from schemas import Postback as PostbackSchema, PostbackCreate
from typing import List, Dict
import logging
import hashlib
from database import SessionLocal, engine, get_db, Base
from typing import Optional
logging.basicConfig()
logging.getLogger('sqlalchemy.engine').setLevel(logging.INFO)

app = FastAPI()

# Create the database tables
Base.metadata.create_all(bind=engine)

def generate_hash(data: Dict) -> str:
    data_string = str(data)
    return hashlib.sha256(data_string.encode()).hexdigest()

@app.get("/")
async def postback(
    SiteID: Optional[str] = None,
    AD: Optional[str] = None,
    AD_ID: Optional[str] = None,
    ADset: Optional[str] = None,
    Adsetset_ID: Optional[str] = None,
    AndroidDeviceID: Optional[str] = None,
    AppID: Optional[str] = None,
    AppName: Optional[str] = None,
    AppVersion: Optional[str] = None,
    AppsFlyerID: Optional[str] = None,
    AttStatus: Optional[str] = None,
    Att_0_1: Optional[str] = None,
    AttributedTouchType: Optional[str] = None,
    BlockedReason: Optional[str] = None,
    BlockedReasonValue: Optional[str] = None,
    BlockedSubReason: Optional[str] = None,
    BundleId: Optional[str] = None,
    Campaign: Optional[str] = None,
    CampaignID: Optional[str] = None,
    CountryCode: Optional[str] = None,
    CustomeruserID: Optional[str] = None,
    DownloadTime: Optional[str] = None,
    EventTrueRevenue: Optional[str] = None,
    EventTrueRevenueUSD: Optional[str] = None,
    IDFV: Optional[str] = None,
    IOSDeviceID: Optional[str] = None,
    InstallTime: Optional[str] = None,
    isLAT: Optional[str] = None,
    IsPrimaryAttribution: Optional[str] = None,
    isRejected: Optional[str] = None,
    IsRetargeting: Optional[str] = None,
    Language: Optional[str] = None,
    OAID: Optional[str] = None,
    Platform: Optional[str] = None,
    PostbackID: Optional[str] = None,
    RetargetingConversionType: Optional[str] = None,
    SubSiteID: Optional[str] = None,
    ClickID: Optional[str] = None,
    CostCurrency: Optional[str] = None,
    CostModel: Optional[str] = None,
    CostValue: Optional[str] = None,
    db: Session = Depends(get_db)
):
    params = {
        'SiteID': SiteID,
        'AD': AD,
        'AD_ID': AD_ID,
        'ADset': ADset,
        'Adsetset_ID': Adsetset_ID,
        'AndroidDeviceID': AndroidDeviceID,
        'AppID': AppID,
        'AppName': AppName,
        'AppVersion': AppVersion,
        'AppsFlyerID': AppsFlyerID,
        'AttStatus': AttStatus,
        'Att-0-1': Att_0_1,
        'AttributedTouchType': AttributedTouchType,
        'BlockedReason': BlockedReason,
        'BlockedReasonValue': BlockedReasonValue,
        'BlockedSubReason': BlockedSubReason,
        'BundleId': BundleId,
        'Campaign': Campaign,
        'CampaignID': CampaignID,
        'CountryCode': CountryCode,
        'CustomeruserID': CustomeruserID,
        'DownloadTime': DownloadTime,
        'EventTrueRevenue': EventTrueRevenue,
        'EventTrueRevenueUSD': EventTrueRevenueUSD,
        'IDFV': IDFV,
        'IOSDeviceID': IOSDeviceID,
        'InstallTime': InstallTime,
        'isLAT': isLAT,
        'IsPrimaryAttribution': IsPrimaryAttribution,
        'isRejected': isRejected,
        'IsRetargeting': IsRetargeting,
        'Language': Language,
        'OAID': OAID,
        'Platform': Platform,
        'PostbackID': PostbackID,
        'RetargetingConversionType': RetargetingConversionType,
        'SubSiteID': SubSiteID,
        'ClickID': ClickID,
        'CostCurrency': CostCurrency,
        'CostModel': CostModel,
        'CostValue': CostValue
    }
    hash_id = generate_hash(params)
    # db = get_db()
    data = {key: value for key, value in params.items() if value is not None}
    postback_data = Postback(hash_id=hash_id, data=data)
    db.add(postback_data)
    db.commit()
    db.refresh(postback_data)
    return postback_data

@app.get("/postbacks/", response_model=List[PostbackSchema])
def read_postbacks(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    postbacks = db.query(Postback).offset(skip).limit(limit).all()
    return postbacks

if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app, host='0.0.0.0', port=5000)
