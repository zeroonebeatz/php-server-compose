all: build symlink

build:
	./main.py

symlink:
	ln -sf $$(pwd)/tmp/docker-compose.yml $$(pwd)/../docker-compose.yml
