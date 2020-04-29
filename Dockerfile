FROM python:3.7

# set a directory for the app
WORKDIR /app

# copy all the files to the container
COPY . .

# install dependencies
RUN pip install pipenv
RUN pipenv install

# define the port number the container should expose
EXPOSE 5000

# run the command
CMD ["pipenv", "run", "python", "./run.py"]