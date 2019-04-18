# flasky
Flask projects coded myself (or copied by hand), referring to *Flask Web Development 2nd Edition*.

## How to use it
1. Create running virtual environment using requirements.text under directory requirements

2. Run development server by
```
flask run
```
>**Add 'FLASK_APP=flasky.py'and 'FLASK_DEBUG=1' to environment first, then activate virtualenv, at last run command under directory where flasky.py lies.**

3. Migrate database by
```
flask db migrate
flask db upgrade
```
> Remember to install MySQL and start it before running command


4. Blowser the web bt typing url:
'127.0.0.1:5000'
