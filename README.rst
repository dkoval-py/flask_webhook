What is this?
~~~~~~~~~~~~~

| Flask webhook 
| Flask application that cat read POST request from GitHub webhook and parce them


Instalation
~~~~~~~~~~~
| Flask webhook application requires Python 3.x

.. code:: sh

    git clone https://github.com/dkoval-py/flask_webhook.git
    pip install -r requirements.txt


Run from source
~~~~~~~~~~~~~~~
| If you would like to run app in debug mode you should change the ``application/.env`` file.

* Run using python interpreter:
.. code:: sh

    python application/webhook.py

* Run using gunicorn as a deamon:
.. code:: sh

    gunicorn -b 0.0.0.0:5000 webhook:app --daemon


Run docker container
~~~~~~~~~~~~~~~~~~~~
| If you would like to run application as docker container, you can two choise:

* Run from source code:
.. code:: sh

    docker build --network host -t webhook:v1.1 .
    docker run -d -p 5000:5000 --restart unless-stopped webhook:v1.1

* Run from Docker image from DockerHub (in this case you don't need to make Instalation block):
.. code:: sh

   docker run -d -p 5000:5000 --restart unless-stopped dkovaldocker/flask-webhook:v1.1

