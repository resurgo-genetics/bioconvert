from biokit.converters.yaml2json import YAML2JSON
from biokit import biokit_data
from easydev import TempFile, md5


import pytest
import os
skiptravis = pytest.mark.skipif( "TRAVIS_PYTHON_VERSION" in os.environ and 
    os.environ['TRAVIS_PYTHON_VERSION'].startswith("2"), reason="On travis")


@skiptravis
def test_conv():
    infile = biokit_data("converters/test_v1.yaml")
    expected_outile = biokit_data("converters/test_v1.json")
    with TempFile(suffix=".json") as tempfile:
        convert = YAML2JSON(infile, tempfile.name)
        convert()

        # Check that the output is correct with a checksum
        # Note that we cannot test the md5 on a gzip file but only 
        # on the original data. This check sum was computed
        # fro the unzipped version of biokit/data/converters/measles.bed
        assert md5(tempfile.name) == md5(expected_outile)
