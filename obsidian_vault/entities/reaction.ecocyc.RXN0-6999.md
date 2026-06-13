---
entity_id: "reaction.ecocyc.RXN0-6999"
entity_type: "reaction"
name: "RXN0-6999"
source_database: "EcoCyc"
source_id: "RXN0-6999"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN0-6999

`reaction.ecocyc.RXN0-6999`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN0-6999`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

EF-P-L-lysine + CPD0-1032 + ATP -> EF-P-lysyl-lysine + AMP + PPI + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT EcoCyc reaction equation: EF-P-L-lysine + CPD0-1032 + ATP -> EF-P-lysyl-lysine + AMP + PPI + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT.

## Biological Role

Catalyzed by EF-P-lysine lysyltransferase (complex.ecocyc.CPLX0-7889). Substrates: ATP (molecule.C00002), (R)-β-lysine (molecule.ecocyc.CPD0-1032), a [protein chain elongation factor P]-L-lysine34 (molecule.ecocyc.EF-P-L-lysine). Products: Diphosphate (molecule.C00013), AMP (molecule.C00020), H+ (molecule.C00080), [a protein chain elongation factor EF-P]-N-(β-L-lysyl)-L-lysine34 (molecule.ecocyc.EF-P-lysyl-lysine).

## Annotation

EF-P-L-lysine + CPD0-1032 + ATP -> EF-P-lysyl-lysine + AMP + PPI + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT

## Outgoing Edges (0)

_None._

## Incoming Edges (9)

- `activates` <-- [[molecule.C00305|molecule.C00305]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `catalyzes` <-- [[complex.ecocyc.CPLX0-7889|complex.ecocyc.CPLX0-7889]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00013|molecule.C00013]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00020|molecule.C00020]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.EF-P-lysyl-lysine|molecule.ecocyc.EF-P-lysyl-lysine]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00002|molecule.C00002]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.ecocyc.CPD0-1032|molecule.ecocyc.CPD0-1032]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.ecocyc.EF-P-L-lysine|molecule.ecocyc.EF-P-L-lysine]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN0-6999`

## Notes

EF-P-L-lysine + CPD0-1032 + ATP -> EF-P-lysyl-lysine + AMP + PPI + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT
