FROM docker.io/jupyter/datascience-notebook:latest

RUN mamba install --yes 'py-xgboost' && \
    mamba install --yes 'polars' && \
    mamba clean --all -f -y && \
    fix-permissions "${CONDA_DIR}" && \
    fix-permissions "/home/${NB_USER}"

RUN mamba install --yes \
    'r-cowplot' \
    'r-languageserver' \
    'r-gtsummary' && \
    mamba clean --all -f -y && \
    fix-permissions "${CONDA_DIR}" && \
    fix-permissions "/home/${NB_USER}"

RUN julia -e 'using Pkg; Pkg.add(["HTTP", "CSV", "DataFrames", "Tidier", "DataFramesMeta", "RDatasets", "RCall", "Distributions", "GLM", "Plots", "StatsBase", "StatsModels", "StatsPlots"])'

USER root
# Generally, Dev Container Features assume that the non-root user (in this case jovyan)
# is in a group with the same name (in this case jovyan). So we must first make that so.
RUN groupadd jovyan \
    && usermod -g jovyan -a -G users jovyan

USER jovyan
