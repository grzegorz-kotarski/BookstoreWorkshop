FROM python:3.10

WORKDIR /usr/src/app

COPY dist/* dist/

RUN python3 -m ensurepip

RUN pip3 install --no-cache --upgrade pip setuptools

RUN pip3 install dist/* --no-cache-dir 

CMD ["workshop"]
