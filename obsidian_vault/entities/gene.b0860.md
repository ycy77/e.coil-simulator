---
entity_id: "gene.b0860"
entity_type: "gene"
name: "artJ"
source_database: "NCBI RefSeq"
source_id: "gene-b0860"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b0860"
  - "artJ"
---

# artJ

`gene.b0860`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b0860`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

artJ (gene.b0860) is a gene entity. It encodes artJ (protein.P30860). Encoded protein function: FUNCTION: Part of the ABC transporter complex ArtPIQMJ involved in arginine transport. Binds L-arginine with high affinity. {ECO:0000269|PubMed:8801422}. EcoCyc product frame: ARTJ-MONOMER. Genomic coordinates: 899844-900575. EcoCyc protein note: artJ encodes the periplasmic binding protein of an L- arginine ABC transporter. Sequence analysis indicates that ArtJ has similarity to the histidine-binding periplasmic protein (HisJ) and lysine/arginine/ornithine binding periplasmic protein (ArgT), both from Salmonella typhimurium. Overexpression of artJ from a plasmid results in the stimulation of L- arginine uptake. Purified ArtJ binds L- arginine with high affinity. It does not bind to the other common amino acids nor to putrescine. ArtJ contains a cleavable signal sequence - the mature protein is located in the periplasmic space .

## Biological Role

Repressed by argR (protein.P0A6D0). Activated by rpoD (protein.P00579).

## Enriched Pathways

- `eco02010` ABC transporters (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P30860|protein.P30860]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (2)

- `activates` <-- [[protein.P00579|protein.P00579]] `RegulonDB` `C` - sigma=sigma70; target=artJ; function=+
- `represses` <-- [[protein.P0A6D0|protein.P0A6D0]] `RegulonDB` `C` - regulator=ArgR; target=artJ; function=-

## External IDs

- `Dbxref:ASAP:ABE-0002927,ECOCYC:EG11628,GeneID:948981`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:899844-900575:-; feature_type=gene
