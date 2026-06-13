---
entity_id: "reaction.ecocyc.1.1.1.283-RXN"
entity_type: "reaction"
name: "1.1.1.283-RXN"
source_database: "EcoCyc"
source_id: "1.1.1.283-RXN"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# 1.1.1.283-RXN

`reaction.ecocyc.1.1.1.283-RXN`

## Static

- Type: `reaction`
- Source: `EcoCyc:1.1.1.283-RXN`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

LACTALD + NADP -> METHYL-GLYOXAL + NADPH + PROTON; direction=RIGHT-TO-LEFT EcoCyc reaction equation: LACTALD + NADP -> METHYL-GLYOXAL + NADPH + PROTON; direction=RIGHT-TO-LEFT.

## Biological Role

Catalyzed by METHYLGLYREDUCT-MONOMER (protein.ecocyc.METHYLGLYREDUCT-MONOMER). Substrates: NADP+ (molecule.C00006), (S)-Lactaldehyde (molecule.C00424). Products: NADPH (molecule.C00005), H+ (molecule.C00080), Methylglyoxal (molecule.C00546).

## Enriched Pathways

- `ecocyc.PWY-5459` methylglyoxal degradation IV (EcoCyc)

## Annotation

LACTALD + NADP -> METHYL-GLYOXAL + NADPH + PROTON; direction=RIGHT-TO-LEFT

## Pathways

- `ecocyc.PWY-5459` methylglyoxal degradation IV (EcoCyc)

## Outgoing Edges (0)

_None._

## Incoming Edges (14)

- `activates` <-- [[molecule.C00051|molecule.C00051]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `activates` <-- [[molecule.ecocyc.2-MERCAPTOETHANOL|molecule.ecocyc.2-MERCAPTOETHANOL]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `activates` <-- [[molecule.ecocyc.DITHIOTHREITOL|molecule.ecocyc.DITHIOTHREITOL]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `catalyzes` <-- [[protein.ecocyc.METHYLGLYREDUCT-MONOMER|protein.ecocyc.METHYLGLYREDUCT-MONOMER]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00005|molecule.C00005]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00546|molecule.C00546]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00006|molecule.C00006]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C00424|molecule.C00424]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `represses` <-- [[molecule.C00038|molecule.C00038]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.C00175|molecule.C00175]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.C19609|molecule.C19609]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.ecocyc.CPD-29|molecule.ecocyc.CPD-29]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.ecocyc.CU_2|molecule.ecocyc.CU_2]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity

## External IDs

- `EcoCyc:1.1.1.283-RXN`

## Notes

LACTALD + NADP -> METHYL-GLYOXAL + NADPH + PROTON; direction=RIGHT-TO-LEFT
