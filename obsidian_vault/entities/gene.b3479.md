---
entity_id: "gene.b3479"
entity_type: "gene"
name: "nikD"
source_database: "NCBI RefSeq"
source_id: "gene-b3479"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b3479"
  - "nikD"
---

# nikD

`gene.b3479`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b3479`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

nikD (gene.b3479) is a gene entity. It encodes nikD (protein.P33593). Encoded protein function: FUNCTION: Part of the ABC transporter complex NikABCDE involved in nickel import. Responsible for energy coupling to the transport system. {ECO:0000255|HAMAP-Rule:MF_01711}. EcoCyc product frame: NIKD-MONOMER. EcoCyc synonyms: hydD, hydC. Genomic coordinates: 3617015-3617779. EcoCyc protein note: NikD is one of two predicted ATP-binding subunits of a high affinity uptake system for Ni2+; NikD contains signature motifs conserved in ATP-binding cassette (ABC) domains .

## Biological Role

Repressed by nikR (protein.P0A6Z6). Activated by fnr (protein.P0A9E5).

## Enriched Pathways

- `eco02010` ABC transporters (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P33593|protein.P33593]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (2)

- `activates` <-- [[protein.P0A9E5|protein.P0A9E5]] `RegulonDB` `C` - regulator=FNR; target=nikD; function=+
- `represses` <-- [[protein.P0A6Z6|protein.P0A6Z6]] `RegulonDB` `S` - regulator=NikR; target=nikD; function=-

## External IDs

- `Dbxref:ASAP:ABE-0011360,ECOCYC:EG12078,GeneID:947989`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:3617015-3617779:+; feature_type=gene
