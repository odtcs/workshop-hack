docker build --tag odtcs-workshop-hack .
docker container rm odtcs-workshop-hack
docker run -p 80:80 --name odtcs-workshop-hack odtcs-workshop-hack
