FROM ecpe4s/rhel8-runner-x86_64

COPY dockers/spack-0.16.2.patch /

RUN mkdir -p /spack && \
    curl -L https://github.com/spack/spack/releases/download/v0.16.2/spack-0.16.2.tar.gz | tar xz -C /spack --strip-components=1 && \
    cd /spack && patch -p1 /spack-0.16.2.patch && \
    source /spack/share/spack/setup-env.sh && \
    spack mirror add E4S https://cache.e4s.io && \
    spack buildcache keys -it && \
    spack config add packages:all:target:[x86_64]

COPY . /recipes

RUN source /spack/share/spack/setup-env.sh && \
    spack repo add /recipes && \
    spack install --only dependencies --use-cache alien
    

