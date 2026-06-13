---
entity_id: "gene.b1126"
entity_type: "gene"
name: "potA"
source_database: "NCBI RefSeq"
source_id: "gene-b1126"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b1126"
  - "potA"
---

# potA

`gene.b1126`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b1126`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

potA (gene.b1126) is a gene entity. It encodes potA (protein.P69874). Encoded protein function: FUNCTION: Part of the ABC transporter complex PotABCD involved in spermidine/putrescine import. Responsible for energy coupling to the transport system. {ECO:0000255|HAMAP-Rule:MF_01726, ECO:0000269|PubMed:1939142, ECO:0000269|PubMed:2249996, ECO:0000269|PubMed:8366082}. EcoCyc product frame: POTA-MONOMER. Genomic coordinates: 1184458-1185594. EcoCyc protein note: PotA is the ATP-binding subunit of a high affinity spermidine uptake system. PotA contains signature motifs conserved in ATP-binding cassette (ABC) proteins . PotA binds nucleotides with the following specificity: ATP>GTP=ADP>CTP=UTP . PotA associates with the membrane through its interaction with PotB and PotC; purified PotA has Mg2+ dependent ATPase activity which is inhibited by spermidine and spermine but not by putrescine; the C-terminal domain of PotA (residues 251-378) may contain a spermidine binding site which is involved in regulation of its ATPase activity . PotA is able to form dimers but each PotA subunit appears to function independently (no cooperativity for ATP during ATP hydrolysis)

## Enriched Pathways

- `eco02010` ABC transporters (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P69874|protein.P69874]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (0)

_None._

## External IDs

- `Dbxref:ASAP:ABE-0003796,ECOCYC:EG10749,GeneID:946323`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:1184458-1185594:-; feature_type=gene
