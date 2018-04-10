import os
from astropy.io import fits as pf
from jwst.saturation.saturation_step import SaturationStep

from ..helpers import add_suffix

BIGDATA = os.environ['TEST_BIGDATA']

def test_saturation_miri():
    """

    Regression test of saturation step performed on uncalibrated MIRI data.

    """
    output_file_base, output_file = add_suffix('saturation1_output.fits', 'saturation')

    try:
        os.remove(output_file)
    except:
        pass



    SaturationStep.call(BIGDATA+'/miri/test_saturation/jw00001001001_01101_00001_MIRIMAGE_dq_init.fits',
                       config_file='saturation.cfg',
                       output_file=output_file_base
    )
    h = pf.open(output_file)
    href = pf.open(BIGDATA+'/miri/test_saturation/jw00001001001_01101_00001_MIRIMAGE_saturation.fits')
    newh = pf.HDUList([h['primary'],h['sci'],h['err'],h['pixeldq'],h['groupdq']])
    newhref = pf.HDUList([href['primary'],href['sci'],href['err'],href['pixeldq'],href['groupdq']])
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