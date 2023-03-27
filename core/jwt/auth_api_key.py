from config.base import settings

from fastapi.security.api_key import APIKeyHeader
from fastapi import Security, HTTPException
from starlette.status import HTTP_403_FORBIDDEN

api_key_header = APIKeyHeader(name = "access_token", auto_error = False)

def get_api_key(api_key_header : str = Security(api_key_header)):
    print(settings.API_KEY)
    if api_key_header == settings.API_KEY:
        return api_key_header
    else :
        raise HTTPException (
            status_code = HTTP_403_FORBIDDEN,
            detail = {
                "status": "Error",
                "status_code": 403,
                "data": None,
                "error": {
                    "status_code": 403,
                    "status": "Error",
                    "message": "Could not validate API KEY"
                }
            }
        )