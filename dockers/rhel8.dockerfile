FROM ecpe4s/rhel8-runner-x86_64

RUN mkdir -p /spack && useradd spack && chown -R spack: /spack

USER spack

# Download last release of spack and configure it to use buildcache
RUN curl -L https://github.com/spack/spack/releases/download/v0.16.3/spack-0.16.3.tar.gz | tar xz -C /spack --strip-components=1 && \
    source /spack/share/spack/setup-env.sh && \
    spack mirror add E4S https://cache.e4s.io && \
    spack buildcache keys -it && \
    spack config add packages:all:target:[x86_64]

# Copy this repo into the container
COPY --chown=spack:spack . /recipes

# setup our recipes
RUN source /spack/share/spack/setup-env.sh && \
    spack repo add /recipes

# Define and compile an alien environment    
RUN source /spack/share/spack/setup-env.sh && \
    spack env activate -d /recipes/envs/alien && \
    spack concretize -f && spack install
#    spack env activate --sh -d /recipes/envs/alien >> /etc/profile.d/alien.sh

# No proper arcane release yet.

# # Define and compile an arcane environment    
# RUN source /spack/share/spack/setup-env.sh && \
#     spack env activate -d /recipes/envs/arcane && \
#     spack concretize -f && spack install

# # Define and compile an arcane and alien environment    
# RUN source /spack/share/spack/setup-env.sh && \
#     spack env activate -d /recipes/envs/alien && \
#     spack concretize -f && spack install
