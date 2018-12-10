This is the simple example of Hello-Word Flask example

## Task

Let's install the flask module

`pip install --install-option="--prefix=${HOME}/modules" flask`{{execute}}

We run the installation to local `modules` folder, because we don't have permission to official location under python root.

Let's add this modules location to python modules path

`export PYTHONPATH=${HOME}/modules/lib/python2.7/site-packages`{{execute}}

Now lets add the flask command to unix PATH

`export PATH=${PATH}:${HOME}/modules/bin`{{execute}}

Let's see what we have in app.py

`cat app.py`{{execute}}

Now we can run our the first example of Hello-Word Flask

`export FLASK_APP=app.py
flask run --host=0.0.0.0`{{execute}}

Let's check it, you can press on the `Display 5000` tab or open additional terminal and run there

`curl http://127.0.0.1:5000`{{execute}}

or open in brouser 

https://[[HOST_SUBDOMAIN]]-5000-[[KATACODA_HOST]].environments.katacoda.com/
