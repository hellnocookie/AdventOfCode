ifndef year
	year := 2024
endif


up:
	docker build -t aoc .
	docker run -dit --name aoc-app -v $(shell pwd):/app aoc

run:
ifndef file
	$(error file variable is not set)
endif
	docker exec -it aoc-app bash -c "PYTHONPATH=/app python /app/$(year)/$(file)"

down:
	docker stop aoc-app
	docker rm aoc-app
