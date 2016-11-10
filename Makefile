HOST=127.0.0.1
TEST_PATH=./

TEXT=http://krzysztofzuraw.com/blog/2016/makefiles-in-python-projects.html

.PHONY: clean-pyc clean-build

clean-pyc:
	find . -name '*.pyc' -exec rm --force {} +
	find . -name '*.pyo' -exec rm --force {} +
	find . -name '*~' -exec rm --force  {} +

clean-build:
	rm --force --recursive build/
	rm --force --recursive dist/
	rm --force --recursive *.egg-info

isort:
	sh -c "isort --skip-glob=.tox --recursive . "

lint:
	flake8 --exclude=.tox

test: clean-pyc
	py.test --verbose --color=yes $(TEST_PATH)

run:
	python manage.py runserver

docker-run:
	docker build \
      --file=./Dockerfile \
      --tag=my_project ./
	docker run \
      --detach=false \
      --name=my_project \
      --publish=$(HOST):8080 \
      my_project

help:
	@echo "    clean-pyc"
	@echo "        Remove python artifacts."
	@echo "    clean-build"
	@echo "        Remove build artifacts."
	@echo "    isort"
	@echo "        Sort import statements."
	@echo "    lint"
	@echo "        Check style with flake8."
	@echo "    test"
	@echo "        Run py.test"
	@echo '    run'
	@echo '        Run the `my_project` service on your local machine.'
	@echo '    docker-run'
	@echo '        Build and run the `my_project` service in a Docker container.'
