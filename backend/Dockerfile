ARG FUNCTION_DIR="/function"
FROM python:3.8-buster
ARG FUNCTION_DIR="/function"

COPY . ${FUNCTION_DIR}

WORKDIR ${FUNCTION_DIR}

RUN apt-get update \
    && apt-get install -y\
    g++ \
    make \
    wget \
    cmake \
    unzip \
    libcurl4-openssl-dev \
    python3 \
    python3-pip \
    && wget -O ./aws-lambda-rie https://github.com/aws/aws-lambda-runtime-interface-emulator/releases/latest/download/aws-lambda-rie \
    && pip install -r requirements.txt \
    && chmod a+x ./aws-lambda-rie \
    && chmod a+x ./lambda.sh

#ENTRYPOINT [ "python3","-m","awslambdaric" ]
ENTRYPOINT [ "./lambda.sh" ]