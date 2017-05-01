# Fraud detection
A simple API to detect credit card fraud based in network collisions

## Requirements
* python 2.7


## Instructions

1. Clone repository

		$ git clone https://github.com/rodrigues882013/fraud_detection.git
		$ cd fraud-detection/
 
2. Install Virtualenv
      
		$ curl -O https://pypi.python.org/packages/source/v/virtualenv/virtualenv-1.9.tar.gz
		$ tar xvfz virtualenv-1.9.tar.gz
		$ cd virtualenv-1.9
		$ python virtualenv.py /path/to/virtualenv/env

3. Switch to new virtualenv created and install requirements

		$ source /path/to/virtualenv/env/bin/active
		$ (env) pip install -r requirements.txt
    
       
5. Running migrations

		$ (env) python manage.py makemigrations
		$ (env) python manage.py migrate
       
6. Running the application

		$ (env) python manage.py runserver

By default django startup application in port 8000

7. Check if two nodes are in the same network collision:

        
		[POST] http://localhost:8000/api/v1/graph/collision/
		{
			"node1": 1,
			"node2": 2,
		}

If everthing is correct your should see the response like this:

		{
			"is_same_network": true
		}
       
Or

       [POST] http://localhost:8000/api/v1/graph/node/collision/
	   {
			"node1": 1,
			"node2": 10,
	   }
	   
In this operation two things are being make, creating new node with id=10 and after 
connect node 1 on node 2 creating the edge (1, 10) what mean that node 1 and node 10
are in the same network collision.


## Tests

For running tests running:

		$ python manage.py test
       

