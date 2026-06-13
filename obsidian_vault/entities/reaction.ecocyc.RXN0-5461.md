---
entity_id: "reaction.ecocyc.RXN0-5461"
entity_type: "reaction"
name: "RXN0-5461"
source_database: "EcoCyc"
source_id: "RXN0-5461"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN0-5461

`reaction.ecocyc.RXN0-5461`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN0-5461`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

DIHYDROXYPENTANEDIONE + ATP -> PROTON + CPD-10551 + ADP; direction=LEFT-TO-RIGHT EcoCyc reaction equation: DIHYDROXYPENTANEDIONE + ATP -> PROTON + CPD-10551 + ADP; direction=LEFT-TO-RIGHT.

## Biological Role

Catalyzed by lsrK (protein.P77432). Substrates: ATP (molecule.C00002), (4S)-4,5-dihydroxypentane-2,3-dione (molecule.ecocyc.DIHYDROXYPENTANEDIONE). Products: ADP (molecule.C00008), H+ (molecule.C00080), (4S)-4-Hydroxy-5-phosphooxypentane-2,3-dione (molecule.C20959).

## Enriched Pathways

- `ecocyc.PWY0-1569` autoinducer AI-2 degradation (EcoCyc)

## Annotation

DIHYDROXYPENTANEDIONE + ATP -> PROTON + CPD-10551 + ADP; direction=LEFT-TO-RIGHT

## Pathways

- `ecocyc.PWY0-1569` autoinducer AI-2 degradation (EcoCyc)

## Outgoing Edges (0)

_None._

## Incoming Edges (7)

- `catalyzes` <-- [[protein.P77432|protein.P77432]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00008|molecule.C00008]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C20959|molecule.C20959]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00002|molecule.C00002]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.ecocyc.DIHYDROXYPENTANEDIONE|molecule.ecocyc.DIHYDROXYPENTANEDIONE]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `represses` <-- [[protein.P0AA04|protein.P0AA04]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity

## External IDs

- `EcoCyc:RXN0-5461`

## Notes

DIHYDROXYPENTANEDIONE + ATP -> PROTON + CPD-10551 + ADP; direction=LEFT-TO-RIGHT
