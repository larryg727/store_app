from store import app
import os

if __name__ == '__main__':
    if os.getenv("ENVIRONMENT") == 'dev':
        app.debug = True
    app.run()
