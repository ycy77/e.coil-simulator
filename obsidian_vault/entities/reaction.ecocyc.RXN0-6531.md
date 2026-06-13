---
entity_id: "reaction.ecocyc.RXN0-6531"
entity_type: "reaction"
name: "RXN0-6531"
source_database: "EcoCyc"
source_id: "RXN0-6531"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN0-6531

`reaction.ecocyc.RXN0-6531`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN0-6531`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

Elongation-Factor-EF-P-L-lysine + CPD0-1032 + ATP -> EF-P-beta-lysyl-L-lysine + AMP + PPI + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT EcoCyc reaction equation: Elongation-Factor-EF-P-L-lysine + CPD0-1032 + ATP -> EF-P-beta-lysyl-L-lysine + AMP + PPI + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT.

## Biological Role

Substrates: ATP (molecule.C00002), (R)-β-lysine (molecule.ecocyc.CPD0-1032), a [elongation-Factor-P]-L-lysine (molecule.ecocyc.Elongation-Factor-EF-P-L-lysine). Products: Diphosphate (molecule.C00013), AMP (molecule.C00020), H+ (molecule.C00080), a [elongation-Factor-P]-N6-(β-lysyl)-L-lysine (molecule.ecocyc.EF-P-beta-lysyl-L-lysine).

## Annotation

Elongation-Factor-EF-P-L-lysine + CPD0-1032 + ATP -> EF-P-beta-lysyl-L-lysine + AMP + PPI + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT

## Outgoing Edges (0)

_None._

## Incoming Edges (7)

- `is_product_of` <-- [[molecule.C00013|molecule.C00013]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00020|molecule.C00020]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.EF-P-beta-lysyl-L-lysine|molecule.ecocyc.EF-P-beta-lysyl-L-lysine]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00002|molecule.C00002]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.ecocyc.CPD0-1032|molecule.ecocyc.CPD0-1032]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.ecocyc.Elongation-Factor-EF-P-L-lysine|molecule.ecocyc.Elongation-Factor-EF-P-L-lysine]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN0-6531`

## Notes

Elongation-Factor-EF-P-L-lysine + CPD0-1032 + ATP -> EF-P-beta-lysyl-L-lysine + AMP + PPI + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT
