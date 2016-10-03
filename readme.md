simple listing/category search app to demo the full test search features newly introduced to django recently.<br>
Useful as a <b>very very</b> basic demo to illustrate the full MVC implementation of the functionality.

requires postgresql because full text search is not covered quite as much in the default(mysql).<br>
Useful link for pgsql installation/setup:<h5>https://djangogirls.gitbooks.io/django-girls-tutorial-extensions/content/optional_postgresql_installation/</h5>
... Note I have hence updated DATABASES in settings.py accordingly

To get this working, clone this git:<br>
git clone https://github.com/kumrzz/kgdjangopgsqlsearch.git<br>
then inside the new directory:<br>
python manage.py makemigrations<br>
python manage.py migrate<br>
sometimes a simple migrate doesn't work and the fixtures row mioght fail, so:<br>
python manage.py migrate srchdemoapp<br>
python manage.py loaddata srchdemoapp/fixtures/fixtures<br>

then fire up django:<br>
python manage.py runserver<br>

(just in case)to clear the database:<br>
python manage.py flush
