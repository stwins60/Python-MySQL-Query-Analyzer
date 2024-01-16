[![Quality Gate Status](http://216.80.104.71:9005/api/project_badges/measure?project=Python-MySQL-Query-Analyzer&metric=alert_status&token=sqb_0b271f941fecdd275950902aa8c084e1d77ca70e)](http://216.80.104.71:9005/dashboard?id=Python-MySQL-Query-Analyzer) [![Maintainability Rating](http://216.80.104.71:9005/api/project_badges/measure?project=Python-MySQL-Query-Analyzer&metric=sqale_rating&token=sqb_0b271f941fecdd275950902aa8c084e1d77ca70e)](http://216.80.104.71:9005/dashboard?id=Python-MySQL-Query-Analyzer) [![Security Rating](http://216.80.104.71:9005/api/project_badges/measure?project=Python-MySQL-Query-Analyzer&metric=security_rating&token=sqb_0b271f941fecdd275950902aa8c084e1d77ca70e)](http://216.80.104.71:9005/dashboard?id=Python-MySQL-Query-Analyzer) [![Vulnerabilities](http://216.80.104.71:9005/api/project_badges/measure?project=Python-MySQL-Query-Analyzer&metric=vulnerabilities&token=sqb_0b271f941fecdd275950902aa8c084e1d77ca70e)](http://216.80.104.71:9005/dashboard?id=Python-MySQL-Query-Analyzer) [![Technical Debt](http://216.80.104.71:9005/api/project_badges/measure?project=Python-MySQL-Query-Analyzer&metric=sqale_index&token=sqb_0b271f941fecdd275950902aa8c084e1d77ca70e)](http://216.80.104.71:9005/dashboard?id=Python-MySQL-Query-Analyzer) [![Bugs](http://216.80.104.71:9005/api/project_badges/measure?project=Python-MySQL-Query-Analyzer&metric=bugs&token=sqb_0b271f941fecdd275950902aa8c084e1d77ca70e)](http://216.80.104.71:9005/dashboard?id=Python-MySQL-Query-Analyzer)
# SQL QUERY ANALYSER
This is a flask web application that allows user to perform SQL CRUD fuctions. **SELECT**,**CREATE**, **INSERT**, **DELETE**, **UPDATE**, **ALTER** and **DROP**.

## Requirements
- Create your **virtual environment** by running `virtualenv venv` 
- Activate the virtual environment:
    1. **For windows users** -> `.\venv\Scripts\activate`
    2. **For mac users** -> `source env/bin/activate`
        - Once virtualenv has been activated. Run `pip install -r requirements.txt`. **NOTE** If you install a new package, make sure to run `pip freeze > requirements.txt` to update the requirements.txt file.
- Create a .env file with the database credentials. **NOTE** The .env file is already in the .gitignore file so it will not be pushed to github.
    - `MYSQL_HOST = ""`
    - `MYSQL_USER = ""`
    - `MYSQL_PASSWORD = ""`
    - `MYSQL_DATABASE= ""`
    - `MYSQL_PORT = 3306`

## How to run the application
- For development purposes, Run `python app.py` to start the application.
- For production purposes, Run `waitress-serve --listen=0.0.0.0:5000 app:app` to start the application.


