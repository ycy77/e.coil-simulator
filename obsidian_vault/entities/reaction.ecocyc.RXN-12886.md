---
entity_id: "reaction.ecocyc.RXN-12886"
entity_type: "reaction"
name: "RXN-12886"
source_database: "EcoCyc"
source_id: "RXN-12886"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN-12886

`reaction.ecocyc.RXN-12886`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN-12886`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

THYMINE + OXYGEN-MOLECULE + FMNH2 + NADH -> CPD-22331 + WATER + FMN + NAD + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT EcoCyc reaction equation: THYMINE + OXYGEN-MOLECULE + FMNH2 + NADH -> CPD-22331 + WATER + FMN + NAD + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT.

## Biological Role

Catalyzed by rutA (protein.P75898). Substrates: NADH (molecule.C00004), Oxygen (molecule.C00007), Thymine (molecule.C00178), Reduced FMN (molecule.C01847). Products: H2O (molecule.C00001), NAD+ (molecule.C00003), FMN (molecule.C00061), H+ (molecule.C00080), (Z)-2-methylureidoacrylate (molecule.ecocyc.CPD-22331).

## Annotation

THYMINE + OXYGEN-MOLECULE + FMNH2 + NADH -> CPD-22331 + WATER + FMN + NAD + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT

## Outgoing Edges (0)

_None._

## Incoming Edges (10)

- `catalyzes` <-- [[protein.P75898|protein.P75898]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00001|molecule.C00001]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00003|molecule.C00003]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00061|molecule.C00061]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.CPD-22331|molecule.ecocyc.CPD-22331]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00004|molecule.C00004]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C00007|molecule.C00007]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C00178|molecule.C00178]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C01847|molecule.C01847]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN-12886`

## Notes

THYMINE + OXYGEN-MOLECULE + FMNH2 + NADH -> CPD-22331 + WATER + FMN + NAD + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT
