---
entity_id: "reaction.ecocyc.OHACYL-COA-DEHYDROG-RXN"
entity_type: "reaction"
name: "OHACYL-COA-DEHYDROG-RXN"
source_database: "EcoCyc"
source_id: "OHACYL-COA-DEHYDROG-RXN"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# OHACYL-COA-DEHYDROG-RXN

`reaction.ecocyc.OHACYL-COA-DEHYDROG-RXN`

## Static

- Type: `reaction`
- Source: `EcoCyc:OHACYL-COA-DEHYDROG-RXN`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

A reaction in the β-oxidation fatty acid degradation. EcoCyc reaction equation: NAD + L-3-HYDROXYACYL-COA -> NADH + 3-KETOACYL-COA + PROTON; direction=REVERSIBLE. A reaction in the β-oxidation fatty acid degradation.

## Biological Role

Catalyzed by fadB (protein.P21177), fadJ (protein.P77399). Substrates: NAD+ (molecule.C00003), a 2,3,4-saturated (3S)-3-hydroxyacyl-CoA (molecule.ecocyc.L-3-HYDROXYACYL-COA). Products: NADH (molecule.C00004), H+ (molecule.C00080), a 2,3,4-saturated 3-oxoacyl-CoA (molecule.ecocyc.3-KETOACYL-COA).

## Enriched Pathways

- `ecocyc.FAO-PWY` fatty acid β-oxidation I (generic) (EcoCyc)

## Annotation

A reaction in the β-oxidation fatty acid degradation.

## Pathways

- `ecocyc.FAO-PWY` fatty acid β-oxidation I (generic) (EcoCyc)

## Outgoing Edges (0)

_None._

## Incoming Edges (7)

- `catalyzes` <-- [[protein.P21177|protein.P21177]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` <-- [[protein.P77399|protein.P77399]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00004|molecule.C00004]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.3-KETOACYL-COA|molecule.ecocyc.3-KETOACYL-COA]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00003|molecule.C00003]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.ecocyc.L-3-HYDROXYACYL-COA|molecule.ecocyc.L-3-HYDROXYACYL-COA]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:OHACYL-COA-DEHYDROG-RXN`

## Notes

NAD + L-3-HYDROXYACYL-COA -> NADH + 3-KETOACYL-COA + PROTON; direction=REVERSIBLE
