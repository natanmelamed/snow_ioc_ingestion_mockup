import snow_ioc_ingestion
import uvicorn
from fastapi import FastAPI

app: FastAPI = FastAPI()
base_url: str = "/wolseleydev.service-now.com/api"
app.include_router(snow_ioc_ingestion.router, prefix=base_url)

if __name__ == '__main__':
    uvicorn.run('snow_ioc_ingestion_main:app', host='0.0.0.0', port=80, reload=True)
