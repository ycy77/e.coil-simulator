---
entity_id: "reaction.ecocyc.COBALAMIN5PSYN-RXN"
entity_type: "reaction"
name: "COBALAMIN5PSYN-RXN"
source_database: "EcoCyc"
source_id: "COBALAMIN5PSYN-RXN"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# COBALAMIN5PSYN-RXN

`reaction.ecocyc.COBALAMIN5PSYN-RXN`

## Static

- Type: `reaction`
- Source: `EcoCyc:COBALAMIN5PSYN-RXN`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

This reaction synthesizes adenosylcobalamin 5'-phosphate. EcoCyc reaction equation: ADENOSYLCOBINAMIDE-GDP + ALPHA-RIBAZOLE-5-P -> ADENOSYLCOBALAMIN-5-P + GMP + PROTON; direction=LEFT-TO-RIGHT. This reaction synthesizes adenosylcobalamin 5'-phosphate.

## Biological Role

Catalyzed by cobS (protein.P36561). Substrates: N1-(5-Phospho-alpha-D-ribosyl)-5,6-dimethylbenzimidazole (molecule.C04778), Adenosine-GDP-cobinamide (molecule.C06510). Products: H+ (molecule.C00080), GMP (molecule.C00144), adenosylcobalamin 5'-phosphate (molecule.ecocyc.ADENOSYLCOBALAMIN-5-P).

## Enriched Pathways

- `ecocyc.COBALSYN-PWY` superpathway of adenosylcobalamin salvage from cobinamide I (EcoCyc)
- `ecocyc.PWY-5509` adenosylcobalamin biosynthesis from adenosylcobinamide-GDP I (EcoCyc)

## Annotation

This reaction synthesizes adenosylcobalamin 5'-phosphate.

## Pathways

- `ecocyc.COBALSYN-PWY` superpathway of adenosylcobalamin salvage from cobinamide I (EcoCyc)
- `ecocyc.PWY-5509` adenosylcobalamin biosynthesis from adenosylcobinamide-GDP I (EcoCyc)

## Outgoing Edges (0)

_None._

## Incoming Edges (6)

- `catalyzes` <-- [[protein.P36561|protein.P36561]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00144|molecule.C00144]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.ADENOSYLCOBALAMIN-5-P|molecule.ecocyc.ADENOSYLCOBALAMIN-5-P]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C04778|molecule.C04778]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C06510|molecule.C06510]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:COBALAMIN5PSYN-RXN`

## Notes

ADENOSYLCOBINAMIDE-GDP + ALPHA-RIBAZOLE-5-P -> ADENOSYLCOBALAMIN-5-P + GMP + PROTON; direction=LEFT-TO-RIGHT
