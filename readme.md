# TinyURL API

## Requirements
 
1. Python (pip if python version is < 3)
2. Redis
3. Docker

## Run instructions

Navigate to the root of the project.

To run the app run the following commands
```
docker-compose up
```
navigate to the below url to view documentation and test enpoint
```
http://localhost:5000/api/docs
```

## Design Considerations

* This application is a TinyURL api created using python and a redis database.

* The redis database uses the shortend url as the key and stores metadata relating to the short url as the value.

* The used-count of a shortend url is increamented only when called by the /getLongURL as this is what I have assumed to be a use of the tiny url. 

* In this implementation if a long url has already been shortened, you cannot generate another shortened url for it. However this can easily be modified by changing the hashing funtion and adding some randomness to it. 

* In this implementation there is no authentication required to generated a shortened url, but that should be added to improve security.

* Somethings to consider when scaling this application:
    1. There should be an LFU cache with a set expiration time so that we do not have to repeatedly get the data from our redis instance
    2. There should also be a small set of pregenerated shortedURL that can be used so that we dont have to spend time generating a shortened url when /generateShortURL request is recieved.
    3. URLs have created date as a field, periodically the database should remove old records as a background task (the meaning of "old" is subject to requirements of the application) 
