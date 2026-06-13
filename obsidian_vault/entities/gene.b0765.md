---
entity_id: "gene.b0765"
entity_type: "gene"
name: "modC"
source_database: "NCBI RefSeq"
source_id: "gene-b0765"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b0765"
  - "modC"
---

# modC

`gene.b0765`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b0765`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

modC (gene.b0765) is a gene entity. It encodes modC (protein.P09833). Encoded protein function: FUNCTION: Part of the ABC transporter complex ModABC involved in molybdenum import. Responsible for energy coupling to the transport system. {ECO:0000255|HAMAP-Rule:MF_01705}. EcoCyc product frame: MODC-MONOMER. EcoCyc synonyms: chlD, narD. Genomic coordinates: 796554-797612. EcoCyc protein note: ModC is the predicted ATP-binding component of of an ABC transporter that mediates the high affinity uptake of molybdate. ModC contains an ABC-ABC domain .

## Biological Role

Repressed by modE (protein.P0A9G8). Activated by rpoD (protein.P00579).

## Enriched Pathways

- `eco02010` ABC transporters (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P09833|protein.P09833]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (2)

- `activates` <-- [[protein.P00579|protein.P00579]] `RegulonDB` `S` - sigma=sigma70; target=modC; function=+
- `represses` <-- [[protein.P0A9G8|protein.P0A9G8]] `RegulonDB` `C` - regulator=ModE; target=modC; function=-

## External IDs

- `Dbxref:ASAP:ABE-0002605,ECOCYC:EG10152,GeneID:945362`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:796554-797612:+; feature_type=gene
