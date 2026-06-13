---
entity_id: "reaction.ecocyc.RXN-15510"
entity_type: "reaction"
name: "RXN-15510"
source_database: "EcoCyc"
source_id: "RXN-15510"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN-15510

`reaction.ecocyc.RXN-15510`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN-15510`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

Protein-pi-phospho-L-histidines + 2-PG -> Protein-Histidines + 23-DIPHOSPHOGLYCERATE; direction=REVERSIBLE EcoCyc reaction equation: Protein-pi-phospho-L-histidines + 2-PG -> Protein-Histidines + 23-DIPHOSPHOGLYCERATE; direction=REVERSIBLE.

## Biological Role

Substrates: 2-Phospho-D-glycerate (molecule.C00631), a [protein]-Nπ-phospho-L-histidine (molecule.ecocyc.Protein-pi-phospho-L-histidines). Products: 2,3-Bisphospho-D-glycerate (molecule.C01159), a [protein]-L-histidine (molecule.ecocyc.Protein-Histidines).

## Annotation

Protein-pi-phospho-L-histidines + 2-PG -> Protein-Histidines + 23-DIPHOSPHOGLYCERATE; direction=REVERSIBLE

## Outgoing Edges (0)

_None._

## Incoming Edges (4)

- `is_product_of` <-- [[molecule.C01159|molecule.C01159]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.Protein-Histidines|molecule.ecocyc.Protein-Histidines]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00631|molecule.C00631]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.ecocyc.Protein-pi-phospho-L-histidines|molecule.ecocyc.Protein-pi-phospho-L-histidines]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN-15510`

## Notes

Protein-pi-phospho-L-histidines + 2-PG -> Protein-Histidines + 23-DIPHOSPHOGLYCERATE; direction=REVERSIBLE
