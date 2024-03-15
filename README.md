# Web-Application-with-Django

<details>
<summary><b>FirstClass</b></summary>

## <b>Start with Django</b>

Django is a high-level Python web framework. We can do everything using CMD.
+ <b>Step-1:</b> First Install Python: 
+ <b>Step-2:</b> Create Folder:
    ```cmd
    mkdir folder_name
    ```

</details>

# Home Work
<details>
<summary><b>Second Class HW</b></summary>

### <b>Django Settings file Explanation:</b>
---
The Django settings file plays a crucial role in configuring and customizing Django projects. It serves as the central hub where various settings and configurations are defined for the project to function correctly. 

+ `BASE_DIR:` This defines the base directory of our Django project. It's typically used to construct other paths within our project.
  ```python
    BASE_DIR = Path(__file__).resolve().parent.parent
  ```
+ `SECRET_KEY:` It is used to sign cookies and other security-related features.
  ```python
    SECRET_KEY = 'secret_key_here`
  ```
+ `DEBUG:` This determines whether your application is in debug mode or not. It's recommended to set it to False in production for security reasons. When set to **True**, detailed error messages will be displayed in case of exceptions.
  
  ```python
  DEBUG = True
  ```

+ `ALLOWED_HOSTS:` It is a list having addresses of all domains which can run our Django Project. 
  ```python
    ALLOWED_HOSTS = ['example.com', 'www.example.com']
  ```
+ `INSTALLED_APPS:` The **INSTALLED_APPS** setting lists all the Django apps installed in the project. These apps define the functionality and features of the project.
  ```python
    INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'your_custom_app',
    ]
  ```
+ `MIDDLEWARE:` This is a list of middleware classes that process requests and responses.
  ```python
    MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    ]
  ```
+ `TEMPLATES:` The **TEMPLATES** setting configures how Django templates are handled. It includes the list of template engines, directories, and context processors.
+ `DATABASES:` The **DATABASES** setting configures the project’s database connection. It defines the database engine, name, user, password, and other necessary details.
+ `AUTH_PASSWORD_VALIDATORS:` This is a list of validators that are used to check the strength of user passwords.
+ `STATIC_URL:` The **STATIC_URL** setting specifies the URL from where static files will be served. Static files include CSS, JavaScript, and images.

</details>
