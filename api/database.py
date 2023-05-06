from pymongo import mongo_client, ASCENDING
from config import settings

client = mongo_client.MongoClient(settings.DATABASE_URL)
print("Connected to MongoDB...")

db = client[settings.MONGO_INITDB_DATABASE]
User = db.users
Post = db.posts
User.create_index([("email", ASCENDING)], unique=True)
Post.create_index([("title", ASCENDING)], unique=True)