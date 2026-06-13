---
entity_id: "reaction.ecocyc.RXN-14255"
entity_type: "reaction"
name: "RXN-14255"
source_database: "EcoCyc"
source_id: "RXN-14255"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN-14255

`reaction.ecocyc.RXN-14255`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN-14255`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

CPD-650 + WATER -> CPD-335 + CO-A + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT EcoCyc reaction equation: CPD-650 + WATER -> CPD-335 + CO-A + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT.

## Biological Role

Catalyzed by acyl-CoA thioesterase II (complex.ecocyc.THIOESTERII-CPLX). Substrates: H2O (molecule.C00001), (R)-3-Hydroxybutanoyl-CoA (molecule.C03561). Products: CoA (molecule.C00010), H+ (molecule.C00080), (R)-3-Hydroxybutanoate (molecule.C01089).

## Annotation

CPD-650 + WATER -> CPD-335 + CO-A + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT

## Outgoing Edges (0)

_None._

## Incoming Edges (6)

- `catalyzes` <-- [[complex.ecocyc.THIOESTERII-CPLX|complex.ecocyc.THIOESTERII-CPLX]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00010|molecule.C00010]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C01089|molecule.C01089]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00001|molecule.C00001]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C03561|molecule.C03561]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN-14255`

## Notes

CPD-650 + WATER -> CPD-335 + CO-A + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT
