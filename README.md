# UKBB_scripts

UKBB_scripts is a collection of scripts for dealing with various aspects of the UKBB. It is currently in development.

ukbb_integrity:
	Checks subjects in a BIDS-format directory to confirm that they have the following modalities: T1, T2, SWI, tfMRI, rfMRI, DWI. A .bulk file is generated for missing files.
	NOTE: Missing files may be missing because they do not exist.

ukbb_structure_conversion:
	Converts downloaded zip folders to BIDS-adjacent (sans .json) format.

ukbb_transfer:
	Functions for verifying that data transfers across systems; dealing with missing BIDS files, handling .lis files, and creating SLURM job files for parallel downloading.
