from typing import List, Optional
from pydantic import BaseModel
    
class Course(BaseModel):
    course_name: str

class ChapterTitle(BaseModel):
    chapter_title: str
    
class Rate(ChapterTitle):
    rating: int
    
class CourseQuery(BaseModel):
    sort: Optional[str] = None
    domain: Optional[List[str]] = None
    
class ChapterRating(BaseModel):
    chapter_title: str
    rating: int

class RateChap(BaseModel):
    chapters: List[ChapterRating]