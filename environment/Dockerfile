# hash:sha256:b0cf6ddf9c99fcc006da0a18317ed8ce71e221d285b29de06d32fa0763a4e3a5
ARG REGISTRY_HOST
FROM $REGISTRY_HOST/codeocean/mambaforge3:24.5.0-0-python3.12.4-ubuntu22.04

ARG DEBIAN_FRONTEND=noninteractive
ARG GIT_ASKPASS
COPY git-ask-pass /

RUN --mount=type=secret,id=git-access-token \
    GIT_ACCESS_TOKEN="$(cat /run/secrets/git-access-token)" \
    pip3 install -U --no-cache-dir \
    h5py==3.16.0 \
    -e git+https://github.com/AllenNeuralDynamics/aind-ophys-decrosstalk-split-session-json-library.git@4c62802#egg=aind-ophys-decrosstalk-split-session-json-library
