---
entity_id: "reaction.ecocyc.GLU6PDEHYDROG-RXN"
entity_type: "reaction"
name: "GLU6PDEHYDROG-RXN"
source_database: "EcoCyc"
source_id: "GLU6PDEHYDROG-RXN"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# GLU6PDEHYDROG-RXN

`reaction.ecocyc.GLU6PDEHYDROG-RXN`

## Static

- Type: `reaction`
- Source: `EcoCyc:GLU6PDEHYDROG-RXN`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

First step in the pentose phosphate pathway. EcoCyc reaction equation: D-glucopyranose-6-phosphate + NADP -> D-6-P-GLUCONO-DELTA-LACTONE + NADPH + PROTON; direction=LEFT-TO-RIGHT. First step in the pentose phosphate pathway.

## Biological Role

Catalyzed by zwf (protein.P0AC53). Substrates: NADP+ (molecule.C00006), D-Glucose 6-phosphate (molecule.C00092). Products: NADPH (molecule.C00005), H+ (molecule.C00080), D-Glucono-1,5-lactone 6-phosphate (molecule.C01236).

## Enriched Pathways

- `ecocyc.GLYCOLYSIS-E-D` superpathway of glycolysis and the Entner-Doudoroff pathway (EcoCyc)
- `ecocyc.OXIDATIVEPENT-PWY` pentose phosphate pathway (oxidative branch) I (EcoCyc)

## Annotation

First step in the pentose phosphate pathway.

## Pathways

- `ecocyc.GLYCOLYSIS-E-D` superpathway of glycolysis and the Entner-Doudoroff pathway (EcoCyc)
- `ecocyc.OXIDATIVEPENT-PWY` pentose phosphate pathway (oxidative branch) I (EcoCyc)

## Outgoing Edges (0)

_None._

## Incoming Edges (7)

- `catalyzes` <-- [[protein.P0AC53|protein.P0AC53]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00005|molecule.C00005]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C01236|molecule.C01236]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00006|molecule.C00006]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C00092|molecule.C00092]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `represses` <-- [[molecule.C00005|molecule.C00005]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity

## External IDs

- `EcoCyc:GLU6PDEHYDROG-RXN`

## Notes

D-glucopyranose-6-phosphate + NADP -> D-6-P-GLUCONO-DELTA-LACTONE + NADPH + PROTON; direction=LEFT-TO-RIGHT
