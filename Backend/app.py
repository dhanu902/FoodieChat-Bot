'''from openai import OpenAI
import os                       # <------ API key is stored as local env variable. cuz its a secret key. so need this
from dotenv import load_dotenv  # <------ to call .env

load_dotenv()

print(os.environ["OPENAI_API_KEY"])             # <------ DEBUG..!! check api key load
OPENAI_API_KEY = os.environ["OPENAI_API_KEY"]   # <------ load the API key here

Client = OpenAI()                               # <------ create object to OpenAI class

'''

from flask import Flask
from dotenv import load_dotenv
import os
from Routes.Search import search_bp

# Load environment variables
load_dotenv()

def create_app():
    app = Flask(__name__)

    # Register Blueprints
    app.register_blueprint(search_bp)

    return app

if __name__ == "__main__":
    app = create_app()
    app.run(debug=True)