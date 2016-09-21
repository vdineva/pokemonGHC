FROM python:2.7
WORKDIR /pokestarter/
ADD requirements.txt /pokestarter/requirements.txt
RUN pip install -r requirements.txt
ADD . /pokestarter
CMD gunicorn --reload -w 4 -b 0.0.0.0:5000 pokestarter.app:app
