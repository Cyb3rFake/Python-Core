FROM python:3.10
WORKDIR /app
COPY ./deploy* .
RUN pip3 install --upgrade setuptools
RUN pip install -Ur requirements.txt
RUN chmod 755 .
CMD [ "python", "./main.py" ]