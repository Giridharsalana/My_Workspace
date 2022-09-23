FROM gitpod/workspace-full

LABEL maintainer="giridharsalana@gmail.com"

# Install custom tools, runtime, etc.
RUN sudo apt-get update -y && sudo apt-get upgrade -y

# Install fish shell
RUN sudo apt-add-repository ppa:fish-shell/release-3 -y && \
	sudo apt update -y && \
	sudo apt install fish -y 

# Prerequisites
RUN sudo apt update && sudo apt install -y curl git unzip xz-utils zip libglu1-mesa wget

# Fish Shell
ENTRYPOINT [ "fish" ]
