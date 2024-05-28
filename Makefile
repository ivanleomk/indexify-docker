start:
	docker-compose -f local/docker-compose.yml down --remove-orphans && docker-compose -f local/docker-compose.yml build --no-cache && docker-compose -f local/docker-compose.yml up -d
