from fastapi import HTTPException, Header

def verify_api_key(api_key: str = Header(...)):
    correct_api_key = "softalya_api_key"
    if api_key != correct_api_key:
        raise HTTPException(status_code=403, detail="Invalid API Key")
