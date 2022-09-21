FROM giridharsalana/ubuntu-container:latest

LABEL maintainer="giridharsalana@gmail.com"

# Update
RUN sudo apt-get update -y && sudo apt-get upgrade -y 

ENTRYPOINT [ "fish" ]
