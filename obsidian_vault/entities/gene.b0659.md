---
entity_id: "gene.b0659"
entity_type: "gene"
name: "ybeY"
source_database: "NCBI RefSeq"
source_id: "gene-b0659"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b0659"
  - "ybeY"
---

# ybeY

`gene.b0659`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b0659`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

ybeY (gene.b0659) is a gene entity. It encodes ybeY (protein.P0A898). Encoded protein function: FUNCTION: Single strand-specific metallo-endoribonuclease involved in late-stage 70S ribosome quality control and in maturation of the 3' terminus of the 16S rRNA. Acts together with the RNase R to eliminate defective 70S ribosomes, but not properly matured 70S ribosomes or individual subunits, by a process mediated specifically by the 30S ribosomal subunit. Involved in the processing of 16S, 23S and 5S rRNAs, with a particularly strong effect on maturation at both the 5'- and 3'-ends of 16S rRNA as well as maturation of the 5'-end of 23S and 5S rRNAs. {ECO:0000255|HAMAP-Rule:MF_00009, ECO:0000269|PubMed:16511207, ECO:0000269|PubMed:20639334, ECO:0000269|PubMed:20807199, ECO:0000269|PubMed:23273979}. EcoCyc product frame: G6362-MONOMER. Genomic coordinates: 691874-692341. EcoCyc protein note: YbeY is a metal-dependent single strand-specific endoribonuclease that is involved in maturation of 16S rRNA and in transcription antitermination at an rRNA promoter . RNase R and YbeY together (but not alone) are able to completely degrade defective 70S ribosomes generated in a ybeY mutant...

## Biological Role

Activated by rpoH (protein.P0AGB3).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0A898|protein.P0A898]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (1)

- `activates` <-- [[protein.P0AGB3|protein.P0AGB3]] `RegulonDB` `S` - sigma=sigma32; target=ybeY; function=+

## External IDs

- `Dbxref:ASAP:ABE-0002255,ECOCYC:G6362,GeneID:946430`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:691874-692341:-; feature_type=gene
