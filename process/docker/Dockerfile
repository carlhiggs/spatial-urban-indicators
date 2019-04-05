########################################################################
# Bangkok Liveability Dockerfile
#  - Modified by Carl Higgs 20190405
#      - added in the following packages to conda environment.yml:
#           - psycopg2 for Postgresql connection
#           - xlrd for opening .xlsx files in Pandas
#      - changed maintainer name
#  - Based on OSMNX Dockerfile, by Geoff Boeing
#  - see original OSMnx licence
#        - License: MIT, see full license in LICENSE.txt
#        - Web: https://github.com/gboeing/osmnx
#
# Build an image from the dockerfile:
# >>> docker build -t ind_bangkok .
#
# Run bash in this container and export final conda environment to a yml file:
# >>> docker run --rm -it -u 0 --name ind_bangkok -v %cd%:/home/jovyan/work ind_bangkok /bin/bash
# >>> conda env export -n base > /home/jovyan/work/environment.yml
#
# Run jupyter lab in this container:
# >>> docker run --rm -it --name ind_bangkok -p 8888:8888 -v %cd%:/home/jovyan/work ind_bangkok
#
# Stop/delete all local docker containers/images:
# >>> docker stop $(docker ps -aq)
# >>> docker rm $(docker ps -aq)
# >>> docker rmi $(docker images -q)
########################################################################

FROM jupyter/base-notebook
LABEL maintainer="Carl Higgs <carl.higgs@rmit.edu.au>"

# symlink and permissions
USER root
RUN ln -s /opt/conda/bin/jupyter /usr/local/bin
USER $NB_UID

# configure conda and install packages in one RUN to keep image tidy
RUN conda config --set show_channel_urls true && \
    conda config --prepend channels conda-forge && \
    conda update --strict-channel-priority --yes -n base conda && \
    conda install --strict-channel-priority --update-all --force-reinstall --yes osmnx python-igraph && \
    conda install -y psycopg2 && \
    conda install -y xlrd && \
    conda clean --yes --all && \
    conda info --all && \
    conda list

# launch notebook in the local working directory that we mount
WORKDIR /home/jovyan/work

# set default command to launch when container is run
CMD ["jupyter", "lab", "--no-browser", "--NotebookApp.token=''", "--NotebookApp.password=''"]

# to test, import OSMnx and print its version
RUN python -c "import osmnx; print(osmnx.__version__)"
