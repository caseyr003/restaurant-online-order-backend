FROM python:3.7-slim

# for flask web server
EXPOSE 5000

# add files
ADD ./app.py ./populate.py ./database.py ./requirements.txt /app/

# set working directory
WORKDIR /app

# install required libraries
RUN pip install -r requirements.txt

# set up sqlite database
RUN python database.py
RUN python populate.py

# This is the runtime command for the container
CMD python app.py
