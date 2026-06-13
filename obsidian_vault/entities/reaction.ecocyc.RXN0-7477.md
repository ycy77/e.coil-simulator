---
entity_id: "reaction.ecocyc.RXN0-7477"
entity_type: "reaction"
name: "RXN0-7477"
source_database: "EcoCyc"
source_id: "RXN0-7477"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN0-7477

`reaction.ecocyc.RXN0-7477`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN0-7477`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

This reaction represents the exonucleolytic cleavage of nucleotides from the 3' end of a tRNA gene as part of the tRNA processing . EcoCyc reaction equation: tRNA-precursor-w-long-5-amp-medium-3-extensions + WATER -> tRNA-precursor-w-long-5-extension-amp-short-3-extension + tRNA-fragment; direction=PHYSIOL-LEFT-TO-RIGHT. This reaction represents the exonucleolytic cleavage of nucleotides from the 3' end of a tRNA gene as part of the tRNA processing .

## Biological Role

Catalyzed by polynucleotide phosphorylase (complex.ecocyc.CPLX0-3521), rph (protein.P0CG19), rnb (protein.P30850). Substrates: H2O (molecule.C00001).

## Enriched Pathways

- `ecocyc.PWY0-1623` polycistronic tRNA processing II (EcoCyc)

## Annotation

This reaction represents the exonucleolytic cleavage of nucleotides from the 3' end of a tRNA gene as part of the tRNA processing .

## Pathways

- `ecocyc.PWY0-1623` polycistronic tRNA processing II (EcoCyc)

## Outgoing Edges (0)

_None._

## Incoming Edges (4)

- `catalyzes` <-- [[complex.ecocyc.CPLX0-3521|complex.ecocyc.CPLX0-3521]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` <-- [[protein.P0CG19|protein.P0CG19]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` <-- [[protein.P30850|protein.P30850]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_substrate_of` <-- [[molecule.C00001|molecule.C00001]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN0-7477`

## Notes

tRNA-precursor-w-long-5-amp-medium-3-extensions + WATER -> tRNA-precursor-w-long-5-extension-amp-short-3-extension + tRNA-fragment; direction=PHYSIOL-LEFT-TO-RIGHT
