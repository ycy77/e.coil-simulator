---
entity_id: "reaction.ecocyc.RXN-20916"
entity_type: "reaction"
name: "RXN-20916"
source_database: "EcoCyc"
source_id: "RXN-20916"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: "CCO-PERI-BAC"
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN-20916

`reaction.ecocyc.RXN-20916`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN-20916`
- Default state: `active`
- Allowed states: `active|blocked`
- Location: CCO-PERI-BAC

## Enriched Summary

The acyltransferase reaction mediated by PagP occurs within the outer membrane; it is incorrectly represented here as 'periplasmic' due to software limitations. EcoCyc reaction equation: 1-Palmitoyl-2-Acyl-Glycerol-P + CPD-21359 -> a-hepta-acylated-core-oligosaccharide-li + 2-Acyl-sn-glycerol-3-phosphates; direction=PHYSIOL-LEFT-TO-RIGHT. The acyltransferase reaction mediated by PagP occurs within the outer membrane; it is incorrectly represented here as 'periplasmic' due to software limitations.

## Biological Role

Catalyzed by pagP (protein.P37001). Substrates: a 1-palmitoyl-2-acyl-sn-glycerol 3-phosphate (molecule.ecocyc.1-Palmitoyl-2-Acyl-Glycerol-P), lipid A-core oligosaccharide (E. coli K-12 core type) (molecule.ecocyc.CPD-21359). Products: 2-Acyl-sn-glycerol 3-phosphate (molecule.C03974), a hepta-acylated core oligosaccharide lipid A (E. coli K-12 type) (molecule.ecocyc.a-hepta-acylated-core-oligosaccharide-li).

## Annotation

The acyltransferase reaction mediated by PagP occurs within the outer membrane; it is incorrectly represented here as 'periplasmic' due to software limitations.

## Outgoing Edges (0)

_None._

## Incoming Edges (5)

- `catalyzes` <-- [[protein.P37001|protein.P37001]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C03974|molecule.C03974]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.a-hepta-acylated-core-oligosaccharide-li|molecule.ecocyc.a-hepta-acylated-core-oligosaccharide-li]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.ecocyc.1-Palmitoyl-2-Acyl-Glycerol-P|molecule.ecocyc.1-Palmitoyl-2-Acyl-Glycerol-P]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.ecocyc.CPD-21359|molecule.ecocyc.CPD-21359]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN-20916`

## Notes

1-Palmitoyl-2-Acyl-Glycerol-P + CPD-21359 -> a-hepta-acylated-core-oligosaccharide-li + 2-Acyl-sn-glycerol-3-phosphates; direction=PHYSIOL-LEFT-TO-RIGHT
