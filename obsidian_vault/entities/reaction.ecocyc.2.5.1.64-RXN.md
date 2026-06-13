---
entity_id: "reaction.ecocyc.2.5.1.64-RXN"
entity_type: "reaction"
name: "2.5.1.64-RXN"
source_database: "EcoCyc"
source_id: "2.5.1.64-RXN"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# 2.5.1.64-RXN

`reaction.ecocyc.2.5.1.64-RXN`

## Static

- Type: `reaction`
- Source: `EcoCyc:2.5.1.64-RXN`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

PROTON + ISOCHORISMATE + 2-KETOGLUTARATE -> CPD-9924 + CARBON-DIOXIDE; direction=LEFT-TO-RIGHT EcoCyc reaction equation: PROTON + ISOCHORISMATE + 2-KETOGLUTARATE -> CPD-9924 + CARBON-DIOXIDE; direction=LEFT-TO-RIGHT.

## Biological Role

Catalyzed by 2-succinyl-5-enolpyruvyl-6-hydroxy-3-cyclohexene-1-carboxylate synthase (complex.ecocyc.CPLX0-7525). Substrates: 2-Oxoglutarate (molecule.C00026), H+ (molecule.C00080), Isochorismate (molecule.C00885). Products: CO2 (molecule.C00011), 2-Succinyl-5-enolpyruvyl-6-hydroxy-3-cyclohexene-1-carboxylate (molecule.C16519).

## Enriched Pathways

- `ecocyc.PWY-5837` 1,4-dihydroxy-2-naphthoate biosynthesis (EcoCyc)

## Annotation

PROTON + ISOCHORISMATE + 2-KETOGLUTARATE -> CPD-9924 + CARBON-DIOXIDE; direction=LEFT-TO-RIGHT

## Pathways

- `ecocyc.PWY-5837` 1,4-dihydroxy-2-naphthoate biosynthesis (EcoCyc)

## Outgoing Edges (0)

_None._

## Incoming Edges (7)

- `catalyzes` <-- [[complex.ecocyc.CPLX0-7525|complex.ecocyc.CPLX0-7525]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00011|molecule.C00011]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C16519|molecule.C16519]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00026|molecule.C00026]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C00885|molecule.C00885]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `represses` <-- [[molecule.ecocyc.CPD0-1354|molecule.ecocyc.CPD0-1354]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity

## External IDs

- `EcoCyc:2.5.1.64-RXN`

## Notes

PROTON + ISOCHORISMATE + 2-KETOGLUTARATE -> CPD-9924 + CARBON-DIOXIDE; direction=LEFT-TO-RIGHT
