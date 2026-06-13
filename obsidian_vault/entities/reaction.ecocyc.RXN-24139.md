---
entity_id: "reaction.ecocyc.RXN-24139"
entity_type: "reaction"
name: "exoribonuclease"
source_database: "EcoCyc"
source_id: "RXN-24139"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# exoribonuclease

`reaction.ecocyc.RXN-24139`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN-24139`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

This reaction represents the removal of a few 3' nucleotides in a tRNA processing pathway . EcoCyc reaction equation: a-tRNA-precursor-w-5-extension-and-medium-3-trailer + WATER -> CPD0-2352 + tRNA-fragment; direction=PHYSIOL-LEFT-TO-RIGHT. This reaction represents the removal of a few 3' nucleotides in a tRNA processing pathway .

## Biological Role

Catalyzed by rnb (protein.P30850). Substrates: H2O (molecule.C00001).

## Enriched Pathways

- `ecocyc.PWY0-1614` monocistronic leuX tRNA processing (EcoCyc)

## Annotation

This reaction represents the removal of a few 3' nucleotides in a tRNA processing pathway .

## Pathways

- `ecocyc.PWY0-1614` monocistronic leuX tRNA processing (EcoCyc)

## Outgoing Edges (0)

_None._

## Incoming Edges (2)

- `catalyzes` <-- [[protein.P30850|protein.P30850]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_substrate_of` <-- [[molecule.C00001|molecule.C00001]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN-24139`

## Notes

a-tRNA-precursor-w-5-extension-and-medium-3-trailer + WATER -> CPD0-2352 + tRNA-fragment; direction=PHYSIOL-LEFT-TO-RIGHT
