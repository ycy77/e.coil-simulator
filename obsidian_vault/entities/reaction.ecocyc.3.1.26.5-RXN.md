---
entity_id: "reaction.ecocyc.3.1.26.5-RXN"
entity_type: "reaction"
name: "3.1.26.5-RXN"
source_database: "EcoCyc"
source_id: "3.1.26.5-RXN"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# 3.1.26.5-RXN

`reaction.ecocyc.3.1.26.5-RXN`

## Static

- Type: `reaction`
- Source: `EcoCyc:3.1.26.5-RXN`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

This is the endonucleolytic cleavage of RNA to remove the excess 5' nucleotide from tRNA precursor, yielding the final 5' terminus of a mature tRNA. EcoCyc reaction equation: CPD0-2352 + WATER -> CPD0-2353 + tRNA-fragment; direction=PHYSIOL-LEFT-TO-RIGHT. This is the endonucleolytic cleavage of RNA to remove the excess 5' nucleotide from tRNA precursor, yielding the final 5' terminus of a mature tRNA.

## Biological Role

Catalyzed by RNase P (complex.ecocyc.CPLX0-1382). Substrates: H2O (molecule.C00001).

## Enriched Pathways

- `ecocyc.PWY-8469` polycistronic tRNA processing I (EcoCyc)
- `ecocyc.PWY0-1614` monocistronic leuX tRNA processing (EcoCyc)

## Annotation

This is the endonucleolytic cleavage of RNA to remove the excess 5' nucleotide from tRNA precursor, yielding the final 5' terminus of a mature tRNA.

## Pathways

- `ecocyc.PWY-8469` polycistronic tRNA processing I (EcoCyc)
- `ecocyc.PWY0-1614` monocistronic leuX tRNA processing (EcoCyc)

## Outgoing Edges (0)

_None._

## Incoming Edges (3)

- `catalyzes` <-- [[complex.ecocyc.CPLX0-1382|complex.ecocyc.CPLX0-1382]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_substrate_of` <-- [[molecule.C00001|molecule.C00001]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `represses` <-- [[molecule.ecocyc.CPD-14142|molecule.ecocyc.CPD-14142]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity

## External IDs

- `EcoCyc:3.1.26.5-RXN`

## Notes

CPD0-2352 + WATER -> CPD0-2353 + tRNA-fragment; direction=PHYSIOL-LEFT-TO-RIGHT
