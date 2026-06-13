---
entity_id: "reaction.ecocyc.2.3.1.180-RXN"
entity_type: "reaction"
name: "2.3.1.180-RXN"
source_database: "EcoCyc"
source_id: "2.3.1.180-RXN"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# 2.3.1.180-RXN

`reaction.ecocyc.2.3.1.180-RXN`

## Static

- Type: `reaction`
- Source: `EcoCyc:2.3.1.180-RXN`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

ACETYL-COA + MALONYL-ACP + PROTON -> Acetoacetyl-ACPs + CO-A + CARBON-DIOXIDE; direction=LEFT-TO-RIGHT EcoCyc reaction equation: ACETYL-COA + MALONYL-ACP + PROTON -> Acetoacetyl-ACPs + CO-A + CARBON-DIOXIDE; direction=LEFT-TO-RIGHT.

## Biological Role

Catalyzed by 3-oxoacyl-[acyl carrier protein] synthase 3 (complex.ecocyc.CPLX0-252). Substrates: Acetyl-CoA (molecule.C00024), H+ (molecule.C00080). Products: CoA (molecule.C00010), CO2 (molecule.C00011).

## Enriched Pathways

- `ecocyc.PWY-4381` fatty acid biosynthesis initiation (type II) (EcoCyc)

## Annotation

ACETYL-COA + MALONYL-ACP + PROTON -> Acetoacetyl-ACPs + CO-A + CARBON-DIOXIDE; direction=LEFT-TO-RIGHT

## Pathways

- `ecocyc.PWY-4381` fatty acid biosynthesis initiation (type II) (EcoCyc)

## Outgoing Edges (0)

_None._

## Incoming Edges (6)

- `catalyzes` <-- [[complex.ecocyc.CPLX0-252|complex.ecocyc.CPLX0-252]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00010|molecule.C00010]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00011|molecule.C00011]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00024|molecule.C00024]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `represses` <-- [[molecule.ecocyc.CPD0-1242|molecule.ecocyc.CPD0-1242]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity

## External IDs

- `EcoCyc:2.3.1.180-RXN`

## Notes

ACETYL-COA + MALONYL-ACP + PROTON -> Acetoacetyl-ACPs + CO-A + CARBON-DIOXIDE; direction=LEFT-TO-RIGHT
