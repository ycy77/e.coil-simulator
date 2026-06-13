---
entity_id: "gene.b2372"
entity_type: "gene"
name: "yfdV"
source_database: "NCBI RefSeq"
source_id: "gene-b2372"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b2372"
  - "yfdV"
---

# yfdV

`gene.b2372`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b2372`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

yfdV (gene.b2372) is a gene entity. It encodes yfdV (protein.P0AA49). Encoded protein function: Uncharacterized transporter YfdV EcoCyc product frame: B2372-MONOMER. Genomic coordinates: 2489242-2490186. EcoCyc protein note: In the Transporter Classification Database, YfdV (from E. coli O6:H1) is an uncharacterised member of the AEC family of auxin efflux transporters; bacterial members of this family are implicated in malonate/malate transport . A variety of potential substrates were identified using an untargeted metabolomics approach .

## Biological Role

Activated by evgA (protein.P0ACZ4), glaR (protein.P37338), nac (protein.Q47005).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0AA49|protein.P0AA49]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (3)

- `activates` <-- [[protein.P0ACZ4|protein.P0ACZ4]] `RegulonDB` `S` - regulator=EvgA; target=yfdV; function=+
- `activates` <-- [[protein.P37338|protein.P37338]] `RegulonDB|EcoCyc` `S` - regulator=GlaR; target=yfdV; function=+ | EcoCyc regulation TYPES=Transcription-Factor-Binding
- `activates` <-- [[protein.Q47005|protein.Q47005]] `RegulonDB` `S` - regulator=Nac; target=yfdV; function=+

## External IDs

- `Dbxref:ASAP:ABE-0007824,ECOCYC:G7235,GeneID:949110`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:2489242-2490186:-; feature_type=gene
