---
entity_id: "reaction.ecocyc.RXN0-5401"
entity_type: "reaction"
name: "RXN0-5401"
source_database: "EcoCyc"
source_id: "RXN0-5401"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: "CCO-OUTER-MEM"
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN0-5401

`reaction.ecocyc.RXN0-5401`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN0-5401`
- Default state: `active`
- Allowed states: `active|blocked`
- Location: CCO-OUTER-MEM

## Enriched Summary

a-murein-lipoprotein + CPD-17931 -> CPD0-1171 + D-ALANINE; direction=PHYSIOL-LEFT-TO-RIGHT EcoCyc reaction equation: a-murein-lipoprotein + CPD-17931 -> CPD0-1171 + D-ALANINE; direction=PHYSIOL-LEFT-TO-RIGHT.

## Biological Role

Catalyzed by ybiS (protein.P0AAX8), erfK (protein.P39176), ycfS (protein.P75954). Substrates: a peptidoglycan internal segment with (L-alanyl-γ-D-glutamyl-meso-2,6-diaminopimeloyl-D-alanine) tetrapeptide (molecule.ecocyc.CPD-17931). Products: D-Alanine (molecule.C00133), a peptidoglycan crosslinked to murein lipoprotein (molecule.ecocyc.CPD0-1171).

## Annotation

a-murein-lipoprotein + CPD-17931 -> CPD0-1171 + D-ALANINE; direction=PHYSIOL-LEFT-TO-RIGHT

## Outgoing Edges (0)

_None._

## Incoming Edges (6)

- `catalyzes` <-- [[protein.P0AAX8|protein.P0AAX8]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` <-- [[protein.P39176|protein.P39176]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` <-- [[protein.P75954|protein.P75954]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00133|molecule.C00133]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.CPD0-1171|molecule.ecocyc.CPD0-1171]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.ecocyc.CPD-17931|molecule.ecocyc.CPD-17931]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN0-5401`

## Notes

a-murein-lipoprotein + CPD-17931 -> CPD0-1171 + D-ALANINE; direction=PHYSIOL-LEFT-TO-RIGHT
