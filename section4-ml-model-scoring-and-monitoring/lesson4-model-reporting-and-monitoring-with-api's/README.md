## Key Points

- API configuration: how to configure simple API's
    + In order to configure an API, you need to create a Python script. It's common to call this script app.py. These are the things you need to accomplish in your app.py script:
        + import needed capabilities from the flask module.
        + instantiate the app using the Flask() command.
        + specify an endpoint for users to interact with.
        + run the app using the run() method, specifying a host and a port.

- Endpoint scripting: how to create endpoint functions that provide meaningful information to API users
    + This endpoint contains a route ('/') and a simple Python function. These are required ingredients in every API endpoint.
    + API's with one simple endpoint can be useful. But it's often even more useful to have multiple, complex endpoints in an API. There's no limit to the number of endpoints an API can have, or what they can do. This part of the lesson is about how to create API's with multiple, complex endpoints, so they can be as useful as possible for your ML projects.

- Calling API's: how to call API's from Python scripts and the command line
    + API's are only useful if we call them. There are many kinds of API's, and several different ways to call them. In this lesson, we've created API's with the Flask module. Our Flask API's can be called in one of several different ways:
        + from the command line
            + You need to use the curl command to call API's from the terminal's command line. WHen you use curl, you need to specify 3 things to call an API:
                + An IP address or URL, like 127.0.0.1. This IP address is called the localhost IP: it always accesses the current machine where your code is running.
                + A port number, like 8000. This needs to be the same port that is mentioned in your app.py configuration file.
                + A query string: this is any string that you want to pass to your API to specify an endpoint and any argument your API endpoint needs
            + The following is a valid API call from the command line:
            ```
            curl 127.0.0.1:8000?user=brad
            ```
        + from a Python script
            + You can also call your API's from within a Python script. Just like a command line API call, you need to specify three important things:
                + an IP address or URL, like 127.0.0.1. This IP address is called the localhost IP: it always accesses the current machine where your code is running.
                + a port number, like 8000. This needs to be the same port that is mentioned in your app.py configuration file.
                + a query string: this is any string that you want to pass to your API to specify an endpoint and any argument your API endpoint needs
            + The following is an example of calling an API from a Python script:
            ```
            print(requests.get('http://127.0.0.1:8000?user=brad').content)
            ```
        + using a hybrid method - calling the command line from a Python script
            + Finally, you can use a hybrid method: calling the command line from within a Python script. Just like you needed in the previous methods, you'll need to specify all of these 3 things in your API call:
                + An IP address or URL, like 127.0.0.1. This IP address is called the localhost IP: it always accesses the current machine where your code is running.
                + A port number, like 8000. This needs to be the same port that is mentioned in your app.py configuration file.
                + A query string: this is any string that you want to pass to your API to specify an endpoint and any argument your API endpoint needs
            + The following is an example line that calls the command line from within a terminal script:
            ```
            response1=subprocess.run(['curl', '127.0.0.1:8000?user=brad'],capture_output=True).
            ```

- Different API protocols: information about other ways to set up advanced API capabilities
    + All of the API calls we've performed in this lesson have been a specific kind called "GET requests". GET requests are the simplest ways to call an API: they provide only a request to "get" some information. They're good for outputting information from the project to users.
    + However, in many cases, you'll want to input information: allow users to post new data or other files for your project to use. In this case, a GET request usually won't work, and you'll want to use another type of API call, a "POST request".
    + GET and POST are the two major types of API calls, and they're both referred to as API "methods".

## Key Terms

- In this lesson, we learned how to perform model reporting and monitoring with API's. We covered the following topics:
    + API configuration: how to configure simple API's
    + Endpoint scripting: creating multiple, complex endpoints for API's
    + Calling API's: how to call API's in several ways
    + Different API Methods: different ways that API's can be called to provide or receive information or files

- Here are terms that were introduced in this lesson:
    + flask: the module we used to create API's in Python
    + endpoint: a specification for how API users interact with an API
    + host: an IP address that specifies where an API will be hosted
    + port: a number that users and API's both need to specify in order to interact
    + route: the name by which a particular endpoint can be accessed by users
    + auxiliary function: a function that helps the rest of a script accomplish its purpose
    + return statement: a final line in a Python function that returns a specified value
    + localhost: a special IP address, 127.0.0.1, that refers to the machine where the code is currently running.
    + query string: a string that comes after an IP address or URL, and specifies arguments to be passed to an API
    + method: a standard procedure for calling an API in a particular way
    + GET: the default type of API call in Flask, used to obtain information from a project
    + POST: a type of API call used to upload information or files to a project
