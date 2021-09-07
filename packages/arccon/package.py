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


class Arccon(CMakePackage):
    """A CMake build system for HPC simulation codes."""

    homepage = "https://gitlab.com/cea-ifpen"
    url = "https://gitlab.com/cea-ifpen/arccon/-/archive/v1.0.0/arccon-v1.0.0.tar.bz2"
    git = "https://gitlab.com/cea-ifpen/arccon.git"

    version(
        '1.0.0',
        sha256="1f276325251c407c141cb6b5e223f06ac7ef41f128714d5d98d27b5d41b0dbcc"
    )  # noqa: E501
    version(
        '1.1.0',
        sha256="34434f8fdd21dc72668bdb02c77a917357d467c0646b9338199492d02c3681f5"
    )  # noqa: E501
    version(
        '1.2.0',
        sha256='1bef325e016439c479ae939262fc29927e1a08b7e827cce3f6aa84b0807c8ae9'
    )  # noqa: E501

    version('master', branch='master')
    version('main', branch='main')

    # FIXME: Add dependencies if required.
    depends_on('cmake@3.11:', type=("build", "link"))
