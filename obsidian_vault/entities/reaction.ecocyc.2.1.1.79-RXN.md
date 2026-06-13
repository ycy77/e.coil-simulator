---
entity_id: "reaction.ecocyc.2.1.1.79-RXN"
entity_type: "reaction"
name: "2.1.1.79-RXN"
source_database: "EcoCyc"
source_id: "2.1.1.79-RXN"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
  - "UNSATURATED-PHOSPHOLIPID METHYLTRANSFERASE"
  - "CYCLOPROPANE SYNTHETASE"
---

# 2.1.1.79-RXN

`reaction.ecocyc.2.1.1.79-RXN`

## Static

- Type: `reaction`
- Source: `EcoCyc:2.1.1.79-RXN`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

ADDS A METHYLENE GROUP ACROSS THE 9,10 POSITION OF A δ(9)- OLEFINIC ACYL CHAIN IN PHOSPHATIDYLETHANOLAMINE OR, MORE SLOWLY, PHOSPHATIDYLGLYCEROL OR PHOSPHATIDYLINOSITOL FORMING A CYCLOPROPANE DERIVATIVE (CF. EC 2.1.1.16). EcoCyc reaction equation: S-ADENOSYLMETHIONINE + Phospholipid-Cis-Olefinic-Fatty-Acids -> Phospholipid-Cis-Cyclopropane-Fatty-Acids + ADENOSYL-HOMO-CYS + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT. ADDS A METHYLENE GROUP ACROSS THE 9,10 POSITION OF A δ(9)- OLEFINIC ACYL CHAIN IN PHOSPHATIDYLETHANOLAMINE OR, MORE SLOWLY, PHOSPHATIDYLGLYCEROL OR PHOSPHATIDYLINOSITOL FORMING A CYCLOPROPANE DERIVATIVE (CF. EC 2.1.1.16).

## Biological Role

Catalyzed by cyclopropane fatty acyl phospholipid synthase (complex.ecocyc.CFA-CPLX). Substrates: S-Adenosyl-L-methionine (molecule.C00019), a [phospholipid] cis-olefinic fatty acid (molecule.ecocyc.Phospholipid-Cis-Olefinic-Fatty-Acids). Products: S-Adenosyl-L-homocysteine (molecule.C00021), H+ (molecule.C00080), a [phospholipid] fatty acid containing cis cyclopropane (molecule.ecocyc.Phospholipid-Cis-Cyclopropane-Fatty-Acids).

## Enriched Pathways

- `ecocyc.PWY0-541` cis-cyclopropane fatty acid (CFA) biosynthesis (EcoCyc)

## Annotation

ADDS A METHYLENE GROUP ACROSS THE 9,10 POSITION OF A δ(9)- OLEFINIC ACYL CHAIN IN PHOSPHATIDYLETHANOLAMINE OR, MORE SLOWLY, PHOSPHATIDYLGLYCEROL OR PHOSPHATIDYLINOSITOL FORMING A CYCLOPROPANE DERIVATIVE (CF. EC 2.1.1.16).

## Pathways

- `ecocyc.PWY0-541` cis-cyclopropane fatty acid (CFA) biosynthesis (EcoCyc)

## Outgoing Edges (0)

_None._

## Incoming Edges (14)

- `catalyzes` <-- [[complex.ecocyc.CFA-CPLX|complex.ecocyc.CFA-CPLX]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00021|molecule.C00021]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.Phospholipid-Cis-Cyclopropane-Fatty-Acids|molecule.ecocyc.Phospholipid-Cis-Cyclopropane-Fatty-Acids]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00019|molecule.C00019]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.ecocyc.Phospholipid-Cis-Olefinic-Fatty-Acids|molecule.ecocyc.Phospholipid-Cis-Olefinic-Fatty-Acids]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `represses` <-- [[molecule.C00021|molecule.C00021]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.ecocyc.BORATE|molecule.ecocyc.BORATE]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.ecocyc.CPD0-1631|molecule.ecocyc.CPD0-1631]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.ecocyc.CPD0-2355|molecule.ecocyc.CPD0-2355]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.ecocyc.DITHIO-NITROBENZOATE|molecule.ecocyc.DITHIO-NITROBENZOATE]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.ecocyc.N-ETHYLMALEIMIDE|molecule.ecocyc.N-ETHYLMALEIMIDE]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.ecocyc.PHMB|molecule.ecocyc.PHMB]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.ecocyc.SINEFUNGIN|molecule.ecocyc.SINEFUNGIN]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity

## External IDs

- `EcoCyc:2.1.1.79-RXN`

## Notes

S-ADENOSYLMETHIONINE + Phospholipid-Cis-Olefinic-Fatty-Acids -> Phospholipid-Cis-Cyclopropane-Fatty-Acids + ADENOSYL-HOMO-CYS + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT
