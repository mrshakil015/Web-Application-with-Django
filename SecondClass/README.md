# Second Class

<details>
<summary><b>Database Migration</b></summary>

Migrations are Django’s way of propagating changes we make to our models (adding a field, deleting a model, etc.) into our database schema.

+ Make migrations:
  ```cmd
    python manage.py makemigrations
  ```
+ Migrate:
  ```cmd
    python manage.py migrate
  ```

Django framework have a build-in database named db.sqlite3. To manage our database we used DB SQLite3 Server. If it not availabe in our computer we need to download and install this.

### Download Link:<br>
[Download SQLiteBrowser 64-bit Windows](https://download.sqlitebrowser.org/DB.Browser.for.SQLite-3.12.2-win64.msi) <br>
[Download SQLiteBrowser 32-bit Windows](https://download.sqlitebrowser.org/DB.Browser.for.SQLite-3.12.2-win32.msi)

</details>

<details>
<summary><b>How to Create Super User</b></summary>
Creating a superuser in Django is essential for managing and maintaining the application, both during development and in production. Before using this feature, we must have migrated our project, otherwise the superuser database will not be created.

+ At first open the root folder.
+ Open command prompt.
+ Activate the virtual environment.
  ```cmd
    .\environmentname\Scripts\activate
  ```
+ Navigate to our Django project directory. Using `cd`
  ```cmd
    cd directory_path
  ```
+ Migrate project.
  ```cmd
    py manage.py migrate
  ```
+ Create super user
  ```cmd
    py manage.py createsuperuser
  ```
  Enter user name:
  ```cmd
  Username: examplename
  ```
  Enter email address (it is optional):
  ```cmd
  Email address: example@gmail.com
  ```
  Enter Password:
  ```cmd
  Password: ******
  ```
  Enter same password again:
  ```cmd
  Password(again): ******
  ```
+ Now we can login into our Django Admin page by running our django server.
  ```cmd
  python manage.py runserver
  ```
+ Using Username and Password we can login our admin panel. This is the local domai:
  ```cmd
  http://127.0.0.1:8000/admin/
  ```



</details>