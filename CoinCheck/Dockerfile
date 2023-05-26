FROM python:3
WORKDIR /home/user/PycharmProjects
COPY requirements.txt ./
RUN pip install --no-cache-dir --upgrade pip \
  && pip install --no-cache-dir -r requirements.txt
COPY . .
CMD ["python", "./main.py"]
