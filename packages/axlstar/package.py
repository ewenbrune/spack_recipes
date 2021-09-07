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
import os

class Axlstar(CMakePackage):
    """Axl generator: a xml based code generator for Alien and Arcane."""

    homepage = "https://gitlab.com/cea-ifpen"
    url = "https://gitlab.com/cea-ifpen/axlstar/-/archive/v2.0.0/axlstar-v2.0.0.tar.bz2"
    git = "https://gitlab.com/cea-ifpen/axlstar.git"

    version("main", branch="main")

    version('2.0.0',sha256="3d4986360a3961274b808f08123a1587bffbbd39f1b77d1ac40db8e0f0b91b3c")

    depends_on("cmake@3.12:", type=("build", ))
    depends_on("arccon@1.1:", type=("build", ))
    depends_on("arcdependencies", type=("build"))
    depends_on("dotnet-core-sdk@3.1:", type=("build", "link", "run"))
