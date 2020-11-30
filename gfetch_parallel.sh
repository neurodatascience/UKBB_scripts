#!/bin/bash
# This code is meant to download UKBB.
# Need: 1) fetch utility, 2) bulkfile 3) keyfile 4) array idx 5) num jobs

# Parse inputs
# Example use: bash UKBB_scripts/gfetch_parallel.sh -u gfetch -a k12345r90001.key -n 10 -f 23156 -b pvcf_blocks.txt
skip=1
while (( "$#" )); do
        case "$1" in
                -u|--util)
                  	# fetch utility path
			fetch=`readlink -f "${2}"`
			shift 2
			;;
		-a|--keyfile)
			# keyfile path ("a" is for consistency with ukbb utils, "authkey")
			# provided utilities have char limit on keypaths
			keyfile="${2}"
			shift 2
			;;
		-n|--numjobs)
			# number of jobs downloading the data (used to determine how much each should download)
			njob="${2}"
			shift 2
			;;
		-f|--field)
			# field id
			field="${2}"
			shift 2
			;;
		-b|--blocklist)
			# pvcf_blocks.txt
			blocklist="${2}"
			shift 2
			;;
		-s|--skip)
			# if 1: skip if file is already present; default 1
			skipflag="${2}"
			shift 2
			;;
                -*|--*=)
                  echo "Invalid flag ${2}" >&2
                  exit 1
                  ;;
        esac
done


# Check that all necessary variables are defined
if [ -z ${fetch} ]; then
	echo "Fetch utility undefined; provide path using -f flag"
	exit 1
fi
if [ -z ${keyfile} ]; then
	echo "Keyfile undefined; provide path using -a flag"
	exit 1
fi
#if [ -z ${idx} ]; then
#	echo "Idx undefined; provide value using -i flag"
#	exit 1
#fi
if [ -z ${njob} ]; then
	echo "Number of jobs undefined; provide value using -n flag"
	exit 1
fi

# Define download unit
dload () {
local chrom
chrom="${1}"
${fetch} ${field} -c${chrom} -a${keyfile}
${fetch} ${field} -c${chrom} -m -a${keyfile}
}

# Define download unit (with blocks!)
dload_block () {
local chrom
local block
chrom="${1}"
block="${2}"
${fetch} ${field} -c${chrom} -b${block} -a${keyfile}
}

chromlist=(`seq 1 22`)
chromlist+=(X Y XY MT)

job_ind=0
if [ -z ${blocklist} ]; then
	for chrom in ${chromlist[@]}; do
		dload ${chrom} &
		job_ind=$((job_ind+1))
		if [ ${job_ind} -ge ${njob} ]; then
			wait
			job_ind=0
		fi
	done
else
	# Go through each line in blocklist to get chrom-block pair
	while read -r binfo; do
		barr=(${binfo})
		chrom=${barr[1]}
		block=${barr[2]}
		if [ ${skip} -eq 1 ]; then
			if [ -f "ukb${field}_c${chrom}_b${block}_v1.vcf.gz" ]; then
				echo "Found file; skipping: ukb${field}_c${chrom}_b${block}_v1.vcf.gz"
				continue
			fi
		fi
		dload_block ${chrom} ${block} &
		job_ind=$((job_ind+1))
		if [ ${job_ind} -ge ${njob} ]; then
			wait
			job_ind=0
		fi
	done < ${blocklist}
fi

