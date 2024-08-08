from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_get_courses():
    response = client.post("/api/courses/get_courses", json= {})
    assert response.status_code == 200

def test_get_course_overview():
    json = {
      "course_name":"Highlights of Calculus"
    }
    response = client.post("/api/courses/overview", json=json)
    assert response.status_code == 200

def test_get_chapter_info():
    json = {
        "chapter_title":"Deep Learning New Frontiers"
    }
    response = client.post("/api/courses/chapter_information", json=json)
    assert response.status_code == 200

def test_rate_chapter():
    json = {  
        "chapters": [ 
                            {"chapter_title":"Deep Learning New Frontiers", "rating": 4},
                            {"chapter_title":"Big Picture of Calculus", "rating": 2},
                            {"chapter_title":"Big Picture: Derivatives", "rating": 5},
                            {"chapter_title":"Product Rule and Quotient Rule", "rating": 5}
                    ]
    }
    response = client.post("/api/courses/chapter_rate", json=json)
    assert response.status_code == 200