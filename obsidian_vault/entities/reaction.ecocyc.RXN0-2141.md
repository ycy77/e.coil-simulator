---
entity_id: "reaction.ecocyc.RXN0-2141"
entity_type: "reaction"
name: "RXN0-2141"
source_database: "EcoCyc"
source_id: "RXN0-2141"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN0-2141

`reaction.ecocyc.RXN0-2141`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN0-2141`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

Cis-delta-3-decenoyl-ACPs + MALONYL-ACP + PROTON -> b-Keto-cis-D5-dodecenoyl-ACPs + ACP + CARBON-DIOXIDE; direction=PHYSIOL-LEFT-TO-RIGHT EcoCyc reaction equation: Cis-delta-3-decenoyl-ACPs + MALONYL-ACP + PROTON -> b-Keto-cis-D5-dodecenoyl-ACPs + ACP + CARBON-DIOXIDE; direction=PHYSIOL-LEFT-TO-RIGHT.

## Biological Role

Catalyzed by 3-oxoacyl-[acyl carrier protein] synthase 1 (complex.ecocyc.FABB-CPLX). Substrates: H+ (molecule.C00080). Products: CO2 (molecule.C00011).

## Enriched Pathways

- `ecocyc.PWY0-862` (5Z)-dodecenoate biosynthesis I (EcoCyc)

## Annotation

Cis-delta-3-decenoyl-ACPs + MALONYL-ACP + PROTON -> b-Keto-cis-D5-dodecenoyl-ACPs + ACP + CARBON-DIOXIDE; direction=PHYSIOL-LEFT-TO-RIGHT

## Pathways

- `ecocyc.PWY0-862` (5Z)-dodecenoate biosynthesis I (EcoCyc)

## Outgoing Edges (0)

_None._

## Incoming Edges (3)

- `catalyzes` <-- [[complex.ecocyc.FABB-CPLX|complex.ecocyc.FABB-CPLX]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00011|molecule.C00011]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN0-2141`

## Notes

Cis-delta-3-decenoyl-ACPs + MALONYL-ACP + PROTON -> b-Keto-cis-D5-dodecenoyl-ACPs + ACP + CARBON-DIOXIDE; direction=PHYSIOL-LEFT-TO-RIGHT
