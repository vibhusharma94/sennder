Sennder [![](https://lh5.googleusercontent.com/-a0ef652_DMA/AAAAAAAAAAI/AAAAAAAAAAA/oh60-sy7sL0/s88-p-k-no-ns-nd/photo.jpg)](https://www.sennder.com/) 



Installation requires `python3` and `python3-dev`  
  
All the installation requirements are taken care by make file.  
  
To start development, create a virtual environment in python 3 and just do ``make develop``  
  
#### Tech used  
* Flask  
* Redis  
* Celery [ used optionally ]  
  
#### Architecture pattern  
* Code is inspired by Command BUS pattern but doesn't fully implement it to avoid unnecessary complexity for the rather simpler projects.  
* Controller[Resource] --> Handler[Business Logic] --> Repository[ Abstraction over DB like ORM ] --> DataStore [ Redis ]  
* It uses celery beat to schedule task to periodically fetch movie data but it's entirely optional because Redis has 1 min expiry time to make sure availability of latest data.  
  
  
#### Instructions for local development installation ####  
  
  
* Install requirements from virtualenv ``make develop``.  
  
  
#### Redis Local Setup * Using Redis as memory store and celery along with Redis as the broker  
* Install on macOS using `brew install Redis`  
* Make sure your Redis server is running on the default port `6379`  
  
  
#### Celery Local Setup * Using celery to periodically fetch movies data [ Optional ]  
* To start celery `make celery`  
  
#### Run the project  
  
Run the project by `make server` or `make server-uwsgi` and visit the site at `http://127.0.0.1:5000`  
  
  
#### Instructions for running/ debugging test(s) ####  
  
* Just run `pytest` to run the test cases and see coverage.   
* To run suite or a single test case.   
  Something like `pytest tests/resource/test_resource.py::BaseResourceTestCase` will work.   
  
  
#### Confusion  
requirements states - "Since accessing the API is a time-intensive operation, it should not happen on every page load. But on the other hand, movie fans are a very anxious crowd when it comes to new releases, so make sure that the information on the page is not older than 1 minute when the page is loaded."  
  
It does not explain how data should be refreshed every min and updated so I have implemented a celery scheduled task to fetch data in 1 min interval and WebSocket using asyncio to push refresh data to the client ( browser) if the page is already loaded.  
To run WebSocket server ``python ioserver.py``.  
  
#### Improvements  
* Code can be further improved by checking movies that are new and only sending those movies to the client.   
* Add more unit testing and Integration test if needed.   
* Better frontend UI and codebase.
* Docker setup
* Better Logging and error handling.
* Serve uwsgi behind Nginx proxy.