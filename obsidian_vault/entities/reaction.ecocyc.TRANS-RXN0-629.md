---
entity_id: "reaction.ecocyc.TRANS-RXN0-629"
entity_type: "reaction"
name: "TRANS-RXN0-629"
source_database: "EcoCyc"
source_id: "TRANS-RXN0-629"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: "CCO-EXTRACELLULAR-CCO-CYTOSOL"
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# TRANS-RXN0-629

`reaction.ecocyc.TRANS-RXN0-629`

## Static

- Type: `reaction`
- Source: `EcoCyc:TRANS-RXN0-629`
- Default state: `active`
- Allowed states: `active|blocked`
- Location: CCO-EXTRACELLULAR-CCO-CYTOSOL

## Enriched Summary

PQQ + PROTON -> PQQ + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT EcoCyc reaction equation: PQQ + PROTON -> PQQ + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT.

## Biological Role

Catalyzed by pyrroloquinoline quinone outer membrane transport complex (complex.ecocyc.CPLX0-9372). Substrates: H+ (molecule.C00080), pyrroloquinoline quinone (molecule.ecocyc.PQQ). Products: H+ (molecule.C00080), pyrroloquinoline quinone (molecule.ecocyc.PQQ).

## Annotation

PQQ + PROTON -> PQQ + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT

## Outgoing Edges (0)

_None._

## Incoming Edges (5)

- `catalyzes` <-- [[complex.ecocyc.CPLX0-9372|complex.ecocyc.CPLX0-9372]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.PQQ|molecule.ecocyc.PQQ]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.ecocyc.PQQ|molecule.ecocyc.PQQ]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:TRANS-RXN0-629`

## Notes

PQQ + PROTON -> PQQ + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT
