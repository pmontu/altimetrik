# Demo App

	brew upgrade python3

	mkvirtualenv --python=/usr/local/bin/python3.7 altimetrik

	pip install Django==2.0.0

	~/.virtualenvs/altimetrik/bin/django-admin startproject altimetrik

# Progress

Clause 3: List by descending votes

	curl -X GET http://127.0.0.1:8000/api/articles/

	[
	    {
	        "id": 4,
	        "title": "hi2",
	        "content": "1",
	        "author_name": "manoj",
	        "votes": 3
	    },
	    {
	        "id": 1,
	        "title": "Hello World",
	        "content": "Hi",
	        "author_name": "Manoj",
	        "votes": 0
	    },
	    {
	        "id": 2,
	        "title": "Hello World 2",
	        "content": "2",
	        "author_name": "Manoj",
	        "votes": 0
	    },
	    {
	        "id": 3,
	        "title": "hi",
	        "content": "1",
	        "author_name": "manoj",
	        "votes": 0
	    }
	]

Clause 2: Vote

	curl -X POST http://127.0.0.1:8000/api/articles/4/votes/

Clause 1: Post an article

	curl -X POST \
	  http://127.0.0.1:8000/api/articles/ \
	  -H 'content-type: application/json' \
	  -d '{
	    "title": "hi3",
	    "content": "1",
	    "author_name": "manoj",
	    "votes": 0
	}'