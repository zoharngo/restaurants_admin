FROM 2251985/restaurants_admin-base:latest
MAINTAINER Zohar Nyego <zoharngo@gmail.com>

# Copy application artifacts
COPY target /wheelhouse

# Install dev/build dependencies
RUN apt-get update && \
    apt-get install -qy gcc python-dev libmysqlclient-dev

# Install application
RUN . /appenv/bin/activate && \
    pip install --no-index -f /wheelhouse restaurants_admin && \
    rm -rf /wheelhouse
