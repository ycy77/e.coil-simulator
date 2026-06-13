---
entity_id: "reaction.ecocyc.RXN0-6485"
entity_type: "reaction"
name: "RXN0-6485"
source_database: "EcoCyc"
source_id: "RXN0-6485"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN0-6485

`reaction.ecocyc.RXN0-6485`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN0-6485`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

This reaction describes the endonucleolytic cleavage occurring between tRNA transcripts in order to separate the tRNA precursors for several polycistronic transcript in TAX-562. It is catalyzed by EG10859-MONOMER for some tRNA processing reactions or by CPLX0-3281 for others . EcoCyc reaction equation: CPD0-2350 + WATER -> CPD0-2352 + CPD0-2350; direction=PHYSIOL-LEFT-TO-RIGHT. This reaction describes the endonucleolytic cleavage occurring between tRNA transcripts in order to separate the tRNA precursors for several polycistronic transcript in TAX-562. It is catalyzed by EG10859-MONOMER for some tRNA processing reactions or by CPLX0-3281 for others .

## Biological Role

Catalyzed by ribonuclease E (complex.ecocyc.CPLX0-3461). Substrates: H2O (molecule.C00001).

## Enriched Pathways

- `ecocyc.PWY-8469` polycistronic tRNA processing I (EcoCyc)

## Annotation

This reaction describes the endonucleolytic cleavage occurring between tRNA transcripts in order to separate the tRNA precursors for several polycistronic transcript in TAX-562. It is catalyzed by EG10859-MONOMER for some tRNA processing reactions or by CPLX0-3281 for others .

## Pathways

- `ecocyc.PWY-8469` polycistronic tRNA processing I (EcoCyc)

## Outgoing Edges (0)

_None._

## Incoming Edges (2)

- `catalyzes` <-- [[complex.ecocyc.CPLX0-3461|complex.ecocyc.CPLX0-3461]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_substrate_of` <-- [[molecule.C00001|molecule.C00001]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN0-6485`

## Notes

CPD0-2350 + WATER -> CPD0-2352 + CPD0-2350; direction=PHYSIOL-LEFT-TO-RIGHT
