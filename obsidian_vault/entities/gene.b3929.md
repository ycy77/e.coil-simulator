---
entity_id: "gene.b3929"
entity_type: "gene"
name: "rraA"
source_database: "NCBI RefSeq"
source_id: "gene-b3929"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b3929"
  - "rraA"
---

# rraA

`gene.b3929`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b3929`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

rraA (gene.b3929) is a gene entity. It encodes rraA (protein.P0A8R0). Encoded protein function: FUNCTION: Globally modulates RNA abundance by binding to RNase E (Rne) and regulating its endonucleolytic activity. Can modulate Rne action in a substrate-dependent manner by altering the composition of the degradosome. Modulates RNA-binding and helicase activities of the degradosome. {ECO:0000269|PubMed:13678585, ECO:0000269|PubMed:16725107, ECO:0000269|PubMed:16771842, ECO:0000269|PubMed:18510556, ECO:0000269|PubMed:20106955}. EcoCyc product frame: EG11879-MONOMER. EcoCyc synonyms: menG, yiiV. Genomic coordinates: 4118845-4119330. EcoCyc protein note: RraA inhibits CPLX0-3461 activity by binding to and masking the C-terminal RNA binding domain of RNase E. The interaction of RraA with the degradosome is facilitated by protein-RNA remodeling via the ATPase activity of RhlB . RraA physically interacts with RNase E, but does not interact with the RNA substrates . High-affinity binding of RraA to RNase E requires the C-terminal domain (CTD) of RNase E . RraA interacts with both RNA-binding sites of RNase E and interferes with their interaction with RNA . RraA also interacts with the RhlB helicase component of the degradosome, and a ternary complex of RraA, RNase E and RhlB can be observed...

## Biological Role

Activated by rpoS (protein.P13445).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0A8R0|protein.P0A8R0]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (1)

- `activates` <-- [[protein.P13445|protein.P13445]] `RegulonDB` `S` - sigma=sigma38; target=rraA; function=+

## External IDs

- `Dbxref:ASAP:ABE-0012837,ECOCYC:EG11879,GeneID:948419`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:4118845-4119330:-; feature_type=gene
