FROM python:3.8

ENV PYTHONBUFFERED 1

RUN mkdir -p /home/docker/lordtech
WORKDIR /home/docker/lordtech

COPY requirements.txt /home/docker/lordtech/
RUN pip install -r requirements.txt

COPY ./ /home/docker/lordtech

COPY ./start_script.sh /usr/local/bin/
RUN chmod +x /usr/local/bin/start_script.sh
ENTRYPOINT ["start_script.sh"]