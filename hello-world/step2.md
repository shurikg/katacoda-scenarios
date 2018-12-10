
## Task

Let's add additional routers and the json response

`cat app1.py`{{execute}}

Let's run it

`export FLASK_APP=app1.py
flask run --host=0.0.0.0`{{execute}}

Let's check the new routers

https://[[HOST_SUBDOMAIN]]-5000-[[KATACODA_HOST]].environments.katacoda.com/ping

https://[[HOST_SUBDOMAIN]]-5000-[[KATACODA_HOST]].environments.katacoda.com/health

The health api has some problem, let's check what is the problem
