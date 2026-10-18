# hash:sha256:3d2f05459373e4704dd1d91b749821a07cca49b2e8e771a6cf31131eaabcf835
ARG REGISTRY_HOST
FROM $REGISTRY_HOST/codeocean/mambaforge3:24.5.0-0-python3.12.4-ubuntu22.04

ARG DEBIAN_FRONTEND=noninteractive
ARG GIT_ASKPASS
COPY git-ask-pass /

RUN pip install -U --no-cache-dir \
    h5py

RUN --mount=type=secret,id=git-access-token \
    GIT_ACCESS_TOKEN="$(cat /run/secrets/git-access-token)" \
    pip3 install -U --no-cache-dir \
    -e git+https://github.com/AllenNeuralDynamics/aind-ophys-decrosstalk-split-session-json-library.git@%3Cshort-sha%3E#egg=aind-ophys-decrosstalk-split-session-json-library
