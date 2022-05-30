ACTIVATE_VENV=. .venv/bin/activate
dev-env: clean
	python3 -m venv .venv
	$(ACTIVATE_VENV); pip3 install -r requirements.txt

clean:
	rm -rf .venv

run:
	$(ACTIVATE_VENV); PYTHONPATH=src CONFIG_FILE=src/config-prod.ini python main.py

refresh-token:
	# This command will pop up a URL that will take you to a page to hit accept.
    # The page will error out, but come back to the CLI and you'll have the token.
	$(ACTIVATE_VENV); PYTHONPATH=src python src/reddit/authorize.py $(CLIENT_ID) $(CLIENT_SECRET) $(USERNAME)
