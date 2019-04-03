SETUP

clone this repository

install docker and docker-compose on your machine

use commands:
```
docker-compose up postgres
docker-compose up --build
and go to default IP http://192.168.99.100
```

API
```
  GET
    http://192.168.99.100/account - get all accounts
    http://192.168.99.100/payment - get all payments
```
```
  POST
    http://192.168.99.100/payment
    params (json):
      account - account id from
      to_account - account id to
      amount - amount of the payment
```
