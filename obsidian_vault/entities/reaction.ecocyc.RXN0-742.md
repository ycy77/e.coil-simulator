---
entity_id: "reaction.ecocyc.RXN0-742"
entity_type: "reaction"
name: "RXN0-742"
source_database: "EcoCyc"
source_id: "RXN0-742"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN0-742

`reaction.ecocyc.RXN0-742`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN0-742`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

5-PHOSPHORIBOSYL-5-AMINOIMIDAZOLE + ATP + HCO3 -> PROTON + CPD0-181 + ADP + Pi; direction=PHYSIOL-LEFT-TO-RIGHT EcoCyc reaction equation: 5-PHOSPHORIBOSYL-5-AMINOIMIDAZOLE + ATP + HCO3 -> PROTON + CPD0-181 + ADP + Pi; direction=PHYSIOL-LEFT-TO-RIGHT.

## Biological Role

Catalyzed by 5-(carboxyamino)imidazole ribonucleotide synthase (complex.ecocyc.PURK-CPLX). Substrates: ATP (molecule.C00002), HCO3- (molecule.C00288), Aminoimidazole ribotide (molecule.C03373). Products: ADP (molecule.C00008), H+ (molecule.C00080), 5-Carboxyamino-1-(5-phospho-D-ribosyl)imidazole (molecule.C15667), phosphate (molecule.ecocyc.Pi).

## Enriched Pathways

- `ecocyc.PWY-6123` inosine-5'-phosphate biosynthesis I (EcoCyc)

## Annotation

5-PHOSPHORIBOSYL-5-AMINOIMIDAZOLE + ATP + HCO3 -> PROTON + CPD0-181 + ADP + Pi; direction=PHYSIOL-LEFT-TO-RIGHT

## Pathways

- `ecocyc.PWY-6123` inosine-5'-phosphate biosynthesis I (EcoCyc)

## Outgoing Edges (0)

_None._

## Incoming Edges (8)

- `catalyzes` <-- [[complex.ecocyc.PURK-CPLX|complex.ecocyc.PURK-CPLX]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00008|molecule.C00008]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C15667|molecule.C15667]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.Pi|molecule.ecocyc.Pi]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00002|molecule.C00002]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C00288|molecule.C00288]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C03373|molecule.C03373]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN0-742`

## Notes

5-PHOSPHORIBOSYL-5-AMINOIMIDAZOLE + ATP + HCO3 -> PROTON + CPD0-181 + ADP + Pi; direction=PHYSIOL-LEFT-TO-RIGHT
