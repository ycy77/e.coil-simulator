---
entity_id: "gene.b1605"
entity_type: "gene"
name: "ydgI"
source_database: "NCBI RefSeq"
source_id: "gene-b1605"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b1605"
  - "ydgI"
---

# ydgI

`gene.b1605`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b1605`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

ydgI (gene.b1605) is a gene entity. It encodes ydgI (protein.P0AAE5). Encoded protein function: FUNCTION: Catalyzes electroneutral exchange between arginine and ornithine to allow high-efficiency energy conversion in the arginine deiminase pathway. {ECO:0000250|UniProtKB:P18275}. EcoCyc product frame: ARCD-MONOMER. EcoCyc synonyms: arcD. Genomic coordinates: 1679557-1680939. EcoCyc protein note: In the Transporter Classification Database, YdgI is a putative arginine:ornithine antiporter and a member of the Basic Amino Acid/Polyamine Antiporter (APA) Family within the Amino Acid-Polyamine-Organocation (APC) Superfamily . ydgI is similar to the arcD gene of Pseudomonas aeruginosa which encodes an arginine:ornithine antiporter .

## Biological Role

Repressed by ArgR-L-arginine DNA-binding transcriptional dual regulator (complex.ecocyc.CPLX0-228), argR (protein.P0A6D0).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0AAE5|protein.P0AAE5]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (2)

- `represses` <-- [[complex.ecocyc.CPLX0-228|complex.ecocyc.CPLX0-228]] `EcoCyc` `database` - EcoCyc regulation TYPES=Transcription-Factor-Binding
- `represses` <-- [[protein.P0A6D0|protein.P0A6D0]] `RegulonDB` `S` - regulator=ArgR; target=ydgI; function=-

## External IDs

- `Dbxref:ASAP:ABE-0005362,ECOCYC:G6861,GeneID:945159`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:1679557-1680939:+; feature_type=gene
