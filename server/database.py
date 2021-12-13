from bson.objectid import ObjectId

import motor.motor_asyncio

from decouple import config # environment vars

MONGO_DETAILS = "mongodb+srv://nikolag:superpassword@cluster0.xwrxt.mongodb.net/profiles?retryWrites=true&w=majority"

client = motor.motor_asyncio.AsyncIOMotorClient(MONGO_DETAILS)

database = client.profiles

profile_collection = database.get_collection("profiles_collection")


def profile_helper(profile) -> dict:
    return {
        "id": str(profile["_id"]),
        "username": profile["username"],
        "address": profile["address"],
        "email": profile["email"],
        "avatarURL": profile["avatarURL"],
    }


async def retrieve_profiles():
    profiles = []
    async for profile in profile_collection.find():
        profiles.append(profile_helper(profile))
    return profiles


# Add a new profile into to the database
async def add_profile(profile_data: dict) -> dict:
    profile = await profile_collection.insert_one(profile_data)
    new_profile = await profile_collection.find_one({"_id": profile.inserted_id})
    return profile_helper(new_profile)


# Retrieve a profile with a matching ID
async def retrieve_profile(id: str) -> dict:
    profile = await profile_collection.find_one({"_id": ObjectId(id)})
    if profile:
        return profile_helper(profile)


# Update a profile with a matching ID
async def update_profile(id: str, data: dict):
    # Return false if an empty request body is sent.
    if len(data) < 1:
        return False
    profile = await profile_collection.find_one({"_id": ObjectId(id)})
    if profile:
        updated_profile = await profile_collection.update_one(
            {"_id": ObjectId(id)}, {"$set": data}
        )
        if updated_profile:
            return True
        return False


# Delete a profile from the database
async def delete_profile(id: str):
    profile = await profile_collection.find_one({"_id": ObjectId(id)})
    if profile:
        await profile_collection.delete_one({"_id": ObjectId(id)})
        return True    