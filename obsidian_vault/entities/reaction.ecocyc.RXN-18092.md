---
entity_id: "reaction.ecocyc.RXN-18092"
entity_type: "reaction"
name: "RXN-18092"
source_database: "EcoCyc"
source_id: "RXN-18092"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: "CCI-PERI-BAC-GN"
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN-18092

`reaction.ecocyc.RXN-18092`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN-18092`
- Default state: `active`
- Allowed states: `active|blocked`
- Location: CCI-PERI-BAC-GN

## Enriched Summary

GLUTATHIONE + GLYCYLGLYCINE -> CPD-19395 + CYS-GLY; direction=PHYSIOL-LEFT-TO-RIGHT EcoCyc reaction equation: GLUTATHIONE + GLYCYLGLYCINE -> CPD-19395 + CYS-GLY; direction=PHYSIOL-LEFT-TO-RIGHT.

## Biological Role

Catalyzed by glutathione hydrolase (complex.ecocyc.CPLX0-7885). Substrates: Glutathione (molecule.C00051), glycyl-glycine (molecule.ecocyc.GLYCYLGLYCINE). Products: Cys-Gly (molecule.C01419), γ-L-glutamyl-glycylglycine (molecule.ecocyc.CPD-19395).

## Annotation

GLUTATHIONE + GLYCYLGLYCINE -> CPD-19395 + CYS-GLY; direction=PHYSIOL-LEFT-TO-RIGHT

## Outgoing Edges (0)

_None._

## Incoming Edges (5)

- `catalyzes` <-- [[complex.ecocyc.CPLX0-7885|complex.ecocyc.CPLX0-7885]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C01419|molecule.C01419]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.CPD-19395|molecule.ecocyc.CPD-19395]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00051|molecule.C00051]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.ecocyc.GLYCYLGLYCINE|molecule.ecocyc.GLYCYLGLYCINE]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN-18092`

## Notes

GLUTATHIONE + GLYCYLGLYCINE -> CPD-19395 + CYS-GLY; direction=PHYSIOL-LEFT-TO-RIGHT
