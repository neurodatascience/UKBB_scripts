# This file has been modified from its original form.
# Data was originally taken from: https://git.fmrib.ox.ac.uk/falmagro/UK_biobank_pipeline_v_1/blob/master/bb_data/UKBB_to_BIDS.json
# It was modified to default to relative pathing (without "BIDS/" top-level directory)

bids_dict = {"SWI/MAG_TE1/SWI_3MM_UPDATED_V1.1_COIL26_ECHO1_17.nii.gz": "sub-@SUBJECT@/anat/sub-@SUBJECT@_acq-magCoil26Echo1_SWImagandphase.nii.gz", "SWI/PHA_TE2/SWI_3MM_UPDATED_V1.1_COIL21_ECHO2_20.nii.gz": "sub-@SUBJECT@/anat/sub-@SUBJECT@_acq-phaCoil21Echo2_SWImagandphase.nii.gz", "SWI/PHA_TE1/SWI_3MM_UPDATED_V1.1_COIL15_ECHO1_20.nii.gz": "sub-@SUBJECT@/anat/sub-@SUBJECT@_acq-phaCoil15Echo1_SWImagandphase.nii.gz", "T1/T1.nii.gz": "sub-@SUBJECT@/anat/sub-@SUBJECT@_T1w.nii.gz", "dMRI/raw/PA.nii.gz": "sub-@SUBJECT@/dwi/sub-@SUBJECT@_acq-PA_dwi.nii.gz", "SWI/PHA_TE1/SWI_3MM_UPDATED_V1.1_COIL09_ECHO1_20.nii.gz": "sub-@SUBJECT@/anat/sub-@SUBJECT@_acq-phaCoil09Echo1_SWImagandphase.nii.gz", "SWI/MAG_TE2/SWI_3MM_UPDATED_V1.1_COIL08_ECHO2_17.nii.gz": "sub-@SUBJECT@/anat/sub-@SUBJECT@_acq-magCoil08Echo2_SWImagandphase.nii.gz", "SWI/PHA_TE2/SWI_3MM_UPDATED_V1.1_COIL22_ECHO2_20.nii.gz": "sub-@SUBJECT@/anat/sub-@SUBJECT@_acq-phaCoil22Echo2_SWImagandphase.nii.gz", "SWI/PHA_TE2/SWI_3MM_UPDATED_V1.1_COIL28_ECHO2_20.nii.gz": "sub-@SUBJECT@/anat/sub-@SUBJECT@_acq-phaCoil28Echo2_SWImagandphase.nii.gz", "SWI/MAG_TE1/SWI_3MM_UPDATED_V1.1_COIL29_ECHO1_17.nii.gz": "sub-@SUBJECT@/anat/sub-@SUBJECT@_acq-magCoil29Echo1_SWImagandphase.nii.gz", "dMRI/raw/PA.bval": "sub-@SUBJECT@/dwi/sub-@SUBJECT@_acq-PA_dwi.bval", "fMRI/tfMRI_SBREF.nii.gz": "sub-@SUBJECT@/func/sub-@SUBJECT@_task-rest_sbref.nii.gz", "SWI/SWI_TOTAL_PHA.nii.gz": "sub-@SUBJECT@/anat/sub-@SUBJECT@_acq-phaTotalEcho1_SWImagandphase.nii.gz", "SWI/MAG_TE1/SWI_3MM_UPDATED_V1.1_COIL08_ECHO1_17.nii.gz": "sub-@SUBJECT@/anat/sub-@SUBJECT@_acq-magCoil08Echo1_SWImagandphase.nii.gz", "SWI/PHA_TE1/SWI_3MM_UPDATED_V1.1_COIL05_ECHO1_20.nii.gz": "sub-@SUBJECT@/anat/sub-@SUBJECT@_acq-phaCoil05Echo1_SWImagandphase.nii.gz", "SWI/MAG_TE1/SWI_3MM_UPDATED_V1.1_COIL12_ECHO1_17.nii.gz": "sub-@SUBJECT@/anat/sub-@SUBJECT@_acq-magCoil12Echo1_SWImagandphase.nii.gz", "SWI/MAG_TE2/SWI_3MM_UPDATED_V1.1_COIL12_ECHO2_17.nii.gz": "sub-@SUBJECT@/anat/sub-@SUBJECT@_acq-magCoil12Echo2_SWImagandphase.nii.gz", "SWI/MAG_TE1/SWI_3MM_UPDATED_V1.1_COIL30_ECHO1_17.nii.gz": "sub-@SUBJECT@/anat/sub-@SUBJECT@_acq-magCoil30Echo1_SWImagandphase.nii.gz", "SWI/MAG_TE1/SWI_3MM_UPDATED_V1.1_COIL05_ECHO1_17.nii.gz": "sub-@SUBJECT@/anat/sub-@SUBJECT@_acq-magCoil05Echo1_SWImagandphase.nii.gz", "SWI/MAG_TE1/SWI_3MM_UPDATED_V1.1_COIL09_ECHO1_17.nii.gz": "sub-@SUBJECT@/anat/sub-@SUBJECT@_acq-magCoil09Echo1_SWImagandphase.nii.gz", "SWI/PHA_TE2/SWI_3MM_UPDATED_V1.1_COIL01_ECHO2_20.nii.gz": "sub-@SUBJECT@/anat/sub-@SUBJECT@_acq-phaCoil01Echo2_SWImagandphase.nii.gz", "SWI/PHA_TE1/SWI_3MM_UPDATED_V1.1_COIL13_ECHO1_20.nii.gz": "sub-@SUBJECT@/anat/sub-@SUBJECT@_acq-phaCoil13Echo1_SWImagandphase.nii.gz", "SWI/PHA_TE2/SWI_3MM_UPDATED_V1.1_COIL13_ECHO2_20.nii.gz": "sub-@SUBJECT@/anat/sub-@SUBJECT@_acq-phaCoil13Echo2_SWImagandphase.nii.gz", "SWI/MAG_TE1/SWI_3MM_UPDATED_V1.1_COIL21_ECHO1_17.nii.gz": "sub-@SUBJECT@/anat/sub-@SUBJECT@_acq-magCoil21Echo1_SWImagandphase.nii.gz", "SWI/MAG_TE1/SWI_3MM_UPDATED_V1.1_COIL22_ECHO1_17.nii.gz": "sub-@SUBJECT@/anat/sub-@SUBJECT@_acq-magCoil22Echo1_SWImagandphase.nii.gz", "SWI/MAG_TE2/SWI_3MM_UPDATED_V1.1_COIL10_ECHO2_17.nii.gz": "sub-@SUBJECT@/anat/sub-@SUBJECT@_acq-magCoil10Echo2_SWImagandphase.nii.gz", "SWI/PHA_TE2/SWI_3MM_UPDATED_V1.1_COIL12_ECHO2_20.nii.gz": "sub-@SUBJECT@/anat/sub-@SUBJECT@_acq-phaCoil12Echo2_SWImagandphase.nii.gz", "SWI/PHA_TE2/SWI_3MM_UPDATED_V1.1_COIL15_ECHO2_20.nii.gz": "sub-@SUBJECT@/anat/sub-@SUBJECT@_acq-phaCoil15Echo2_SWImagandphase.nii.gz", "SWI/SWI_TOTAL_MAG.nii.gz": "sub-@SUBJECT@/anat/sub-@SUBJECT@_acq-magTotalEcho1_SWImagandphase.nii.gz", "SWI/PHA_TE2/SWI_3MM_UPDATED_V1.1_COIL09_ECHO2_20.nii.gz": "sub-@SUBJECT@/anat/sub-@SUBJECT@_acq-phaCoil09Echo2_SWImagandphase.nii.gz", "SWI/MAG_TE1/SWI_3MM_UPDATED_V1.1_COIL16_ECHO1_17.nii.gz": "sub-@SUBJECT@/anat/sub-@SUBJECT@_acq-magCoil16Echo1_SWImagandphase.nii.gz", "fMRI/rfMRI_SBREF.nii.gz": "sub-@SUBJECT@/func/sub-@SUBJECT@_task-hariri_sbref.nii.gz", "SWI/SWI_TOTAL_MAG_TE2.nii.gz": "sub-@SUBJECT@/anat/sub-@SUBJECT@_acq-magTotalEcho2_SWImagandphase.nii.gz", "SWI/PHA_TE1/SWI_3MM_UPDATED_V1.1_COIL18_ECHO1_20.nii.gz": "sub-@SUBJECT@/anat/sub-@SUBJECT@_acq-phaCoil18Echo1_SWImagandphase.nii.gz", "SWI/MAG_TE1/SWI_3MM_UPDATED_V1.1_COIL23_ECHO1_17.nii.gz": "sub-@SUBJECT@/anat/sub-@SUBJECT@_acq-magCoil23Echo1_SWImagandphase.nii.gz", "SWI/PHA_TE1/SWI_3MM_UPDATED_V1.1_COIL30_ECHO1_20.nii.gz": "sub-@SUBJECT@/anat/sub-@SUBJECT@_acq-phaCoil30Echo1_SWImagandphase.nii.gz", "SWI/PHA_TE1/SWI_3MM_UPDATED_V1.1_COIL31_ECHO1_20.nii.gz": "sub-@SUBJECT@/anat/sub-@SUBJECT@_acq-phaCoil31Echo1_SWImagandphase.nii.gz", "SWI/MAG_TE2/SWI_3MM_UPDATED_V1.1_COIL02_ECHO2_17.nii.gz": "sub-@SUBJECT@/anat/sub-@SUBJECT@_acq-magCoil02Echo2_SWImagandphase.nii.gz", "SWI/SWI_TOTAL_PHA_TE2.nii.gz": "sub-@SUBJECT@/anat/sub-@SUBJECT@_acq-phaTotalEcho2_SWImagandphase.nii.gz", "SWI/PHA_TE1/SWI_3MM_UPDATED_V1.1_COIL07_ECHO1_20.nii.gz": "sub-@SUBJECT@/anat/sub-@SUBJECT@_acq-phaCoil07Echo1_SWImagandphase.nii.gz", "SWI/MAG_TE2/SWI_3MM_UPDATED_V1.1_COIL31_ECHO2_17.nii.gz": "sub-@SUBJECT@/anat/sub-@SUBJECT@_acq-magCoil31Echo2_SWImagandphase.nii.gz", "SWI/MAG_TE2/SWI_3MM_UPDATED_V1.1_COIL29_ECHO2_17.nii.gz": "sub-@SUBJECT@/anat/sub-@SUBJECT@_acq-magCoil29Echo2_SWImagandphase.nii.gz", "dMRI/raw/AP.bvec": "sub-@SUBJECT@/dwi/sub-@SUBJECT@_acq-AP_dwi.bvec", "SWI/MAG_TE1/SWI_3MM_UPDATED_V1.1_COIL13_ECHO1_17.nii.gz": "sub-@SUBJECT@/anat/sub-@SUBJECT@_acq-magCoil13Echo1_SWImagandphase.nii.gz", "SWI/MAG_TE1/SWI_3MM_UPDATED_V1.1_COIL24_ECHO1_17.nii.gz": "sub-@SUBJECT@/anat/sub-@SUBJECT@_acq-magCoil24Echo1_SWImagandphase.nii.gz", "SWI/MAG_TE2/SWI_3MM_UPDATED_V1.1_COIL19_ECHO2_17.nii.gz": "sub-@SUBJECT@/anat/sub-@SUBJECT@_acq-magCoil19Echo2_SWImagandphase.nii.gz", "SWI/PHA_TE2/SWI_3MM_UPDATED_V1.1_COIL25_ECHO2_20.nii.gz": "sub-@SUBJECT@/anat/sub-@SUBJECT@_acq-phaCoil25Echo2_SWImagandphase.nii.gz", "T2_FLAIR/T2_FLAIR.nii.gz": "sub-@SUBJECT@/anat/sub-@SUBJECT@_FLAIR.nii.gz", "SWI/MAG_TE2/SWI_3MM_UPDATED_V1.1_COIL25_ECHO2_17.nii.gz": "sub-@SUBJECT@/anat/sub-@SUBJECT@_acq-magCoil25Echo2_SWImagandphase.nii.gz", "SWI/MAG_TE2/SWI_3MM_UPDATED_V1.1_COIL24_ECHO2_17.nii.gz": "sub-@SUBJECT@/anat/sub-@SUBJECT@_acq-magCoil24Echo2_SWImagandphase.nii.gz", "SWI/MAG_TE2/SWI_3MM_UPDATED_V1.1_COIL22_ECHO2_17.nii.gz": "sub-@SUBJECT@/anat/sub-@SUBJECT@_acq-magCoil22Echo2_SWImagandphase.nii.gz", "SWI/MAG_TE1/SWI_3MM_UPDATED_V1.1_COIL01_ECHO1_17.nii.gz": "sub-@SUBJECT@/anat/sub-@SUBJECT@_acq-magCoil01Echo1_SWImagandphase.nii.gz", "SWI/PHA_TE1/SWI_3MM_UPDATED_V1.1_COIL04_ECHO1_20.nii.gz": "sub-@SUBJECT@/anat/sub-@SUBJECT@_acq-phaCoil04Echo1_SWImagandphase.nii.gz", "SWI/PHA_TE1/SWI_3MM_UPDATED_V1.1_COIL27_ECHO1_20.nii.gz": "sub-@SUBJECT@/anat/sub-@SUBJECT@_acq-phaCoil27Echo1_SWImagandphase.nii.gz", "SWI/PHA_TE2/SWI_3MM_UPDATED_V1.1_COIL27_ECHO2_20.nii.gz": "sub-@SUBJECT@/anat/sub-@SUBJECT@_acq-phaCoil27Echo2_SWImagandphase.nii.gz", "SWI/MAG_TE1/SWI_3MM_UPDATED_V1.1_COIL14_ECHO1_17.nii.gz": "sub-@SUBJECT@/anat/sub-@SUBJECT@_acq-magCoil14Echo1_SWImagandphase.nii.gz", "dMRI/raw/AP.nii.gz": "sub-@SUBJECT@/dwi/sub-@SUBJECT@_acq-AP_dwi.nii.gz", "SWI/MAG_TE2/SWI_3MM_UPDATED_V1.1_COIL01_ECHO2_17.nii.gz": "sub-@SUBJECT@/anat/sub-@SUBJECT@_acq-magCoil01Echo2_SWImagandphase.nii.gz", "SWI/MAG_TE1/SWI_3MM_UPDATED_V1.1_COIL28_ECHO1_17.nii.gz": "sub-@SUBJECT@/anat/sub-@SUBJECT@_acq-magCoil28Echo1_SWImagandphase.nii.gz", "SWI/MAG_TE1/SWI_3MM_UPDATED_V1.1_COIL03_ECHO1_17.nii.gz": "sub-@SUBJECT@/anat/sub-@SUBJECT@_acq-magCoil03Echo1_SWImagandphase.nii.gz", "SWI/PHA_TE2/SWI_3MM_UPDATED_V1.1_COIL30_ECHO2_20.nii.gz": "sub-@SUBJECT@/anat/sub-@SUBJECT@_acq-phaCoil30Echo2_SWImagandphase.nii.gz", "SWI/MAG_TE1/SWI_3MM_UPDATED_V1.1_COIL15_ECHO1_17.nii.gz": "sub-@SUBJECT@/anat/sub-@SUBJECT@_acq-magCoil15Echo1_SWImagandphase.nii.gz", "SWI/PHA_TE2/SWI_3MM_UPDATED_V1.1_COIL23_ECHO2_20.nii.gz": "sub-@SUBJECT@/anat/sub-@SUBJECT@_acq-phaCoil23Echo2_SWImagandphase.nii.gz", "SWI/MAG_TE2/SWI_3MM_UPDATED_V1.1_COIL28_ECHO2_17.nii.gz": "sub-@SUBJECT@/anat/sub-@SUBJECT@_acq-magCoil28Echo2_SWImagandphase.nii.gz", "SWI/MAG_TE1/SWI_3MM_UPDATED_V1.1_COIL27_ECHO1_17.nii.gz": "sub-@SUBJECT@/anat/sub-@SUBJECT@_acq-magCoil27Echo1_SWImagandphase.nii.gz", "SWI/MAG_TE1/SWI_3MM_UPDATED_V1.1_COIL19_ECHO1_17.nii.gz": "sub-@SUBJECT@/anat/sub-@SUBJECT@_acq-magCoil19Echo1_SWImagandphase.nii.gz", "SWI/MAG_TE2/SWI_3MM_UPDATED_V1.1_COIL16_ECHO2_17.nii.gz": "sub-@SUBJECT@/anat/sub-@SUBJECT@_acq-magCoil16Echo2_SWImagandphase.nii.gz", "SWI/MAG_TE2/SWI_3MM_UPDATED_V1.1_COIL05_ECHO2_17.nii.gz": "sub-@SUBJECT@/anat/sub-@SUBJECT@_acq-magCoil05Echo2_SWImagandphase.nii.gz", "SWI/PHA_TE2/SWI_3MM_UPDATED_V1.1_COIL32_ECHO2_20.nii.gz": "sub-@SUBJECT@/anat/sub-@SUBJECT@_acq-phaCoil32Echo2_SWImagandphase.nii.gz", "SWI/MAG_TE1/SWI_3MM_UPDATED_V1.1_COIL07_ECHO1_17.nii.gz": "sub-@SUBJECT@/anat/sub-@SUBJECT@_acq-magCoil07Echo1_SWImagandphase.nii.gz", "SWI/MAG_TE1/SWI_3MM_UPDATED_V1.1_COIL02_ECHO1_17.nii.gz": "sub-@SUBJECT@/anat/sub-@SUBJECT@_acq-magCoil02Echo1_SWImagandphase.nii.gz", "SWI/PHA_TE1/SWI_3MM_UPDATED_V1.1_COIL01_ECHO1_20.nii.gz": "sub-@SUBJECT@/anat/sub-@SUBJECT@_acq-phaCoil01Echo1_SWImagandphase.nii.gz", "SWI/MAG_TE2/SWI_3MM_UPDATED_V1.1_COIL30_ECHO2_17.nii.gz": "sub-@SUBJECT@/anat/sub-@SUBJECT@_acq-magCoil30Echo2_SWImagandphase.nii.gz", "SWI/MAG_TE2/SWI_3MM_UPDATED_V1.1_COIL23_ECHO2_17.nii.gz": "sub-@SUBJECT@/anat/sub-@SUBJECT@_acq-magCoil23Echo2_SWImagandphase.nii.gz", "SWI/PHA_TE2/SWI_3MM_UPDATED_V1.1_COIL26_ECHO2_20.nii.gz": "sub-@SUBJECT@/anat/sub-@SUBJECT@_acq-phaCoil26Echo2_SWImagandphase.nii.gz", "SWI/MAG_TE2/SWI_3MM_UPDATED_V1.1_COIL09_ECHO2_17.nii.gz": "sub-@SUBJECT@/anat/sub-@SUBJECT@_acq-magCoil09Echo2_SWImagandphase.nii.gz", "SWI/MAG_TE2/SWI_3MM_UPDATED_V1.1_COIL03_ECHO2_17.nii.gz": "sub-@SUBJECT@/anat/sub-@SUBJECT@_acq-magCoil03Echo2_SWImagandphase.nii.gz", "raw/SWI_TOTAL_MAG_notNorm_TE2.nii.gz": "sub-@SUBJECT@/anat/sub-@SUBJECT@_acq-magTotalNotNormEcho2_SWImagandphase.nii.gz", "SWI/MAG_TE2/SWI_3MM_UPDATED_V1.1_COIL17_ECHO2_17.nii.gz": "sub-@SUBJECT@/anat/sub-@SUBJECT@_acq-magCoil17Echo2_SWImagandphase.nii.gz", "SWI/PHA_TE1/SWI_3MM_UPDATED_V1.1_COIL12_ECHO1_20.nii.gz": "sub-@SUBJECT@/anat/sub-@SUBJECT@_acq-phaCoil12Echo1_SWImagandphase.nii.gz", "SWI/PHA_TE2/SWI_3MM_UPDATED_V1.1_COIL06_ECHO2_20.nii.gz": "sub-@SUBJECT@/anat/sub-@SUBJECT@_acq-phaCoil06Echo2_SWImagandphase.nii.gz", "SWI/PHA_TE1/SWI_3MM_UPDATED_V1.1_COIL11_ECHO1_20.nii.gz": "sub-@SUBJECT@/anat/sub-@SUBJECT@_acq-phaCoil11Echo1_SWImagandphase.nii.gz", "SWI/MAG_TE1/SWI_3MM_UPDATED_V1.1_COIL31_ECHO1_17.nii.gz": "sub-@SUBJECT@/anat/sub-@SUBJECT@_acq-magCoil31Echo1_SWImagandphase.nii.gz", "SWI/PHA_TE2/SWI_3MM_UPDATED_V1.1_COIL11_ECHO2_20.nii.gz": "sub-@SUBJECT@/anat/sub-@SUBJECT@_acq-phaCoil11Echo2_SWImagandphase.nii.gz", "SWI/PHA_TE1/SWI_3MM_UPDATED_V1.1_COIL21_ECHO1_20.nii.gz": "sub-@SUBJECT@/anat/sub-@SUBJECT@_acq-phaCoil21Echo1_SWImagandphase.nii.gz", "fMRI/rfMRI.nii.gz": "sub-@SUBJECT@/func/sub-@SUBJECT@_task-rest_bold.nii.gz", "SWI/PHA_TE1/SWI_3MM_UPDATED_V1.1_COIL22_ECHO1_20.nii.gz": "sub-@SUBJECT@/anat/sub-@SUBJECT@_acq-phaCoil22Echo1_SWImagandphase.nii.gz", "raw/SWI_TOTAL_MAG_notNorm.nii.gz": "sub-@SUBJECT@/anat/sub-@SUBJECT@_acq-magTotalNotNormEcho1_SWImagandphase.nii.gz", "SWI/PHA_TE1/SWI_3MM_UPDATED_V1.1_COIL06_ECHO1_20.nii.gz": "sub-@SUBJECT@/anat/sub-@SUBJECT@_acq-phaCoil06Echo1_SWImagandphase.nii.gz", "SWI/MAG_TE1/SWI_3MM_UPDATED_V1.1_COIL11_ECHO1_17.nii.gz": "sub-@SUBJECT@/anat/sub-@SUBJECT@_acq-magCoil11Echo1_SWImagandphase.nii.gz", "SWI/PHA_TE1/SWI_3MM_UPDATED_V1.1_COIL25_ECHO1_20.nii.gz": "sub-@SUBJECT@/anat/sub-@SUBJECT@_acq-phaCoil25Echo1_SWImagandphase.nii.gz", "SWI/PHA_TE1/SWI_3MM_UPDATED_V1.1_COIL16_ECHO1_20.nii.gz": "sub-@SUBJECT@/anat/sub-@SUBJECT@_acq-phaCoil16Echo1_SWImagandphase.nii.gz", "raw/T1_notNorm.nii.gz": "sub-@SUBJECT@/anat/sub-@SUBJECT@_acq-notNorm_T1w.nii.gz", "SWI/PHA_TE2/SWI_3MM_UPDATED_V1.1_COIL31_ECHO2_20.nii.gz": "sub-@SUBJECT@/anat/sub-@SUBJECT@_acq-phaCoil31Echo2_SWImagandphase.nii.gz", "dMRI/raw/PA.bvec": "sub-@SUBJECT@/dwi/sub-@SUBJECT@_acq-PA_dwi.bvec", "SWI/MAG_TE2/SWI_3MM_UPDATED_V1.1_COIL07_ECHO2_17.nii.gz": "sub-@SUBJECT@/anat/sub-@SUBJECT@_acq-magCoil07Echo2_SWImagandphase.nii.gz", "SWI/MAG_TE1/SWI_3MM_UPDATED_V1.1_COIL04_ECHO1_17.nii.gz": "sub-@SUBJECT@/anat/sub-@SUBJECT@_acq-magCoil04Echo1_SWImagandphase.nii.gz", "SWI/MAG_TE2/SWI_3MM_UPDATED_V1.1_COIL27_ECHO2_17.nii.gz": "sub-@SUBJECT@/anat/sub-@SUBJECT@_acq-magCoil27Echo2_SWImagandphase.nii.gz", "SWI/PHA_TE2/SWI_3MM_UPDATED_V1.1_COIL24_ECHO2_20.nii.gz": "sub-@SUBJECT@/anat/sub-@SUBJECT@_acq-phaCoil24Echo2_SWImagandphase.nii.gz", "SWI/MAG_TE1/SWI_3MM_UPDATED_V1.1_COIL17_ECHO1_17.nii.gz": "sub-@SUBJECT@/anat/sub-@SUBJECT@_acq-magCoil17Echo1_SWImagandphase.nii.gz", "raw/PA_SBREF.nii.gz": "sub-@SUBJECT@/dwi/sub-@SUBJECT@_acq-PA_sbref.nii.gz", "SWI/PHA_TE1/SWI_3MM_UPDATED_V1.1_COIL19_ECHO1_20.nii.gz": "sub-@SUBJECT@/anat/sub-@SUBJECT@_acq-phaCoil19Echo1_SWImagandphase.nii.gz", "SWI/MAG_TE2/SWI_3MM_UPDATED_V1.1_COIL20_ECHO2_17.nii.gz": "sub-@SUBJECT@/anat/sub-@SUBJECT@_acq-magCoil20Echo2_SWImagandphase.nii.gz", "SWI/MAG_TE2/SWI_3MM_UPDATED_V1.1_COIL18_ECHO2_17.nii.gz": "sub-@SUBJECT@/anat/sub-@SUBJECT@_acq-magCoil18Echo2_SWImagandphase.nii.gz", "SWI/PHA_TE1/SWI_3MM_UPDATED_V1.1_COIL24_ECHO1_20.nii.gz": "sub-@SUBJECT@/anat/sub-@SUBJECT@_acq-phaCoil24Echo1_SWImagandphase.nii.gz", "SWI/PHA_TE2/SWI_3MM_UPDATED_V1.1_COIL19_ECHO2_20.nii.gz": "sub-@SUBJECT@/anat/sub-@SUBJECT@_acq-phaCoil19Echo2_SWImagandphase.nii.gz", "SWI/PHA_TE1/SWI_3MM_UPDATED_V1.1_COIL20_ECHO1_20.nii.gz": "sub-@SUBJECT@/anat/sub-@SUBJECT@_acq-phaCoil20Echo1_SWImagandphase.nii.gz", "SWI/PHA_TE2/SWI_3MM_UPDATED_V1.1_COIL29_ECHO2_20.nii.gz": "sub-@SUBJECT@/anat/sub-@SUBJECT@_acq-phaCoil29Echo2_SWImagandphase.nii.gz", "SWI/MAG_TE2/SWI_3MM_UPDATED_V1.1_COIL32_ECHO2_17.nii.gz": "sub-@SUBJECT@/anat/sub-@SUBJECT@_acq-magCoil32Echo2_SWImagandphase.nii.gz", "SWI/PHA_TE1/SWI_3MM_UPDATED_V1.1_COIL29_ECHO1_20.nii.gz": "sub-@SUBJECT@/anat/sub-@SUBJECT@_acq-phaCoil29Echo1_SWImagandphase.nii.gz", "raw/T2_FLAIR_notNorm.nii.gz": "sub-@SUBJECT@/anat/sub-@SUBJECT@_acq-notNorm_FLAIR.nii.gz", "SWI/PHA_TE1/SWI_3MM_UPDATED_V1.1_COIL02_ECHO1_20.nii.gz": "sub-@SUBJECT@/anat/sub-@SUBJECT@_acq-phaCoil02Echo1_SWImagandphase.nii.gz", "SWI/PHA_TE2/SWI_3MM_UPDATED_V1.1_COIL20_ECHO2_20.nii.gz": "sub-@SUBJECT@/anat/sub-@SUBJECT@_acq-phaCoil20Echo2_SWImagandphase.nii.gz", "SWI/PHA_TE1/SWI_3MM_UPDATED_V1.1_COIL28_ECHO1_20.nii.gz": "sub-@SUBJECT@/anat/sub-@SUBJECT@_acq-phaCoil28Echo1_SWImagandphase.nii.gz", "SWI/PHA_TE1/SWI_3MM_UPDATED_V1.1_COIL26_ECHO1_20.nii.gz": "sub-@SUBJECT@/anat/sub-@SUBJECT@_acq-phaCoil26Echo1_SWImagandphase.nii.gz", "SWI/PHA_TE2/SWI_3MM_UPDATED_V1.1_COIL07_ECHO2_20.nii.gz": "sub-@SUBJECT@/anat/sub-@SUBJECT@_acq-phaCoil07Echo2_SWImagandphase.nii.gz", "SWI/MAG_TE2/SWI_3MM_UPDATED_V1.1_COIL04_ECHO2_17.nii.gz": "sub-@SUBJECT@/anat/sub-@SUBJECT@_acq-magCoil04Echo2_SWImagandphase.nii.gz", "SWI/MAG_TE1/SWI_3MM_UPDATED_V1.1_COIL25_ECHO1_17.nii.gz": "sub-@SUBJECT@/anat/sub-@SUBJECT@_acq-magCoil25Echo1_SWImagandphase.nii.gz", "SWI/MAG_TE1/SWI_3MM_UPDATED_V1.1_COIL18_ECHO1_17.nii.gz": "sub-@SUBJECT@/anat/sub-@SUBJECT@_acq-magCoil18Echo1_SWImagandphase.nii.gz", "fMRI/tfMRI.nii.gz": "sub-@SUBJECT@/func/sub-@SUBJECT@_task-hariri_bold.nii.gz", "SWI/PHA_TE2/SWI_3MM_UPDATED_V1.1_COIL18_ECHO2_20.nii.gz": "sub-@SUBJECT@/anat/sub-@SUBJECT@_acq-phaCoil18Echo2_SWImagandphase.nii.gz", "SWI/MAG_TE2/SWI_3MM_UPDATED_V1.1_COIL21_ECHO2_17.nii.gz": "sub-@SUBJECT@/anat/sub-@SUBJECT@_acq-magCoil21Echo2_SWImagandphase.nii.gz", "SWI/MAG_TE1/SWI_3MM_UPDATED_V1.1_COIL32_ECHO1_17.nii.gz": "sub-@SUBJECT@/anat/sub-@SUBJECT@_acq-magCoil32Echo1_SWImagandphase.nii.gz", "SWI/MAG_TE2/SWI_3MM_UPDATED_V1.1_COIL13_ECHO2_17.nii.gz": "sub-@SUBJECT@/anat/sub-@SUBJECT@_acq-magCoil13Echo2_SWImagandphase.nii.gz", "SWI/PHA_TE1/SWI_3MM_UPDATED_V1.1_COIL08_ECHO1_20.nii.gz": "sub-@SUBJECT@/anat/sub-@SUBJECT@_acq-phaCoil08Echo1_SWImagandphase.nii.gz", "SWI/MAG_TE1/SWI_3MM_UPDATED_V1.1_COIL20_ECHO1_17.nii.gz": "sub-@SUBJECT@/anat/sub-@SUBJECT@_acq-magCoil20Echo1_SWImagandphase.nii.gz", "SWI/PHA_TE2/SWI_3MM_UPDATED_V1.1_COIL14_ECHO2_20.nii.gz": "sub-@SUBJECT@/anat/sub-@SUBJECT@_acq-phaCoil14Echo2_SWImagandphase.nii.gz", "SWI/PHA_TE1/SWI_3MM_UPDATED_V1.1_COIL23_ECHO1_20.nii.gz": "sub-@SUBJECT@/anat/sub-@SUBJECT@_acq-phaCoil23Echo1_SWImagandphase.nii.gz", "SWI/PHA_TE2/SWI_3MM_UPDATED_V1.1_COIL17_ECHO2_20.nii.gz": "sub-@SUBJECT@/anat/sub-@SUBJECT@_acq-phaCoil17Echo2_SWImagandphase.nii.gz", "SWI/MAG_TE2/SWI_3MM_UPDATED_V1.1_COIL15_ECHO2_17.nii.gz": "sub-@SUBJECT@/anat/sub-@SUBJECT@_acq-magCoil15Echo2_SWImagandphase.nii.gz", "SWI/PHA_TE2/SWI_3MM_UPDATED_V1.1_COIL08_ECHO2_20.nii.gz": "sub-@SUBJECT@/anat/sub-@SUBJECT@_acq-phaCoil08Echo2_SWImagandphase.nii.gz", "SWI/MAG_TE1/SWI_3MM_UPDATED_V1.1_COIL06_ECHO1_17.nii.gz": "sub-@SUBJECT@/anat/sub-@SUBJECT@_acq-magCoil06Echo1_SWImagandphase.nii.gz", "SWI/PHA_TE2/SWI_3MM_UPDATED_V1.1_COIL03_ECHO2_20.nii.gz": "sub-@SUBJECT@/anat/sub-@SUBJECT@_acq-phaCoil03Echo2_SWImagandphase.nii.gz", "SWI/PHA_TE1/SWI_3MM_UPDATED_V1.1_COIL17_ECHO1_20.nii.gz": "sub-@SUBJECT@/anat/sub-@SUBJECT@_acq-phaCoil17Echo1_SWImagandphase.nii.gz", "raw/AP_SBREF.nii.gz": "sub-@SUBJECT@/dwi/sub-@SUBJECT@_acq-AP_sbref.nii.gz", "SWI/PHA_TE2/SWI_3MM_UPDATED_V1.1_COIL02_ECHO2_20.nii.gz": "sub-@SUBJECT@/anat/sub-@SUBJECT@_acq-phaCoil02Echo2_SWImagandphase.nii.gz", "SWI/MAG_TE1/SWI_3MM_UPDATED_V1.1_COIL10_ECHO1_17.nii.gz": "sub-@SUBJECT@/anat/sub-@SUBJECT@_acq-magCoil10Echo1_SWImagandphase.nii.gz", "SWI/PHA_TE1/SWI_3MM_UPDATED_V1.1_COIL03_ECHO1_20.nii.gz": "sub-@SUBJECT@/anat/sub-@SUBJECT@_acq-phaCoil03Echo1_SWImagandphase.nii.gz", "SWI/PHA_TE2/SWI_3MM_UPDATED_V1.1_COIL16_ECHO2_20.nii.gz": "sub-@SUBJECT@/anat/sub-@SUBJECT@_acq-phaCoil16Echo2_SWImagandphase.nii.gz", "SWI/PHA_TE2/SWI_3MM_UPDATED_V1.1_COIL04_ECHO2_20.nii.gz": "sub-@SUBJECT@/anat/sub-@SUBJECT@_acq-phaCoil04Echo2_SWImagandphase.nii.gz", "SWI/MAG_TE2/SWI_3MM_UPDATED_V1.1_COIL14_ECHO2_17.nii.gz": "sub-@SUBJECT@/anat/sub-@SUBJECT@_acq-magCoil14Echo2_SWImagandphase.nii.gz", "SWI/MAG_TE2/SWI_3MM_UPDATED_V1.1_COIL26_ECHO2_17.nii.gz": "sub-@SUBJECT@/anat/sub-@SUBJECT@_acq-magCoil26Echo2_SWImagandphase.nii.gz", "SWI/PHA_TE1/SWI_3MM_UPDATED_V1.1_COIL14_ECHO1_20.nii.gz": "sub-@SUBJECT@/anat/sub-@SUBJECT@_acq-phaCoil14Echo1_SWImagandphase.nii.gz", "SWI/PHA_TE2/SWI_3MM_UPDATED_V1.1_COIL10_ECHO2_20.nii.gz": "sub-@SUBJECT@/anat/sub-@SUBJECT@_acq-phaCoil10Echo2_SWImagandphase.nii.gz", "SWI/PHA_TE1/SWI_3MM_UPDATED_V1.1_COIL10_ECHO1_20.nii.gz": "sub-@SUBJECT@/anat/sub-@SUBJECT@_acq-phaCoil10Echo1_SWImagandphase.nii.gz", "SWI/PHA_TE1/SWI_3MM_UPDATED_V1.1_COIL32_ECHO1_20.nii.gz": "sub-@SUBJECT@/anat/sub-@SUBJECT@_acq-phaCoil32Echo1_SWImagandphase.nii.gz", "dMRI/raw/AP.bval": "sub-@SUBJECT@/dwi/sub-@SUBJECT@_acq-AP_dwi.bval", "SWI/PHA_TE2/SWI_3MM_UPDATED_V1.1_COIL05_ECHO2_20.nii.gz": "sub-@SUBJECT@/anat/sub-@SUBJECT@_acq-phaCoil05Echo2_SWImagandphase.nii.gz", "SWI/MAG_TE2/SWI_3MM_UPDATED_V1.1_COIL06_ECHO2_17.nii.gz": "sub-@SUBJECT@/anat/sub-@SUBJECT@_acq-magCoil06Echo2_SWImagandphase.nii.gz", "SWI/MAG_TE2/SWI_3MM_UPDATED_V1.1_COIL11_ECHO2_17.nii.gz": "sub-@SUBJECT@/anat/sub-@SUBJECT@_acq-magCoil11Echo2_SWImagandphase.nii.gz"}