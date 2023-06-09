# Speed up your development with - _**Atlas + GCP App Engine**_

## Quickstart: 


### 1. Configure Atlas Environment


### 2. Google cloud setup


* Clone this repository on the Cloud terminal using below command.

  ```git clone  https://@github.com/theshanbhag/gen-ai-chatbot.git```

* Once All the above steps are complete we will navigate inside the cloned repo.
```cd Atlas-AppEngine-Integration/```
* Update the MongoDB URI in your config.txt file.
```vi config.txt```

* Finally deploy the application using:
```gcloud app deploy```
![img.png](images/img07.png)



### Verification

* The app can be accessed from the link generated from last step.
![img.png](images/img08.png)


* Open the link in new browser tab.
![img.png](images/img09.png)


* Create new entries in the sample App to verify the data is being written to MongoDB.

* Navigate to Atlas and see if the data is being written to MongoDB.