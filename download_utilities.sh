#!/bin/bash
ADDRESS="biobank.ndph.ox.ac.uk/showcase/util/"
wget  -nd  ${ADDRESS}/ukbconv -P ${1}/
wget  -nd  ${ADDRESS}/ukbunpack -P ${1}/
wget  -nd  ${ADDRESS}/ukbfetch -P ${1}/
wget  -nd  ${ADDRESS}/ukblink -P ${1}/
wget  -nd  ${ADDRESS}/ukbgene -P ${1}/
wget  -nd  ${ADDRESS}/encoding.ukb -P ${1}/
