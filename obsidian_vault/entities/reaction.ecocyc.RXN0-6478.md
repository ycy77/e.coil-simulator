---
entity_id: "reaction.ecocyc.RXN0-6478"
entity_type: "reaction"
name: "endoribonuclease"
source_database: "EcoCyc"
source_id: "RXN0-6478"
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

`reaction.ecocyc.RXN0-6478`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN0-6478`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

This reaction describes the endonucleolytic cleavage occurring between tRNA transcripts in order to separate the tRNA precursors for several polycistronic transcript in TAX-562. It is catalyzed by EG10859-MONOMER for some tRNA processing reactions or by CPLX0-3281 for others . EcoCyc reaction equation: CPD0-2350 + WATER -> CPD0-2351 + CPD0-2350; direction=PHYSIOL-LEFT-TO-RIGHT. This reaction describes the endonucleolytic cleavage occurring between tRNA transcripts in order to separate the tRNA precursors for several polycistronic transcript in TAX-562. It is catalyzed by EG10859-MONOMER for some tRNA processing reactions or by CPLX0-3281 for others .

## Biological Role

Catalyzed by RNase III (complex.ecocyc.CPLX0-3281), ribonuclease E (complex.ecocyc.CPLX0-3461). Substrates: H2O (molecule.C00001).

## Annotation

This reaction describes the endonucleolytic cleavage occurring between tRNA transcripts in order to separate the tRNA precursors for several polycistronic transcript in TAX-562. It is catalyzed by EG10859-MONOMER for some tRNA processing reactions or by CPLX0-3281 for others .

## Outgoing Edges (0)

_None._

## Incoming Edges (3)

- `catalyzes` <-- [[complex.ecocyc.CPLX0-3281|complex.ecocyc.CPLX0-3281]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` <-- [[complex.ecocyc.CPLX0-3461|complex.ecocyc.CPLX0-3461]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_substrate_of` <-- [[molecule.C00001|molecule.C00001]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN0-6478`

## Notes

CPD0-2350 + WATER -> CPD0-2351 + CPD0-2350; direction=PHYSIOL-LEFT-TO-RIGHT
