---
entity_id: "reaction.ecocyc.3.1.27.6-RXN"
entity_type: "reaction"
name: "3.1.27.6-RXN"
source_database: "EcoCyc"
source_id: "3.1.27.6-RXN"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: "CCO-PERI-BAC"
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# 3.1.27.6-RXN

`reaction.ecocyc.3.1.27.6-RXN`

## Static

- Type: `reaction`
- Source: `EcoCyc:3.1.27.6-RXN`
- Default state: `active`
- Allowed states: `active|blocked`
- Location: CCO-PERI-BAC

## Enriched Summary

This reaction is the endonucleolytic cleavage of RNA to yield nucleoside 3'-phosphates and 3'-phosphooligonucleotides with 2',3'-cyclic phosphate intermediates. EcoCyc reaction equation: mRNA-Holder + WATER -> mRNA-Fragments; direction=PHYSIOL-LEFT-TO-RIGHT. This reaction is the endonucleolytic cleavage of RNA to yield nucleoside 3'-phosphates and 3'-phosphooligonucleotides with 2',3'-cyclic phosphate intermediates.

## Biological Role

Catalyzed by putative RNase adaptor protein YicC (complex.ecocyc.CPLX0-11240), rna (protein.P21338). Substrates: H2O (molecule.C00001), an mRNA (molecule.ecocyc.mRNA-Holder).

## Annotation

This reaction is the endonucleolytic cleavage of RNA to yield nucleoside 3'-phosphates and 3'-phosphooligonucleotides with 2',3'-cyclic phosphate intermediates.

## Outgoing Edges (0)

_None._

## Incoming Edges (6)

- `catalyzes` <-- [[complex.ecocyc.CPLX0-11240|complex.ecocyc.CPLX0-11240]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` <-- [[protein.P21338|protein.P21338]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_substrate_of` <-- [[molecule.C00001|molecule.C00001]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.ecocyc.mRNA-Holder|molecule.ecocyc.mRNA-Holder]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `represses` <-- [[molecule.C00305|molecule.C00305]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.ecocyc.CA_2|molecule.ecocyc.CA_2]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity

## External IDs

- `EcoCyc:3.1.27.6-RXN`

## Notes

mRNA-Holder + WATER -> mRNA-Fragments; direction=PHYSIOL-LEFT-TO-RIGHT
