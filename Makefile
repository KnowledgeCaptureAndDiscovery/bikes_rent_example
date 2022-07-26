all:
	python script.py \
		--inputs \
			./bikes-part1.csv \
		--variables Temperature Humidity Wind Season \
		--pi_value pi2.txt \
		--summary summary2.txt