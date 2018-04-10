import os
from astropy.io import fits as pf
from jwst.flatfield.flat_field_step import FlatFieldStep

from ..helpers import add_suffix

BIGDATA = os.environ['TEST_BIGDATA']

def test_flat_field_niriss():
    """

    Regression test of flat_field step performed on NIRISS data.

    """
    output_file_base, output_file = add_suffix('flatfield1_output.fits', 'flat_field')

    try:
        os.remove(output_file)
    except:
        pass



    FlatFieldStep.call(BIGDATA+'/niriss/test_flat_field/jw00034001001_01101_00001_NIRISS_ramp_fit.fits',
                       output_file=output_file_base
                       )
    h = pf.open(output_file)
    href = pf.open(BIGDATA+'/niriss/test_flat_field/jw00034001001_01101_00001_NIRISS_flat_field.fits')
    newh = pf.HDUList([h['primary'],h['sci'],h['err'],h['dq']])
    newhref = pf.HDUList([href['primary'],href['sci'],href['err'],href['dq']])
    result = pf.diff.FITSDiff(newh,
                              newhref,
                              ignore_keywords = ['DATE','CAL_VER','CAL_VCS','CRDS_VER','CRDS_CTX'],
                              rtol = 0.00001
    )
    result.report()
    try:
        assert result.identical == True
    except AssertionError as e:
        print(result.report())
        raise AssertionError(e)