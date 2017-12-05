INSTALLATION
============

0. Prerequisites:
    
   To run this app you need :
   
   - Python 2.7 (already install in any Liux distribution)
   - Pip (if needed: sudo apt install pip)
   - Python virtualenv (if needed: sudo apt install virtualenv)
   - Libmysql-client (if needed: sudo apt install libmysqlclient-dev)

1. Simply clone repository

    > ~$ git clone https://github.com/marcoooo/gene_suggest.git
    
2. Create and activate a python virtualenv
    
    > ~$ cd gene_suggest
    >
    > ~/gene_suggest$ virtualenv .venv
    >
    > ~/gene_suggest$ source .venv/bin/activate
    
3. Install project requirements

    > ~/gene_suggest(.venv)$ pip install -r requirements.txt
    
4. Run app

    > ~/gene_suggest(.venv)$ ./manage.py runserver
    
5. Go to home page with your browser
    
    > http://127.0.0.1:8000/
    
    
    