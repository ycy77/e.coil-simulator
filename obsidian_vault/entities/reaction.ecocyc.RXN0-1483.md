---
entity_id: "reaction.ecocyc.RXN0-1483"
entity_type: "reaction"
name: "RXN0-1483"
source_database: "EcoCyc"
source_id: "RXN0-1483"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: "CCO-PERI-BAC|CCO-CYTOSOL"
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN0-1483

`reaction.ecocyc.RXN0-1483`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN0-1483`
- Default state: `active`
- Allowed states: `active|blocked`
- Location: CCO-PERI-BAC|CCO-CYTOSOL

## Enriched Summary

FE+2 + PROTON + OXYGEN-MOLECULE -> FE+3 + WATER; direction=PHYSIOL-LEFT-TO-RIGHT EcoCyc reaction equation: FE+2 + PROTON + OXYGEN-MOLECULE -> FE+3 + WATER; direction=PHYSIOL-LEFT-TO-RIGHT.

## Biological Role

Catalyzed by bacterioferritin (complex.ecocyc.CPLX0-1421), cueO (protein.P36649). Substrates: Oxygen (molecule.C00007), H+ (molecule.C00080), Fe2+ (molecule.C14818). Products: H2O (molecule.C00001), Fe3+ (molecule.C14819).

## Annotation

FE+2 + PROTON + OXYGEN-MOLECULE -> FE+3 + WATER; direction=PHYSIOL-LEFT-TO-RIGHT

## Outgoing Edges (0)

_None._

## Incoming Edges (9)

- `activates` <-- [[molecule.ecocyc.CU_2|molecule.ecocyc.CU_2]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `catalyzes` <-- [[complex.ecocyc.CPLX0-1421|complex.ecocyc.CPLX0-1421]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` <-- [[protein.P36649|protein.P36649]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00001|molecule.C00001]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C14819|molecule.C14819]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00007|molecule.C00007]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C14818|molecule.C14818]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `represses` <-- [[molecule.C00038|molecule.C00038]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity

## External IDs

- `EcoCyc:RXN0-1483`

## Notes

FE+2 + PROTON + OXYGEN-MOLECULE -> FE+3 + WATER; direction=PHYSIOL-LEFT-TO-RIGHT
