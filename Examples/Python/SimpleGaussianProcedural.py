#!/usr/bin/env python
#=========================================================================
#
#  Copyright Insight Software Consortium
#
#  Licensed under the Apache License, Version 2.0 (the "License");
#  you may not use this file except in compliance with the License.
#  You may obtain a copy of the License at
#
#         http://www.apache.org/licenses/LICENSE-2.0.txt
#
#  Unless required by applicable law or agreed to in writing, software
#  distributed under the License is distributed on an "AS IS" BASIS,
#  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#  See the License for the specific language governing permissions and
#  limitations under the License.
#
#=========================================================================

from __future__ import print_function

import SimpleITK as sitk
import sys
import os

if len ( sys.argv ) < 4:
    print( "Usage: %s <input> <sigma> <output>" % ( sys.argv[0] ) )
    sys.exit ( 1 )


image = sitk.ReadImage( sys.argv[1] )

pixelID = image.GetPixelIDValue()

image  = sitk.SmoothingRecursiveGaussian( image,  float( sys.argv[2] ) )

sitk.WriteImage( sitk.Cast( image, pixelID ), sys.argv[3] )


if ( not "SITK_NOSHOW" in os.environ ):
    sitk.Show( sitk.Cast( image, pixelID ), "Simple Gaussian Procedural" )
