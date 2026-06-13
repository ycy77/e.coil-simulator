---
entity_id: "reaction.ecocyc.RXN-20913"
entity_type: "reaction"
name: "RXN-20913"
source_database: "EcoCyc"
source_id: "RXN-20913"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: "CCO-PERI-BAC"
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN-20913

`reaction.ecocyc.RXN-20913`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN-20913`
- Default state: `active`
- Allowed states: `active|blocked`
- Location: CCO-PERI-BAC

## Enriched Summary

a-1-palmitoyl-2-acyl-phosphatidylserine + CPD-21359 -> a-hepta-acylated-core-oligosaccharide-li + 1-Lysophosphatidylserines; direction=PHYSIOL-LEFT-TO-RIGHT EcoCyc reaction equation: a-1-palmitoyl-2-acyl-phosphatidylserine + CPD-21359 -> a-hepta-acylated-core-oligosaccharide-li + 1-Lysophosphatidylserines; direction=PHYSIOL-LEFT-TO-RIGHT.

## Biological Role

Catalyzed by pagP (protein.P37001). Substrates: lipid A-core oligosaccharide (E. coli K-12 core type) (molecule.ecocyc.CPD-21359), a 1-palmitoyl-2-acyl-phosphatidylserine (molecule.ecocyc.a-1-palmitoyl-2-acyl-phosphatidylserine). Products: a 1-lysophosphatidylserine (molecule.ecocyc.1-Lysophosphatidylserines), a hepta-acylated core oligosaccharide lipid A (E. coli K-12 type) (molecule.ecocyc.a-hepta-acylated-core-oligosaccharide-li).

## Annotation

a-1-palmitoyl-2-acyl-phosphatidylserine + CPD-21359 -> a-hepta-acylated-core-oligosaccharide-li + 1-Lysophosphatidylserines; direction=PHYSIOL-LEFT-TO-RIGHT

## Outgoing Edges (0)

_None._

## Incoming Edges (5)

- `catalyzes` <-- [[protein.P37001|protein.P37001]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.ecocyc.1-Lysophosphatidylserines|molecule.ecocyc.1-Lysophosphatidylserines]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.a-hepta-acylated-core-oligosaccharide-li|molecule.ecocyc.a-hepta-acylated-core-oligosaccharide-li]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.ecocyc.CPD-21359|molecule.ecocyc.CPD-21359]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.ecocyc.a-1-palmitoyl-2-acyl-phosphatidylserine|molecule.ecocyc.a-1-palmitoyl-2-acyl-phosphatidylserine]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN-20913`

## Notes

a-1-palmitoyl-2-acyl-phosphatidylserine + CPD-21359 -> a-hepta-acylated-core-oligosaccharide-li + 1-Lysophosphatidylserines; direction=PHYSIOL-LEFT-TO-RIGHT
