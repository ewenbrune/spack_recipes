##############################################################################
# Copyright (c) 2013-2018, Lawrence Livermore National Security, LLC.
# Produced at the Lawrence Livermore National Laboratory.
#
# This file is part of Spack.
# Created by Todd Gamblin, tgamblin@llnl.gov, All rights reserved.
# LLNL-CODE-647188
#
# For details, see https://github.com/spack/spack
# Please also see the NOTICE and LICENSE files for our notice and the LGPL.
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU Lesser General Public License (as
# published by the Free Software Foundation) version 2.1, February 1999.
#
# This program is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the IMPLIED WARRANTY OF
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the terms and
# conditions of the GNU Lesser General Public License for more details.
#
# You should have received a copy of the GNU Lesser General Public
# License along with this program; if not, write to the Free Software
# Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA 02111-1307 USA
##############################################################################
from spack import *


class Arccore(CMakePackage):
    """Base functionalities for simulation codes."""
    homepage = "https://gitlab.com/cea-ifpen"
    url = "https://gitlab.com/cea-ifpen/arccore/-/archive/v1.2.4.0/arccore-v1.2.4.0.tar.gz"
    git = "https://gitlab.com/cea-ifpen/arccore.git"
    list_url = "https://gitlab.com/cea-ifpen/arccore/-/releases"
    list_depth = 1

    variant(
        "build_mode",
        default="Release",
        description="Arccore build type",
        values=("Debug", "Check", "Release"),
    )

    version(
        '2.0.0',
        sha256='fd385c961ca333757575a93bf1dbfe9417b8c3ff83d2d1956b5d4ed432c9bedc'
    )  # noqa: E501
    version(
        '2.0.1',
        sha256='d06508ff14d7f2b5e277fa5fc788eb7fd891886d7ffd65bee41c6a12d2ec58ae'
    )  # noqa: E501

    version('master', branch='master')
    version('main', branch='main')
    version('dev_cea', branch='dev/cea')

    variant('mpi', default=True, description='Use MPI')

    # Arccon must be exported to client
    depends_on("arccon", type=("build", "link"))
    depends_on("cmake@3.13:", type="build")
    depends_on('glib')
    depends_on('mpi', when='+mpi')

    def cmake_args(self):
        args = [
            self.define("BUILD_SHARED_LIBS", True),
            self.define_from_variant("ARCCORE_USE_MPI", "mpi"),
        ]

        args.append(
            self.define_from_variant("ARCCORE_BUILD_MODE", 'build_mode'))

        if "build_mode=Debug" in self.spec or "build_mode=Check" in self.spec:
            args.append(self.define("ARCCORE_CHECK", True))
        if "build_mode=Debug" in self.spec:
            args.append(self.define("ARCCORE_DEBUG", True))

        return args
