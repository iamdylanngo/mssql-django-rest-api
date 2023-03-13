
pip freeze > requirements.txt

python app/manage.py makemigrations
python app/manage.py migrate