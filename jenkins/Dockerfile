FROM jenkins/jenkins:lts

USER root
RUN apt update
RUN apt install tox -y
RUN wget https://releases.hashicorp.com/terraform/0.12.24/terraform_0.12.24_linux_amd64.zip
RUN unzip terraform_0.12.24_linux_amd64.zip
RUN mv terraform /usr/local/bin



