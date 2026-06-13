---
entity_id: "reaction.ecocyc.GLUCOKIN-RXN"
entity_type: "reaction"
name: "GLUCOKIN-RXN"
source_database: "EcoCyc"
source_id: "GLUCOKIN-RXN"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# GLUCOKIN-RXN

`reaction.ecocyc.GLUCOKIN-RXN`

## Static

- Type: `reaction`
- Source: `EcoCyc:GLUCOKIN-RXN`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

Glucopyranose + ATP -> D-glucopyranose-6-phosphate + ADP + PROTON; direction=LEFT-TO-RIGHT EcoCyc reaction equation: Glucopyranose + ATP -> D-glucopyranose-6-phosphate + ADP + PROTON; direction=LEFT-TO-RIGHT.

## Biological Role

Catalyzed by glk (protein.P0A6V8). Substrates: ATP (molecule.C00002), D-Glucose (molecule.C00031). Products: ADP (molecule.C00008), H+ (molecule.C00080), D-Glucose 6-phosphate (molecule.C00092).

## Enriched Pathways

- `ecocyc.GLUCOSE1PMETAB-PWY` glucose and glucose-1-phosphate degradation (EcoCyc)
- `ecocyc.GLYCOCAT-PWY` glycogen degradation I (EcoCyc)
- `ecocyc.PWY0-1182` trehalose degradation II (cytosolic) (EcoCyc)
- `ecocyc.TREDEGLOW-PWY` trehalose degradation I (low osmolarity) (EcoCyc)

## Annotation

Glucopyranose + ATP -> D-glucopyranose-6-phosphate + ADP + PROTON; direction=LEFT-TO-RIGHT

## Pathways

- `ecocyc.GLUCOSE1PMETAB-PWY` glucose and glucose-1-phosphate degradation (EcoCyc)
- `ecocyc.GLYCOCAT-PWY` glycogen degradation I (EcoCyc)
- `ecocyc.PWY0-1182` trehalose degradation II (cytosolic) (EcoCyc)
- `ecocyc.TREDEGLOW-PWY` trehalose degradation I (low osmolarity) (EcoCyc)

## Outgoing Edges (0)

_None._

## Incoming Edges (8)

- `catalyzes` <-- [[protein.P0A6V8|protein.P0A6V8]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00008|molecule.C00008]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00092|molecule.C00092]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00002|molecule.C00002]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C00031|molecule.C00031]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `represses` <-- [[molecule.C00074|molecule.C00074]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.C00329|molecule.C00329]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity

## External IDs

- `EcoCyc:GLUCOKIN-RXN`

## Notes

Glucopyranose + ATP -> D-glucopyranose-6-phosphate + ADP + PROTON; direction=LEFT-TO-RIGHT
