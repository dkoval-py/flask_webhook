What is this?
~~~~~~~~~~~~~

| Flask webhook 
| Flask application that cat read POST request from GitHub webhook and parce them

Installation
~~~~~~~~~~~~

Flask webhook requires Python 3.x.

.. code:: sh

    git clone https://github.com/dkoval-py/flask_webhook.git
    pip install -r requirements.txt

Run
~~~
| If you would like to run app in debug mode you should change the ``application/.env`` file.

| Run using python interpreter:
.. code:: sh

    python application/webhook.py

| Run using gunicorn as a deamon:
.. code:: sh

    gunicorn -b 0.0.0.0:5000 webhook:app --daemon
