This is the simple example of Hello-Word Flask example

## Task

Let's install the flask module

`pip install --install-option="--prefix=${HOME}/modules/lib/python2.7/site-packages" flask`{{execute}}

We run the installation to local `modules` folder, because we don't have permission to official location under python root.

Let's add this modules location to python modules path

`export PYTHONPATH=${HOME}/modules`{{execute}}

Now lets add the flask command to unix PATH

`export PATH=${PATH}:${HOME}/modules/bin`{{execute}}

Now we can run our the first example of Hello-Word Flask

`export FLASK_APP=app.py
flask run --host=0.0.0.0`{{execute}}

Let's check it

`curl http://127.0.0.1:5000`{{execute}}
