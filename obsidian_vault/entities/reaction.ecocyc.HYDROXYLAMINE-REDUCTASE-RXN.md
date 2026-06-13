---
entity_id: "reaction.ecocyc.HYDROXYLAMINE-REDUCTASE-RXN"
entity_type: "reaction"
name: "HYDROXYLAMINE-REDUCTASE-RXN"
source_database: "EcoCyc"
source_id: "HYDROXYLAMINE-REDUCTASE-RXN"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# HYDROXYLAMINE-REDUCTASE-RXN

`reaction.ecocyc.HYDROXYLAMINE-REDUCTASE-RXN`

## Static

- Type: `reaction`
- Source: `EcoCyc:HYDROXYLAMINE-REDUCTASE-RXN`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

AMMONIUM + WATER + Acceptor -> PROTON + Donor-H2 + HYDROXYLAMINE; direction=RIGHT-TO-LEFT EcoCyc reaction equation: AMMONIUM + WATER + Acceptor -> PROTON + Donor-H2 + HYDROXYLAMINE; direction=RIGHT-TO-LEFT.

## Biological Role

Catalyzed by hcp (protein.P75825). Substrates: H2O (molecule.C00001), ammonium (molecule.ecocyc.AMMONIUM). Products: H+ (molecule.C00080), Hydroxylamine (molecule.C00192).

## Annotation

AMMONIUM + WATER + Acceptor -> PROTON + Donor-H2 + HYDROXYLAMINE; direction=RIGHT-TO-LEFT

## Outgoing Edges (0)

_None._

## Incoming Edges (7)

- `activates` <-- [[molecule.C01326|molecule.C01326]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `catalyzes` <-- [[protein.P75825|protein.P75825]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00192|molecule.C00192]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00001|molecule.C00001]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.ecocyc.AMMONIUM|molecule.ecocyc.AMMONIUM]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `represses` <-- [[molecule.C00007|molecule.C00007]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity

## External IDs

- `EcoCyc:HYDROXYLAMINE-REDUCTASE-RXN`

## Notes

AMMONIUM + WATER + Acceptor -> PROTON + Donor-H2 + HYDROXYLAMINE; direction=RIGHT-TO-LEFT
