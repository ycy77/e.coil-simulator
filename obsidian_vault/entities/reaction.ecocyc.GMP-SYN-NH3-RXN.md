---
entity_id: "reaction.ecocyc.GMP-SYN-NH3-RXN"
entity_type: "reaction"
name: "GMP-SYN-NH3-RXN"
source_database: "EcoCyc"
source_id: "GMP-SYN-NH3-RXN"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# GMP-SYN-NH3-RXN

`reaction.ecocyc.GMP-SYN-NH3-RXN`

## Static

- Type: `reaction`
- Source: `EcoCyc:GMP-SYN-NH3-RXN`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

This reaction is involved in GMP biosynthesis. EcoCyc reaction equation: XANTHOSINE-5-PHOSPHATE + AMMONIA + ATP -> GMP + AMP + PPI + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT. This reaction is involved in GMP biosynthesis.

## Biological Role

Catalyzed by GMP synthetase (complex.ecocyc.GMP-SYN-CPLX). Substrates: ATP (molecule.C00002), Ammonia (molecule.C00014), Xanthosine 5'-phosphate (molecule.C00655). Products: Diphosphate (molecule.C00013), AMP (molecule.C00020), H+ (molecule.C00080), GMP (molecule.C00144).

## Annotation

This reaction is involved in GMP biosynthesis.

## Outgoing Edges (0)

_None._

## Incoming Edges (13)

- `catalyzes` <-- [[complex.ecocyc.GMP-SYN-CPLX|complex.ecocyc.GMP-SYN-CPLX]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00013|molecule.C00013]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00020|molecule.C00020]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00144|molecule.C00144]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00002|molecule.C00002]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C00014|molecule.C00014]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C00655|molecule.C00655]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `represses` <-- [[molecule.C00013|molecule.C00013]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.C00212|molecule.C00212]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.ecocyc.CPD0-1033|molecule.ecocyc.CPD0-1033]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.ecocyc.CPD0-1627|molecule.ecocyc.CPD0-1627]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.ecocyc.DECOYININE|molecule.ecocyc.DECOYININE]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity

## External IDs

- `EcoCyc:GMP-SYN-NH3-RXN`

## Notes

XANTHOSINE-5-PHOSPHATE + AMMONIA + ATP -> GMP + AMP + PPI + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT
