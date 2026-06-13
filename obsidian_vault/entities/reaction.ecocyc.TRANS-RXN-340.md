---
entity_id: "reaction.ecocyc.TRANS-RXN-340"
entity_type: "reaction"
name: "bicozamycin:H+ antiport"
source_database: "EcoCyc"
source_id: "TRANS-RXN-340"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: "CCO-PM-BAC-NEG"
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# bicozamycin:H+ antiport

`reaction.ecocyc.TRANS-RXN-340`

## Static

- Type: `reaction`
- Source: `EcoCyc:TRANS-RXN-340`
- Default state: `active`
- Allowed states: `active|blocked`
- Location: CCO-PM-BAC-NEG

## Enriched Summary

CPD-20921 + PROTON -> CPD-20921 + PROTON; direction=REVERSIBLE EcoCyc reaction equation: CPD-20921 + PROTON -> CPD-20921 + PROTON; direction=REVERSIBLE.

## Biological Role

Catalyzed by bcr (protein.P28246). Substrates: H+ (molecule.C00080), bicozamycin (molecule.ecocyc.CPD-20921). Products: H+ (molecule.C00080), bicozamycin (molecule.ecocyc.CPD-20921).

## Annotation

CPD-20921 + PROTON -> CPD-20921 + PROTON; direction=REVERSIBLE

## Outgoing Edges (0)

_None._

## Incoming Edges (5)

- `catalyzes` <-- [[protein.P28246|protein.P28246]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.CPD-20921|molecule.ecocyc.CPD-20921]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.ecocyc.CPD-20921|molecule.ecocyc.CPD-20921]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:TRANS-RXN-340`

## Notes

CPD-20921 + PROTON -> CPD-20921 + PROTON; direction=REVERSIBLE
