---
entity_id: "gene.b1804"
entity_type: "gene"
name: "rnd"
source_database: "NCBI RefSeq"
source_id: "gene-b1804"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b1804"
  - "rnd"
---

# rnd

`gene.b1804`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b1804`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

rnd (gene.b1804) is a gene entity. It encodes rnd (protein.P09155). Encoded protein function: FUNCTION: Exonuclease involved in the 3' processing of various precursor tRNAs. Initiates hydrolysis at the 3'-terminus of an RNA molecule and releases 5'-mononucleotides. {ECO:0000255|HAMAP-Rule:MF_01899, ECO:0000269|PubMed:3041371, ECO:0000269|PubMed:6263886}. EcoCyc product frame: EG10858-MONOMER. Genomic coordinates: 1886864-1887991. EcoCyc protein note: Ribonuclease D (RNase D) is an exonuclease involved in the 3' ribonucleolytic processing of precursor tRNA. Though RNase D appears to be a minor player in this task and is not required for viability or proper tRNA processing, it can support such processing in the absence of other exonucleases (RNase II, RNase BN, RNase T and RNase PH) . In vitro, RNase D cleaves tRNA nonprocessively (randomly) from the 3' end to yield 5"-mononucleotides and active tRNA. Cleavage of tRNA slows at the CCA nucleotide sequence, allowing aminoacylation of the tRNA that prevents additional cleavage . RNase D activity is very dependent on the structure of the 3' end of the target tRNA, with cleavage of altered tRNA proceeding much faster than cleavage of wild type, and no cleavage of tRNA bearing a 3' phosphate...

## Biological Role

Activated by rpoD (protein.P00579).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P09155|protein.P09155]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (1)

- `activates` <-- [[protein.P00579|protein.P00579]] `RegulonDB` `S` - sigma=sigma70; target=rnd; function=+

## External IDs

- `Dbxref:ASAP:ABE-0006003,ECOCYC:EG10858,GeneID:946328`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:1886864-1887991:-; feature_type=gene
