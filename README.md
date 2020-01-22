# UKBB_scripts

UKBB_scripts is a collection of scripts for dealing with various aspects of the UKBB. It is currently in development.

Usage for .zip -> BIDS conversion:
 Command line:
   python3 ukbb_structure_conversion.py ZIP_FILE [--raw_dir RAW] [--source_dir SOURCE] [--derivatives_dir DERIVS]
 Python interpreter
   ukbb_structure_conversion.bids_from_zip(ZIP_FILE, raw_dir=RAW, source_dir=SOURCE, derivs_dir=DERIVS)

NOTE:
 Several files provided under the UKBB are not covered by the current version of BIDS (e.g. derivatives, SWI). Derivatives are placed in a derivatives folder prepended by the subject ID. SWI are placed in 'sources' with a format as-close to BIDS as possible (the suffixes in particular are likely to change).

ukbb_integrity:
	Checks subjects in a BIDS-format directory to confirm that they have the following modalities: T1, T2, SWI, tfMRI, rfMRI, DWI. A .bulk file is generated for missing files.
	NOTE: Missing files may be missing because they do not exist.

ukbb_structure_conversion:
	Converts downloaded zip folders to BIDS-adjacent (sans .json) format.

ukbb_transfer:
	Functions for verifying that data transfers across systems; dealing with missing BIDS files, handling .lis files, and creating SLURM job files for parallel downloading.
