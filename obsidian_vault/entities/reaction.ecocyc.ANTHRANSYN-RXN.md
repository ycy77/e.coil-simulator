---
entity_id: "reaction.ecocyc.ANTHRANSYN-RXN"
entity_type: "reaction"
name: "ANTHRANSYN-RXN"
source_database: "EcoCyc"
source_id: "ANTHRANSYN-RXN"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# ANTHRANSYN-RXN

`reaction.ecocyc.ANTHRANSYN-RXN`

## Static

- Type: `reaction`
- Source: `EcoCyc:ANTHRANSYN-RXN`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

CHORISMATE + GLN -> PROTON + ANTHRANILATE + PYRUVATE + GLT; direction=PHYSIOL-LEFT-TO-RIGHT EcoCyc reaction equation: CHORISMATE + GLN -> PROTON + ANTHRANILATE + PYRUVATE + GLT; direction=PHYSIOL-LEFT-TO-RIGHT.

## Biological Role

Catalyzed by anthranilate synthase (complex.ecocyc.ANTHRANSYN-CPLX). Substrates: L-Glutamine (molecule.C00064), Chorismate (molecule.C00251). Products: Pyruvate (molecule.C00022), L-Glutamate (molecule.C00025), H+ (molecule.C00080), Anthranilate (molecule.C00108).

## Enriched Pathways

- `ecocyc.TRPSYN-PWY` L-tryptophan biosynthesis (EcoCyc)

## Annotation

CHORISMATE + GLN -> PROTON + ANTHRANILATE + PYRUVATE + GLT; direction=PHYSIOL-LEFT-TO-RIGHT

## Pathways

- `ecocyc.TRPSYN-PWY` L-tryptophan biosynthesis (EcoCyc)

## Outgoing Edges (0)

_None._

## Incoming Edges (9)

- `catalyzes` <-- [[complex.ecocyc.ANTHRANSYN-CPLX|complex.ecocyc.ANTHRANSYN-CPLX]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00022|molecule.C00022]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00025|molecule.C00025]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00108|molecule.C00108]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00064|molecule.C00064]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C00251|molecule.C00251]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `represses` <-- [[molecule.C00078|molecule.C00078]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.ecocyc.CPD0-1544|molecule.ecocyc.CPD0-1544]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity

## External IDs

- `EcoCyc:ANTHRANSYN-RXN`

## Notes

CHORISMATE + GLN -> PROTON + ANTHRANILATE + PYRUVATE + GLT; direction=PHYSIOL-LEFT-TO-RIGHT
