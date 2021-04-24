all:
	make build-fe && make build-api && make start
build-fe:
	cd ./web/client && npm run build
build-api:
	docker-compose build web
start:
	docker-compose up