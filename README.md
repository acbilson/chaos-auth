# chaos-auth
A Python Flask service to supply identity, authentication and authorization IndieWeb-style.

Thanks goes to [Beto Dealmeida](https://taoetc.org/) for being the first to publish an IndieAuth server for Flask, and one of the first to publish an IndieAuth server, period.

This iteration is (will be?) hosted by myself at https://auth.alexbilson.dev.

At least while I grasp the full extent of the IndieAuth spec, I'll be making changes which could lock the server to my personal use. If you plan to depend upon an IndieAuth server, it may be better to use Beto's if you experience trouble with mine. Someday I'll have it stable and open to all, but not today.

## Steps

1. Clone the code to your auth server of choice.
2. Add a config.toml file with your settings to the same directory as your app.py file. Use the config.toml.example template.
3. Configure your auth server behind a web proxy configured for https, such as Nginx.
3. Update your OAuth provider callback to your auth server. 

## Notes

For testing on http://localhost, you can remove the https requirement by setting the following environment variable:

```export OAUTHLIB_INSECURE_TRANSPORT=1```

(thanks to Sascha's [post](https://stackoverflow.com/questions/27785375/testing-flask-oauthlib-locally-without-https))

The OAuth provider callback is not obvious. The flask-dance package sets the callback url to /prefix/provider/authorized (e.g. /login/github/authorized).
