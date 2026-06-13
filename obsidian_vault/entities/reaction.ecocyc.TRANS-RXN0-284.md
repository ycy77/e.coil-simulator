---
entity_id: "reaction.ecocyc.TRANS-RXN0-284"
entity_type: "reaction"
name: "TRANS-RXN0-284"
source_database: "EcoCyc"
source_id: "TRANS-RXN0-284"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: "CCO-PM-BAC-NEG"
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# TRANS-RXN0-284

`reaction.ecocyc.TRANS-RXN0-284`

## Static

- Type: `reaction`
- Source: `EcoCyc:TRANS-RXN0-284`
- Default state: `active`
- Allowed states: `active|blocked`
- Location: CCO-PM-BAC-NEG

## Enriched Summary

PHENYLACETALDEHYDE -> PHENYLACETALDEHYDE; direction=LEFT-TO-RIGHT EcoCyc reaction equation: PHENYLACETALDEHYDE -> PHENYLACETALDEHYDE; direction=LEFT-TO-RIGHT.

## Biological Role

Substrates: Phenylacetaldehyde (molecule.C00601). Products: Phenylacetaldehyde (molecule.C00601).

## Enriched Pathways

- `ecocyc.2PHENDEG-PWY` phenylethylamine degradation I (EcoCyc)

## Annotation

PHENYLACETALDEHYDE -> PHENYLACETALDEHYDE; direction=LEFT-TO-RIGHT

## Pathways

- `ecocyc.2PHENDEG-PWY` phenylethylamine degradation I (EcoCyc)

## Outgoing Edges (0)

_None._

## Incoming Edges (2)

- `is_product_of` <-- [[molecule.C00601|molecule.C00601]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00601|molecule.C00601]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:TRANS-RXN0-284`

## Notes

PHENYLACETALDEHYDE -> PHENYLACETALDEHYDE; direction=LEFT-TO-RIGHT
