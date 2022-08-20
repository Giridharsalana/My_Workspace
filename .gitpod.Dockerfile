FROM gitpod/workspace-full

LABEL maintainer="giridharsalana@gmail.com"

# Install custom tools, runtime, etc.
RUN sudo apt-get update -y && sudo apt-get upgrade -y 

# Install fish shell
RUN sudo apt-add-repository ppa:fish-shell/release-3 -y && \
	sudo apt update -y && \
	sudo apt install fish -y 

# Custom Setup Creation
RUN mkdir -p /home/$USER/.config/fish/
RUN echo "function c\n    clear\nend" > /home/$USER/.config/fish/config.fish
ENV SHELL /usr/bin/fish
ENV LANG=C.UTF-8 LANGUAGE=C.UTF-8 LC_ALL=C.UTF-8
ENTRYPOINT [ "fish" ]
