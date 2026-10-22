from fastapi import FastAPI
from config.settings import get_settings

def create_app()-> FastAPI:
    setting = get_settings()
    app =  FastAPI(
        title =setting.api_service_title,    
        version=setting.api_version

    )
    @app.get("/health")
    async def health_check():
        return {"status":"healthy shashwat"} 

    @app.post("/chat")
    async def chat_endpoint():
        return{"message" : "chat endpoint ending of the AI - ULTRON"}
    

    return app

