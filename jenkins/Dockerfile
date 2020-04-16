FROM jenkins/jenkins:lts

USER root
RUN apt update
RUN apt install tox -y

# Terraform
RUN wget https://releases.hashicorp.com/terraform/0.12.24/terraform_0.12.24_linux_amd64.zip
RUN unzip terraform_0.12.24_linux_amd64.zip
RUN mv terraform /usr/local/bin

# Kubectl
RUN wget https://storage.googleapis.com/kubernetes-release/release/v1.16.6/bin/linux/amd64/kubectl
RUN chmod +x kubectl
RUN mv kubectl /usr/local/bin
RUN kubectl version --client

# DOctl
RUN wget https://github.com/digitalocean/doctl/releases/download/v1.40.0/doctl-1.40.0-linux-amd64.tar.gz
RUN tar xf doctl-1.40.0-linux-amd64.tar.gz
RUN mv doctl /usr/local/bin
RUN doctl --help



