---
entity_id: "gene.b4106"
entity_type: "gene"
name: "phnC"
source_database: "NCBI RefSeq"
source_id: "gene-b4106"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b4106"
  - "phnC"
---

# phnC

`gene.b4106`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b4106`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

phnC (gene.b4106) is a gene entity. It encodes phnC (protein.P16677). Encoded protein function: FUNCTION: Part of the ABC transporter complex PhnCDE involved in phosphonates, phosphate esters, phosphite and phosphate import. Responsible for energy coupling to the transport system. {ECO:0000269|PubMed:1846145, ECO:0000269|PubMed:8388873}. EcoCyc product frame: PHNC-MONOMER. Genomic coordinates: 4324377-4325165. EcoCyc protein note: phnC encodes the ATP binding subunit of a phosphonate/phosphate uptake system that is considered to be cryptic in E. coli K-12.phnC contains signature motifs conserved in ATP-binding cassette proteins .

## Biological Role

Activated by rpoD (protein.P00579), phoB (protein.P0AFJ5).

## Enriched Pathways

- `eco02010` ABC transporters (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P16677|protein.P16677]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (2)

- `activates` <-- [[protein.P00579|protein.P00579]] `RegulonDB` `S` - sigma=sigma70; target=phnC; function=+
- `activates` <-- [[protein.P0AFJ5|protein.P0AFJ5]] `RegulonDB|EcoCyc` `S` - regulator=PhoB; target=phnC; function=+ | EcoCyc regulation TYPES=Transcription-Factor-Binding

## External IDs

- `Dbxref:ASAP:ABE-0013444,ECOCYC:EG10713,GeneID:948623`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:4324377-4325165:-; feature_type=gene
