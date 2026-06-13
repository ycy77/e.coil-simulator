---
entity_id: "reaction.ecocyc.RXN-11479"
entity_type: "reaction"
name: "RXN-11479"
source_database: "EcoCyc"
source_id: "RXN-11479"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN-11479

`reaction.ecocyc.RXN-11479`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN-11479`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

Glutaryl-ACP-methyl-esters + MALONYL-ACP + PROTON -> 3-Ketopimeloyl-ACP-methyl-esters + CARBON-DIOXIDE + ACP; direction=LEFT-TO-RIGHT EcoCyc reaction equation: Glutaryl-ACP-methyl-esters + MALONYL-ACP + PROTON -> 3-Ketopimeloyl-ACP-methyl-esters + CARBON-DIOXIDE + ACP; direction=LEFT-TO-RIGHT.

## Biological Role

Catalyzed by 3-oxoacyl-[acyl carrier protein] synthase 2 (complex.ecocyc.3-OXOACYL-ACP-SYNTHII-CPLX), 3-oxoacyl-[acyl carrier protein] synthase 1 (complex.ecocyc.FABB-CPLX). Substrates: H+ (molecule.C00080). Products: CO2 (molecule.C00011).

## Enriched Pathways

- `ecocyc.PWY-6519` 8-amino-7-oxononanoate biosynthesis I (EcoCyc)

## Annotation

Glutaryl-ACP-methyl-esters + MALONYL-ACP + PROTON -> 3-Ketopimeloyl-ACP-methyl-esters + CARBON-DIOXIDE + ACP; direction=LEFT-TO-RIGHT

## Pathways

- `ecocyc.PWY-6519` 8-amino-7-oxononanoate biosynthesis I (EcoCyc)

## Outgoing Edges (0)

_None._

## Incoming Edges (6)

- `catalyzes` <-- [[complex.ecocyc.3-OXOACYL-ACP-SYNTHII-CPLX|complex.ecocyc.3-OXOACYL-ACP-SYNTHII-CPLX]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` <-- [[complex.ecocyc.FABB-CPLX|complex.ecocyc.FABB-CPLX]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00011|molecule.C00011]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `represses` <-- [[molecule.ecocyc.CPD-6901|molecule.ecocyc.CPD-6901]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.ecocyc.CPD0-1242|molecule.ecocyc.CPD0-1242]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity

## External IDs

- `EcoCyc:RXN-11479`

## Notes

Glutaryl-ACP-methyl-esters + MALONYL-ACP + PROTON -> 3-Ketopimeloyl-ACP-methyl-esters + CARBON-DIOXIDE + ACP; direction=LEFT-TO-RIGHT
