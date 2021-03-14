from flask import Flask, request
from dotenv import load_dotenv
from werkzeug.middleware.dispatcher import DispatcherMiddleware
from prometheus_client import make_wsgi_app
import os, json


app = Flask(__name__)
load_dotenv() # Initialize variables from .env file


# Add prometheus wsgi middleware to route /metrics requests
app.wsgi_app = DispatcherMiddleware(app.wsgi_app, {
    '/metrics': make_wsgi_app()
})

@app.route('/', methods=['POST'])
def web_hook():
    try:
        data = json.loads(request.data)
    except ValueError:
        return False
    else:
        branch_name = data['ref'].split('/')[2]

    # Block for debug regime
    if os.getenv('ENV') == 'Dev':
        input_file = 'input.txt'
        try: 
            # Write all json input data from GitHub to a file input.txt
            with open(input_file, 'a', encoding='utf-8') as inp:
                json.dump(data, inp)
        except EnvironmentError:
            with open(input_file, 'a', encoding='utf-8') as inp:
                inp.write('Error: Write out to file failed')        

    # Check from which branch webhook has been triggered
    if branch_name == 'main' or branch_name == 'master':
        print('This is a master branch')
    else:    
        print(f'THis is a {branch_name} branch')

    return 'Ok'


if __name__ == '__main__':
    app.run(port=os.getenv('PORT'), host=os.getenv('HOST'))
