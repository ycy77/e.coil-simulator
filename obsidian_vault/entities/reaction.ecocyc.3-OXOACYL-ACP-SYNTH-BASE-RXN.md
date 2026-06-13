---
entity_id: "reaction.ecocyc.3-OXOACYL-ACP-SYNTH-BASE-RXN"
entity_type: "reaction"
name: "3-OXOACYL-ACP-SYNTH-BASE-RXN"
source_database: "EcoCyc"
source_id: "3-OXOACYL-ACP-SYNTH-BASE-RXN"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# 3-OXOACYL-ACP-SYNTH-BASE-RXN

`reaction.ecocyc.3-OXOACYL-ACP-SYNTH-BASE-RXN`

## Static

- Type: `reaction`
- Source: `EcoCyc:3-OXOACYL-ACP-SYNTH-BASE-RXN`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

This reaction is involved in the elongation of fatty acids. EcoCyc reaction equation: MALONYL-ACP + ACETYL-ACP + PROTON -> ACP + Acetoacetyl-ACPs + CARBON-DIOXIDE; direction=PHYSIOL-LEFT-TO-RIGHT. This reaction is involved in the elongation of fatty acids.

## Biological Role

Catalyzed by 3-oxoacyl-[acyl carrier protein] synthase 2 (complex.ecocyc.3-OXOACYL-ACP-SYNTHII-CPLX), 3-oxoacyl-[acyl carrier protein] synthase 1 (complex.ecocyc.FABB-CPLX). Substrates: H+ (molecule.C00080). Products: CO2 (molecule.C00011).

## Enriched Pathways

- `ecocyc.PWY-5965` fatty acid biosynthesis initiation III (EcoCyc)
- `ecocyc.PWY-5966` fatty acid biosynthesis initiation II (EcoCyc)

## Annotation

This reaction is involved in the elongation of fatty acids.

## Pathways

- `ecocyc.PWY-5965` fatty acid biosynthesis initiation III (EcoCyc)
- `ecocyc.PWY-5966` fatty acid biosynthesis initiation II (EcoCyc)

## Outgoing Edges (0)

_None._

## Incoming Edges (7)

- `catalyzes` <-- [[complex.ecocyc.3-OXOACYL-ACP-SYNTHII-CPLX|complex.ecocyc.3-OXOACYL-ACP-SYNTHII-CPLX]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` <-- [[complex.ecocyc.FABB-CPLX|complex.ecocyc.FABB-CPLX]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00011|molecule.C00011]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `represses` <-- [[molecule.ecocyc.CPD-6901|molecule.ecocyc.CPD-6901]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.ecocyc.CPD0-1242|molecule.ecocyc.CPD0-1242]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.ecocyc.IODOACETAMIDE|molecule.ecocyc.IODOACETAMIDE]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity

## External IDs

- `EcoCyc:3-OXOACYL-ACP-SYNTH-BASE-RXN`

## Notes

MALONYL-ACP + ACETYL-ACP + PROTON -> ACP + Acetoacetyl-ACPs + CARBON-DIOXIDE; direction=PHYSIOL-LEFT-TO-RIGHT
