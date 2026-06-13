---
entity_id: "reaction.ecocyc.RXN0-1684"
entity_type: "reaction"
name: "RXN0-1684"
source_database: "EcoCyc"
source_id: "RXN0-1684"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: "CCO-EXTRACELLULAR-CCO-CYTOSOL"
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN0-1684

`reaction.ecocyc.RXN0-1684`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN0-1684`
- Default state: `active`
- Allowed states: `active|blocked`
- Location: CCO-EXTRACELLULAR-CCO-CYTOSOL

## Enriched Summary

FERRIC-CITRATE-COMPLEX + PROTON -> FERRIC-CITRATE-COMPLEX + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT EcoCyc reaction equation: FERRIC-CITRATE-COMPLEX + PROTON -> FERRIC-CITRATE-COMPLEX + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT.

## Biological Role

Catalyzed by ferric citrate outer membrane transport complex (complex.ecocyc.CPLX0-1943). Substrates: H+ (molecule.C00080), Fe(III)dicitrate (molecule.C06229). Products: H+ (molecule.C00080), Fe(III)dicitrate (molecule.C06229).

## Annotation

FERRIC-CITRATE-COMPLEX + PROTON -> FERRIC-CITRATE-COMPLEX + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT

## Outgoing Edges (0)

_None._

## Incoming Edges (5)

- `catalyzes` <-- [[complex.ecocyc.CPLX0-1943|complex.ecocyc.CPLX0-1943]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C06229|molecule.C06229]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C06229|molecule.C06229]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN0-1684`

## Notes

FERRIC-CITRATE-COMPLEX + PROTON -> FERRIC-CITRATE-COMPLEX + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT
