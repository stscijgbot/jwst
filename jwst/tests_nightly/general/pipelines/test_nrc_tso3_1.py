
import os
from astropy.io import fits as pf
from jwst.pipeline.calwebb_tso3 import Tso3Pipeline
# DISABLED
# import pandokia.helpers.filecomp as filecomp

BIGDATA = os.environ['TEST_BIGDATA']


def test_tso3_pipeline1():
    """Regression test of calwebb_tso3 pipeline on NIRCam simulated data.

    Default imaging mode outlier_detection will be tested here.
    """
    testname = "test_tso3_pipeline1"
    print("Running TEST: {}".format(testname))
    # Define where this test data resides in testing tree
    subdir = 'pipelines/nircam_caltso3/'  # Can NOT start with path separator

    # You need to have a tda dict for:
    #  - recording information to make FlagOK work
    #  - recording parameters to the task as attributes
    global tda
    tda = {}

    output = [
        # one dict for each output file to compare (i.e. each <val>)
        {
            'file'      : 'jw93065-a3001_t1_nircam_f150w-wlp8_phot.ecsv',
            'reference' : os.path.join(BIGDATA,subdir,'jw93065-a3001_t1_nircam_f150w-wlp8_phot_ref.ecsv'),
            'comparator': 'diff',
            'args'      : {},
        }
    ]

    try:
        os.remove("jw93065002001_02101_00001_nrca1_a3001_crfints.fits")
        os.remove("jw93065-a3001_t1_nircam_f150w-wlp8_phot.ecsv")
    except Exception:
        pass

    # Run pipeline step...
    asn_file = os.path.join(BIGDATA, subdir,
                            "jw93065-a3001_20170511t111213_tso3_001_asn.json")
    Tso3Pipeline.call(asn_file,
                      config_file='calwebb_tso3_1.cfg')

    # Compare level-2c product
    fname = 'jw93065002001_02101_00001_nrca1_a3001_crfints.fits'
    reffile = 'jw93065002001_02101_00001_nrca1_a3001_crfints_ref.fits'
    extn_list = ['primary', 'sci', 'dq', 'err']

    refname = os.path.join(BIGDATA, subdir, reffile)
    print(' Fitsdiff comparison between the level-2c file - a:', fname)
    print(' ... and the reference file - b:', refname)

    result = perform_FITS_comparison(fname, refname, extn_list=extn_list)
    result.report()
    try:
        assert result.identical is True
    except AssertionError as e:
        print(result.report())
        raise AssertionError(e)

    # compare the output files - use this exact command
    # DISABLED
    # filecomp.compare_files(output, (__file__, testname), tda=tda,)


def test_tso3_pipeline2():
    """Regression test of calwebb_tso3 pipeline on NIRCam simulated data.

    Scaled imaging mode outlier_detection will be tested here.
    """
    testname = "test_tso3_pipeline2"
    print("Running TEST: {}".format(testname))

    # Define where this test data resides in testing tree
    subdir = 'pipelines/nircam_caltso3/'  # Can NOT start with path separator

    # You need to have a tda dict for:
    #  - recording information to make FlagOK work
    #  - recording parameters to the task as attributes
    global tda
    tda = {}

    output = [
        # one dict for each output file to compare (i.e. each <val>)
        {
            'file'      : 'jw93065-a3002_t1_nircam_f150w-wlp8_phot.ecsv',
            'reference' : os.path.join(BIGDATA,subdir,'jw93065-a3002_t1_nircam_f150w-wlp8_phot_ref.ecsv'),
            'comparator': 'diff',
            'args'      : {},
        }
    ]

    try:
        os.remove("jw93065002002_02101_00001_nrca1_a3002_crfints.fits")
        os.remove("jw93065-a3002_t1_nircam_f150w-wlp8_phot.ecsv")
    except Exception:
        pass

    # Run pipeline step...
    asn_file = os.path.join(BIGDATA, subdir,
                            "jw93065-a3002_20170511t111213_tso3_001_asn.json")
    Tso3Pipeline.call(asn_file,
                      config_file='calwebb_tso3_2.cfg')

    # Compare level-2c product
    fname = 'jw93065002002_02101_00001_nrca1_a3002_crfints.fits'
    reffile = 'jw93065002002_02101_00001_nrca1_a3002_crfints_ref.fits'
    extn_list = ['primary', 'sci', 'dq', 'err']

    refname = os.path.join(BIGDATA, subdir, reffile)
    print(' Fitsdiff comparison between the level-2c file - a:', fname)
    print(' ... and the reference file - b:', refname)

    result = perform_FITS_comparison(fname, refname, extn_list=extn_list)
    result.report()
    try:
        assert result.identical is True
    except AssertionError as e:
        print(result.report())
        raise AssertionError(e)

    # compare the output files - use this exact command
    # DISABLED
    # filecomp.compare_files(output, (__file__, testname), tda=tda,)


# Utility function to simplify FITS comparisons
def perform_FITS_comparison(filename, refname, **pars):
    """Perform FITSDIFF comparison.

    Comparision will be done on `filename` in current directory with
        file that has same filename in `BIGDATA` directory.

        Parameters
        ----------
        filename : str
            Filename (no path) for file to be compared

        refname : str
            Full filename (with path) of file to be used as reference

        extn_list : list
            List of FITS extensions to include in comparison.
            Default: ['primary', 'sci', 'con', 'wht', 'hdrtab']

        ignore_kws : list
            List of header keywords to ignore during comparison
            Default: ['DATE','CAL_VER','CAL_VCS','CRDS_VER','CRDS_CTX']

        ignore_fields : list
            List of header keywords to ignore during comparison
            Default: ['DATE']

        rtol : float
            Level of difference below which constitutes agreement in values
            Default: 0.00001

        Returns
        -------
        result : obj
            astropy.io.fits.diff.FITSDIFF object with results of comparison

        filenames : list
            List of input and reference filenames used for comparison

    """
    extn_list = pars.get('extn_list',
                         ['primary', 'sci', 'con', 'wht', 'hdrtab'])
    ignore_kws = pars.get('ignore_kws',
                          ['DATE', 'CAL_VER', 'CAL_VCS',
                           'CRDS_VER', 'CRDS_CTX'])
    ignore_fields = pars.get('ignore_fields', ['DATE'])
    rtol = pars.get('rtol', 0.00001)

    # Compare resampled product
    h = pf.open(filename)
    href = pf.open(refname)
    newh = pf.HDUList([h[extn] for extn in extn_list])
    newhref = pf.HDUList([href[extn] for extn in extn_list])
    result = pf.diff.FITSDiff(newh,
                              newhref,
                              ignore_keywords=ignore_kws,
                              ignore_fields=ignore_fields,
                              rtol=rtol)
    return result