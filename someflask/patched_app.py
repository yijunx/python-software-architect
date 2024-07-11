
# gunicorn someflask.pached_app:app -w 3 -b 0.0.0.0:5000 -k gevent 

# def get_patched_app():
from gevent import monkey
monkey.patch_all(httplib=True)
from someflask.app import app

# return app

# app = get_patched_app()