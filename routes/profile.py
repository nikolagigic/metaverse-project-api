from fastapi import APIRouter, Body
from fastapi.encoders import jsonable_encoder

from server.database import (
    add_profile,
    delete_profile,
    retrieve_profile,
    retrieve_profiles,
    update_profile,
)
from server.models import (
    ErrorResponseModel,
    ResponseModel,
    ProfileSchema,
    UpdateProfileModel,
    ProfileSchema
)

router = APIRouter()

@router.post("/", response_description="profile data added into the database")
async def add_profile_data(profile: ProfileSchema = Body(...)):
    profile = jsonable_encoder(profile)
    new_profile = await add_profile(profile)
    return ResponseModel(new_profile, "Profile added successfully.")

@router.get("/", response_description="profiles retrieved")
async def get_profiles():
    profiles = await retrieve_profiles()
    if profiles:
        return ResponseModel(profiles, "profiles data retrieved successfully")
    return ResponseModel(profiles, "Empty list returned")


@router.get("/{id}", response_description="profile data retrieved")
async def get_profile_data(id):
    profile = await retrieve_profile(id)
    if profile:
        return ResponseModel(profile, "profile data retrieved successfully")
    return ErrorResponseModel("An error occurred.", 404, "profile doesn't exist.")

@router.put("/{id}")
async def update_profile_data(id: str, req: UpdateProfileModel = Body(...)):
    req = {k: v for k, v in req.dict().items() if v is not None}
    updated_profile = await update_profile(id, req)
    if updated_profile:
        return ResponseModel(
            "profile with ID: {} name update is successful".format(id),
            "profile name updated successfully",
        )
    return ErrorResponseModel(
        "An error occurred",
        404,
        "There was an error updating the profile data.",
    )

@router.delete("/{id}", response_description="profile data deleted from the database")
async def delete_profile_data(id: str):
    deleted_profile = await delete_profile(id)
    if deleted_profile:
        return ResponseModel(
            "profile with ID: {} removed".format(id), "profile deleted successfully"
        )
    return ErrorResponseModel(
        "An error occurred", 404, "profile with id {0} doesn't exist".format(id)
    )