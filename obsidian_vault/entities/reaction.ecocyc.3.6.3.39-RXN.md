---
entity_id: "reaction.ecocyc.3.6.3.39-RXN"
entity_type: "reaction"
name: "3.6.3.39-RXN"
source_database: "EcoCyc"
source_id: "3.6.3.39-RXN"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: "CCO-PM-BAC-NEG"
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# 3.6.3.39-RXN

`reaction.ecocyc.3.6.3.39-RXN`

## Static

- Type: `reaction`
- Source: `EcoCyc:3.6.3.39-RXN`
- Default state: `active`
- Allowed states: `active|blocked`
- Location: CCO-PM-BAC-NEG

## Enriched Summary

Lipopolysaccharides + WATER + ATP -> Lipopolysaccharides + Pi + ADP + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT EcoCyc reaction equation: Lipopolysaccharides + WATER + ATP -> Lipopolysaccharides + Pi + ADP + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT.

## Biological Role

Substrates: H2O (molecule.C00001), ATP (molecule.C00002), Lipopolysaccharide (molecule.C00338). Products: ADP (molecule.C00008), H+ (molecule.C00080), Lipopolysaccharide (molecule.C00338), phosphate (molecule.ecocyc.Pi).

## Annotation

Lipopolysaccharides + WATER + ATP -> Lipopolysaccharides + Pi + ADP + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT

## Outgoing Edges (0)

_None._

## Incoming Edges (7)

- `is_product_of` <-- [[molecule.C00008|molecule.C00008]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00338|molecule.C00338]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.Pi|molecule.ecocyc.Pi]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00001|molecule.C00001]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C00002|molecule.C00002]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C00338|molecule.C00338]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:3.6.3.39-RXN`

## Notes

Lipopolysaccharides + WATER + ATP -> Lipopolysaccharides + Pi + ADP + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT
