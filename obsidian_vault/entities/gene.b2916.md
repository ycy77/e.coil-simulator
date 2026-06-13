---
entity_id: "gene.b2916"
entity_type: "gene"
name: "argP"
source_database: "NCBI RefSeq"
source_id: "gene-b2916"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b2916"
  - "argP"
---

# argP

`gene.b2916`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b2916`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

argP (gene.b2916) is a gene entity. It encodes argP (protein.P0A8S1). Encoded protein function: FUNCTION: Controls the transcription of genes involved in arginine and lysine metabolism. Activates transcription of several genes, including argO, lysP, lysC, asd, dapB, dapD, lysA, gdhA and argK. Acts by binding directly to their promoter or control region (PubMed:10600368, PubMed:15150242, PubMed:17504942, PubMed:21441513, PubMed:21890697). ArgP dimer by itself is able to bind the argO promoter-operator region to form a binary complex, but the formation of a ternary complex with RNA polymerase is greatly stimulated only in presence of a coeffector. Both arginine and lysine are coeffectors at the argO promoter, but only arginine is competent to activate transcription. Lysine has repressive effects (PubMed:15150242, PubMed:17504942). ArgP also mediates lysine repression of dapB, and gdhA in vivo, but via an alternative mechanism: ArgP binding is directly reduced upon the addition of lysine (PubMed:21890697). Binds in vitro to the promoter region of dnaA and to the upstream region of the nrd promoter, but these genes are probably not regulated by ArgP in vivo (PubMed:21890697, PubMed:9254708, PubMed:9819053). In vitro, also binds to the three 13-mers located in the origin region (oriC) and blocks the initiation of replication (PubMed:1733927)...

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0A8S1|protein.P0A8S1]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (0)

_None._

## External IDs

- `Dbxref:ASAP:ABE-0009574,ECOCYC:EG10490,GeneID:944867`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:3059753-3060646:+; feature_type=gene
