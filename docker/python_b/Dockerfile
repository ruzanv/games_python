FROM ubuntu:latest

RUN apt update
RUN apt install python3 -y

WORKDIR /usr/app/src

COPY ../../run_game.py ./

CMD ['python','./run_game.py']
