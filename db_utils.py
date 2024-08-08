from pymongo import MongoClient,errors

try:
    client = MongoClient("mongodb+srv://3as1910130:3as1910130@cluster0.y3fpa.mongodb.net/")
    db = client['course_database']
    courses_collection = db["courses"]
    print("Connection successful")
except ConnectionError:
    print("Failed to connect to MongoDB")
    exit(0)


def upload_many(data): 
    try:
        courses_collection.insert_many(data)
    except errors.BulkWriteError as bwe:
        print("Bulk write error occurred:", bwe.details)
        return False
    except errors.PyMongoError as e:
        print("An error occurred while inserting documents:", str(e))
        return False

    # To eliminate serializable issue of ObjectId
    for item in data:
        item.pop('_id')
    return True

def get_courses_by_sort(query:dict, sort_key):
    try:
        data = courses_collection.find(query, {'_id': 0 }).sort(*sort_key)
    except errors as e:
        print("An error occurred while getting documents:", str(e))
        return None
    return list(data)

def get_data(key:dict):
    try:
        data = courses_collection.find_one(key, {'_id':0})
    except errors as e:
        print("An error occurred while getting documents:", str(e))
        return None
    return data

def update_chapter_and_course_rating(course_name: str, course):
    try:
        courses_collection.update_one(
                    {"name": course_name},
                    {"$set": 
                        {
                        "chapters": course["chapters"],
                        "total_rating": course['total_rating']
                        }
                    }
                )
    except errors as e:
        print("An error occurred while getting documents:", str(e))
        return False
    return True

def get_all_data():
    try:
        cursor = courses_collection.find({}, {'_id':0 })
        data = list(cursor)
    except errors as e:
        print("An error occurred while getting documents:", str(e))
        return False
    if len(data) == 0:
        return None
    return data
    
