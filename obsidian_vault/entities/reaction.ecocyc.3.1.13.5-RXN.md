---
entity_id: "reaction.ecocyc.3.1.13.5-RXN"
entity_type: "reaction"
name: "3.1.13.5-RXN"
source_database: "EcoCyc"
source_id: "3.1.13.5-RXN"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# 3.1.13.5-RXN

`reaction.ecocyc.3.1.13.5-RXN`

## Static

- Type: `reaction`
- Source: `EcoCyc:3.1.13.5-RXN`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

This reaction is the nonprocessive, exonucleolytic cleavage of the 3' end of tRNA precursor to yield mature tRNA and ribonucleoside 5'-monophosphates. EcoCyc reaction equation: tRNA-precursors + WATER -> tRNA-Holder + Nucleoside-Monophosphates; direction=PHYSIOL-LEFT-TO-RIGHT. This reaction is the nonprocessive, exonucleolytic cleavage of the 3' end of tRNA precursor to yield mature tRNA and ribonucleoside 5'-monophosphates.

## Biological Role

Catalyzed by rnd (protein.P09155). Substrates: H2O (molecule.C00001). Products: a nucleoside 5'-monophosphate (molecule.ecocyc.Nucleoside-Monophosphates), a tRNA (molecule.ecocyc.tRNA-Holder).

## Annotation

This reaction is the nonprocessive, exonucleolytic cleavage of the 3' end of tRNA precursor to yield mature tRNA and ribonucleoside 5'-monophosphates.

## Outgoing Edges (0)

_None._

## Incoming Edges (7)

- `activates` <-- [[molecule.C00238|molecule.C00238]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `activates` <-- [[molecule.ecocyc.AMMONIUM|molecule.ecocyc.AMMONIUM]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `catalyzes` <-- [[protein.P09155|protein.P09155]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.ecocyc.Nucleoside-Monophosphates|molecule.ecocyc.Nucleoside-Monophosphates]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.tRNA-Holder|molecule.ecocyc.tRNA-Holder]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00001|molecule.C00001]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `represses` <-- [[molecule.ecocyc.EDTA|molecule.ecocyc.EDTA]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity

## External IDs

- `EcoCyc:3.1.13.5-RXN`

## Notes

tRNA-precursors + WATER -> tRNA-Holder + Nucleoside-Monophosphates; direction=PHYSIOL-LEFT-TO-RIGHT
