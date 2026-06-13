---
entity_id: "reaction.ecocyc.RXN0-20"
entity_type: "reaction"
name: "RXN0-20"
source_database: "EcoCyc"
source_id: "RXN0-20"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN0-20

`reaction.ecocyc.RXN0-20`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN0-20`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

Prolipoprotein-Cysteines + L-1-PHOSPHATIDYL-GLYCEROL -> MONOMER0-4342 + SN-GLYCEROL-1-PHOSPHATE + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT EcoCyc reaction equation: Prolipoprotein-Cysteines + L-1-PHOSPHATIDYL-GLYCEROL -> MONOMER0-4342 + SN-GLYCEROL-1-PHOSPHATE + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT.

## Biological Role

Catalyzed by lgt (protein.P60955). Substrates: Phosphatidylglycerol (molecule.C00344), a [prolipoprotein]-L-cysteine (molecule.ecocyc.Prolipoprotein-Cysteines). Products: H+ (molecule.C00080), sn-Glycerol 1-phosphate (molecule.C00623), a [prolipoprotein]-S-1,2-diacyl-sn-glyceryl-L-cysteine (molecule.ecocyc.MONOMER0-4342).

## Enriched Pathways

- `ecocyc.PWY-7884` lipoprotein posttranslational modification (Gram-negative bacteria) (EcoCyc)

## Annotation

Prolipoprotein-Cysteines + L-1-PHOSPHATIDYL-GLYCEROL -> MONOMER0-4342 + SN-GLYCEROL-1-PHOSPHATE + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT

## Pathways

- `ecocyc.PWY-7884` lipoprotein posttranslational modification (Gram-negative bacteria) (EcoCyc)

## Outgoing Edges (0)

_None._

## Incoming Edges (6)

- `catalyzes` <-- [[protein.P60955|protein.P60955]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00623|molecule.C00623]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.MONOMER0-4342|molecule.ecocyc.MONOMER0-4342]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00344|molecule.C00344]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.ecocyc.Prolipoprotein-Cysteines|molecule.ecocyc.Prolipoprotein-Cysteines]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN0-20`

## Notes

Prolipoprotein-Cysteines + L-1-PHOSPHATIDYL-GLYCEROL -> MONOMER0-4342 + SN-GLYCEROL-1-PHOSPHATE + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT
