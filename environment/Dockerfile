# hash:sha256:9f00dccac4546cbe0a36627e1bd7cce6b86776ffcbce51bff14358740ec7b1c2
ARG REGISTRY_HOST
FROM $REGISTRY_HOST/codeocean/jupyterlab:3.6.1-miniconda4.12.0-python3.9-ubuntu20.04

ARG DEBIAN_FRONTEND=noninteractive

ARG GIT_ASKPASS
ARG GIT_ACCESS_TOKEN
COPY git-ask-pass /

RUN apt-get update \
    && apt-get install -y --no-install-recommends \
        vim=2:8.1.2269-1ubuntu5.22 \
    && rm -rf /var/lib/apt/lists/*

RUN pip install -U --no-cache-dir \
    h5py==3.11.0
