@echo off
call conda activate mvc
cd "D:/code/MVC_project/reserve_system/"
start python manage.py runserver
pause
