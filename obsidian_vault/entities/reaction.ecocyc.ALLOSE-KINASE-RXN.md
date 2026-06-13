---
entity_id: "reaction.ecocyc.ALLOSE-KINASE-RXN"
entity_type: "reaction"
name: "ALLOSE-KINASE-RXN"
source_database: "EcoCyc"
source_id: "ALLOSE-KINASE-RXN"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
  - "Allokinase"
---

# ALLOSE-KINASE-RXN

`reaction.ecocyc.ALLOSE-KINASE-RXN`

## Static

- Type: `reaction`
- Source: `EcoCyc:ALLOSE-KINASE-RXN`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

D-Allopyranose + ATP -> PROTON + D-ALLOSE-6-PHOSPHATE + ADP; direction=LEFT-TO-RIGHT EcoCyc reaction equation: D-Allopyranose + ATP -> PROTON + D-ALLOSE-6-PHOSPHATE + ADP; direction=LEFT-TO-RIGHT.

## Biological Role

Catalyzed by alsK (protein.P32718). Substrates: ATP (molecule.C00002), D-allopyranose (molecule.ecocyc.D-Allopyranose). Products: ADP (molecule.C00008), H+ (molecule.C00080), D-Allose 6-phosphate (molecule.C02962).

## Enriched Pathways

- `ecocyc.PWY0-44` D-allose degradation (EcoCyc)

## Annotation

D-Allopyranose + ATP -> PROTON + D-ALLOSE-6-PHOSPHATE + ADP; direction=LEFT-TO-RIGHT

## Pathways

- `ecocyc.PWY0-44` D-allose degradation (EcoCyc)

## Outgoing Edges (0)

_None._

## Incoming Edges (6)

- `catalyzes` <-- [[protein.P32718|protein.P32718]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00008|molecule.C00008]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C02962|molecule.C02962]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00002|molecule.C00002]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.ecocyc.D-Allopyranose|molecule.ecocyc.D-Allopyranose]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:ALLOSE-KINASE-RXN`

## Notes

D-Allopyranose + ATP -> PROTON + D-ALLOSE-6-PHOSPHATE + ADP; direction=LEFT-TO-RIGHT
