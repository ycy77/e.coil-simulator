---
entity_id: "reaction.ecocyc.TRANS-RXN-1592"
entity_type: "reaction"
name: "TRANS-RXN-1592"
source_database: "EcoCyc"
source_id: "TRANS-RXN-1592"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: "CCO-EXTRACELLULAR-CCO-CYTOSOL"
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# TRANS-RXN-1592

`reaction.ecocyc.TRANS-RXN-1592`

## Static

- Type: `reaction`
- Source: `EcoCyc:TRANS-RXN-1592`
- Default state: `active`
- Allowed states: `active|blocked`
- Location: CCO-EXTRACELLULAR-CCO-CYTOSOL

## Enriched Summary

ADENOSYLCOBALAMIN + PROTON -> ADENOSYLCOBALAMIN + PROTON; direction=LEFT-TO-RIGHT EcoCyc reaction equation: ADENOSYLCOBALAMIN + PROTON -> ADENOSYLCOBALAMIN + PROTON; direction=LEFT-TO-RIGHT.

## Biological Role

Catalyzed by cobalamin outer membrane transport complex (complex.ecocyc.CPLX0-1924). Substrates: H+ (molecule.C00080), Cobamide coenzyme (molecule.C00194). Products: H+ (molecule.C00080), Cobamide coenzyme (molecule.C00194).

## Annotation

ADENOSYLCOBALAMIN + PROTON -> ADENOSYLCOBALAMIN + PROTON; direction=LEFT-TO-RIGHT

## Outgoing Edges (0)

_None._

## Incoming Edges (5)

- `catalyzes` <-- [[complex.ecocyc.CPLX0-1924|complex.ecocyc.CPLX0-1924]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00194|molecule.C00194]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C00194|molecule.C00194]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:TRANS-RXN-1592`

## Notes

ADENOSYLCOBALAMIN + PROTON -> ADENOSYLCOBALAMIN + PROTON; direction=LEFT-TO-RIGHT
