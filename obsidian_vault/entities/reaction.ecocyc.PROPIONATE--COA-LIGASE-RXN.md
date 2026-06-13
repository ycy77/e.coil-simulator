---
entity_id: "reaction.ecocyc.PROPIONATE--COA-LIGASE-RXN"
entity_type: "reaction"
name: "PROPIONATE--COA-LIGASE-RXN"
source_database: "EcoCyc"
source_id: "PROPIONATE--COA-LIGASE-RXN"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
  - "PROPIONYL-COA SYNTHETASE"
---

# PROPIONATE--COA-LIGASE-RXN

`reaction.ecocyc.PROPIONATE--COA-LIGASE-RXN`

## Static

- Type: `reaction`
- Source: `EcoCyc:PROPIONATE--COA-LIGASE-RXN`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

CO-A + PROPIONATE + ATP -> PROPIONYL-COA + PPI + AMP; direction=PHYSIOL-LEFT-TO-RIGHT EcoCyc reaction equation: CO-A + PROPIONATE + ATP -> PROPIONYL-COA + PPI + AMP; direction=PHYSIOL-LEFT-TO-RIGHT.

## Biological Role

Catalyzed by acs (protein.P27550), prpE (protein.P77495). Substrates: ATP (molecule.C00002), CoA (molecule.C00010), Propanoate (molecule.C00163). Products: Diphosphate (molecule.C00013), AMP (molecule.C00020), Propanoyl-CoA (molecule.C00100).

## Enriched Pathways

- `ecocyc.PWY0-42` 2-methylcitrate cycle I (EcoCyc)

## Annotation

CO-A + PROPIONATE + ATP -> PROPIONYL-COA + PPI + AMP; direction=PHYSIOL-LEFT-TO-RIGHT

## Pathways

- `ecocyc.PWY0-42` 2-methylcitrate cycle I (EcoCyc)

## Outgoing Edges (0)

_None._

## Incoming Edges (8)

- `catalyzes` <-- [[protein.P27550|protein.P27550]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` <-- [[protein.P77495|protein.P77495]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00013|molecule.C00013]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00020|molecule.C00020]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00100|molecule.C00100]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00002|molecule.C00002]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C00010|molecule.C00010]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C00163|molecule.C00163]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:PROPIONATE--COA-LIGASE-RXN`

## Notes

CO-A + PROPIONATE + ATP -> PROPIONYL-COA + PPI + AMP; direction=PHYSIOL-LEFT-TO-RIGHT
