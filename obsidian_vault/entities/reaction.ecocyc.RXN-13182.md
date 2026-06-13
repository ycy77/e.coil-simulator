---
entity_id: "reaction.ecocyc.RXN-13182"
entity_type: "reaction"
name: "RXN-13182"
source_database: "EcoCyc"
source_id: "RXN-13182"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: "CCO-PERI-BAC"
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN-13182

`reaction.ecocyc.RXN-13182`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN-13182`
- Default state: `active`
- Allowed states: `active|blocked`
- Location: CCO-PERI-BAC

## Enriched Summary

N-ACETYL-9-O-ACETYLNEURAMINATE + WATER -> N-ACETYLNEURAMINATE + PROTON + ACET; direction=PHYSIOL-LEFT-TO-RIGHT EcoCyc reaction equation: N-ACETYL-9-O-ACETYLNEURAMINATE + WATER -> N-ACETYLNEURAMINATE + PROTON + ACET; direction=PHYSIOL-LEFT-TO-RIGHT.

## Biological Role

Catalyzed by nanS (protein.P39370). Substrates: H2O (molecule.C00001), N-acetyl-9-O-acetylneuraminate (molecule.ecocyc.N-ACETYL-9-O-ACETYLNEURAMINATE). Products: Acetate (molecule.C00033), H+ (molecule.C00080), N-Acetylneuraminate (molecule.C00270).

## Annotation

N-ACETYL-9-O-ACETYLNEURAMINATE + WATER -> N-ACETYLNEURAMINATE + PROTON + ACET; direction=PHYSIOL-LEFT-TO-RIGHT

## Outgoing Edges (0)

_None._

## Incoming Edges (6)

- `catalyzes` <-- [[protein.P39370|protein.P39370]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00033|molecule.C00033]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00270|molecule.C00270]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00001|molecule.C00001]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.ecocyc.N-ACETYL-9-O-ACETYLNEURAMINATE|molecule.ecocyc.N-ACETYL-9-O-ACETYLNEURAMINATE]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN-13182`

## Notes

N-ACETYL-9-O-ACETYLNEURAMINATE + WATER -> N-ACETYLNEURAMINATE + PROTON + ACET; direction=PHYSIOL-LEFT-TO-RIGHT
