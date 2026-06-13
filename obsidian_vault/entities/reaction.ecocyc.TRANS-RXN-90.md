---
entity_id: "reaction.ecocyc.TRANS-RXN-90"
entity_type: "reaction"
name: "Ag+ export"
source_database: "EcoCyc"
source_id: "TRANS-RXN-90"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: "CCO-EXTRACELLULAR-CCO-CYTOSOL"
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# Ag+ export

`reaction.ecocyc.TRANS-RXN-90`

## Static

- Type: `reaction`
- Source: `EcoCyc:TRANS-RXN-90`
- Default state: `active`
- Allowed states: `active|blocked`
- Location: CCO-EXTRACELLULAR-CCO-CYTOSOL

## Enriched Summary

PROTON + AG+ -> PROTON + AG+; direction=PHYSIOL-LEFT-TO-RIGHT EcoCyc reaction equation: PROTON + AG+ -> PROTON + AG+; direction=PHYSIOL-LEFT-TO-RIGHT.

## Biological Role

Catalyzed by copper/silver export system (complex.ecocyc.CPLX0-1721). Substrates: H+ (molecule.C00080), Ag+ (molecule.ecocyc.AG_). Products: H+ (molecule.C00080), Ag+ (molecule.ecocyc.AG_).

## Annotation

PROTON + AG+ -> PROTON + AG+; direction=PHYSIOL-LEFT-TO-RIGHT

## Outgoing Edges (0)

_None._

## Incoming Edges (5)

- `catalyzes` <-- [[complex.ecocyc.CPLX0-1721|complex.ecocyc.CPLX0-1721]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.AG|molecule.ecocyc.AG_]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.ecocyc.AG|molecule.ecocyc.AG_]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:TRANS-RXN-90`

## Notes

PROTON + AG+ -> PROTON + AG+; direction=PHYSIOL-LEFT-TO-RIGHT
