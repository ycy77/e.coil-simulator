---
entity_id: "reaction.ecocyc.RIBOSYLHOMOCYSTEINASE-RXN"
entity_type: "reaction"
name: "RIBOSYLHOMOCYSTEINASE-RXN"
source_database: "EcoCyc"
source_id: "RIBOSYLHOMOCYSTEINASE-RXN"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RIBOSYLHOMOCYSTEINASE-RXN

`reaction.ecocyc.RIBOSYLHOMOCYSTEINASE-RXN`

## Static

- Type: `reaction`
- Source: `EcoCyc:RIBOSYLHOMOCYSTEINASE-RXN`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

CPD-564 -> HOMO-CYS + DIHYDROXYPENTANEDIONE; direction=LEFT-TO-RIGHT EcoCyc reaction equation: CPD-564 -> HOMO-CYS + DIHYDROXYPENTANEDIONE; direction=LEFT-TO-RIGHT.

## Biological Role

Catalyzed by luxS (protein.P45578). Substrates: S-Ribosyl-L-homocysteine (molecule.C03539). Products: L-Homocysteine (molecule.C00155), (4S)-4,5-dihydroxypentane-2,3-dione (molecule.ecocyc.DIHYDROXYPENTANEDIONE).

## Enriched Pathways

- `ecocyc.PWY-6151` S-adenosyl-L-methionine salvage I (EcoCyc)
- `ecocyc.PWY-6153` autoinducer AI-2 biosynthesis I (EcoCyc)

## Annotation

CPD-564 -> HOMO-CYS + DIHYDROXYPENTANEDIONE; direction=LEFT-TO-RIGHT

## Pathways

- `ecocyc.PWY-6151` S-adenosyl-L-methionine salvage I (EcoCyc)
- `ecocyc.PWY-6153` autoinducer AI-2 biosynthesis I (EcoCyc)

## Outgoing Edges (0)

_None._

## Incoming Edges (4)

- `catalyzes` <-- [[protein.P45578|protein.P45578]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00155|molecule.C00155]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.DIHYDROXYPENTANEDIONE|molecule.ecocyc.DIHYDROXYPENTANEDIONE]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C03539|molecule.C03539]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RIBOSYLHOMOCYSTEINASE-RXN`

## Notes

CPD-564 -> HOMO-CYS + DIHYDROXYPENTANEDIONE; direction=LEFT-TO-RIGHT
