########################################################################
# Bangkok Liveability Dockerfile
#  - Modified by Carl Higgs 20190405
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

# Install OpenJDK-8
RUN apt-get update \
 && apt-get install -y openjdk-8-jdk \
 && apt-get install -y ant \
 && apt-get install ca-certificates-java \
 && apt-get clean \
 && update-ca-certificates -f;

ENV JAVA_HOME /usr/lib/jvm/java-8-openjdk-amd64/
RUN export JAVA_HOME

# set locale
ENV TZ 'Australia/Melbourne'
RUN echo $TZ > /etc/timezone \ 
 && apt-get update && apt-get install -y tzdata \
 && rm /etc/localtime \
 && ln -snf /usr/share/zoneinfo/$TZ /etc/localtime \
 && dpkg-reconfigure -f noninteractive tzdata \
 && apt-get clean \
 && locale-gen en_AU.UTF-8 
 
ENV LC_ALL=en_AU.UTF-8  
ENV LANG=en_AU.UTF-8   
ENV LANGUAGE=en_AU.UTF-8
ENV PGCLIENTENCODING=UTF8
RUN export LC_ALL LANG LANGUAGE PGCLIENTENCODING

# Install OSM tools
RUN wget https://bretth.dev.openstreetmap.org/osmosis-build/osmosis-latest.tgz  \
 && mkdir osmosis                                                               \
 && mv osmosis-latest.tgz osmosis                                               \
 && cd osmosis                                                                  \
 && tar xvfz osmosis-latest.tgz                                                 \
 && rm osmosis-latest.tgz                                                       \
 && chmod a+x bin/osmosis                    

RUN apt-get install -y osm2pgsql

# install firefox for web automation (e.g. html to png)
RUN apt-get update && \
    apt-get install -y firefox

# Install tinytex, a minimal TeX distribution for making pdf documentation
RUN apt-get update && apt-get install -y perl wget libfontconfig1 && \
    wget -qO- "https://yihui.name/gh/tinytex/tools/install-unx.sh" | sh  && \
    apt-get clean
ENV PATH="${PATH}:bin"
RUN tlmgr install xetex xcolor pgf fancyhdr parskip babel-english  \ 
    units lastpage mdwtools comment genmisc  fontawesome times     \
    fncychap titlesec tabulary varwidth wrapfig capt-of needspace  \
    polyglossia fontspec cmap gnu-freefont \
 && fmtutil-sys --all

# instal the make build tools, for compiling sphinx documentation
RUN apt-get update && apt-get install -y make

# install fonts (including locale-specific)
RUN apt-get update && apt-get install -y fonts-unfonts-core fonts-unfonts-extra fonts-tlwg-loma fonts-tlwg-loma-otf fonts-thai-tlwg

# launch notebook in the local working directory that we mount
USER $NB_UID 
WORKDIR /home/jovyan/work

# configure conda and install packages
RUN conda config --set show_channel_urls true                                    \
 && conda config --prepend channels conda-forge                                  \
 && conda update --strict-channel-priority --yes -n base conda                   \
 && conda install --strict-channel-priority --update-all --force-reinstall --yes \ 
      osmnx python-igraph psycopg2 geoalchemy2 rasterio xarray                   \
      folium sphinx xlrd geckodriver selenium seaborn bokeh                      \
 && conda install -y --channel conda-forge --force-reinstall proj4=5.2.0         \
 && conda clean --yes --all                                                      \
 && conda info --all                                                             \
 && conda list

# add latex tools to path
ENV PATH=/home/jovyan/bin:$PATH

# install additional python libraries
# sphinx libraries are for documentation
# netcdf4 is for reading .nc files from Copernicus satellite data using xarray
RUN pip install sphinx_rtd_theme sphinxmark \
 && conda install -y netcdf4 basemap

# Add proj4 epsg codes to path (req'd for basemap)
ENV PATH = /usr/share/proj:$PATH

# set default command to launch when container is run
CMD ["jupyter", "lab", "--no-browser", "--NotebookApp.token=''", "--NotebookApp.password=''"]

# to test, import OSMnx and print its version
RUN python -c "import osmnx; print(osmnx.__version__)"
