---
entity_id: "gene.b3078"
entity_type: "gene"
name: "ygjI"
source_database: "NCBI RefSeq"
source_id: "gene-b3078"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b3078"
  - "ygjI"
---

# ygjI

`gene.b3078`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b3078`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

ygjI (gene.b3078) is a gene entity. It encodes ygjI (protein.P42590). Encoded protein function: Inner membrane transporter YgjI EcoCyc product frame: YGJI-MONOMER. Genomic coordinates: 3226234-3227667. EcoCyc protein note: The YgjI protein is an uncharacterised member of the Glutamate:GABA Antiporter (GGA) family of transporters within the Amino Acid-Polyamine-Organocation (APC) Superfamily .

## Biological Role

Repressed by nac (protein.Q47005). Activated by glaR (protein.P37338).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P42590|protein.P42590]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (2)

- `activates` <-- [[protein.P37338|protein.P37338]] `RegulonDB` `S` - regulator=GlaR; target=ygjI; function=+
- `represses` <-- [[protein.Q47005|protein.Q47005]] `RegulonDB` `S` - regulator=Nac; target=ygjI; function=-

## External IDs

- `Dbxref:ASAP:ABE-0010110,ECOCYC:EG12720,GeneID:947579`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:3226234-3227667:+; feature_type=gene
