from urllib.parse import urlparse
from application import create_app

app = create_app()

env = app.config['FLASK_ENV']
local = app.config['LOCAL']
remote = app.config['REMOTE']

local_url = urlparse(local)
host, port = local_url.netloc.split(':')

app.logger.info(f"Flask app running in {env} at {local}")
app.logger.info(f"View the site at {remote}")

if __name__ == "__main__":
    app.run(
        host=host,
        port=port,
        debug=(env == 'development')
        )
