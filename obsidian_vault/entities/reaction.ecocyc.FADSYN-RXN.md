---
entity_id: "reaction.ecocyc.FADSYN-RXN"
entity_type: "reaction"
name: "FADSYN-RXN"
source_database: "EcoCyc"
source_id: "FADSYN-RXN"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# FADSYN-RXN

`reaction.ecocyc.FADSYN-RXN`

## Static

- Type: `reaction`
- Source: `EcoCyc:FADSYN-RXN`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

This reaction produces FAD from FMN. EcoCyc reaction equation: FMN + ATP + PROTON -> FAD + PPI; direction=REVERSIBLE. This reaction produces FAD from FMN.

## Biological Role

Catalyzed by ribF (protein.P0AG40). Substrates: ATP (molecule.C00002), FMN (molecule.C00061), H+ (molecule.C00080). Products: Diphosphate (molecule.C00013), FAD (molecule.C00016).

## Enriched Pathways

- `ecocyc.RIBOSYN2-PWY` flavin biosynthesis I (bacteria and plants) (EcoCyc)

## Annotation

This reaction produces FAD from FMN.

## Pathways

- `ecocyc.RIBOSYN2-PWY` flavin biosynthesis I (bacteria and plants) (EcoCyc)

## Outgoing Edges (0)

_None._

## Incoming Edges (6)

- `catalyzes` <-- [[protein.P0AG40|protein.P0AG40]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00013|molecule.C00013]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00016|molecule.C00016]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00002|molecule.C00002]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C00061|molecule.C00061]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:FADSYN-RXN`

## Notes

FMN + ATP + PROTON -> FAD + PPI; direction=REVERSIBLE
