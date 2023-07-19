# spack_recipes

Spack recipes for Arcane and Alien

TODO: explain how to add this repo to spack

## Arcane

To compile Arcane with 'Mono' support, we need to t specify the constraint `^cmake~openssl`

To compile Arcane in Debug mode:

```{.sh}
spack install arcane build_type=Debug ^arccore build_mode=Debug
```

To compile Arcane in Check mode:

```{.sh}
spack install arcane ^arccore build_mode=Check
```

To compile Arcane in Release mode:

```{.sh}
spack install arcane ^arccore build_mode=Release
```

To compile Arcane in Debug mode, with `gcc 11.3` and `mpich 4.1`:

```{.sh}
spack install arcane build_type=Debug %gcc@11.3.0 ^arccore build_mode=Debug build_type=Debug ^mpich@4.1
```

Note that `arccore` will automatically be set to `build_mode=Debug` when asking for `arcane build_type=Debug`.
