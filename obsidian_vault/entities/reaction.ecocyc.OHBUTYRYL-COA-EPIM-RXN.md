---
entity_id: "reaction.ecocyc.OHBUTYRYL-COA-EPIM-RXN"
entity_type: "reaction"
name: "OHBUTYRYL-COA-EPIM-RXN"
source_database: "EcoCyc"
source_id: "OHBUTYRYL-COA-EPIM-RXN"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# OHBUTYRYL-COA-EPIM-RXN

`reaction.ecocyc.OHBUTYRYL-COA-EPIM-RXN`

## Static

- Type: `reaction`
- Source: `EcoCyc:OHBUTYRYL-COA-EPIM-RXN`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

A reaction in the β-oxidation cycle, this reaction takes place when particular types of unsaturated fatty acids are degraded. EcoCyc reaction equation: D-3-HYDROXYACYL-COA -> L-3-HYDROXYACYL-COA; direction=REVERSIBLE. A reaction in the β-oxidation cycle, this reaction takes place when particular types of unsaturated fatty acids are degraded.

## Biological Role

Catalyzed by fadB (protein.P21177), fadJ (protein.P77399). Substrates: a 2,3,4-saturated (3R)-3-hydroxyacyl-CoA (molecule.ecocyc.D-3-HYDROXYACYL-COA). Products: a 2,3,4-saturated (3S)-3-hydroxyacyl-CoA (molecule.ecocyc.L-3-HYDROXYACYL-COA).

## Enriched Pathways

- `ecocyc.FAO-PWY` fatty acid β-oxidation I (generic) (EcoCyc)

## Annotation

A reaction in the β-oxidation cycle, this reaction takes place when particular types of unsaturated fatty acids are degraded.

## Pathways

- `ecocyc.FAO-PWY` fatty acid β-oxidation I (generic) (EcoCyc)

## Outgoing Edges (0)

_None._

## Incoming Edges (4)

- `catalyzes` <-- [[protein.P21177|protein.P21177]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` <-- [[protein.P77399|protein.P77399]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.ecocyc.L-3-HYDROXYACYL-COA|molecule.ecocyc.L-3-HYDROXYACYL-COA]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.ecocyc.D-3-HYDROXYACYL-COA|molecule.ecocyc.D-3-HYDROXYACYL-COA]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:OHBUTYRYL-COA-EPIM-RXN`

## Notes

D-3-HYDROXYACYL-COA -> L-3-HYDROXYACYL-COA; direction=REVERSIBLE
