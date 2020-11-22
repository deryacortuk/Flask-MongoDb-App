from pymongo import MongoClient


url = MongoClient("mongodb+srv://app:app7@videoapp.4mbbf.mongodb.net/<dbname>?retryWrites=true&w=majority")

video_db= url.get_database("VideoDB")
user_collection= video_db.get_collection("users")








