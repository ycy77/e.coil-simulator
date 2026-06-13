---
entity_id: "protein.P0ACR0"
entity_type: "protein"
name: "allS"
source_database: "UniProt"
source_id: "P0ACR0"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "allS glxA1 ybbS b0504 JW0492"
---

# allS

`protein.P0ACR0`

## Static

- Type: `protein`
- Source: `UniProt:P0ACR0`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`

## Enriched Summary

FUNCTION: Positive regulator essential for the expression of allD operon. Binds to the allD promoter. {ECO:0000269|PubMed:12460564}.

## Biological Role

Component of AllS-allantoin DNA-binding transcriptional activator (complex.ecocyc.MONOMER0-2221).

## Annotation

FUNCTION: Positive regulator essential for the expression of allD operon. Binds to the allD promoter. {ECO:0000269|PubMed:12460564}.

## Outgoing Edges (1)

- `is_component_of` --> [[complex.ecocyc.MONOMER0-2221|complex.ecocyc.MONOMER0-2221]] `EcoCyc` `database` - EcoCyc component coefficient=

## Incoming Edges (1)

- `encodes` <-- [[gene.b0504|gene.b0504]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P0ACR0`
- `KEGG:ecj:JW0492;eco:b0504;ecoc:C3026_02475;`
- `GeneID:75170528;75202347;945139;`
- `GO:GO:0003700; GO:0006355; GO:0043565; GO:0045893`

## Notes

HTH-type transcriptional activator AllS
