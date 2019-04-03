SETUP

clone this repository

install docker and docker-compose on your machine

use commands:
```
docker-compose up postgres
docker-compose up --build
and go to default IP http://192.168.99.100
```


**Get available accounts**
----
  Returns json data about accounts.

* **URL**

  /account

* **Method:**

  `GET`
  
*  **URL Params**
  
  None

* **Data Params**

  None

* **Success Response:**

  * **Code:** 200 <br />
    **Content:** `{
        "id": "26271333-ad32-495d-9be6-511148572aaf",
        "balance": "0.00",
        "currency": "USD"
    }`
* **Error Response:**

  None
  
  
  
**Get payments**
----
  Returns json data about payments.

* **URL**

  /payment

* **Method:**

  `GET`
  
*  **URL Params**
  
  None

* **Data Params**

  None

* **Success Response:**

  * **Code:** 200 <br />
    **Content:** `{
        "id": 1,
        "amount": "123.12",
        "direction": 1,
        "tr_hash": "2df0fe0c-a7e9-41bf-918a-58bfe61d8abf",
        "account": "a22d244e-bc86-4f4e-8ce8-b087f6281011",
        "to_account": "a22d244e-bc86-4f4e-8ce8-b087f6281011"
    },`
* **Error Response:**

  None
