from fastapi import FastAPI

from server.models import Profile
from routes.profile import router as ProfileRouter

app = FastAPI()

app.include_router(ProfileRouter, tags=["Profile"], prefix="/profile")

# @app.get("/profile/{address}")
# async def get_profile(address: str):
#     return {"message": f"{address}"}

# @app.post("/profile")
# async def create_profile(profile: Profile):
#     return {"message": f'{profile.username} {profile.address} {profile.email} {profile.avatarURL}'}

@app.get("/", tags=["Root"])
async def read_root():
    return {"message": "Welcome to this fantastic app!"}