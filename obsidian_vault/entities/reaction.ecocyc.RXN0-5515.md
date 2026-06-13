---
entity_id: "reaction.ecocyc.RXN0-5515"
entity_type: "reaction"
name: "RXN0-5515"
source_database: "EcoCyc"
source_id: "RXN0-5515"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN0-5515

`reaction.ecocyc.RXN0-5515`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN0-5515`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

This reaction is part of the phospholipid biosynthesis pathway. EcoCyc reaction equation: CTP + 2-3-4-Saturated-L-Phosphatidates + PROTON -> PPI + CDP-2-3-4-Saturated-Diacylglycerols; direction=PHYSIOL-LEFT-TO-RIGHT. This reaction is part of the phospholipid biosynthesis pathway.

## Biological Role

Catalyzed by cdsA (protein.P0ABG1). Substrates: CTP (molecule.C00063), H+ (molecule.C00080), a 2,3,4-saturated 1,2-diacyl-sn-glycerol 3-phosphate (molecule.ecocyc.2-3-4-Saturated-L-Phosphatidates). Products: Diphosphate (molecule.C00013), a CDP-2,3,4-saturated-diacylglycerol (molecule.ecocyc.CDP-2-3-4-Saturated-Diacylglycerols).

## Annotation

This reaction is part of the phospholipid biosynthesis pathway.

## Outgoing Edges (0)

_None._

## Incoming Edges (13)

- `activates` <-- [[molecule.C00020|molecule.C00020]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `activates` <-- [[molecule.C00865|molecule.C00865]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `activates` <-- [[molecule.ecocyc.BRIJ97|molecule.ecocyc.BRIJ97]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `activates` <-- [[molecule.ecocyc.CPD0-1629|molecule.ecocyc.CPD0-1629]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `catalyzes` <-- [[protein.P0ABG1|protein.P0ABG1]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00013|molecule.C00013]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.CDP-2-3-4-Saturated-Diacylglycerols|molecule.ecocyc.CDP-2-3-4-Saturated-Diacylglycerols]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00063|molecule.C00063]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.ecocyc.2-3-4-Saturated-L-Phosphatidates|molecule.ecocyc.2-3-4-Saturated-L-Phosphatidates]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `represses` <-- [[molecule.C00063|molecule.C00063]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.C00458|molecule.C00458]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.ecocyc.EDTA|molecule.ecocyc.EDTA]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity

## External IDs

- `EcoCyc:RXN0-5515`

## Notes

CTP + 2-3-4-Saturated-L-Phosphatidates + PROTON -> PPI + CDP-2-3-4-Saturated-Diacylglycerols; direction=PHYSIOL-LEFT-TO-RIGHT
