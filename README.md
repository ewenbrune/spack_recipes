# spack_recipes

Spack recipes for Arcane and Alien

You need at least `spack` version `0.23.1`

Before using spack, you have to add this directory to the spack repo list with the following command:

```{.sh}
spack repo add /path/to/this/repository
```

To compile Arcane in Debug mode:

```{.sh}
spack install arcane@extractConfig
```

To get install path:
```
spack location -i arcane
```
