FROM python:slim@sha256:27f90d79cc85e9b7b2560063ef44fa0e9eaae7a7c3f5a9f74563065c5477cc24
WORKDIR /app

# COPY DEPENDENCY FILE AND BUILD THE DEPENDENCIES
COPY requirements.txt ./app
RUN pip install -r requirements.txt

# COPY THE REST OF THE FILES INTO CONTAINER WORKING DIRECTORY
COPY quotes.json app.py /app/

EXPOSE 5000

# RUN THE APPLICATION
ENTRYPOINT [ "uvicorn", "app:app" ]

# --host 0.0.0.0 helps to run the application on all the address, else
# the application will only run on 127.0.0.1, which is useful when you
# run the application in local system
# --host 0.0.0.0 open the application to all interface ( lo, eth0 )
CMD [ "--reload", "--host", "0.0.0.0","--port 5000" ]
