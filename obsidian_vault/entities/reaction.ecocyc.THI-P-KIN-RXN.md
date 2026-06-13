---
entity_id: "reaction.ecocyc.THI-P-KIN-RXN"
entity_type: "reaction"
name: "THI-P-KIN-RXN"
source_database: "EcoCyc"
source_id: "THI-P-KIN-RXN"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# THI-P-KIN-RXN

`reaction.ecocyc.THI-P-KIN-RXN`

## Static

- Type: `reaction`
- Source: `EcoCyc:THI-P-KIN-RXN`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

The final reaction in the conversion of thiamin to thiamin pyrophosphate. Thiamin pyrophosphate is a cofactor for many enzyme catalyzed reactions. EcoCyc reaction equation: THIAMINE-P + ATP -> THIAMINE-PYROPHOSPHATE + ADP; direction=LEFT-TO-RIGHT. The final reaction in the conversion of thiamin to thiamin pyrophosphate. Thiamin pyrophosphate is a cofactor for many enzyme catalyzed reactions.

## Biological Role

Catalyzed by thiL (protein.P0AGG0). Substrates: ATP (molecule.C00002), Thiamin monophosphate (molecule.C01081). Products: ADP (molecule.C00008), Thiamin diphosphate (molecule.C00068).

## Enriched Pathways

- `ecocyc.PWY-6894` thiamine diphosphate biosynthesis I (E. coli) (EcoCyc)
- `ecocyc.PWY-6897` thiamine diphosphate salvage II (EcoCyc)
- `ecocyc.PWY-8457` thiamine diphosphate salvage V (EcoCyc)

## Annotation

The final reaction in the conversion of thiamin to thiamin pyrophosphate. Thiamin pyrophosphate is a cofactor for many enzyme catalyzed reactions.

## Pathways

- `ecocyc.PWY-6894` thiamine diphosphate biosynthesis I (E. coli) (EcoCyc)
- `ecocyc.PWY-6897` thiamine diphosphate salvage II (EcoCyc)
- `ecocyc.PWY-8457` thiamine diphosphate salvage V (EcoCyc)

## Outgoing Edges (0)

_None._

## Incoming Edges (15)

- `activates` <-- [[molecule.C00238|molecule.C00238]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `activates` <-- [[molecule.ecocyc.AMMONIUM|molecule.ecocyc.AMMONIUM]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `activates` <-- [[molecule.ecocyc.RB|molecule.ecocyc.RB_]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `catalyzes` <-- [[protein.P0AGG0|protein.P0AGG0]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00008|molecule.C00008]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00068|molecule.C00068]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00002|molecule.C00002]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C01081|molecule.C01081]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `represses` <-- [[molecule.C00008|molecule.C00008]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.C00013|molecule.C00013]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.C00020|molecule.C00020]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.ecocyc.CPD-29|molecule.ecocyc.CPD-29]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.ecocyc.CPD0-1426|molecule.ecocyc.CPD0-1426]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.ecocyc.EDTA|molecule.ecocyc.EDTA]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.ecocyc.N-ETHYLMALEIMIDE|molecule.ecocyc.N-ETHYLMALEIMIDE]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity

## External IDs

- `EcoCyc:THI-P-KIN-RXN`

## Notes

THIAMINE-P + ATP -> THIAMINE-PYROPHOSPHATE + ADP; direction=LEFT-TO-RIGHT
