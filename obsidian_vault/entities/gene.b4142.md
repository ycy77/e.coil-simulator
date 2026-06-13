---
entity_id: "gene.b4142"
entity_type: "gene"
name: "groS"
source_database: "NCBI RefSeq"
source_id: "gene-b4142"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b4142"
  - "groS"
---

# groS

`gene.b4142`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b4142`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

groS (gene.b4142) is a gene entity. It encodes groES (protein.P0A6F9). Encoded protein function: FUNCTION: Together with the chaperonin GroEL, plays an essential role in assisting protein folding (PubMed:10532860, PubMed:16751100, PubMed:1676490, PubMed:18418386, PubMed:18987317, PubMed:20603018, PubMed:24816391, PubMed:2573517, PubMed:2897629). The GroEL-GroES system forms a nano-cage that allows encapsulation of the non-native substrate proteins and provides a physical environment optimized to promote and accelerate protein folding, probably by preventing aggregation and by entropically destabilizing folding intermediates (PubMed:16751100, PubMed:18418386, PubMed:18987317, PubMed:20603018, PubMed:24816391). GroES binds to the apical surface of the GroEL ring, thereby capping the opening of the GroEL channel (PubMed:9285585). Regulates the ATPase activity of GroEL (PubMed:1361169, PubMed:1676490). {ECO:0000269|PubMed:10532860, ECO:0000269|PubMed:1361169, ECO:0000269|PubMed:16751100, ECO:0000269|PubMed:1676490, ECO:0000269|PubMed:18418386, ECO:0000269|PubMed:18987317, ECO:0000269|PubMed:20603018, ECO:0000269|PubMed:24816391, ECO:0000269|PubMed:2573517, ECO:0000269|PubMed:2897629, ECO:0000269|PubMed:9285585}.; FUNCTION: (Microbial infection) Essential for the assembly of several bacteriophages. {ECO:0000269|PubMed:379350, ECO:0000269|PubMed:7015340}...

## Biological Role

Repressed by lrp (protein.P0ACJ0). Activated by nac (protein.Q47005).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0A6F9|protein.P0A6F9]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (2)

- `activates` <-- [[protein.Q47005|protein.Q47005]] `RegulonDB|EcoCyc` `S` - regulator=Nac; target=groS; function=+ | EcoCyc regulation TYPES=Transcription-Factor-Binding
- `represses` <-- [[protein.P0ACJ0|protein.P0ACJ0]] `EcoCyc` `database` - EcoCyc regulation TYPES=Transcription-Factor-Binding

## External IDs

- `Dbxref:ASAP:ABE-0013566,ECOCYC:EG10600,GeneID:948655`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:4370688-4370981:+; feature_type=gene
