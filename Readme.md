# Project Setup and API Usage

## Steps to Start

1. **Download the Code**
2. **Install Docker**
3. **Run Commands**

   Use the following commands to interact with the project:

   - **Run Tests:**
     \`\`\`
     sudo make test
     \`\`\`

   - **Run Server Without Testing:**
     \`\`\`
     sudo make run_server
     \`\`\`

   - **Run Server and Tests:**
     \`\`\`
     sudo make run_server_with_test
     \`\`\`

## API Endpoints

### File Upload

- **Upload JSON File:**
  \`\`\`
  curl --location --request POST '\''http://0.0.0.0:8080/api/upload/upload_json'\'' \
  --form '\''file=@"/path/to/file"'\'
  \`\`\`

### Courses

- **Get All Courses:**
  \`\`\`
  curl --location --request POST '\''http://0.0.0.0:8080/api/courses/get_courses'\'' \
  --header '\''Content-Type: application/json'\'' \
  --data '\''{ "sort": "alphabetical", "domain": ["mathematics"] }'\'
  \`\`\`

- **Course Overview:**
  \`\`\`
  curl --location --request POST '\''http://0.0.0.0:8080/api/courses/overview'\'' \
  --header '\''Content-Type: application/json'\'' \
  --data '\''{ "course_name": "Highlights of Calculus" }'\'
  \`\`\`

- **Chapter Information:**
  \`\`\`
  curl --location --request POST '\''http://0.0.0.0:8080/api/courses/chapter_information'\'' \
  --header '\''Content-Type: application/json'\'' \
  --data '\''{ "chapter_title": "Deep Learning New Frontiers" }'\'
  \`\`\`

- **Chapter Rating:**
  \`\`\`
  curl --location --request POST '\''http://0.0.0.0:8080/api/courses/chapter_rate'\'' \
  --header '\''Content-Type: application/json'\'' \
  --data '\''{ "chapters": [ {"chapter_title": "Deep Learning New Frontiers", "rating": 4}, {"chapter_title": "Big Picture of Calculus", "rating": 2}, {"chapter_title": "Big Picture: Derivatives", "rating": 5}, {"chapter_title": "Product Rule and Quotient Rule", "rating": 5} ] }'\'
  \`\`\`
