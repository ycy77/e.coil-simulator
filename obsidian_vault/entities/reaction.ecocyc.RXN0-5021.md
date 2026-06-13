---
entity_id: "reaction.ecocyc.RXN0-5021"
entity_type: "reaction"
name: "RXN0-5021"
source_database: "EcoCyc"
source_id: "RXN0-5021"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN0-5021

`reaction.ecocyc.RXN0-5021`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN0-5021`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

This reaction is the 5' to 3' synthesis of an RNA primer on a single-stranded DNA template. EcoCyc reaction equation: Single-Stranded-DNAs + Ribonucleoside-Triphosphates -> ssDNA-RNA-primer-hybrid + PPI; direction=PHYSIOL-LEFT-TO-RIGHT. This reaction is the 5' to 3' synthesis of an RNA primer on a single-stranded DNA template.

## Biological Role

Catalyzed by dnaG (protein.P0ABS5). Substrates: a ribonucleoside triphosphate (molecule.ecocyc.Ribonucleoside-Triphosphates). Products: Diphosphate (molecule.C00013).

## Annotation

This reaction is the 5' to 3' synthesis of an RNA primer on a single-stranded DNA template.

## Outgoing Edges (0)

_None._

## Incoming Edges (3)

- `catalyzes` <-- [[protein.P0ABS5|protein.P0ABS5]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00013|molecule.C00013]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.ecocyc.Ribonucleoside-Triphosphates|molecule.ecocyc.Ribonucleoside-Triphosphates]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN0-5021`

## Notes

Single-Stranded-DNAs + Ribonucleoside-Triphosphates -> ssDNA-RNA-primer-hybrid + PPI; direction=PHYSIOL-LEFT-TO-RIGHT
