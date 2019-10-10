.PHONY: help

help:
	@echo 'Command:'
	@echo 'install    install the package.'
	@echo 'pack       pack the package only in local.'
	@echo 'upload     upload package to official pypi site.'
	@echo 'test       upload packge to test pypi site.'
	@echo 'clean      clean package files.'

install:
	python setup.py install

pack:
	python setup.py sdist --formats=gztar

upload:
	python setup.py sdist --formats=gztar
	twine upload dist/*

test:
	python setup.py sdist --formats=gztar
	python -m twine upload --repository-url https://test.pypi.org/legacy/ dist/*

clean:
	rm -rf dist *.egg-info build
	find . -name '*.py[co]' | xargs rm -f
