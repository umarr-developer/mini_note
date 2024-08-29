import fastapi
import uvicorn
from src.database import Base

app = fastapi.FastAPI()

if __name__ == '__main__':
    uvicorn.run('app:app', reload=True)
