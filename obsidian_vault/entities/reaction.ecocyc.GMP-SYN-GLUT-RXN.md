---
entity_id: "reaction.ecocyc.GMP-SYN-GLUT-RXN"
entity_type: "reaction"
name: "GMP-SYN-GLUT-RXN"
source_database: "EcoCyc"
source_id: "GMP-SYN-GLUT-RXN"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# GMP-SYN-GLUT-RXN

`reaction.ecocyc.GMP-SYN-GLUT-RXN`

## Static

- Type: `reaction`
- Source: `EcoCyc:GMP-SYN-GLUT-RXN`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

This reaction is involved in GMP biosynthesis. EcoCyc reaction equation: WATER + GLN + XANTHOSINE-5-PHOSPHATE + ATP -> PROTON + GLT + GMP + PPI + AMP; direction=PHYSIOL-LEFT-TO-RIGHT. This reaction is involved in GMP biosynthesis.

## Biological Role

Catalyzed by GMP synthetase (complex.ecocyc.GMP-SYN-CPLX). Substrates: H2O (molecule.C00001), ATP (molecule.C00002), L-Glutamine (molecule.C00064), Xanthosine 5'-phosphate (molecule.C00655). Products: Diphosphate (molecule.C00013), AMP (molecule.C00020), L-Glutamate (molecule.C00025), H+ (molecule.C00080), GMP (molecule.C00144).

## Enriched Pathways

- `ecocyc.PWY-7221` guanosine ribonucleotides de novo biosynthesis (EcoCyc)

## Annotation

This reaction is involved in GMP biosynthesis.

## Pathways

- `ecocyc.PWY-7221` guanosine ribonucleotides de novo biosynthesis (EcoCyc)

## Outgoing Edges (0)

_None._

## Incoming Edges (19)

- `catalyzes` <-- [[complex.ecocyc.GMP-SYN-CPLX|complex.ecocyc.GMP-SYN-CPLX]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00013|molecule.C00013]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00020|molecule.C00020]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00025|molecule.C00025]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00144|molecule.C00144]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00001|molecule.C00001]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C00002|molecule.C00002]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C00064|molecule.C00064]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C00655|molecule.C00655]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `represses` <-- [[molecule.C00013|molecule.C00013]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.ecocyc.3-BROMOPYRUVATE|molecule.ecocyc.3-BROMOPYRUVATE]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.ecocyc.CPD-29|molecule.ecocyc.CPD-29]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.ecocyc.CPD0-1033|molecule.ecocyc.CPD0-1033]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.ecocyc.CPD0-1035|molecule.ecocyc.CPD0-1035]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.ecocyc.CPD0-1036|molecule.ecocyc.CPD0-1036]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.ecocyc.CPD0-1627|molecule.ecocyc.CPD0-1627]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.ecocyc.DITHIO-NITROBENZOATE|molecule.ecocyc.DITHIO-NITROBENZOATE]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.ecocyc.TRIS|molecule.ecocyc.TRIS]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity

## External IDs

- `EcoCyc:GMP-SYN-GLUT-RXN`

## Notes

WATER + GLN + XANTHOSINE-5-PHOSPHATE + ATP -> PROTON + GLT + GMP + PPI + AMP; direction=PHYSIOL-LEFT-TO-RIGHT
