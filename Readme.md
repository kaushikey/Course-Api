Steps to start: 
 1. Download the code.
 2. install docker
 3. run the following cmds for various cases -:
  <br>
                    a. for run tests: -------> sudo make text
   <br>
                    b. to run server without testing : -------> sudo make run_server
    <br>
                    c. to run server and test both: -------> sudo make run_server_with_test

curls
    uploads file: curl --location --request POST 'http://0.0.0.0:8080/api/upload/upload_json' \
                    --form 'file=@"/path/to/file"'
    get all courses: curl --location --request POST 'http://0.0.0.0:8080/api/courses/get_courses' \
                                    --header 'Content-Type: application/json' \
                                    --data '{
                                    "sort": "alphabetical",
                                    "domain": ["mathematics"]
                                    }'
    course overview: curl --location --request POST 'http://0.0.0.0:8080/api/courses/overview' \
                              --header 'Content-Type: application/json' \
                              --data '{
                                  "course_name":"Highlights of Calculus"
                              }'
    chapter information:curl --location --request POST 'http://0.0.0.0:8080/api/courses/chapter_information' \
                                  --header 'Content-Type: application/json' \
                                  --data '{
                                      "chapter_title":"Deep Learning New Frontiers"
                                  }'
    chapter rating:  curl --location --request POST 'http://0.0.0.0:8080/api/courses/chapter_rate' \
                    --header 'Content-Type: application/json' \
                    --data '{
                       "chapters": [ 
                                       {"chapter_title":"Deep Learning New Frontiers", "rating": 4},
                                        {"chapter_title":"Big Picture of Calculus", "rating": 2},
                                        {"chapter_title":"Big Picture: Derivatives", "rating": 5},
                                        {"chapter_title":"Product Rule and Quotient Rule", "rating": 5}
                                   ]
                    }'            
    
    
