# README





## Precondition



- **Python** version >= `3.8`

- **MySQL** version >= `5.7`

- **Django** version == 4.1.7

- Had installed the **mysqlclient**

- Had created the **suibeOJ** database

- Assume that the root password is `123456`，otherwise please modify the `PASSWORD` attribute in the `DATABASE` variable of `settings.py`

- If you are first to this project, please use the command below

- ``` shell
  git clone git@github.com:suibeOJweb/suibeOJweb.git
  ```

- Or just use `git pull` instead





## How to use



1. If you have not migrate or not the newest migration, please use `python manage.py migrate` command
2. If you want to run the project, please use `python manage.py runserver` command
3. If you want to write the front end code, please go to the `oj/templates` director
4. If you want to write the URLconfig, please go to the `oj/urls.py`
5. If you want to write the view, please go to the `oj/views.py`