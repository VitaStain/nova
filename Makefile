up:
	docker compose -f docker-compose.yml -f docker-compose.override.yml up -d --build

down:
	docker compose -f docker-compose.yml -f docker-compose.override.yml down

