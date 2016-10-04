# Pokemon Sample Application

A sample application created to use in the **Creating a Continuous Integration/Deployment System** workshop for the
**Grace Hopper Celebration of Women in Computing 2016**. This application returns a random starter Pokemon
as a web page and as an API call.


## Workshop Setup Steps
### Installation
* Download  and install [Docker Toolbox](https://www.docker.com/products/docker-toolbox)
* Download and unzip [ngrok](https://ngrok.com/)
* Fork this repository

### Windows/Mac Setup
* Open Kitematic, which is included in Docker Toolbox
* Open the Docker CLI in Kitematic
* Clone this repository or download the docker-compose.yml file from GitHub
* Navigate in the Docker CLI to where the docker-compose.yml is located and run `docker-compose up`
* The Jenkins, test environment, and production environment will be accessable through Kitematic 

### Linux Setup
* Clone this repository or download the docker-compose.yml file from GitHub
* Navigate to where the docker-compose.yml is located and run `docker-compose up`
* The jenkins and demo environments will be located at:
  * Jenkins: http://localhost:8080
  * Test Environment: http://localhost:5050
  * Production Environment: http://localhost:5000


## Aditional GitHub Integration Setup
#### Pull Request Status Updates
1. GitHub, go to *Settings -> Personal access tokens*
2. Click **Generate new token**
3. Give the token a description and click the checkbox for **repo:status**
4. Click **Generate token** and copy the created token
5. In Jenkins, go to  **Manage Jenkins -> Configure System**
6. Scroll down to **GitHub Pull Request Builder**
7. Click the **Add** button by **Credentials**
8. Select **Secret text** as **Kind**
9. Paste your access token into **Secret** and give it a name in the **ID**
10. Click **Add** and then select your created credential

#### Pull Request Webhook with Local Jenkins
1. Run ngrok to connect your local Jenkins to the internet using `./ngrok http <jenkins-ip>:8080`
2. Navigate to your forked repository on GitHub and go to **Settings -> Webhooks**
3. Copy your ngrok URL into the Payload URL  and add **/ghprbhook/** to the end. There *MUST* be a / at the end of the URL, otherwise you will get a 403 error.
4. Select **Let me select individual events** and check **Pull request**, **Pull request review comment**, and **Issue comment**.
5. For pull request jobs, under **Build Triggers**, check **Use github hooks for build triggering**.


#### Push Webhook with Local Jenkins
1. Create a second webhook with **/github-webhook/** at the end. Again, there *MUST* be a / at the end.
2. Select **Just the push event**
3. For the Trigger Pipeline job, check **Build when a change is pushed to GitHub**.


## Running Application Locally
If you would like to run the web application outside of the Docker enviornmnets, you can use the following steps.
### To Run
```
pip install -r requirements.txt
python pokestarter/app.py
```

#### Homepage
Open a browser and navigate to http://localhost:5000.

#### API
**Request**
```
curl http://localhost:5000/api
```
**Response**
```
{
  "pokemon": "Squirtle"
}
```

### To Test
```
pip install -r test-requirements.txt
nosetests -sv tests/unit
nosetests -sv tests/functional
```
