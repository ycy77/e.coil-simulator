---
entity_id: "reaction.ecocyc.ASNSYNA-RXN"
entity_type: "reaction"
name: "ASNSYNA-RXN"
source_database: "EcoCyc"
source_id: "ASNSYNA-RXN"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# ASNSYNA-RXN

`reaction.ecocyc.ASNSYNA-RXN`

## Static

- Type: `reaction`
- Source: `EcoCyc:ASNSYNA-RXN`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

This is one of two reactions in E. coli that synthesizes asparagine from aspartate. The other reaction uses glutamine as the preferred nitrogen donor. EcoCyc reaction equation: L-ASPARTATE + AMMONIUM + ATP -> PROTON + ASN + PPI + AMP; direction=PHYSIOL-LEFT-TO-RIGHT. This is one of two reactions in E. coli that synthesizes asparagine from aspartate. The other reaction uses glutamine as the preferred nitrogen donor.

## Biological Role

Catalyzed by asparagine synthetase A (complex.ecocyc.ASNSYNA-CPLX), asparagine synthetase B (complex.ecocyc.ASNSYNB-CPLX). Substrates: ATP (molecule.C00002), L-Aspartate (molecule.C00049), ammonium (molecule.ecocyc.AMMONIUM). Products: Diphosphate (molecule.C00013), AMP (molecule.C00020), H+ (molecule.C00080), L-Asparagine (molecule.C00152).

## Enriched Pathways

- `ecocyc.ASPARAGINESYN-PWY` L-asparagine biosynthesis II (EcoCyc)

## Annotation

This is one of two reactions in E. coli that synthesizes asparagine from aspartate. The other reaction uses glutamine as the preferred nitrogen donor.

## Pathways

- `ecocyc.ASPARAGINESYN-PWY` L-asparagine biosynthesis II (EcoCyc)

## Outgoing Edges (0)

_None._

## Incoming Edges (12)

- `catalyzes` <-- [[complex.ecocyc.ASNSYNA-CPLX|complex.ecocyc.ASNSYNA-CPLX]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` <-- [[complex.ecocyc.ASNSYNB-CPLX|complex.ecocyc.ASNSYNB-CPLX]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00013|molecule.C00013]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00020|molecule.C00020]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00152|molecule.C00152]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00002|molecule.C00002]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C00049|molecule.C00049]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.ecocyc.AMMONIUM|molecule.ecocyc.AMMONIUM]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `represses` <-- [[molecule.C00014|molecule.C00014]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.C00020|molecule.C00020]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.C00152|molecule.C00152]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity

## External IDs

- `EcoCyc:ASNSYNA-RXN`

## Notes

L-ASPARTATE + AMMONIUM + ATP -> PROTON + ASN + PPI + AMP; direction=PHYSIOL-LEFT-TO-RIGHT
