---
entity_id: "molecule.C00921"
entity_type: "small_molecule"
name: "Dihydropteroate"
source_database: "KEGG"
source_id: "C00921"
default_state: "low"
allowed_states: "absent|low|medium|high"
subcellular_location: ""
enriched_summary_quality: "placeholder"
tags:
  - entity/small_molecule
  - source/KEGG
aliases:
  - "Dihydropteroate"
  - "7,8-Dihydropteroate"
---

# Dihydropteroate

`molecule.C00921`

## Static

- Type: `small_molecule`
- Source: `KEGG:C00921`
- Default state: `low`
- Allowed states: `absent|low|medium|high`

## Enriched Summary

KEGG compound: Dihydropteroate; 7,8-Dihydropteroate EcoCyc common name: 7,8-dihydropteroate.

## Biological Role

Consumed as substrate in 1 reaction(s). Produced in 1 reaction(s).

## Enriched Pathways

- `eco00790` Folate biosynthesis (KEGG)

## Annotation

KEGG compound: Dihydropteroate; 7,8-Dihydropteroate

## Pathways

- `eco00790` Folate biosynthesis (KEGG)

## Outgoing Edges (4)

- `is_product_of` --> [[reaction.ecocyc.H2PTEROATESYNTH-RXN|reaction.ecocyc.H2PTEROATESYNTH-RXN]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` --> [[reaction.ecocyc.DIHYDROFOLATESYNTH-RXN|reaction.ecocyc.DIHYDROFOLATESYNTH-RXN]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `represses` --> [[reaction.ecocyc.FOLYLPOLYGLUTAMATESYNTH-RXN|reaction.ecocyc.FOLYLPOLYGLUTAMATESYNTH-RXN]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` --> [[reaction.ecocyc.H2PTEROATESYNTH-RXN|reaction.ecocyc.H2PTEROATESYNTH-RXN]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity

## Incoming Edges (0)

_None._

## External IDs

- `KEGG:C00921`

## Notes

Included because it appears in at least one E. coli KEGG pathway.
