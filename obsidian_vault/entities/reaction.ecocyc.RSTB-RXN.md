---
entity_id: "reaction.ecocyc.RSTB-RXN"
entity_type: "reaction"
name: "RSTB-RXN"
source_database: "EcoCyc"
source_id: "RSTB-RXN"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RSTB-RXN

`reaction.ecocyc.RSTB-RXN`

## Static

- Type: `reaction`
- Source: `EcoCyc:RSTB-RXN`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

In this reaction sensor kinase-phosphotransferase RstB autophosphorylates. Based on analogy to other sensor proteins the phosphorylation site is shown as a histidine residue. EcoCyc reaction equation: RSTB-MONOMER + ATP -> PHOSPHO-RSTB + ADP; direction=LEFT-TO-RIGHT. In this reaction sensor kinase-phosphotransferase RstB autophosphorylates. Based on analogy to other sensor proteins the phosphorylation site is shown as a histidine residue.

## Biological Role

Substrates: ATP (molecule.C00002). Products: ADP (molecule.C00008).

## Enriched Pathways

- `ecocyc.PWY0-1497` RstBA Two-Component Signal Transduction System (EcoCyc)

## Annotation

In this reaction sensor kinase-phosphotransferase RstB autophosphorylates. Based on analogy to other sensor proteins the phosphorylation site is shown as a histidine residue.

## Pathways

- `ecocyc.PWY0-1497` RstBA Two-Component Signal Transduction System (EcoCyc)

## Outgoing Edges (0)

_None._

## Incoming Edges (2)

- `is_product_of` <-- [[molecule.C00008|molecule.C00008]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00002|molecule.C00002]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RSTB-RXN`

## Notes

RSTB-MONOMER + ATP -> PHOSPHO-RSTB + ADP; direction=LEFT-TO-RIGHT
