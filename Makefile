.PHONY: setup

all:
	$(MAKE) -C cpp
	cd svelte; npx rollup -c
	
clean:
	rm -rf venv/ compile_commands.json .cache/ __pycache__/
	$(MAKE) -C cpp clean

cdb:
	$(MAKE) | compiledb -p-

setup:
	python3 -m venv venv
	venv/bin/pip3 install -r requirements.txt

test:
	$(MAKE) -C tests