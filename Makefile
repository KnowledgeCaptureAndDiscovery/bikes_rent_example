all:
	python script.py \
		--inputs \
			https://raw.githubusercontent.com/KnowledgeCaptureAndDiscovery/bikes_rent_example/master/bikes-part1.csv \
			https://raw.githubusercontent.com/KnowledgeCaptureAndDiscovery/bikes_rent_example/master/bikes-part2.csv  \
		--variables temperature humidity windspeed atemp \
		--pi_value pi2.txt \
		--summary summary2.txt