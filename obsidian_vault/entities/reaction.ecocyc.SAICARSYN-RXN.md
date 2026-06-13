---
entity_id: "reaction.ecocyc.SAICARSYN-RXN"
entity_type: "reaction"
name: "SAICARSYN-RXN"
source_database: "EcoCyc"
source_id: "SAICARSYN-RXN"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# SAICARSYN-RXN

`reaction.ecocyc.SAICARSYN-RXN`

## Static

- Type: `reaction`
- Source: `EcoCyc:SAICARSYN-RXN`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

This is the seventh step in de novo purine biosynthesis EcoCyc reaction equation: ATP + PHOSPHORIBOSYL-CARBOXY-AMINOIMIDAZOLE + L-ASPARTATE -> PROTON + ADP + Pi + P-RIBOSYL-4-SUCCCARB-AMINOIMIDAZOLE; direction=PHYSIOL-LEFT-TO-RIGHT. This is the seventh step in de novo purine biosynthesis

## Biological Role

Catalyzed by phosphoribosylaminoimidazole-succinocarboxamide synthase (complex.ecocyc.SAICARSYN-CPLX). Substrates: ATP (molecule.C00002), L-Aspartate (molecule.C00049), 1-(5-Phospho-D-ribosyl)-5-amino-4-imidazolecarboxylate (molecule.C04751). Products: ADP (molecule.C00008), H+ (molecule.C00080), 1-(5'-Phosphoribosyl)-5-amino-4-(N-succinocarboxamide)-imidazole (molecule.C04823), phosphate (molecule.ecocyc.Pi).

## Enriched Pathways

- `ecocyc.PWY-6123` inosine-5'-phosphate biosynthesis I (EcoCyc)

## Annotation

This is the seventh step in de novo purine biosynthesis

## Pathways

- `ecocyc.PWY-6123` inosine-5'-phosphate biosynthesis I (EcoCyc)

## Outgoing Edges (0)

_None._

## Incoming Edges (10)

- `catalyzes` <-- [[complex.ecocyc.SAICARSYN-CPLX|complex.ecocyc.SAICARSYN-CPLX]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00008|molecule.C00008]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C04823|molecule.C04823]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.Pi|molecule.ecocyc.Pi]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00002|molecule.C00002]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C00049|molecule.C00049]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C04751|molecule.C04751]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `represses` <-- [[molecule.C00130|molecule.C00130]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.C01384|molecule.C01384]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity

## External IDs

- `EcoCyc:SAICARSYN-RXN`

## Notes

ATP + PHOSPHORIBOSYL-CARBOXY-AMINOIMIDAZOLE + L-ASPARTATE -> PROTON + ADP + Pi + P-RIBOSYL-4-SUCCCARB-AMINOIMIDAZOLE; direction=PHYSIOL-LEFT-TO-RIGHT
