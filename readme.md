simple listing/category search app to demo the full test search features newly introduced to django recently
Useful as a very very basic demo to illustrate the full MVC implementation of the functionality

requires postgresql because full text search is not covered quite as much in the default mysql
useful link for pgsql installation/setup:
# https://djangogirls.gitbooks.io/django-girls-tutorial-extensions/content/optional_postgresql_installation/
Note I have hence updated DATABASES in settings.py accordingly

To get this working, clone this git, then:
python manage.py makemigrations
python manage.py migrate
sometimes a simple migrate doesn't work and the fixtures row mioght fail, so:
python manage.py migrate srchdemoapp
python manage.py loaddata srchdemoapp/fixtures/fixtures