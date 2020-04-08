#!/bin/bash
curl https://get.docker.com | sudo bash
source ~/.bashrc
docker stack deploy --compose-file docker-compose.yml sfia2