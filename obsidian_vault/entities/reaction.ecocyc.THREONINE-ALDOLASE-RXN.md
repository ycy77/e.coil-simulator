---
entity_id: "reaction.ecocyc.THREONINE-ALDOLASE-RXN"
entity_type: "reaction"
name: "THREONINE-ALDOLASE-RXN"
source_database: "EcoCyc"
source_id: "THREONINE-ALDOLASE-RXN"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# THREONINE-ALDOLASE-RXN

`reaction.ecocyc.THREONINE-ALDOLASE-RXN`

## Static

- Type: `reaction`
- Source: `EcoCyc:THREONINE-ALDOLASE-RXN`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

THR -> ACETALD + GLY; direction=REVERSIBLE EcoCyc reaction equation: THR -> ACETALD + GLY; direction=REVERSIBLE.

## Biological Role

Catalyzed by low-specificity L-threonine aldolase (complex.ecocyc.LTAA-CPLX). Substrates: L-Threonine (molecule.C00188). Products: Glycine (molecule.C00037), Acetaldehyde (molecule.C00084).

## Enriched Pathways

- `ecocyc.PWY-5436` L-threonine degradation IV (EcoCyc)

## Annotation

THR -> ACETALD + GLY; direction=REVERSIBLE

## Pathways

- `ecocyc.PWY-5436` L-threonine degradation IV (EcoCyc)

## Outgoing Edges (0)

_None._

## Incoming Edges (4)

- `catalyzes` <-- [[complex.ecocyc.LTAA-CPLX|complex.ecocyc.LTAA-CPLX]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00037|molecule.C00037]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00084|molecule.C00084]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00188|molecule.C00188]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:THREONINE-ALDOLASE-RXN`

## Notes

THR -> ACETALD + GLY; direction=REVERSIBLE
