# spack_recipes

Spack recipes for Arcane and Alien

You need at least `spack` version `0.23.1`

Before using spack, you have to add this directory to the spack repo list with the following command:

```{.sh}
spack repo add /path/to/this/repository
```

To compile Arcane in Debug mode:

```{.sh}
spack install arcane build_type=Debug build_mode=Debug
```

To compile Arcane in Check mode:

```{.sh}
spack install arcane build_mode=Check
```

To compile Arcane in Release mode:

```{.sh}
spack install arcane build_mode=Release
```

To compile Arcane with Alien

```{.sh}
spack install arcane +alien
```

To compile Arcane using GCC with CUDA support using Clang as CUDA compiler

```{.sh}
spack -v install arcane build_type=Debug ~mpi ~hdf5 ~dotnet_wrapper cuda_arch=75 +cuda +cuda_clang %gcc
```
