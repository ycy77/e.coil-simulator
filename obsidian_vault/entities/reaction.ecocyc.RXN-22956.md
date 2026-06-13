---
entity_id: "reaction.ecocyc.RXN-22956"
entity_type: "reaction"
name: "RXN-22956"
source_database: "EcoCyc"
source_id: "RXN-22956"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN-22956

`reaction.ecocyc.RXN-22956`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN-22956`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

NI+2 + HypB + GTP + WATER -> Ni_HypB + GDP + Pi + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT EcoCyc reaction equation: NI+2 + HypB + GTP + WATER -> Ni_HypB + GDP + Pi + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT.

## Biological Role

Catalyzed by FKBP-type peptidyl-prolyl cis-trans isomerase SlyD (complex.ecocyc.CPLX0-7536). Substrates: H2O (molecule.C00001), GTP (molecule.C00044), Nickel(2+) (molecule.C19609). Products: GDP (molecule.C00035), H+ (molecule.C00080), phosphate (molecule.ecocyc.Pi).

## Enriched Pathways

- `ecocyc.PWY-8319` NiFe(CO)(CN)2 cofactor biosynthesis (EcoCyc)

## Annotation

NI+2 + HypB + GTP + WATER -> Ni_HypB + GDP + Pi + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT

## Pathways

- `ecocyc.PWY-8319` NiFe(CO)(CN)2 cofactor biosynthesis (EcoCyc)

## Outgoing Edges (0)

_None._

## Incoming Edges (7)

- `catalyzes` <-- [[complex.ecocyc.CPLX0-7536|complex.ecocyc.CPLX0-7536]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00035|molecule.C00035]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.Pi|molecule.ecocyc.Pi]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00001|molecule.C00001]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C00044|molecule.C00044]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C19609|molecule.C19609]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN-22956`

## Notes

NI+2 + HypB + GTP + WATER -> Ni_HypB + GDP + Pi + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT
