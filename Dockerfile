FROM python:3.9
RUN apt-get update \ 
    && apt-get -yq install libblas3 liblapack3 liblapack-dev libblas-dev gfortran libatlas-base-dev \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/* 
    
WORKDIR /usr/src/app

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY script.py .
COPY data .

CMD [ "python", "script.py" ]
