
.PHONY: venv
venv: .venv
	@echo "Virtual environment is ready."

.venv: requirements.txt
	python3 -m venv .venv
	@echo "Virtual environment created."
	. .venv/bin/activate && pip install -r requirements.txt
	@touch .venv

.PHONY: run
run: venv src/generate.py
	@echo "Running..."
	@if [ ! -f .env ]; then \
		echo "WARNING: .env file does not exist! 'example.env' copied to '.env'. Please update the configurations in the .env file running this target."; \
		cp example.env .env; \
		exit 1; \
	fi
	. .venv/bin/activate && python3 src/generate.py
	@echo "Finished."


.PHONY: start
start: run

.PHONY: up
up: run
