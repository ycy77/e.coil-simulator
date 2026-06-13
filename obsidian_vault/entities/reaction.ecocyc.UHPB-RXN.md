---
entity_id: "reaction.ecocyc.UHPB-RXN"
entity_type: "reaction"
name: "UHPB-RXN"
source_database: "EcoCyc"
source_id: "UHPB-RXN"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# UHPB-RXN

`reaction.ecocyc.UHPB-RXN`

## Static

- Type: `reaction`
- Source: `EcoCyc:UHPB-RXN`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

In this reaction sensor kinase-phosphotransferase UhpB autophosphorylates. The UhpB protein contains an invariant histidine residue which is thought to be the phosphorylation site. EcoCyc reaction equation: UHPB-MONOMER + ATP -> PHOSPHO-UHPB + ADP; direction=LEFT-TO-RIGHT. In this reaction sensor kinase-phosphotransferase UhpB autophosphorylates. The UhpB protein contains an invariant histidine residue which is thought to be the phosphorylation site.

## Biological Role

Substrates: ATP (molecule.C00002). Products: ADP (molecule.C00008).

## Enriched Pathways

- `ecocyc.PWY0-1492` UhpBA Two Component Signal Transduction System (EcoCyc)

## Annotation

In this reaction sensor kinase-phosphotransferase UhpB autophosphorylates. The UhpB protein contains an invariant histidine residue which is thought to be the phosphorylation site.

## Pathways

- `ecocyc.PWY0-1492` UhpBA Two Component Signal Transduction System (EcoCyc)

## Outgoing Edges (0)

_None._

## Incoming Edges (2)

- `is_product_of` <-- [[molecule.C00008|molecule.C00008]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00002|molecule.C00002]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:UHPB-RXN`

## Notes

UHPB-MONOMER + ATP -> PHOSPHO-UHPB + ADP; direction=LEFT-TO-RIGHT
