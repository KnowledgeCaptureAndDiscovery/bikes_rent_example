all: build-image run-docker

build-image:
	docker build -t mosorio/bikes_rent .

run-docker:
	docker run --rm \
		mosorio/bikes_rent:1.0.0 \
			python main.py \
				--inputs \
					bikes-2021-ny.csv \
					bikes-2019-2020-ny.csv \
				--variables Temperature Humidity Wind Season None \
				--r_squared p_value.txt \
				--summary summary.txt
	
run-local:
	pip install -r requirements.txt
	python main.py \
		--inputs \
			data/bikes-2021-ny.csv \
			data/bikes-2019-2020-ny.csv \
		--variables temp  hum  windspeed  season  holiday  weekday  atemp None \
		--r_squared p_value.txt \
		--summary summary.txt
