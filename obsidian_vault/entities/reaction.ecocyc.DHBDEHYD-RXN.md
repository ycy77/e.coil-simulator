---
entity_id: "reaction.ecocyc.DHBDEHYD-RXN"
entity_type: "reaction"
name: "DHBDEHYD-RXN"
source_database: "EcoCyc"
source_id: "DHBDEHYD-RXN"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# DHBDEHYD-RXN

`reaction.ecocyc.DHBDEHYD-RXN`

## Static

- Type: `reaction`
- Source: `EcoCyc:DHBDEHYD-RXN`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

This is the third reaction in the enterobactin biosynthetic pathway. The reaction synthesizes 2,3-dihydroxybenzoate which is the substrate along with serine in the second part of the pathway. EcoCyc reaction equation: NAD + DIHYDRO-DIOH-BENZOATE -> PROTON + NADH + 2-3-DIHYDROXYBENZOATE; direction=LEFT-TO-RIGHT. This is the third reaction in the enterobactin biosynthetic pathway. The reaction synthesizes 2,3-dihydroxybenzoate which is the substrate along with serine in the second part of the pathway.

## Biological Role

Catalyzed by 2,3-dihydro-2,3-dihydroxybenzoate dehydrogenase (complex.ecocyc.ENTA-CPLX). Substrates: NAD+ (molecule.C00003), (2S,3S)-2,3-Dihydro-2,3-dihydroxybenzoate (molecule.C04171). Products: NADH (molecule.C00004), H+ (molecule.C00080), 2,3-Dihydroxybenzoate (molecule.C00196).

## Enriched Pathways

- `ecocyc.PWY-5901` 2,3-dihydroxybenzoate biosynthesis (EcoCyc)

## Annotation

This is the third reaction in the enterobactin biosynthetic pathway. The reaction synthesizes 2,3-dihydroxybenzoate which is the substrate along with serine in the second part of the pathway.

## Pathways

- `ecocyc.PWY-5901` 2,3-dihydroxybenzoate biosynthesis (EcoCyc)

## Outgoing Edges (0)

_None._

## Incoming Edges (6)

- `catalyzes` <-- [[complex.ecocyc.ENTA-CPLX|complex.ecocyc.ENTA-CPLX]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00004|molecule.C00004]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00196|molecule.C00196]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00003|molecule.C00003]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C04171|molecule.C04171]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:DHBDEHYD-RXN`

## Notes

NAD + DIHYDRO-DIOH-BENZOATE -> PROTON + NADH + 2-3-DIHYDROXYBENZOATE; direction=LEFT-TO-RIGHT
