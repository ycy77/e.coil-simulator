---
entity_id: "gene.b3302"
entity_type: "gene"
name: "rpmD"
source_database: "NCBI RefSeq"
source_id: "gene-b3302"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b3302"
  - "rpmD"
---

# rpmD

`gene.b3302`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b3302`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

rpmD (gene.b3302) is a gene entity. It encodes rpmD (protein.P0AG51). Encoded protein function: Large ribosomal subunit protein uL30 (50S ribosomal protein L30) EcoCyc product frame: EG10888-MONOMER. Genomic coordinates: 3444543-3444722. EcoCyc protein note: The L30 protein is a component of the 50S subunit of the ribosome. L30 crosslinks to 23S rRNA . An rpmD mutant has a growth and ribosomal assembly defect at 20°C .

## Biological Role

Repressed by rpsH (protein.P0A7W7).

## Enriched Pathways

- `eco03010` Ribosome (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0AG51|protein.P0AG51]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (1)

- `represses` <-- [[protein.P0A7W7|protein.P0A7W7]] `RegulonDB` `S` - regulator=RpsH; target=rpmD; function=-

## External IDs

- `Dbxref:ASAP:ABE-0010821,ECOCYC:EG10888,GeneID:947797`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:3444543-3444722:-; feature_type=gene
