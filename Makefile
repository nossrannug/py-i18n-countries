.PHONY: build

clean:
	@rm -rf build
	@rm -rf dist
	@rm -rf src/py_i18n_countries.egg-info
	@rm -rf py_i18n_countries.egg-info

build:
	@make clean
	@python setup.py bdist_wheel