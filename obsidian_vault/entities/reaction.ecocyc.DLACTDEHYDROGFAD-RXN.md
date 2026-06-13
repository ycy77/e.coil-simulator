---
entity_id: "reaction.ecocyc.DLACTDEHYDROGFAD-RXN"
entity_type: "reaction"
name: "DLACTDEHYDROGFAD-RXN"
source_database: "EcoCyc"
source_id: "DLACTDEHYDROGFAD-RXN"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: "CCO-PM-BAC-NEG"
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# DLACTDEHYDROGFAD-RXN

`reaction.ecocyc.DLACTDEHYDROGFAD-RXN`

## Static

- Type: `reaction`
- Source: `EcoCyc:DLACTDEHYDROGFAD-RXN`
- Default state: `active`
- Allowed states: `active|blocked`
- Location: CCO-PM-BAC-NEG

## Enriched Summary

This reaction is part of the respiratory chain of E. coli. EcoCyc reaction equation: Ubiquinones + D-LACTATE -> Ubiquinols + PYRUVATE; direction=LEFT-TO-RIGHT. This reaction is part of the respiratory chain of E. coli.

## Biological Role

Catalyzed by dld (protein.P06149). Substrates: (R)-Lactate (molecule.C00256), a ubiquinone (molecule.ecocyc.Ubiquinones). Products: Pyruvate (molecule.C00022), Ubiquinol (molecule.C00390).

## Enriched Pathways

- `ecocyc.PWY-5386` methylglyoxal degradation I (EcoCyc)
- `ecocyc.PWY0-1565` D-lactate to cytochrome bo oxidase electron transfer (EcoCyc)

## Annotation

This reaction is part of the respiratory chain of E. coli.

## Pathways

- `ecocyc.PWY-5386` methylglyoxal degradation I (EcoCyc)
- `ecocyc.PWY0-1565` D-lactate to cytochrome bo oxidase electron transfer (EcoCyc)

## Outgoing Edges (0)

_None._

## Incoming Edges (9)

- `activates` <-- [[molecule.C00865|molecule.C00865]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `catalyzes` <-- [[protein.P06149|protein.P06149]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00022|molecule.C00022]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00390|molecule.C00390]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00256|molecule.C00256]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.ecocyc.Ubiquinones|molecule.ecocyc.Ubiquinones]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `represses` <-- [[molecule.C00209|molecule.C00209]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.C01444|molecule.C01444]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.ecocyc.CPD0-1604|molecule.ecocyc.CPD0-1604]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity

## External IDs

- `EcoCyc:DLACTDEHYDROGFAD-RXN`

## Notes

Ubiquinones + D-LACTATE -> Ubiquinols + PYRUVATE; direction=LEFT-TO-RIGHT
