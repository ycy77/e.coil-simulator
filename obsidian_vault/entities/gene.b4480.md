---
entity_id: "gene.b4480"
entity_type: "gene"
name: "hdfR"
source_database: "NCBI RefSeq"
source_id: "gene-b4480"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b4480"
  - "hdfR"
---

# hdfR

`gene.b4480`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b4480`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

hdfR (gene.b4480) is a gene entity. It encodes hdfR (protein.P0A8R9). Encoded protein function: FUNCTION: Negatively regulates the transcription of the flagellar master operon flhDC by binding to the upstream region of the operon. {ECO:0000269|PubMed:10913108}. EcoCyc product frame: EG11449-MONOMER. EcoCyc synonyms: b3762, yifA, yifD, b3763. Genomic coordinates: 3947128-3947967. EcoCyc protein note: "Hns-dependent flhDC regulator," HdfR, negatively regulates the expression of the flagellar master operon, flhDC and positively regulates the expression of the gltBD operon . H-NS is a direct activator of the flhDC operon and represses transcription of hdfR. Using a machine learning framework that integrates and analyzes data from 10 different sources, it was determined that HdfR is involved in antibiotic resistance . HdfR is a transcriptional regulator that belongs to the LysR family. It consist of two domains, an amino-terminal domain that contains a potential helix-turn-helix DNA-binding motif and a carboxy-terminal domain involved in co-inducer recognition . Little is known about the regulatory role of HdfR, and the binding sites for this transcription factor have not yet been determined...

## Biological Role

Repressed by hns (protein.P0ACF8).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0A8R9|protein.P0A8R9]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (1)

- `represses` <-- [[protein.P0ACF8|protein.P0ACF8]] `RegulonDB` `S` - regulator=H-NS; target=hdfR; function=-

## External IDs

- `Dbxref:ASAP:ABE-0174109,ECOCYC:EG11449,GeneID:2847698`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:3947128-3947967:-; feature_type=gene
