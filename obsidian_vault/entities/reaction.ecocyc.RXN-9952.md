---
entity_id: "reaction.ecocyc.RXN-9952"
entity_type: "reaction"
name: "RXN-9952"
source_database: "EcoCyc"
source_id: "RXN-9952"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN-9952

`reaction.ecocyc.RXN-9952`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN-9952`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

CPD-2961 + NADP -> RIBULOSE-5P + CARBON-DIOXIDE + NADPH; direction=LEFT-TO-RIGHT EcoCyc reaction equation: CPD-2961 + NADP -> RIBULOSE-5P + CARBON-DIOXIDE + NADPH; direction=LEFT-TO-RIGHT.

## Biological Role

Catalyzed by 6-phosphogluconate dehydrogenase, decarboxylating (complex.ecocyc.6PGLUCONDEHYDROG-CPLX). Substrates: NADP+ (molecule.C00006), 6-Phospho-D-gluconate (molecule.C00345). Products: NADPH (molecule.C00005), CO2 (molecule.C00011), D-Ribulose 5-phosphate (molecule.C00199).

## Enriched Pathways

- `ecocyc.OXIDATIVEPENT-PWY` pentose phosphate pathway (oxidative branch) I (EcoCyc)

## Annotation

CPD-2961 + NADP -> RIBULOSE-5P + CARBON-DIOXIDE + NADPH; direction=LEFT-TO-RIGHT

## Pathways

- `ecocyc.OXIDATIVEPENT-PWY` pentose phosphate pathway (oxidative branch) I (EcoCyc)

## Outgoing Edges (0)

_None._

## Incoming Edges (11)

- `catalyzes` <-- [[complex.ecocyc.6PGLUCONDEHYDROG-CPLX|complex.ecocyc.6PGLUCONDEHYDROG-CPLX]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00005|molecule.C00005]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00011|molecule.C00011]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00199|molecule.C00199]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00006|molecule.C00006]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C00345|molecule.C00345]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `represses` <-- [[molecule.C00002|molecule.C00002]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.C00005|molecule.C00005]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.C00199|molecule.C00199]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.C00279|molecule.C00279]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.C00354|molecule.C00354]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity

## External IDs

- `EcoCyc:RXN-9952`

## Notes

CPD-2961 + NADP -> RIBULOSE-5P + CARBON-DIOXIDE + NADPH; direction=LEFT-TO-RIGHT
