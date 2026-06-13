---
entity_id: "gene.b0158"
entity_type: "gene"
name: "btuF"
source_database: "NCBI RefSeq"
source_id: "gene-b0158"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b0158"
  - "btuF"
---

# btuF

`gene.b0158`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b0158`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

btuF (gene.b0158) is a gene entity. It encodes btuF (protein.P37028). Encoded protein function: FUNCTION: Part of the ABC transporter complex BtuCDF involved in vitamin B12 import. Binds vitamin B12 and delivers it to the periplasmic surface of BtuC. {ECO:0000255|HAMAP-Rule:MF_01000, ECO:0000269|PubMed:11790740}. EcoCyc product frame: EG12334-MONOMER. EcoCyc synonyms: yadT. Genomic coordinates: 177662-178462. EcoCyc protein note: BtuF is the periplasmic binding protein of an ATP-dependent vitamin B12 uptake system. Purified BtuF binds cyanocobalamin with high affinity (Kd approx 15 nM) ; purified BtuF binds cobinamide with high affinity (Kd = 40 nM) Purified BtuF contains two structurally similar lobes connected by a single linking α-helix; Vitamin B12 binds in a deep cleft between the two lobes

## Biological Role

Activated by rpoD (protein.P00579), rpoS (protein.P13445).

## Enriched Pathways

- `eco02010` ABC transporters (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P37028|protein.P37028]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (2)

- `activates` <-- [[protein.P00579|protein.P00579]] `RegulonDB` `S` - sigma=sigma70; target=btuF; function=+
- `activates` <-- [[protein.P13445|protein.P13445]] `RegulonDB` `S` - sigma=sigma38; target=btuF; function=+

## External IDs

- `Dbxref:ASAP:ABE-0000542,ECOCYC:EG12334,GeneID:947574`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:177662-178462:-; feature_type=gene
