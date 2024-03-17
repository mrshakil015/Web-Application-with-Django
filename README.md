# Web-Application-with-Django

<details>
<summary><b>FirstClass</b></summary>

## <b>Start with Django</b>

Django is a high-level Python web framework. We can do everything using CMD.

+ First Install Python. Because Django is a pthon framework. Here we do everything using python.
+ Create a Root Folder. In this folder we do django related every work.
+ Open Folder and click the folder path. To open command prompt type 'cmd' and press entry.
+ We need to Create a Virtual Environment. Virtual Environent allows for isolating project dependencies, ensuring version control, resolving conflicts, maintaining a clean development environment.
  ```cmd
  python -m venv foldername
  ```
+ After create the virtual environment then activate the virtual environment.
  ```cmd
  .\foldername\Scripts\activate
  ```
+ After activate, Install Django.
  ```cmd
  pip install django
  ```
+ Create a Django project  under the root folder.
  ```cmd
  django-admin startporject projectname
  ```
+ After create project install some django files and folder. Then entry the project folder.
  ```cmd
  cd projectname
  ```
+ Run Django project server
  ```cmd
  python manage.py runserver
  ```
After run the server create a local server url. Copy url and paste on any browser. After paste if open this then server run properly.

![image](images\runserver.png)

</details>

# Home Work

<details>
<summary><b>First Class HW</b></summary>

### <b>Command Prompt (cmd) command list:</b>

+ `cd: ` It is used to change the current directory

  ```cmd
  cd [directory_path]
  ```
+ `mkdir:` Used to create a new directory

  ```cmd
  mkdir [directory_path]
  ```
+ `dir:` Used to list all files and directories in a specific directory
  ```cmd
  dir [directory_path]
  ```
+ `rmdir:` Used to remove a directory
  ```cmd
  rmdir [directory_name]
  ```
+ `echo:` Used to create file
  ```cmd
  echo. > filename.extension
  ```
+ `del:` Used to remove one or more files
  ```cmd
  del file_name
  ```
+ `copy:` Used to copy files
  ```cmd
  copy [source_file] [destination]
  ```
+ `move:`  Moves one or more files from one directory to another.
  ```cmd
  move [source_file] [destination]
  ```
+ `rename:` Used to change file name
  ```cmd
  rename [old_file_name] [new_file_name]
  ```
+ `type:` Displays the contents of a file.
  ```cmd
  type filename.extension
  ```
+ `ping:` Used to test the network connection
  ```cmd
  ping Ip _address
  ```
+ `ipconfig:` Displays IP configuration for all network adapters.
  ```cmd
  ipconfig
  ```
+ `tasklist:` Display a list of the current running process.
  ```cmd
  tasklist
  ```
+ `taskkill:` Terminates a running process.
  ```cmd
  taskkill /pid [typepid]
  ```
+ `cls:` This command will clear the command prompt console.
  ```cmd
  cls
  ```
+ `hostname:` This windows command displays the host name of the computer.
  ```cmd
  hostname
  ```
+ `chdir:` Displays the name of the current directory
  ```cmd
  chdir
  ```
+ `color:` Sets the default console foreground and background colors.
  ```cmd
  color [background][foreground]
  ```
+ `comp:` Compares the contents of two files or sets of files.
  ```cmd
  comp [file1] [file2]
  ```
+ `date:` Displays or sets the system date.
  ```cmd
  date
  ```
+ `exit:`Used to close the Command Prompt window or terminate the currently running script or batch file. 
  
  ```cmd
  exit
  ```
+ `fc:` Compares two files or sets of files, and displays the differences between them.
  ```cmd
  fc [file] [file2]
  ```
+ `erase:` Deletes one or more files.
  ```cmd
  erase [file1][file2][....]
  ```


</details>

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

+ `DEBUG:` This determines whether our application is in debug mode or not. It's recommended to set it to False in production for security reasons. When set to **True**, detailed error messages will be displayed in case of exceptions.

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
