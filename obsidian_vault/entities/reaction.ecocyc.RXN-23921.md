---
entity_id: "reaction.ecocyc.RXN-23921"
entity_type: "reaction"
name: "RXN-23921"
source_database: "EcoCyc"
source_id: "RXN-23921"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN-23921

`reaction.ecocyc.RXN-23921`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN-23921`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

L-ORNITHINE + ATP -> CPD-26475 + AMP + PPI + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT EcoCyc reaction equation: L-ORNITHINE + ATP -> CPD-26475 + AMP + PPI + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT.

## Biological Role

Catalyzed by lysine—tRNA ligase (complex.ecocyc.LYSU-CPLX). Substrates: ATP (molecule.C00002), L-Ornithine (molecule.C00077). Products: Diphosphate (molecule.C00013), AMP (molecule.C00020), H+ (molecule.C00080), 3-aminopiperidine-2-one (molecule.ecocyc.CPD-26475).

## Annotation

L-ORNITHINE + ATP -> CPD-26475 + AMP + PPI + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT

## Outgoing Edges (0)

_None._

## Incoming Edges (7)

- `catalyzes` <-- [[complex.ecocyc.LYSU-CPLX|complex.ecocyc.LYSU-CPLX]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00013|molecule.C00013]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00020|molecule.C00020]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.CPD-26475|molecule.ecocyc.CPD-26475]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00002|molecule.C00002]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C00077|molecule.C00077]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN-23921`

## Notes

L-ORNITHINE + ATP -> CPD-26475 + AMP + PPI + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT
