---
entity_id: "reaction.ecocyc.ADENYL-KIN-RXN"
entity_type: "reaction"
name: "ADENYL-KIN-RXN"
source_database: "EcoCyc"
source_id: "ADENYL-KIN-RXN"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# ADENYL-KIN-RXN

`reaction.ecocyc.ADENYL-KIN-RXN`

## Static

- Type: `reaction`
- Source: `EcoCyc:ADENYL-KIN-RXN`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

This reaction interconverts adenine nucleotides. EcoCyc reaction equation: AMP + ATP -> ADP; direction=REVERSIBLE. This reaction interconverts adenine nucleotides.

## Biological Role

Catalyzed by adk (protein.P69441). Substrates: ATP (molecule.C00002), AMP (molecule.C00020). Products: ADP (molecule.C00008).

## Enriched Pathways

- `ecocyc.PWY-7219` adenosine ribonucleotides de novo biosynthesis (EcoCyc)

## Annotation

This reaction interconverts adenine nucleotides.

## Pathways

- `ecocyc.PWY-7219` adenosine ribonucleotides de novo biosynthesis (EcoCyc)

## Outgoing Edges (0)

_None._

## Incoming Edges (8)

- `activates` <-- [[molecule.C00305|molecule.C00305]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `catalyzes` <-- [[protein.P69441|protein.P69441]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00008|molecule.C00008]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00002|molecule.C00002]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C00020|molecule.C00020]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `represses` <-- [[molecule.ecocyc.CPD0-1137|molecule.ecocyc.CPD0-1137]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.ecocyc.CPD0-1552|molecule.ecocyc.CPD0-1552]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[protein.P0AA04|protein.P0AA04]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity

## External IDs

- `EcoCyc:ADENYL-KIN-RXN`

## Notes

AMP + ATP -> ADP; direction=REVERSIBLE
