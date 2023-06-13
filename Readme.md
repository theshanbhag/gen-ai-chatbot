
## Quickstart: 


### 1. Configure Atlas Environment


### 2. MongoDB setup


* Clone this repository on the Cloud terminal using below command.

  ```git clone  https://@github.com/theshanbhag/gen-ai-chatbot.git```

* Update the mongodb srv of your cluster in main.py file.
* Create a database with name "XYZ-Corp" in your MongoDB cluster with collection Customer.
* Add a sample document to it:
  ```
   {
    "_id":{"$oid":"6488127b353fb41c00a9650b"},
    "customer_id":"111",
    "conversation":[],
    "Name":"Venkatesh Shanbhag"
   } 
  ```
* Create a collection with name Insurance and add below document to it.
  ```
  {
  "_id":{"$oid":"64881424353fb41c00a9650c"},
  "context":"You are a Customer support agent with name Sara working for XYZ-corp.\nIt does provides property Insurance. Sara will not reply for any queries regarding other types of insurance.\nThe company covers insurance of properties like - Hospitals, offices, shops, apartments.\nMax insurance covered will decline over period of time.\nXYZ-Corp only covers Fire and Earthquake hazard insurance. \nYou are allowed to provide only the details regarding the company itself.\nDo not repond with sentiment in any of the responses.",
  "type":"Intro"
  }
  ```
* Create a collection with name Claims and add below document:
  ```
  {"_id":{"$oid":"64881476353fb41c00a9650d"},
  "claim_number":"12345",
  "Name":"Venkatesh Shanbhag",
  "Claim_amount":{"$numberLong":"10000"},
  "Currency":"USD",
  "Claim_status":"In progress","customer_id":"111"
  }
  ```
* Set up a search index with name 'default' on Claims collection. follow the search setup documentation: https://www.mongodb.com/docs/atlas/atlas-search/create-index/

### 3. Google cloud setup

* Update the project name.

Run the application:

```commandline
python3 main.py
```