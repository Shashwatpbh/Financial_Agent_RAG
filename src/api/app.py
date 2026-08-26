from fastapi import FastAPI
from config.setting import get_settings

def create_app()-> FastAPI:
    setting = get_settings()
    app =  FastAPI(
        title =setting.api_service_title,    
        version=setting.api_version

    )
    @app.get("/health")
    async def health_check():
        return {"status":"healthy"} 

    @app.post("/chat")
    async def chat_endpoint():
        return{"message" : "chat endpoint"}

    return app 

