## Key Points

- Review of Python Type Hints
```
from typing import Union

def foo(a: Union[list,str], b: int = 5) -> str:
    pass
```

- Fundamentals of FastAPI
    - FastAPI is a modern API framework that relies heavily on type hints for its capabilities.
    - As the name suggests, FastAPI is designed to be fast in execution and also in development. It is built for maximum flexibility in that it is solely an API. You are not tied into particular backends, frontends, etc. thus enabling composability with your favorite packages and/or existing infrastructure.
    - Getting started is as simple as writing a main.py containing:
```
from fastapi import FastAPI

# Instantiate the app.
app = FastAPI()

# Define a GET on the specified endpoint.
@app.get("/")
async def say_hello():
    return {"greeting": "Hello World!"}
```

    - To run our app, we will use uvicorn in our shell: uvicorn main:app --reload. By default, our app will be available locally at http://127.0.0.1:8000. The --reload allows you to make changes to your code and have them instantly deployed without restarting uvicorn.
    - FastAPI's type checking uses a mix of standard Python type hints in function definitions as well as the package Pydantic to define data models which define the types that are expected in a request body, like the following example:
```
# Import Union since our Item object will have tags that can be strings or a list.
from typing import Union 

from fastapi import FastAPI
# BaseModel from Pydantic is used to define data objects.
from pydantic import BaseModel

# Declare the data object with its components and their type.
class TaggedItem(BaseModel):
    name: str
    tags: Union[str, list] 
    item_id: int

app = FastAPI()

# This allows sending of data (our TaggedItem) via POST to the API.
@app.post("/items/")
async def create_item(item: TaggedItem):
    return item
```

    - This little bit of code unlocks many features such as converting the body to JSON, converting and validating types as necessary, and generating automatic documentation (which we can visit by going to 127.0.0.1:8000/docs or the equivalent URL when live).
    - This little bit of code unlocks many features such as converting the body to JSON, converting and validating types as necessary, and generating automatic documentation (which we can visit by going to 127.0.0.1:8000/docs or the equivalent URL when live).
```
# A GET that in this case just returns the item_id we pass, 
# but a future iteration may link the item_id here to the one we defined in our TaggedItem.
@app.get("/items/{item_id}")
async def get_items(item_id: int, count: int = 1):
    return {"fetch": f"Fetched {count} of {item_id}"}

# Note, parameters not declared in the path are automatically query parameters.
```

    - Path and query parameters are naturally strings since they are part of the endpoint URL. However, the type hints automatically convert the variables to their specified type. FastAPI automatically understands the distinction between path and query parameters by parsing the declaration. Note, to create optional query parameters use Optional from the typing module.
    - If we wanted to query the above API running on our local machine it would be via http://127.0.0.1:8000/items/42/?count=1.

- Local API Testing
    - As we saw previous running FastAPI locally is straight forward: uvicorn main:app --reload.
    - However, this is clunky, and likely impossible if we want to run our tests automatically in our Continuous Integration framework. To get around this FastAPI includes a built-in testing framework:
```
from fastapi.testclient import TestClient

# Import our app from main.py.
from main import app

# Instantiate the testing client with our app.
client = TestClient(app)

# Write tests using the same syntax as with the requests module.
def test_api_locally_get_root():
    r = client.get("/")
    assert r.status_code == 200
```

- Heroku Revisited
    - Install the Heroku CLI. I used the Ubunutu installation instructions: curl https://cli-assets.heroku.com/install.sh | sh
    - Type 'heroku' to see the full list of commands.
    - To create an app with a specific name and to specify it as Python app use: heroku create name-of-the-app --buildpack heroku/python
    - Note that manually specifying it as a Python app is not necessary. Heroku will automatically try and detect the language of your app. In the case of Python it searches for either a requirements.txt or setup.py.
    - We can view our apps buildpacks using heroku buildpacks --app name-of-the-app.
    - Now we'll initiate our folder as a git repository and commit it so we can connect it to our new Heroku app.
```
git init
git add *
git commit -m "Initial commit."
```

    - Connect the repo to our new app: heroku git:remote --app name-of-the-app.
    - The app will launch after a few moments.
    - Enter into the Heroku VM using: heroku run bash --app name-of-the-app.
    - There is not much to see here. Explore the various Unix commands such as pwd, and ls. Doing 'ls .. reveals many of the standard folders one would expect in a Unix environment. Note this is very lightweight, not even vi is included!

- Live API Testing

## Key Terms