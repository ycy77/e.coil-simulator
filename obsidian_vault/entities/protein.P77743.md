---
entity_id: "protein.P77743"
entity_type: "protein"
name: "prpR"
source_database: "UniProt"
source_id: "P77743"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "prpR yahP b0330 JW0322"
---

# prpR

`protein.P77743`

## Static

- Type: `protein`
- Source: `UniProt:P77743`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`

## Enriched Summary

FUNCTION: Involved in the transcriptional regulation of the propionate catabolism operon.

## Biological Role

Component of DNA-binding transcriptional dual regulator PrpR-(2S,3S)-2-methylcitrate (complex.ecocyc.MONOMER0-2421).

## Annotation

FUNCTION: Involved in the transcriptional regulation of the propionate catabolism operon.

## Outgoing Edges (1)

- `is_component_of` --> [[complex.ecocyc.MONOMER0-2421|complex.ecocyc.MONOMER0-2421]] `EcoCyc` `database` - EcoCyc component coefficient=

## Incoming Edges (1)

- `encodes` <-- [[gene.b0330|gene.b0330]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P77743`
- `KEGG:ecj:JW0322;eco:b0330;ecoc:C3026_01620;ecoc:C3026_24790;`
- `GeneID:944987;`
- `GO:GO:0000156; GO:0000987; GO:0001216; GO:0003700; GO:0005524; GO:0005737; GO:0009314; GO:0019629; GO:0032993; GO:0045892; GO:0045893`

## Notes

Propionate catabolism operon regulatory protein
