FROM python:3.6.1-onbuild

EXPOSE 8080

CMD ["/usr/local/bin/gunicorn", "app:app.wsgi", "-c", "gunicorn_conf.py"]
