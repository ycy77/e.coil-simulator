---
entity_id: "reaction.ecocyc.PABASYN-RXN"
entity_type: "reaction"
name: "PABASYN-RXN"
source_database: "EcoCyc"
source_id: "PABASYN-RXN"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# PABASYN-RXN

`reaction.ecocyc.PABASYN-RXN`

## Static

- Type: `reaction`
- Source: `EcoCyc:PABASYN-RXN`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

This reaction is the first step in the biosynthesis of p-aminobenzoate (PABA) and is also involved in folate biosynthesis. EcoCyc reaction equation: GLN + CHORISMATE -> 4-AMINO-4-DEOXYCHORISMATE + GLT; direction=PHYSIOL-LEFT-TO-RIGHT. This reaction is the first step in the biosynthesis of p-aminobenzoate (PABA) and is also involved in folate biosynthesis.

## Biological Role

Catalyzed by 4-amino-4-deoxychorismate synthase (complex.ecocyc.PABASYN-CPLX). Substrates: L-Glutamine (molecule.C00064), Chorismate (molecule.C00251). Products: L-Glutamate (molecule.C00025), 4-Amino-4-deoxychorismate (molecule.C11355).

## Enriched Pathways

- `ecocyc.PWY-6543` 4-aminobenzoate biosynthesis I (EcoCyc)

## Annotation

This reaction is the first step in the biosynthesis of p-aminobenzoate (PABA) and is also involved in folate biosynthesis.

## Pathways

- `ecocyc.PWY-6543` 4-aminobenzoate biosynthesis I (EcoCyc)

## Outgoing Edges (0)

_None._

## Incoming Edges (7)

- `catalyzes` <-- [[complex.ecocyc.PABASYN-CPLX|complex.ecocyc.PABASYN-CPLX]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00025|molecule.C00025]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C11355|molecule.C11355]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00064|molecule.C00064]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C00251|molecule.C00251]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `represses` <-- [[molecule.ecocyc.CPD0-1627|molecule.ecocyc.CPD0-1627]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.ecocyc.CPD0-1681|molecule.ecocyc.CPD0-1681]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity

## External IDs

- `EcoCyc:PABASYN-RXN`

## Notes

GLN + CHORISMATE -> 4-AMINO-4-DEOXYCHORISMATE + GLT; direction=PHYSIOL-LEFT-TO-RIGHT
