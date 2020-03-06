#!/bin/bash

## Input parsing
set -e -u
workers=1
shift
while (( "$#" )); do
	case "$1" in
		-a|--authkey)
			authkey="`readlink -f ${2}`"
			shift 2
			;;
		-u|--ukbgene)
			ukbgene="`readlink -f ${2}`"
			shift 2
			;;
		-w|--workers)
			workers="${2}"
			shift 2;;
		-*|--*=)
			echo "Invalid flag ${1}" >&2
			exit 1
			;;
	esac
done

chroms=(`seq 23 -1 1`)
chroms+=(X Y XY MT)

### Calls
if [ ! -e calls ]; then
	datalad create --description "Calls genetics data (UKBB)" calls
fi
cd calls
i=0
for ch in ${chroms[@]}; do
	((i=i%${workers})); ((i++==0)) && wait
	datalad run ${ukbgene} cal -a${authkey} -c${ch}
done
# Get .fam file (they're all identical)
datalad run ${ukbgene} cal -m -a${authkey} -c1
cd ../

# Get .bim files
raw=.raw
mkdir ${raw}
datalad run wget -nd biobank.ndph.ox.ac.uk/showcase/showcase/auxdata/ukb_snp_bim.tar -P ${raw}
datalad run --input ${raw}/ukb_snp_bim.tar tar -xf ${raw}/ukb_snp_bim.tar -C calls/

# Marker QC
datalad run wget -nd  biobank.ndph.ox.ac.uk/showcase/showcase/auxdata/ukb_snp_qc.txt

# Relatedness
datalad run ${ukbgene} rel -a${authkey}

### Haplotypes
mkdir haplotypes
cd haplotypes
for ch in ${chroms[@]}; do
	datalad run ${ukbgene} hap -a${authkey} -c${ch}
done
cd ../
# bgi
datalad run wget -nd biobank.ctsu.ox.ac.uk/crystal/crystal/auxdata/ukb_hap_bgi.tgz -P ${raw}
datalad run --input ${raw}/ukb_hap_bgi.tgz tar -xf ${raw}/ukb_hap_bgi.tgz -C haplotypes/

### Miscellaneous
# intensity
mkdir misc
cd misc
for ch in ${chroms[@]}; do
	datalad run ${ukbgene} int -a${authkey} -c${ch}
	datalad run ${ukbgene} con -a${authkey} -c${ch}
	datalad run ${ukbgene} l2r -a${authkey} -c${ch}
	datalad run ${ukbgene} baf -a${authkey} -c${ch}
done
cd ../

# Posterior
datalad run wget  -nd  biobank.ctsu.ox.ac.uk/crystal/crystal/auxdata/ukb_snp_posterior.tar -P ${raw}
datalad run --input ${raw}/ukb_snp_posterior.tar tar -xf ${raw}/ukb_snp_posterior.tar -C misc/

# Batch
datalad run wget  -nd  biobank.ctsu.ox.ac.uk/crystal/crystal/auxdata/ukb_snp_posterior.batch -P misc/


### Imputed
mkdir imputed
# bgi index files
datalad run wget -nd  biobank.ctsu.ox.ac.uk/crystal/crystal/auxdata/ukb_imp_bgi.tgz -P ${raw}
datalad run --input ${raw}/ukb_imp_bgi.tgz tar -xf ${tmpdir}/ukb_imp_bgi.tgz -C imputed/

# imputation minor allele freq and information scores
datalad run wget -nd  biobank.ctsu.ox.ac.uk/crystal/crystal/auxdata/ukb_imp_mfi.tgz -P ${raw}
datalad run --input ${raw}/ukb_imp_mfi.tgz tar -xf ${tmpdir}/ukb_imp_mfi.tgz -C imputed/

cd imputed/
# Imputation data (very large)
i=0
for ch in ${chroms[@]}; do
	((i=i%${workers})); ((i++==0)) && wait
	datalad run ${ukbgene} imp -a${authkey} -c${ch}
	datalad run ${ukbgene} imp -m -a${authkey} -c${ch}
done
wait
cd ../
