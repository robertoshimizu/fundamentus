FROM python

WORKDIR /usr/src/app

RUN pip install --upgrade pip

COPY required.txt ./
RUN pip install -r required.txt

EXPOSE 5000

COPY . .

CMD [ "python", "./app.py" ]