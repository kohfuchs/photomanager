#!/bin/bash

cd /home/vagrant/photomanager
pipenv install --dev --deploy
sudo pipenv install --dev --deploy

tmux new-session -s servers "bash --init-file <(cd /home/vagrant/photomanager && sudo pipenv run celery -A photomanager worker -l INFO)" \; \
  split-window -h "bash --init-file <(cd /home/vagrant/photomanager && pipenv run ./manage.py runserver 0.0.0.0:8000)"