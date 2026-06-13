---
entity_id: "reaction.ecocyc.ENOYL-COA-HYDRAT-RXN"
entity_type: "reaction"
name: "ENOYL-COA-HYDRAT-RXN"
source_database: "EcoCyc"
source_id: "ENOYL-COA-HYDRAT-RXN"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# ENOYL-COA-HYDRAT-RXN

`reaction.ecocyc.ENOYL-COA-HYDRAT-RXN`

## Static

- Type: `reaction`
- Source: `EcoCyc:ENOYL-COA-HYDRAT-RXN`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

A reaction in the β-oxidation of fatty acids. EcoCyc reaction equation: L-3-HYDROXYACYL-COA -> TRANS-D2-ENOYL-COA + WATER; direction=REVERSIBLE. A reaction in the β-oxidation of fatty acids.

## Biological Role

Catalyzed by fadB (protein.P21177), fadJ (protein.P77399). Substrates: a 2,3,4-saturated (3S)-3-hydroxyacyl-CoA (molecule.ecocyc.L-3-HYDROXYACYL-COA). Products: H2O (molecule.C00001), a (2E)-2-enoyl-CoA (molecule.ecocyc.TRANS-D2-ENOYL-COA).

## Enriched Pathways

- `ecocyc.FAO-PWY` fatty acid β-oxidation I (generic) (EcoCyc)

## Annotation

A reaction in the β-oxidation of fatty acids.

## Pathways

- `ecocyc.FAO-PWY` fatty acid β-oxidation I (generic) (EcoCyc)

## Outgoing Edges (0)

_None._

## Incoming Edges (6)

- `catalyzes` <-- [[protein.P21177|protein.P21177]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` <-- [[protein.P77399|protein.P77399]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00001|molecule.C00001]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.TRANS-D2-ENOYL-COA|molecule.ecocyc.TRANS-D2-ENOYL-COA]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.ecocyc.L-3-HYDROXYACYL-COA|molecule.ecocyc.L-3-HYDROXYACYL-COA]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `represses` <-- [[molecule.ecocyc.CPD-14729|molecule.ecocyc.CPD-14729]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity

## External IDs

- `EcoCyc:ENOYL-COA-HYDRAT-RXN`

## Notes

L-3-HYDROXYACYL-COA -> TRANS-D2-ENOYL-COA + WATER; direction=REVERSIBLE
