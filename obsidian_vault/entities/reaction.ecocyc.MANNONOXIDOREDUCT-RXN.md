---
entity_id: "reaction.ecocyc.MANNONOXIDOREDUCT-RXN"
entity_type: "reaction"
name: "MANNONOXIDOREDUCT-RXN"
source_database: "EcoCyc"
source_id: "MANNONOXIDOREDUCT-RXN"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# MANNONOXIDOREDUCT-RXN

`reaction.ecocyc.MANNONOXIDOREDUCT-RXN`

## Static

- Type: `reaction`
- Source: `EcoCyc:MANNONOXIDOREDUCT-RXN`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

Part of the glucuronate pathway. EcoCyc reaction equation: NAD + D-MANNONATE -> FRUCTURONATE + PROTON + NADH; direction=REVERSIBLE. Part of the glucuronate pathway.

## Biological Role

Catalyzed by uxuB (protein.P39160). Substrates: NAD+ (molecule.C00003), D-Mannonate (molecule.C00514). Products: NADH (molecule.C00004), H+ (molecule.C00080), D-Fructuronate (molecule.C00905).

## Enriched Pathways

- `ecocyc.PWY-7242` D-fructuronate degradation (EcoCyc)

## Annotation

Part of the glucuronate pathway.

## Pathways

- `ecocyc.PWY-7242` D-fructuronate degradation (EcoCyc)

## Outgoing Edges (0)

_None._

## Incoming Edges (13)

- `activates` <-- [[molecule.C00038|molecule.C00038]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `activates` <-- [[molecule.C00305|molecule.C00305]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `activates` <-- [[molecule.ecocyc.CA_2|molecule.ecocyc.CA_2]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `activates` <-- [[molecule.ecocyc.MN_2|molecule.ecocyc.MN_2]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `catalyzes` <-- [[protein.P39160|protein.P39160]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00004|molecule.C00004]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00905|molecule.C00905]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00003|molecule.C00003]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C00514|molecule.C00514]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `represses` <-- [[molecule.C00002|molecule.C00002]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.C00003|molecule.C00003]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.ecocyc.CPD-29|molecule.ecocyc.CPD-29]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity

## External IDs

- `EcoCyc:MANNONOXIDOREDUCT-RXN`

## Notes

NAD + D-MANNONATE -> FRUCTURONATE + PROTON + NADH; direction=REVERSIBLE
