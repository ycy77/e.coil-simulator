---
entity_id: "reaction.ecocyc.RXN-19362"
entity_type: "reaction"
name: "RXN-19362"
source_database: "EcoCyc"
source_id: "RXN-19362"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: "CCO-PERI-BAC"
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN-19362

`reaction.ecocyc.RXN-19362`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN-19362`
- Default state: `active`
- Allowed states: `active|blocked`
- Location: CCO-PERI-BAC

## Enriched Summary

CPD-20966 + Lipopolysaccharides -> Glucosyl-Lipopolysaccharides + CPD-9646; direction=PHYSIOL-LEFT-TO-RIGHT EcoCyc reaction equation: CPD-20966 + Lipopolysaccharides -> Glucosyl-Lipopolysaccharides + CPD-9646; direction=PHYSIOL-LEFT-TO-RIGHT.

## Biological Role

Catalyzed by yfdI (protein.P76507). Substrates: Lipopolysaccharide (molecule.C00338), β-D-Glc-PP-Und (molecule.ecocyc.CPD-20966). Products: di-trans,poly-cis-Undecaprenyl phosphate (molecule.C17556), an α-D-glucosyl-lipopolysaccharide (molecule.ecocyc.Glucosyl-Lipopolysaccharides).

## Annotation

CPD-20966 + Lipopolysaccharides -> Glucosyl-Lipopolysaccharides + CPD-9646; direction=PHYSIOL-LEFT-TO-RIGHT

## Outgoing Edges (0)

_None._

## Incoming Edges (5)

- `catalyzes` <-- [[protein.P76507|protein.P76507]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C17556|molecule.C17556]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.Glucosyl-Lipopolysaccharides|molecule.ecocyc.Glucosyl-Lipopolysaccharides]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00338|molecule.C00338]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.ecocyc.CPD-20966|molecule.ecocyc.CPD-20966]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN-19362`

## Notes

CPD-20966 + Lipopolysaccharides -> Glucosyl-Lipopolysaccharides + CPD-9646; direction=PHYSIOL-LEFT-TO-RIGHT
