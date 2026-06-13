---
entity_id: "reaction.ecocyc.RIBOKIN-RXN"
entity_type: "reaction"
name: "RIBOKIN-RXN"
source_database: "EcoCyc"
source_id: "RIBOKIN-RXN"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RIBOKIN-RXN

`reaction.ecocyc.RIBOKIN-RXN`

## Static

- Type: `reaction`
- Source: `EcoCyc:RIBOKIN-RXN`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

carbon compounds degradation EcoCyc reaction equation: D-Ribofuranose + ATP -> CPD-15317 + ADP + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT. carbon compounds degradation

## Biological Role

Catalyzed by ribokinase (complex.ecocyc.CPLX0-7647). Substrates: ATP (molecule.C00002), D-ribofuranose (molecule.ecocyc.D-Ribofuranose). Products: ADP (molecule.C00008), H+ (molecule.C00080), D-ribofuranose 5-phosphate (molecule.ecocyc.CPD-15317).

## Enriched Pathways

- `ecocyc.RIBOKIN-PWY` ribose phosphorylation (EcoCyc)

## Annotation

carbon compounds degradation

## Pathways

- `ecocyc.RIBOKIN-PWY` ribose phosphorylation (EcoCyc)

## Outgoing Edges (0)

_None._

## Incoming Edges (7)

- `activates` <-- [[molecule.ecocyc.Pi|molecule.ecocyc.Pi]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `catalyzes` <-- [[complex.ecocyc.CPLX0-7647|complex.ecocyc.CPLX0-7647]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00008|molecule.C00008]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.CPD-15317|molecule.ecocyc.CPD-15317]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00002|molecule.C00002]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.ecocyc.D-Ribofuranose|molecule.ecocyc.D-Ribofuranose]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RIBOKIN-RXN`

## Notes

D-Ribofuranose + ATP -> CPD-15317 + ADP + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT
