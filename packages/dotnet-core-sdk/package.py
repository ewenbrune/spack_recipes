# Copyright 2013-2019 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from os import symlink
from spack import *


class DotnetCoreSdk(Package):
    """The .NET Core SDK is a powerful development environment to write
    applications for all types of infrastructure."""

    homepage = "https://www.microsoft.com/net/"
    git = "https://github.com/dotnet/core.git"
    # From https://github.com/dotnet/dotnet-docker/blob/main/src/sdk/3.1/focal/amd64/Dockerfile
    url = "https://dotnetcli.azureedge.net/dotnet/Sdk/3.1.414/dotnet-sdk-3.1.414-linux-x64.tar.gz"

    version('2.1.300',
            url='https://download.microsoft.com/download/8/8/5/88544F33-836A'
            '-49A5-8B67-451C24709A8F/dotnet-sdk-2.1.300-linux-x64.tar.gz',
            sha256=
            'fabca4c8825182ff18e5a2f82dfe75aecd10260ee9e7c85a8c4b3d108e5d8e1b')

    version('3.1.101',
            url='https://download.visualstudio.microsoft.com/download/pr/c4b'
            '503d6-2f41-4908-b634-270a0a1dcfca/c5a20e42868a48a2cd1ae27cf'
            '038044c/dotnet-sdk-3.1.101-linux-x64.tar.gz',
            sha512='eeee75323be762c329176d5856ec2ecfd16f06607965614df006730e'
            'd648a5b5d12ac7fd1942fe37cfc97e3013e796ef278e7c7bc4f32b86'
            '80585c4884a8a6a1')

    version(
        '3.1.414',
        sha512=
        'f0a133a2bfbbdb6e3f35ad543bfd8e48f35e2a0e0bd719f712853d686e5f453b89569504813fde33baf8788dfe509bb3bc7ad69026588761f0a07362eac76104',
        when="target=x86_64")

    version(
        '3.1.414',
        url=
        'https://dotnetcli.azureedge.net/dotnet/Sdk/3.1.414/dotnet-sdk-3.1.414-linux-arm64.tar.gz',
        sha512=
        '42b526d4ae914a0f1b04cbefe70b2c052eae9791dce54431ee5aff2e1bba5dbd08f49505a835319dab0551e9e9788f239e53ac154760cc8c0a85512cbe568408',
        when="target=aarch64")

    variant('telemetry',
            default=False,
            description='allow collection of telemetry data')

    def setup_environment(self, spack_env, run_env):
        if '-telemetry' in self.spec:
            spack_env.set('DOTNET_CLI_TELEMETRY_OPTOUT', 1)

    def install(self, spec, prefix):
        mkdirp('bin')
        symlink('../dotnet', 'bin/dotnet')
        install_tree(".", prefix)
