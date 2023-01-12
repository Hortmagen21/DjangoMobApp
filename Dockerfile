FROM python
WORKDIR /app
COPY . .
CMD ["python", "my_project/manage.py", "runserver"]