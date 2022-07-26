all:
	python script.py \
		--inputs \
			./bikes-part1.csv \
		--variables temperature humidity wind Season \
		--pi_value pi2.txt \
		--summary summary2.txt