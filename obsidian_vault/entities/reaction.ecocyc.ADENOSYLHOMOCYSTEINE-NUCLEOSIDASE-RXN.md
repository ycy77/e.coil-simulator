---
entity_id: "reaction.ecocyc.ADENOSYLHOMOCYSTEINE-NUCLEOSIDASE-RXN"
entity_type: "reaction"
name: "ADENOSYLHOMOCYSTEINE-NUCLEOSIDASE-RXN"
source_database: "EcoCyc"
source_id: "ADENOSYLHOMOCYSTEINE-NUCLEOSIDASE-RXN"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# ADENOSYLHOMOCYSTEINE-NUCLEOSIDASE-RXN

`reaction.ecocyc.ADENOSYLHOMOCYSTEINE-NUCLEOSIDASE-RXN`

## Static

- Type: `reaction`
- Source: `EcoCyc:ADENOSYLHOMOCYSTEINE-NUCLEOSIDASE-RXN`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

ADENOSYL-HOMO-CYS + WATER -> CPD-564 + ADENINE; direction=LEFT-TO-RIGHT EcoCyc reaction equation: ADENOSYL-HOMO-CYS + WATER -> CPD-564 + ADENINE; direction=LEFT-TO-RIGHT.

## Biological Role

Catalyzed by 5'-methylthioadenosine/S-adenosylhomocysteine nucleosidase (complex.ecocyc.CPLX0-1541). Substrates: H2O (molecule.C00001), S-Adenosyl-L-homocysteine (molecule.C00021). Products: Adenine (molecule.C00147), S-Ribosyl-L-homocysteine (molecule.C03539).

## Enriched Pathways

- `ecocyc.PWY-6151` S-adenosyl-L-methionine salvage I (EcoCyc)
- `ecocyc.PWY-6153` autoinducer AI-2 biosynthesis I (EcoCyc)

## Annotation

ADENOSYL-HOMO-CYS + WATER -> CPD-564 + ADENINE; direction=LEFT-TO-RIGHT

## Pathways

- `ecocyc.PWY-6151` S-adenosyl-L-methionine salvage I (EcoCyc)
- `ecocyc.PWY-6153` autoinducer AI-2 biosynthesis I (EcoCyc)

## Outgoing Edges (0)

_None._

## Incoming Edges (14)

- `catalyzes` <-- [[complex.ecocyc.CPLX0-1541|complex.ecocyc.CPLX0-1541]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00147|molecule.C00147]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C03539|molecule.C03539]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00001|molecule.C00001]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C00021|molecule.C00021]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `represses` <-- [[molecule.ecocyc.5-CHLOROFORMYCIN|molecule.ecocyc.5-CHLOROFORMYCIN]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.ecocyc.5-ETHYLTHIOADENOSINE|molecule.ecocyc.5-ETHYLTHIOADENOSINE]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.ecocyc.5-METHYLTHIOFORMYCIN|molecule.ecocyc.5-METHYLTHIOFORMYCIN]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.ecocyc.5-METHYLTHIOTUBERCIDIN|molecule.ecocyc.5-METHYLTHIOTUBERCIDIN]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.ecocyc.5-N-PROPYLTHIOADENOSINE|molecule.ecocyc.5-N-PROPYLTHIOADENOSINE]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.ecocyc.CPD-26593|molecule.ecocyc.CPD-26593]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.ecocyc.FORMYCIN-A|molecule.ecocyc.FORMYCIN-A]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.ecocyc.S-FORMYCINYLHOMOCYSTEINE|molecule.ecocyc.S-FORMYCINYLHOMOCYSTEINE]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.ecocyc.S-TUBERCIDINYLHOMOCYSTEINE|molecule.ecocyc.S-TUBERCIDINYLHOMOCYSTEINE]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity

## External IDs

- `EcoCyc:ADENOSYLHOMOCYSTEINE-NUCLEOSIDASE-RXN`

## Notes

ADENOSYL-HOMO-CYS + WATER -> CPD-564 + ADENINE; direction=LEFT-TO-RIGHT
