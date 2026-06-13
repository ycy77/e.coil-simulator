---
entity_id: "reaction.ecocyc.TRANS-RXN-357"
entity_type: "reaction"
name: "enterobactin export"
source_database: "EcoCyc"
source_id: "TRANS-RXN-357"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: "CCO-EXTRACELLULAR-CCO-CYTOSOL"
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# enterobactin export

`reaction.ecocyc.TRANS-RXN-357`

## Static

- Type: `reaction`
- Source: `EcoCyc:TRANS-RXN-357`
- Default state: `active`
- Allowed states: `active|blocked`
- Location: CCO-EXTRACELLULAR-CCO-CYTOSOL

## Enriched Summary

ENTEROBACTIN + PROTON -> ENTEROBACTIN + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT EcoCyc reaction equation: ENTEROBACTIN + PROTON -> ENTEROBACTIN + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT.

## Biological Role

Catalyzed by multidrug efflux pump AcrAB-TolC (complex.ecocyc.TRANS-CPLX-201). Substrates: H+ (molecule.C00080), Enterochelin (molecule.C05821). Products: H+ (molecule.C00080), Enterochelin (molecule.C05821).

## Annotation

ENTEROBACTIN + PROTON -> ENTEROBACTIN + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT

## Outgoing Edges (0)

_None._

## Incoming Edges (5)

- `catalyzes` <-- [[complex.ecocyc.TRANS-CPLX-201|complex.ecocyc.TRANS-CPLX-201]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C05821|molecule.C05821]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C05821|molecule.C05821]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:TRANS-RXN-357`

## Notes

ENTEROBACTIN + PROTON -> ENTEROBACTIN + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT
