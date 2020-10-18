########################################################################
# Bangkok Liveability Dockerfile
#  - Modified by Carl Higgs 20190405
#  - Based on OSMNX Dockerfile, by Geoff Boeing
#  - see original OSMnx licence
#        - License: MIT, see full license in LICENSE.txt
#        - Web: https://github.com/gboeing/osmnx
#
# Build an image from the dockerfile:
# >>> docker build -t carlhiggs/ind_bangkok .
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
LABEL maintainer="Carl Higgs <carlhiggs@gmail.com>"

# set environment variables
ENV JAVA_HOME /usr/lib/jvm/java-8-openjdk-amd64/
ENV PGCLIENTENCODING=UTF8
# add bin to path so tex commands can be run fromm commandline
ENV PATH="${PATH}:bin"

USER root
RUN apt-get update                                                                               && \
    ln -s /opt/conda/bin/jupyter /usr/local/bin                                                  && \
    # Install OpenJDK-8
    apt-get install -y openjdk-8-jdk ant ca-certificates-java                                    && \
    update-ca-certificates -f                                                                    && \
    # Install required software
    apt-get install -y osm2pgsql firefox perl wget libfontconfig1 make wkhtmltopdf                  \
      fonts-unfonts-core fonts-unfonts-extra fonts-tlwg-loma fonts-tlwg-loma-otf fonts-thai-tlwg && \
    # install OSM tools
    wget https://github.com/openstreetmap/osmosis/releases/download/0.48.0/osmosis-0.48.0.tgz    && \
    mkdir osmosis                                                                                && \
    mv osmosis-0.48.0.tgz osmosis                                                                && \
    cd osmosis                                                                                   && \
    tar xvfz osmosis-0.48.0.tgz                                                                  && \
    rm osmosis-0.48.0.tgz                                                                        && \
    chmod a+x bin/osmosis                                                                        && \
    # install TinyTex
    wget -qO- "https://yihui.org/tinytex/install-bin-unix.sh" | sh                               && \
    /home/jovyan/bin/tlmgr install xetex xcolor pgf fancyhdr parskip babel-english                  \ 
        units lastpage mdwtools comment fontawesome times                                           \
        fncychap titlesec tabulary varwidth wrapfig capt-of needspace                               \
        polyglossia fontspec cmap gnu-freefont  oberdiek upquote latexmk makeindex                  \
        --repository=http://mirror.ctan.org/systems/texlive/tlnet                                && \
    /home/jovyan/bin/fmtutil-sys --all                                                           && \
    # Install conda packages
    conda config --set show_channel_urls true                                                    && \
    conda config --prepend channels conda-forge                                                  && \
    conda update --strict-channel-priority --yes -n base conda                                   && \
    conda install --strict-channel-priority --update-all --force-reinstall --yes                    \ 
        osmnx python-igraph psycopg2 geoalchemy2 rasterio folium sphinx xlrd selenium seaborn       \
        contextily rasterstats pandana  pyproj psutil geckdriver                                 && \
    conda clean --yes --all                                                                      && \
    conda info --all                                                                             && \
    conda list                                                                                   && \
    # additional Python libraries
    pip install sphinx_rtd_theme sphinxmark                                                      && \
    apt-get clean                                                               

# launch notebook in the local working directory that we mount
USER $NB_UID 
WORKDIR /home/jovyan/work

# add latex tools to path
ENV PATH=/home/jovyan/bin:$PATH

# Add proj4 epsg codes to path (req'd for basemap)
ENV PATH = /usr/share/proj:$PATH

# set default command to launch when container is run
CMD ["jupyter", "lab", "--no-browser", "--NotebookApp.token=''", "--NotebookApp.password=''"]

# to test, import OSMnx and print its version
RUN python -c "import osmnx; print(osmnx.__version__)"
