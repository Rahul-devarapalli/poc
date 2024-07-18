from fastapi import FastAPI, HTTPException
from fastapi.responses import Response
from pydantic import BaseModel
import yaml
from typing import Any, Dict

app = FastAPI()

YAML_FILE_PATH = 'data/data.yaml'

class DataModel(BaseModel):
    data: Dict[str, Any]

@app.get("/get-yaml", response_class=Response, responses={200: {"content": {"application/x-yaml": {}}}})
async def get_yaml():
    try:
        with open(YAML_FILE_PATH, 'r') as file:
            yaml_data = file.read()
        return Response(content=yaml_data, media_type="application/x-yaml")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@app.get("/health")
async def read_root():
    return {"message": "Welcome to the FastAPI application!"}

if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app, host='127.0.0.1', port=8000)
