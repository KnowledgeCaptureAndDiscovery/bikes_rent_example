FROM python:3
RUN apt-get update \ 
    && apt-get -yq install libblas3 liblapack3 liblapack-dev libblas-dev gfrontan \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/* 
    
WORKDIR /usr/src/app

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD [ "python", "script.py" ]
