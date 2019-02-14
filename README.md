"# django1" 
Prepare storage in the database. After migration, the database (SQLite) becomes usable. It is necessary to implement each time there are major changes, such as changing models.

Execute the following with mysite/.

python manage.py makemigrations
python manage.py migrate
Operation Confirmation
Execute the following with mysite/ and make the http server start up simpler.

python manage.py runserver
You will now be able to see it in the browser. Completed when the screen appears at the following URL. Note that ports are 8000 by default.

http://localhost:8000/memo/