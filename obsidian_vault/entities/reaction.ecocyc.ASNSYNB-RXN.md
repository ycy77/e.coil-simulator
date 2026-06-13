---
entity_id: "reaction.ecocyc.ASNSYNB-RXN"
entity_type: "reaction"
name: "ASNSYNB-RXN"
source_database: "EcoCyc"
source_id: "ASNSYNB-RXN"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# ASNSYNB-RXN

`reaction.ecocyc.ASNSYNB-RXN`

## Static

- Type: `reaction`
- Source: `EcoCyc:ASNSYNB-RXN`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

GLN + L-ASPARTATE + ATP + WATER -> PROTON + GLT + ASN + PPI + AMP; direction=PHYSIOL-LEFT-TO-RIGHT EcoCyc reaction equation: GLN + L-ASPARTATE + ATP + WATER -> PROTON + GLT + ASN + PPI + AMP; direction=PHYSIOL-LEFT-TO-RIGHT.

## Biological Role

Catalyzed by asparagine synthetase B (complex.ecocyc.ASNSYNB-CPLX). Substrates: H2O (molecule.C00001), ATP (molecule.C00002), L-Aspartate (molecule.C00049), L-Glutamine (molecule.C00064). Products: Diphosphate (molecule.C00013), AMP (molecule.C00020), L-Glutamate (molecule.C00025), H+ (molecule.C00080), L-Asparagine (molecule.C00152).

## Enriched Pathways

- `ecocyc.ASPARAGINE-BIOSYNTHESIS` L-asparagine biosynthesis I (EcoCyc)

## Annotation

GLN + L-ASPARTATE + ATP + WATER -> PROTON + GLT + ASN + PPI + AMP; direction=PHYSIOL-LEFT-TO-RIGHT

## Pathways

- `ecocyc.ASPARAGINE-BIOSYNTHESIS` L-asparagine biosynthesis I (EcoCyc)

## Outgoing Edges (0)

_None._

## Incoming Edges (14)

- `catalyzes` <-- [[complex.ecocyc.ASNSYNB-CPLX|complex.ecocyc.ASNSYNB-CPLX]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00013|molecule.C00013]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00020|molecule.C00020]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00025|molecule.C00025]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00152|molecule.C00152]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00001|molecule.C00001]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C00002|molecule.C00002]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C00049|molecule.C00049]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C00064|molecule.C00064]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `represses` <-- [[molecule.C00606|molecule.C00606]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.C03618|molecule.C03618]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.ecocyc.CPD-18649|molecule.ecocyc.CPD-18649]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.ecocyc.CPD0-1054|molecule.ecocyc.CPD0-1054]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity

## External IDs

- `EcoCyc:ASNSYNB-RXN`

## Notes

GLN + L-ASPARTATE + ATP + WATER -> PROTON + GLT + ASN + PPI + AMP; direction=PHYSIOL-LEFT-TO-RIGHT
