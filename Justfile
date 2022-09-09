set dotenv-load
set shell := ["/opt/homebrew/bin/fish", "-c"]

# instantiates a local python virtualenv
init:
	if not test -d src/venv; python -m venv src/venv; end;
	if not test -d src/venv/lib/python3.10/site-packages/werkzeug; echo 'install packages to continue'; end

# tests that we're using a virtualenv
venv:
	if test (which python) = "/usr/local/bin/python"; echo 'not a virtualenv, please activate' && return 1; else; return 0; end

# runs a local development instance
run: init venv
	python src/main.py

# builds a development docker image.
build:
  set COMMIT_ID (git rev-parse --short HEAD); \
  docker build \
  --target dev \
  -t acbilson/auth:latest \
  -t acbilson/auth:$COMMIT_ID .

# starts a development docker image.
start:
  docker run --rm \
  --expose $EXPOSED_PORT -p $EXPOSED_PORT:80 \
  -e "SITE=$SITE" \
  -e "FLASK_SECRET_KEY=$FLASK_SECRET_KEY" \
  -e "SESSION_SECRET=$SESSION_SECRET" \
  -e "ADMIN_USER=$ADMIN_USER" \
  -e "ADMIN_PASSWORD=$ADMIN_PASSWORD" \
  -v $SOURCE_PATH/src:/mnt/src \
  --name auth \
  acbilson/auth:latest

# runs smoke tests on local docker image
smoke:
	set TOKEN (xh -b GET "http://localhost:7000/token" --auth "$ADMIN_USER:$ADMIN_PASSWORD" | jq -r .token) && xh GET "http://localhost:7000/auth" Authorization:"Bearer $TOKEN"
