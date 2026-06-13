---
entity_id: "reaction.ecocyc.RXN0-1682"
entity_type: "reaction"
name: "RXN0-1682"
source_database: "EcoCyc"
source_id: "RXN0-1682"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: "CCO-EXTRACELLULAR-CCO-CYTOSOL"
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN0-1682

`reaction.ecocyc.RXN0-1682`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN0-1682`
- Default state: `active`
- Allowed states: `active|blocked`
- Location: CCO-EXTRACELLULAR-CCO-CYTOSOL

## Enriched Summary

FERRIC-ENTEROBACTIN-COMPLEX + PROTON -> FERRIC-ENTEROBACTIN-COMPLEX + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT EcoCyc reaction equation: FERRIC-ENTEROBACTIN-COMPLEX + PROTON -> FERRIC-ENTEROBACTIN-COMPLEX + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT.

## Biological Role

Catalyzed by ferric enterobactin outer membrane transport complex (complex.ecocyc.CPLX0-1941). Substrates: H+ (molecule.C00080), Fe-enterobactin (molecule.C06230). Products: H+ (molecule.C00080), Fe-enterobactin (molecule.C06230).

## Annotation

FERRIC-ENTEROBACTIN-COMPLEX + PROTON -> FERRIC-ENTEROBACTIN-COMPLEX + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT

## Outgoing Edges (0)

_None._

## Incoming Edges (5)

- `catalyzes` <-- [[complex.ecocyc.CPLX0-1941|complex.ecocyc.CPLX0-1941]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C06230|molecule.C06230]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C06230|molecule.C06230]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN0-1682`

## Notes

FERRIC-ENTEROBACTIN-COMPLEX + PROTON -> FERRIC-ENTEROBACTIN-COMPLEX + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT
