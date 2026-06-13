---
entity_id: "gene.b3055"
entity_type: "gene"
name: "ygiM"
source_database: "NCBI RefSeq"
source_id: "gene-b3055"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b3055"
  - "ygiM"
---

# ygiM

`gene.b3055`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b3055`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

ygiM (gene.b3055) is a gene entity. It encodes ygiM (protein.P0ADT8). Encoded protein function: Uncharacterized protein YgiM EcoCyc product frame: EG12434-MONOMER. EcoCyc synonyms: ecfG, htrG. Genomic coordinates: 3201207-3201827. EcoCyc protein note: Proteomic analysis of membrane preparations suggests that YgiM forms a homo-oligomeric complex . The C-terminus of YgiM is located in the cytoplasm . YgiM is predicted to be a bitopic inner membrane protein . YgiM contains a carboxy-terminal tail-anchor sequence which targets to peroxisomes in yeast and mammalian cells . Transcription of ygiM is regulated by RpoE (σE) . EcfG: "extracytoplasmic function G"

## Biological Role

Repressed by nac (protein.Q47005). Activated by rpoE (protein.P0AGB6).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0ADT8|protein.P0ADT8]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (2)

- `activates` <-- [[protein.P0AGB6|protein.P0AGB6]] `RegulonDB` `S` - sigma=sigma24; target=ygiM; function=+
- `represses` <-- [[protein.Q47005|protein.Q47005]] `RegulonDB|EcoCyc` `S` - regulator=Nac; target=ygiM; function=- | EcoCyc regulation TYPES=Transcription-Factor-Binding

## External IDs

- `Dbxref:ASAP:ABE-0010028,ECOCYC:EG12434,GeneID:947555`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:3201207-3201827:+; feature_type=gene
