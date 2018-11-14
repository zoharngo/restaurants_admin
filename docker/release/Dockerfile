FROM 2251985/restaurants_admin-base:latest
MAINTAINER Zohar Nyego <zoharngo@gmail.com>

# Copy application artifacts
COPY target /wheelhouse

# Install application
RUN . /appenv/bin/activate && \
    pip install --no-index -f /wheelhouse restaurants_admin && \
    rm -rf /wheelhouse

COPY scripts/release.sh /usr/local/bin/release.sh
COPY scripts/wait_for_it.sh /usr/local/bin/wait_for_it.sh
RUN chmod +x /usr/local/bin/release.sh
RUN chmod +x /usr/local/bin/wait_for_it.sh

# Set defaults for entrypoint and command string
ENTRYPOINT ["release.sh"]