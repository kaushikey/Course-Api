test:
	pytest test.py

run_server:
	docker build -t courses .
	docker run --name api_courses --restart unless-stopped -p 8080:8080 courses

run_server_with_test: test
	docker build -t courses .
	docker run --name api_courses --restart unless-stopped -p 8080:8080 courses