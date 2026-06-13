---
entity_id: "reaction.ecocyc.RXN0-7479"
entity_type: "reaction"
name: "RXN0-7479"
source_database: "EcoCyc"
source_id: "RXN0-7479"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN0-7479

`reaction.ecocyc.RXN0-7479`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN0-7479`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

This reaction cleaves the stem loop from a Rho-independent extension at the 3' end of a transcript EcoCyc reaction equation: a-polycistronic-transcript-containing-tRNA-amp-mRNA + WATER -> a-polycistronic-containing-mRNA-amp-tRNA-with-a-short-3-exte + RNA-Fragments; direction=PHYSIOL-LEFT-TO-RIGHT. This reaction cleaves the stem loop from a Rho-independent extension at the 3' end of a transcript

## Biological Role

Catalyzed by ribonuclease E (complex.ecocyc.CPLX0-3461). Substrates: H2O (molecule.C00001), a polycistronic transcript containing tRNA & mRNA (molecule.ecocyc.a-polycistronic-transcript-containing-tRNA-amp-mRNA).

## Enriched Pathways

- `ecocyc.PWY0-1626` polycistronic tRNA processing III (EcoCyc)

## Annotation

This reaction cleaves the stem loop from a Rho-independent extension at the 3' end of a transcript

## Pathways

- `ecocyc.PWY0-1626` polycistronic tRNA processing III (EcoCyc)

## Outgoing Edges (0)

_None._

## Incoming Edges (3)

- `catalyzes` <-- [[complex.ecocyc.CPLX0-3461|complex.ecocyc.CPLX0-3461]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_substrate_of` <-- [[molecule.C00001|molecule.C00001]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.ecocyc.a-polycistronic-transcript-containing-tRNA-amp-mRNA|molecule.ecocyc.a-polycistronic-transcript-containing-tRNA-amp-mRNA]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN0-7479`

## Notes

a-polycistronic-transcript-containing-tRNA-amp-mRNA + WATER -> a-polycistronic-containing-mRNA-amp-tRNA-with-a-short-3-exte + RNA-Fragments; direction=PHYSIOL-LEFT-TO-RIGHT
