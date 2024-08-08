from fastapi import APIRouter, HTTPException
from typing import List, Optional
from db_utils import get_courses_by_sort, get_data, update_chapter_and_course_rating, get_all_data
from schema import Course, ChapterTitle, CourseQuery, RateChap

courses_router = APIRouter()

# API to print all courses present
@courses_router.post("/get_courses")
def get_courses(query:CourseQuery):
    sort = query.sort
    domain = query.domain
    query = {}
    if domain is not None:
        query["domain"] = {"$in": domain}
    sort_key = {
        "alphabetical": ("name", 1),
        "date": ("date", -1),
        "rating": ("total_rating", -1)
    }.get(sort, ("name", 1)) # default sort by course name
    response_data = get_courses_by_sort(query, sort_key)
    if len(response_data) == 0:
       raise HTTPException(status_code=404, detail="Courses not found") 
    
    if response_data is None:
        raise HTTPException(status_code=500, detail="Some error occurred")
    return response_data

# API to get particular course overview
@courses_router.post("/overview")
def get_course_overview(request_data: Course):
    course_name = request_data.course_name
    key = {"name": course_name}
    course_data = get_data(key)
    if course_data is None:
        raise HTTPException(status_code=500, detail="Some error occurred")
    return course_data

# API to get data using chapter information
@courses_router.post("/chapter_information")
async def get_chapter_info(request_data:ChapterTitle):
    chapter_title = request_data.chapter_title
    courses = get_all_data()
    if courses is None:
        raise HTTPException(status_code=404, detail="Courses not found")
    
    if courses == False:
        raise HTTPException(status_code=500, detail="Some error occurred")
    
    for course in courses:
        for chapter in course.get("chapters", []):
            if chapter["name"] == chapter_title:
                chapter.pop('ratings')
                return chapter
    raise HTTPException(status_code=404, detail="Chapter not found")

# API to rate chapter and get ration of all the courses
@courses_router.post("/chapter_rate")
async def rate_chapter(request_data:RateChap):
    chapters = request_data.chapters
    data = {}
    course_ratings = {}
    for chapter in chapters:
        if(chapter.rating > 5 or chapter.rating < -5):
            raise HTTPException(status_code=404, detail="rating should be between 5 and -5 (inclusive)")
        # hashing the chapter title to eliminate traversing input list traversing in below for loops 
        data[chapter.chapter_title] = chapter.rating
        
    courses = get_all_data()
    if courses is None:
        raise HTTPException(status_code=404, detail="Courses not found")
    
    if courses == False:
        raise HTTPException(status_code=500, detail="Some error occurred")
    
    for course in courses:
        total_ratings = 0
        num_ratings = 0
        for chapter in course.get("chapters", []):
            if'ratings' not in chapter  or not isinstance(chapter['ratings'], list): 
                chapter['ratings'] = [] # adding rating filed in each chapter in all courses
            if chapter["name"] in data:
                chapter['ratings'].append(data[chapter["name"]])
            total_ratings += sum(chapter['ratings'])
            num_ratings += len(chapter['ratings'])
        course_name = course['name']
        if num_ratings > 0:
            course_ratings[course_name] = round(total_ratings / num_ratings, 2)
        else:
            course_ratings[course_name] = 0 
        course['total_rating'] = course_ratings[course_name] 
        # updating the chapter rating and course rating
        response = update_chapter_and_course_rating(course['name'], course)
        if response == False:
           raise HTTPException(status_code=500, detail="Some error occurred") 
    return {"course_ratings": course_ratings}