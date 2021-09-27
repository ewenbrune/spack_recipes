FROM ecpe4s/rhel8-runner-x86_64

RUN mkdir -p /spack && \
    curl -L https://github.com/spack/spack/releases/download/v0.16.3/spack-0.16.3.tar.gz | tar xz -C /spack --strip-components=1 && \
    source /spack/share/spack/setup-env.sh && \
    spack mirror add E4S https://cache.e4s.io && \
    spack buildcache keys -it && \
    spack config add packages:all:target:[x86_64]

COPY . /recipes

# setup our recipes
RUN source /spack/share/spack/setup-env.sh && \
    spack repo add /recipes
    
RUN source /spack/share/spack/setup-env.sh && \
    spack install --use-cache alien+hypre+petsc~xml~hdf5+move+ref

#RUN source /spack/share/spack/setup-env.sh && \
#    spack install arcane~wrapper~hwloc

