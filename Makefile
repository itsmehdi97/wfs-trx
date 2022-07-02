all: test

test:
	find . -name "*.pyc" -type f -delete
	tox

upload:
	python3.9 setup.py sdist bdist_wheel
	twine upload dist/*$(shell python3 setup.py --version)*
