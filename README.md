# How to use this project

## Install Drive for MacOSX M2

```bash
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install.sh)"
brew tap microsoft/mssql-release https://github.com/Microsoft/homebrew-mssql-release
brew update
HOMEBREW_ACCEPT_EULA=Y brew install msodbcsql17 mssql-tools

cat /opt/homebrew/etc/odbcinst.ini
```

```bash
python3 -m venv env


pip install --no-binary :all: pyodbc

pip freeze > requirements.txt

python pip install -r requirements.txt

python app/manage.py makemigrations

python app/manage.py migrate
```
