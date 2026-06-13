---
entity_id: "reaction.ecocyc.RXN-24136"
entity_type: "reaction"
name: "RXN-24136"
source_database: "EcoCyc"
source_id: "RXN-24136"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN-24136

`reaction.ecocyc.RXN-24136`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN-24136`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

This reaction represents the 2nd step in tRNA processing of a monocistronic tRNA precursor where the 3' terminator is cleaved by an endoribonuclease, as determined in TAX-562 . EcoCyc reaction equation: a-monocistronic-tRNA-transcript-with-long-3-extension + WATER -> CPD0-2354 + tRNA-terminator-regions; direction=PHYSIOL-LEFT-TO-RIGHT. This reaction represents the 2nd step in tRNA processing of a monocistronic tRNA precursor where the 3' terminator is cleaved by an endoribonuclease, as determined in TAX-562 .

## Biological Role

Catalyzed by ribonuclease E (complex.ecocyc.CPLX0-3461). Substrates: H2O (molecule.C00001).

## Enriched Pathways

- `ecocyc.PWY-8468` monocistronic tRNA processing I (EcoCyc)

## Annotation

This reaction represents the 2nd step in tRNA processing of a monocistronic tRNA precursor where the 3' terminator is cleaved by an endoribonuclease, as determined in TAX-562 .

## Pathways

- `ecocyc.PWY-8468` monocistronic tRNA processing I (EcoCyc)

## Outgoing Edges (0)

_None._

## Incoming Edges (2)

- `catalyzes` <-- [[complex.ecocyc.CPLX0-3461|complex.ecocyc.CPLX0-3461]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_substrate_of` <-- [[molecule.C00001|molecule.C00001]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN-24136`

## Notes

a-monocistronic-tRNA-transcript-with-long-3-extension + WATER -> CPD0-2354 + tRNA-terminator-regions; direction=PHYSIOL-LEFT-TO-RIGHT
