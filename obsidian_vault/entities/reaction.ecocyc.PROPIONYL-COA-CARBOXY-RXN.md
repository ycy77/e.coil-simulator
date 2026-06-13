---
entity_id: "reaction.ecocyc.PROPIONYL-COA-CARBOXY-RXN"
entity_type: "reaction"
name: "PROPIONYL-COA-CARBOXY-RXN"
source_database: "EcoCyc"
source_id: "PROPIONYL-COA-CARBOXY-RXN"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# PROPIONYL-COA-CARBOXY-RXN

`reaction.ecocyc.PROPIONYL-COA-CARBOXY-RXN`

## Static

- Type: `reaction`
- Source: `EcoCyc:PROPIONYL-COA-CARBOXY-RXN`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

This is the first reaction of one pathway of propionate metabolism, following the activation of propionate to propionyl-CoA. Also, propionyl-CoA is produced internally by the breakdown of odd-numbered fatty acids, and is further catabolized. EcoCyc reaction equation: ATP + HCO3 + PROPIONYL-COA -> PROTON + ADP + Pi + D-METHYL-MALONYL-COA; direction=REVERSIBLE. This is the first reaction of one pathway of propionate metabolism, following the activation of propionate to propionyl-CoA. Also, propionyl-CoA is produced internally by the breakdown of odd-numbered fatty acids, and is further catabolized.

## Biological Role

Catalyzed by PROPIONYL-COA-CARBOXY-MONOMER (protein.ecocyc.PROPIONYL-COA-CARBOXY-MONOMER). Substrates: ATP (molecule.C00002), Propanoyl-CoA (molecule.C00100), HCO3- (molecule.C00288). Products: ADP (molecule.C00008), H+ (molecule.C00080), (S)-Methylmalonyl-CoA (molecule.C00683), phosphate (molecule.ecocyc.Pi).

## Enriched Pathways

- `ecocyc.PROPIONMET-PWY` propanoyl CoA degradation I (EcoCyc)

## Annotation

This is the first reaction of one pathway of propionate metabolism, following the activation of propionate to propionyl-CoA. Also, propionyl-CoA is produced internally by the breakdown of odd-numbered fatty acids, and is further catabolized.

## Pathways

- `ecocyc.PROPIONMET-PWY` propanoyl CoA degradation I (EcoCyc)

## Outgoing Edges (0)

_None._

## Incoming Edges (8)

- `catalyzes` <-- [[protein.ecocyc.PROPIONYL-COA-CARBOXY-MONOMER|protein.ecocyc.PROPIONYL-COA-CARBOXY-MONOMER]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00008|molecule.C00008]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00683|molecule.C00683]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.Pi|molecule.ecocyc.Pi]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00002|molecule.C00002]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C00100|molecule.C00100]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C00288|molecule.C00288]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:PROPIONYL-COA-CARBOXY-RXN`

## Notes

ATP + HCO3 + PROPIONYL-COA -> PROTON + ADP + Pi + D-METHYL-MALONYL-COA; direction=REVERSIBLE
