---
entity_id: "gene.b2295"
entity_type: "gene"
name: "yfbV"
source_database: "NCBI RefSeq"
source_id: "gene-b2295"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b2295"
  - "yfbV"
---

# yfbV

`gene.b2295`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b2295`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

yfbV (gene.b2295) is a gene entity. It encodes yfbV (protein.P0A8D9). Encoded protein function: UPF0208 membrane protein YfbV EcoCyc product frame: G7189-MONOMER. Genomic coordinates: 2412677-2413132. EcoCyc protein note: YfbV is involved in insulating the nonstructured regions of the chromosome from the Ter macrodomain . Membrane topology predictions using experimentally determined C terminus locations indicate that YfbV has two transmembrane helices, and the C-terminus is located in the cytoplasm . YfbV was identified in a phylogenetic screen that found proteins containing domains that only occur in organisms that also contain a EG10204-MONOMER Dam methyltransferase .

## Biological Role

Repressed by nac (protein.Q47005).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0A8D9|protein.P0A8D9]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (1)

- `represses` <-- [[protein.Q47005|protein.Q47005]] `RegulonDB` `S` - regulator=Nac; target=yfbV; function=-

## External IDs

- `Dbxref:ASAP:ABE-0007575,ECOCYC:G7189,GeneID:946774`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:2412677-2413132:-; feature_type=gene
