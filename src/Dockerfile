FROM python:3.6-slim-stretch

ADD requirements.txt /
RUN pip install -r /requirements.txt

ADD . /app
WORKDIR /app

EXPOSE 5000
CMD [ "python" , "app.py"]

# ## Run with Docker

# With **[Docker](https://www.docker.com)**, you can quickly build and run the entire application in minutes :whale:

# ```shell
# # 1. First, clone the repo
# $ git clone https://github.com/mtobeiyf/keras-flask-deploy-webapp.git
# $ cd keras-flask-deploy-webapp

# # 2. Build Docker image
# $ docker build -t keras_flask_app .

# # 3. Run!
# $ docker run -it --rm -p 5000:5000 keras_flask_app
# ```

# Open http://localhost:5000 and wait till the webpage is loaded.