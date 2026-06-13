---
entity_id: "gene.b3480"
entity_type: "gene"
name: "nikE"
source_database: "NCBI RefSeq"
source_id: "gene-b3480"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b3480"
  - "nikE"
---

# nikE

`gene.b3480`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b3480`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

nikE (gene.b3480) is a gene entity. It encodes nikE (protein.P33594). Encoded protein function: FUNCTION: Part of the ABC transporter complex NikABCDE involved in nickel import. Responsible for energy coupling to the transport system. {ECO:0000255|HAMAP-Rule:MF_01712}. EcoCyc product frame: NIKE-MONOMER. EcoCyc synonyms: hydD, hydC. Genomic coordinates: 3617776-3618582. EcoCyc protein note: NikE is one of two predicted ATP-binding subunits of a high affinity uptake system for Ni2+; NikE contains signature motifs conserved in ATP-binding cassette (ABC) domains .

## Biological Role

Repressed by nikR (protein.P0A6Z6). Activated by fnr (protein.P0A9E5).

## Enriched Pathways

- `eco02010` ABC transporters (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P33594|protein.P33594]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (2)

- `activates` <-- [[protein.P0A9E5|protein.P0A9E5]] `RegulonDB` `C` - regulator=FNR; target=nikE; function=+
- `represses` <-- [[protein.P0A6Z6|protein.P0A6Z6]] `RegulonDB` `S` - regulator=NikR; target=nikE; function=-

## External IDs

- `Dbxref:ASAP:ABE-0011362,ECOCYC:EG12079,GeneID:947987`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:3617776-3618582:+; feature_type=gene
