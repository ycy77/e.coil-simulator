---
entity_id: "reaction.ecocyc.RXN-24137"
entity_type: "reaction"
name: "endoribonuclease"
source_database: "EcoCyc"
source_id: "RXN-24137"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# endoribonuclease

`reaction.ecocyc.RXN-24137`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN-24137`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

This reaction describes the endoribonucleolytic cleavage of the Rho-independent terminator at the 3' end of a tRNA precursor in TAX-562 . EcoCyc reaction equation: CPD0-2351 + WATER -> CPD0-2354 + tRNA-fragment; direction=PHYSIOL-LEFT-TO-RIGHT. This reaction describes the endoribonucleolytic cleavage of the Rho-independent terminator at the 3' end of a tRNA precursor in TAX-562 .

## Biological Role

Catalyzed by ribonuclease E (complex.ecocyc.CPLX0-3461). Substrates: H2O (molecule.C00001).

## Annotation

This reaction describes the endoribonucleolytic cleavage of the Rho-independent terminator at the 3' end of a tRNA precursor in TAX-562 .

## Outgoing Edges (0)

_None._

## Incoming Edges (2)

- `catalyzes` <-- [[complex.ecocyc.CPLX0-3461|complex.ecocyc.CPLX0-3461]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_substrate_of` <-- [[molecule.C00001|molecule.C00001]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN-24137`

## Notes

CPD0-2351 + WATER -> CPD0-2354 + tRNA-fragment; direction=PHYSIOL-LEFT-TO-RIGHT
