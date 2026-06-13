---
entity_id: "reaction.ecocyc.RXN-16393"
entity_type: "reaction"
name: "RXN-16393"
source_database: "EcoCyc"
source_id: "RXN-16393"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN-16393

`reaction.ecocyc.RXN-16393`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN-16393`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

DODECANOATE + CO-A + ATP -> LAUROYLCOA-CPD + PPI + AMP; direction=PHYSIOL-LEFT-TO-RIGHT EcoCyc reaction equation: DODECANOATE + CO-A + ATP -> LAUROYLCOA-CPD + PPI + AMP; direction=PHYSIOL-LEFT-TO-RIGHT.

## Biological Role

Substrates: ATP (molecule.C00002), CoA (molecule.C00010), Dodecanoic acid (molecule.C02679). Products: Diphosphate (molecule.C00013), AMP (molecule.C00020), Lauroyl-CoA (molecule.C01832).

## Enriched Pathways

- `ecocyc.PWY-5971` palmitate biosynthesis II (type II fatty acid synthase) (EcoCyc)

## Annotation

DODECANOATE + CO-A + ATP -> LAUROYLCOA-CPD + PPI + AMP; direction=PHYSIOL-LEFT-TO-RIGHT

## Pathways

- `ecocyc.PWY-5971` palmitate biosynthesis II (type II fatty acid synthase) (EcoCyc)

## Outgoing Edges (0)

_None._

## Incoming Edges (6)

- `is_product_of` <-- [[molecule.C00013|molecule.C00013]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00020|molecule.C00020]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C01832|molecule.C01832]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00002|molecule.C00002]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C00010|molecule.C00010]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C02679|molecule.C02679]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN-16393`

## Notes

DODECANOATE + CO-A + ATP -> LAUROYLCOA-CPD + PPI + AMP; direction=PHYSIOL-LEFT-TO-RIGHT
