---
entity_id: "reaction.ecocyc.GDP-GLUCOSIDASE-RXN"
entity_type: "reaction"
name: "GDP-GLUCOSIDASE-RXN"
source_database: "EcoCyc"
source_id: "GDP-GLUCOSIDASE-RXN"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# GDP-GLUCOSIDASE-RXN

`reaction.ecocyc.GDP-GLUCOSIDASE-RXN`

## Static

- Type: `reaction`
- Source: `EcoCyc:GDP-GLUCOSIDASE-RXN`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

GDP-D-GLUCOSE + WATER -> GDP + Glucopyranose + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT EcoCyc reaction equation: GDP-D-GLUCOSE + WATER -> GDP + Glucopyranose + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT.

## Biological Role

Catalyzed by GDP-mannose mannosyl hydrolase (complex.ecocyc.CPLX0-7712). Substrates: H2O (molecule.C00001), GDP-glucose (molecule.C00394). Products: D-Glucose (molecule.C00031), GDP (molecule.C00035), H+ (molecule.C00080).

## Annotation

GDP-D-GLUCOSE + WATER -> GDP + Glucopyranose + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT

## Outgoing Edges (0)

_None._

## Incoming Edges (6)

- `catalyzes` <-- [[complex.ecocyc.CPLX0-7712|complex.ecocyc.CPLX0-7712]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00031|molecule.C00031]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00035|molecule.C00035]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00001|molecule.C00001]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C00394|molecule.C00394]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:GDP-GLUCOSIDASE-RXN`

## Notes

GDP-D-GLUCOSE + WATER -> GDP + Glucopyranose + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT
