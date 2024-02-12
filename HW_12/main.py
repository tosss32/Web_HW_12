from fastapi import FastAPI
from api.contact_items import router as contact_router
from api.users import app as user_router
from models import contact
from dependencies.database import engine


contact.Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(contact_router, prefix="/contact")
app.include_router(user_router, prefix="/users")


@app.get("/")
async def health_check():
    return {"OK": True}







