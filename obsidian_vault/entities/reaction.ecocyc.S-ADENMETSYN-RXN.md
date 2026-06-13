---
entity_id: "reaction.ecocyc.S-ADENMETSYN-RXN"
entity_type: "reaction"
name: "S-ADENMETSYN-RXN"
source_database: "EcoCyc"
source_id: "S-ADENMETSYN-RXN"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# S-ADENMETSYN-RXN

`reaction.ecocyc.S-ADENMETSYN-RXN`

## Static

- Type: `reaction`
- Source: `EcoCyc:S-ADENMETSYN-RXN`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

This reaction catalyzes the only known route of biosynthesis of the intracellular alkylating agent adenosylmethionine. EcoCyc reaction equation: ATP + MET + WATER -> S-ADENOSYLMETHIONINE + Pi + PPI; direction=LEFT-TO-RIGHT. This reaction catalyzes the only known route of biosynthesis of the intracellular alkylating agent adenosylmethionine.

## Biological Role

Catalyzed by methionine adenosyltransferase (complex.ecocyc.S-ADENMETSYN-CPLX). Substrates: H2O (molecule.C00001), ATP (molecule.C00002), L-Methionine (molecule.C00073). Products: Diphosphate (molecule.C00013), S-Adenosyl-L-methionine (molecule.C00019), phosphate (molecule.ecocyc.Pi).

## Enriched Pathways

- `ecocyc.PWY-6151` S-adenosyl-L-methionine salvage I (EcoCyc)
- `ecocyc.SAM-PWY` S-adenosyl-L-methionine biosynthesis (EcoCyc)

## Annotation

This reaction catalyzes the only known route of biosynthesis of the intracellular alkylating agent adenosylmethionine.

## Pathways

- `ecocyc.PWY-6151` S-adenosyl-L-methionine salvage I (EcoCyc)
- `ecocyc.SAM-PWY` S-adenosyl-L-methionine biosynthesis (EcoCyc)

## Outgoing Edges (0)

_None._

## Incoming Edges (16)

- `catalyzes` <-- [[complex.ecocyc.S-ADENMETSYN-CPLX|complex.ecocyc.S-ADENMETSYN-CPLX]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00013|molecule.C00013]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00019|molecule.C00019]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.Pi|molecule.ecocyc.Pi]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00001|molecule.C00001]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C00002|molecule.C00002]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C00073|molecule.C00073]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `represses` <-- [[molecule.C00013|molecule.C00013]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.C00019|molecule.C00019]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.C00536|molecule.C00536]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.ecocyc.CPD0-1054|molecule.ecocyc.CPD0-1054]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.ecocyc.CPD0-1386|molecule.ecocyc.CPD0-1386]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.ecocyc.CPD0-1437|molecule.ecocyc.CPD0-1437]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.ecocyc.CPD0-1438|molecule.ecocyc.CPD0-1438]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.ecocyc.L-2-AMINOHEXANOATE|molecule.ecocyc.L-2-AMINOHEXANOATE]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.ecocyc.Pi|molecule.ecocyc.Pi]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity

## External IDs

- `EcoCyc:S-ADENMETSYN-RXN`

## Notes

ATP + MET + WATER -> S-ADENOSYLMETHIONINE + Pi + PPI; direction=LEFT-TO-RIGHT
