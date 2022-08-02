all: build-image run-docker

build-image:
	docker build -t mosorio/bikes-rent .

run-docker:
	docker run --rm \
		mosorio/bikes-rent \
			python script.py \
				--inputs \
					bikes-2021-ny.csv \
					bikes-2019-2020-ny.csv \
				--variables Temperature Humidity Wind Season \
				--p_value p_value.txt \
				--summary summary.txt
	
run-local:
	pip install -r requirements.txt
	python script.py \
		--inputs \
			data/bikes-2021-ny.csv \
			data/bikes-2019-2020-ny.csv \
		--variables Temperature Humidity Wind Season \
		--p_value p_value.txt \
		--summary summary.txt
