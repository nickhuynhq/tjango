import environ

# Initialise environment variables
env = environ.Env()
environ.Env.read_env()

CLIENT_ID = env("CLIENT_ID")
CLIENT_SECRET = env("CLIENT_SECRET")
REDIRECT_URI = "http://127.0.0.1:8000/spotify/redirect"