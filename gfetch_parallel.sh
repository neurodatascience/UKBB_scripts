#!/bin/bash
# This code is meant to download UKBB.
# Need: 1) fetch utility, 2) bulkfile 3) keyfile 4) array idx 5) num batch

# TODO: need to add block parsing for gfetch

# Parse inputs
while (( "$#" )); do
        case "$1" in
                -u|--util)
                  	# fetch utility path
			fetch=`readlink -f "${2}"`
			shift 2
			;;
		-b|--bulk)
			# bulk file path
			bulk=`readlink -f "${2}"`
			shift 2
			;;
		-a|--keyfile)
			# keyfile path ("a" is for consistency with ukbb utils, "authkey")
			keyfile=`readlink -f "${2}"`
			shift 2
			;;
#		-i|--index)
#			# starting index; if this is the fifth job in 10, idx=4.
#			idx="${2}"
#			shift 2
#			;;
		-l|--blocks)
			# number of blocks
			blocks="${2}"
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
if [ -z ${bulk} ]; then
	echo "Bulk file undefined; provide path using -b flag"
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

chromlist=(`seq 1 22`)
chromlist+=(X Y XY MT)

job_ind=0
for chrom in ${chromlist[@]}; do
	dload ${chrom} &
	job_ind=$((job_ind+1))
	if [ ${job_ind} -ge ${njob} ]; then
		wait
		job_ind=0
	fi
done

