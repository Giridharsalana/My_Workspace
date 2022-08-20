FROM giridharsalana/ubuntu-container:latest

LABEL maintainer="giridharsalana@gmail.com"

# Install custom tools, runtime, etc.
RUN sudo apt-get update -y && sudo apt-get upgrade -y 

ENTRYPOINT [ "bash" ]
