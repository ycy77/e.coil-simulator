---
entity_id: "gene.b1847"
entity_type: "gene"
name: "yebF"
source_database: "NCBI RefSeq"
source_id: "gene-b1847"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b1847"
  - "yebF"
---

# yebF

`gene.b1847`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b1847`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

yebF (gene.b1847) is a gene entity. It encodes yebF (protein.P33219). Encoded protein function: Protein YebF EcoCyc product frame: EG11807-MONOMER. Genomic coordinates: 1930034-1930390. EcoCyc protein note: YebF is a secreted protein of unknown function . The precise mechanism by which YebF is secreted to the extracellular medium is not clear however the outer membrane porins EG10671-MONOMER "OmpF", EG10670-MONOMER "OmpC" and EG12117-MONOMER "OmpX" contribute to the process. Deletion of ompF or ompX severely impairs YebF secretion whilst deletion of ompC impairs secretion to a lesser extent. Overexpression of ompF from a plasmid restores secretion of YebF in an ompF deletion strain. YebF blocks conductance of OmpF channels in planar lipid bilayer experiments. Pull-down experiments using his-tagged YebF suggest that YebF interacts with OmpX and OmpF/C. YebF interacts with OmpF/C at the periplasmic face of the outer membrane . An NMR derived solution structure of YebF indicates that the protein is composed of an ordered core surrounded by a dynamic surface including two extended loop structures . YebF has been used as a carrier protein to direct secretion of fusion proteins (eg.YebF-α-amylase and YebF-human interleukin-2) to the culture medium

## Biological Role

Repressed by lrp (protein.P0ACJ0).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P33219|protein.P33219]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (1)

- `represses` <-- [[protein.P0ACJ0|protein.P0ACJ0]] `EcoCyc` `database` - EcoCyc regulation TYPES=Transcription-Factor-Binding

## External IDs

- `Dbxref:ASAP:ABE-0006141,ECOCYC:EG11807,GeneID:946363`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:1930034-1930390:-; feature_type=gene
