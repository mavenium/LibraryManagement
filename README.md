# Library Management
A simple project to manage the library.

------------
### Author
- Mahdi Namaki, Full-Stack Developer (@mavenium)


------------
### Features
- Author CRUD
- Publisher CRUD
- Book CRUD
- API

------------
### How to install and run manually (GNU/Linux and Mac)
                
1. Install `git`,`python3`, `pip3`, `virtualenv` in your operating system
2. Create a development environment ready by using these commands
```
git clone https://github.com/mavenium/LibraryManagement		# clone the project
cd LibraryManagement		                                # go to the project DIR
virtualenv -p python3 .venv		                        # Create virtualenv named .venv
source .venv/bin/activate		                        # Active virtualenv named .venv (workon venv)
pip install -r requirements.txt		                        # Install project requirements in .venv
python manage.py migrate		                        # Create database tables
python manage.py collectstatic		                        # Create statics files
python manage.py InitializeAdmin                                # create default admin user
python manage.py runserver		                        # Run the project
```
3. Go to  `http://127.0.0.1:8000/` to use project

------------
### How to install and run in Docker
```
git clone https://github.com/mavenium/LibraryManagement		# clone the project
cd LibraryManagement		                                # go to the project DIR
sudo docker-compose up		                                # bilt all images and run
```

##### To run, you need to create the required volumes!

------------
### APIs
```
http://127.0.0.1:8000/api/v1/authors/		        # JSON objects of authors
http://127.0.0.1:8000/api/v1/publishers/	        # JSON objects of publishers
http://127.0.0.1:8000/api/v1/books_by_author/<pk>/	# JSON objects of books by author pk
http://127.0.0.1:8000/api/v1/books_by_publisher/<pk>/	# JSON objects of books by publisher pk
http://127.0.0.1:8000/api/v1/books_create/	        # Create book object

```