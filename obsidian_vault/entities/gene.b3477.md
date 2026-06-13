---
entity_id: "gene.b3477"
entity_type: "gene"
name: "nikB"
source_database: "NCBI RefSeq"
source_id: "gene-b3477"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b3477"
  - "nikB"
---

# nikB

`gene.b3477`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b3477`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

nikB (gene.b3477) is a gene entity. It encodes nikB (protein.P33591). Encoded protein function: FUNCTION: Involved in a nickel transport system, probably translocates nickel through the bacterial inner membrane. EcoCyc product frame: NIKB-MONOMER. EcoCyc synonyms: hydC, hydD. Genomic coordinates: 3615241-3616185. EcoCyc protein note: NikB is one of two predicted inner membrane subunits of a high affinity uptake system for Ni2+; NikB contains six potential transmembrane α-helices .

## Biological Role

Repressed by nikR (protein.P0A6Z6). Activated by fnr (protein.P0A9E5).

## Enriched Pathways

- `eco02010` ABC transporters (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P33591|protein.P33591]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (2)

- `activates` <-- [[protein.P0A9E5|protein.P0A9E5]] `RegulonDB` `C` - regulator=FNR; target=nikB; function=+
- `represses` <-- [[protein.P0A6Z6|protein.P0A6Z6]] `RegulonDB` `S` - regulator=NikR; target=nikB; function=-

## External IDs

- `Dbxref:ASAP:ABE-0011356,ECOCYC:EG12076,GeneID:947986`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:3615241-3616185:+; feature_type=gene
