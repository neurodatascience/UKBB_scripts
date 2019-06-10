UKBB_Data is a collection of scripts for dealing with various aspects of the UKBB.

ukbb_integrity:
	Checks subjects in a BIDS-format directory to confirm that they have the following modalities: T1, T2, SWI, tfMRI, rfMRI, DWI. A .bulk file is generated for missing files.
	NOTE: Missing files may be missing because they do not exist.

ukbb_structure_conversion:
	Converts (MODALITY)/(files...) to BIDS-adjacent (sans .json) format.

ukbb_transfer:
	Functions for verifying that data transfers across systems; dealing with missing BIDS files, handling .lis files, and creating SLURM job files for parallel downloading.
