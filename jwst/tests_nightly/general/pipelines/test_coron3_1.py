import os
from astropy.io import fits as pf
from jwst.pipeline.calwebb_coron3 import Coron3Pipeline

BIGDATA = os.environ['TEST_BIGDATA']


def test_coron3_pipeline1():
    """Regression test of calwebb_coron3 pipeline.

    Test will be performed on NIRCam simulated data.
    """
    subdir = os.path.join(BIGDATA, 'nircam', 'test_coron3')
    asn_name = 'jw99999-a3001_20170327t121212_coron3_001_asn.json'
    asn_file = os.path.join(subdir, asn_name)
    Coron3Pipeline.call(asn_file, config_file='calwebb_coron3.cfg')

    # Compare psfstack product
    n_cur = 'jw99999-a3001_t1_nircam_f140m-maskbar_psfstack.fits'
    n_ref_name = 'jw99999-a3001_t1_nircam_f140m-maskbar_psfstack_ref.fits'
    n_ref = os.path.join(subdir, n_ref_name)
    print(' Fitsdiff comparison between the psfstack product file - a:', n_cur)
    print(' ... and the reference file - b:', n_ref)

    h = pf.open(n_cur)
    href = pf.open(n_ref)
    newh = pf.HDUList([h['primary'], h['sci'], h['err'], h['dq']])
    newhref = pf.HDUList([href['primary'], href['sci'],
                         href['err'], href['dq']])
    kws_to_ignore = ['DATE', 'CAL_VER', 'CAL_VCS', 'CRDS_VER', 'CRDS_CTX']

    result = pf.diff.FITSDiff(newh,
                              newhref,
                              ignore_keywords=kws_to_ignore,
                              rtol=0.00001)
    result.report()
    try:
        assert result.identical is True
    except AssertionError as e:
        print(result.report())
        raise AssertionError(e)

    # Compare psfalign product
    n_cur = 'jw9999947001_02102_00001_nrcb3_a3001_psfalign.fits'
    n_ref_name = 'jw99999-a3001_t1_nircam_f140m-maskbar_psfalign_ref.fits'
    n_ref = os.path.join(subdir, n_ref_name)
    print(' Fitsdiff comparison between the psfalign product file - a:', n_cur)
    print(' ... and the reference file - b:', n_ref)
    h = pf.open(n_cur)
    href = pf.open(n_ref)
    newh = pf.HDUList([h['primary'], h['sci'], h['err'], h['dq']])
    newhref = pf.HDUList([href['primary'],
                         href['sci'], href['err'], href['dq']])

    result = pf.diff.FITSDiff(newh,
                              newhref,
                              ignore_keywords=kws_to_ignore,
                              rtol=0.00001)
    result.report()
    try:
        assert result.identical is True
    except AssertionError as e:
        print(result.report())
        raise AssertionError(e)

    # Compare psfsub product
    n_cur = 'jw9999947001_02102_00001_nrcb3_a3001_psfsub.fits'
    n_ref_name = 'jw9999947001_02102_00001_nrcb3_psfsub_ref.fits'
    n_ref = os.path.join(subdir, n_ref_name)
    print(' Fitsdiff comparison between the psfsub product file - a:', n_cur)
    print(' ... and the reference file - b:', n_ref)

    h = pf.open(n_cur)
    href = pf.open(n_ref)
    newh = pf.HDUList([h['primary'], h['sci'], h['err'], h['dq']])
    newhref = pf.HDUList([href['primary'], href['sci'],
                          href['err'], href['dq']])

    result = pf.diff.FITSDiff(newh,
                              newhref,
                              ignore_keywords=kws_to_ignore,
                              rtol=0.00001)
    result.report()
    try:
        assert result.identical is True
    except AssertionError as e:
        print(result.report())
        raise AssertionError(e)

    # Compare level-2c product
    n_cur = 'jw9999947001_02102_00001_nrcb3_a3001_crfints.fits'
    n_ref_name = 'jw9999947001_02102_00001_nrcb3_a3001_crfints_ref.fits'
    n_ref = os.path.join(subdir, n_ref_name)
    print(' Fitsdiff comparison between the level-2c product file - a:', n_cur)
    print(' ... and the reference file - b:', n_ref)

    h = pf.open(n_cur)
    href = pf.open(n_ref)
    newh = pf.HDUList([h['primary'], h['sci'], h['err'], h['dq']])
    newhref = pf.HDUList([href['primary'], href['sci'],
                          href['err'], href['dq']])

    result = pf.diff.FITSDiff(newh,
                              newhref,
                              ignore_keywords=kws_to_ignore,
                              rtol=0.00001)
    result.report()
    try:
        assert result.identical is True
    except AssertionError as e:
        print(result.report())
        raise AssertionError(e)

    n_cur = 'jw9999947001_02102_00002_nrcb3_a3001_crfints.fits'
    h = pf.open(n_cur)
    n_ref = os.path.join(subdir,
                        'jw9999947001_02102_00002_nrcb3_a3001_crfints_ref.fits')
    print(' Fitsdiff comparison between the level-2c product file - a:', n_cur)
    print(' ... and the reference file - b:', n_ref)

    href = pf.open(n_ref)
    newh = pf.HDUList([h['primary'], h['sci'], h['err'], h['dq']])
    newhref = pf.HDUList([href['primary'], href['sci'],
                          href['err'], href['dq']])
    result = pf.diff.FITSDiff(newh,
                              newhref,
                              ignore_keywords=kws_to_ignore,
                              rtol=0.00001)

    result.report()
    try:
        assert result.identical is True
    except AssertionError as e:
        print(result.report())
        raise AssertionError(e)

    # Compare i2d product
    n_cur = 'jw99999-a3001_t1_nircam_f140m-maskbar_i2d.fits'
    n_ref = os.path.join(subdir,
                         'jw99999-a3001_t1_nircam_f140m-maskbar_i2d_ref.fits')
    print(' Fitsdiff comparison between the i2d product file - a:', n_cur)
    print(' ... and the reference file - b:', n_ref)

    h = pf.open(n_cur)
    href = pf.open(n_ref)

    newh = pf.HDUList([h['primary'], h['sci'],
                       h['con'], h['wht'], h['hdrtab']])
    newhref = pf.HDUList([href['primary'], href['sci'],
                          href['con'], href['wht'], href['hdrtab']])
    result = pf.diff.FITSDiff(newh,
                              newhref,
                              ignore_keywords=kws_to_ignore,
                              ignore_fields=kws_to_ignore,
                              rtol=0.00001)

    result.report()
    try:
        assert result.identical is True
    except AssertionError as e:
        print(result.report())
        raise AssertionError(e)