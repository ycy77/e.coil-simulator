---
entity_id: "reaction.ecocyc.RXN-14251"
entity_type: "reaction"
name: "RXN-14251"
source_database: "EcoCyc"
source_id: "RXN-14251"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN-14251

`reaction.ecocyc.RXN-14251`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN-14251`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

S-3-HYDROXYBUTANOYL-COA + WATER -> CPD-1843 + CO-A + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT EcoCyc reaction equation: S-3-HYDROXYBUTANOYL-COA + WATER -> CPD-1843 + CO-A + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT.

## Biological Role

Catalyzed by acyl-CoA thioesterase II (complex.ecocyc.THIOESTERII-CPLX). Substrates: H2O (molecule.C00001), (S)-3-Hydroxybutanoyl-CoA (molecule.C01144). Products: CoA (molecule.C00010), H+ (molecule.C00080), (S)-3-hydroxybutanoate (molecule.ecocyc.CPD-1843).

## Annotation

S-3-HYDROXYBUTANOYL-COA + WATER -> CPD-1843 + CO-A + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT

## Outgoing Edges (0)

_None._

## Incoming Edges (6)

- `catalyzes` <-- [[complex.ecocyc.THIOESTERII-CPLX|complex.ecocyc.THIOESTERII-CPLX]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00010|molecule.C00010]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.CPD-1843|molecule.ecocyc.CPD-1843]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00001|molecule.C00001]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C01144|molecule.C01144]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN-14251`

## Notes

S-3-HYDROXYBUTANOYL-COA + WATER -> CPD-1843 + CO-A + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT
