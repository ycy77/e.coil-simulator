---
entity_id: "molecule.C20959"
entity_type: "small_molecule"
name: "(4S)-4-Hydroxy-5-phosphooxypentane-2,3-dione"
source_database: "KEGG"
source_id: "C20959"
default_state: "low"
allowed_states: "absent|low|medium|high"
subcellular_location: ""
enriched_summary_quality: "placeholder"
tags:
  - entity/small_molecule
  - source/KEGG
aliases:
  - "(4S)-4-Hydroxy-5-phosphooxypentane-2,3-dione"
  - "(4S)-4-Hydroxy-5-phosphonooxypentane-2,3-dione"
  - "Phospho-DPD"
  - "P-DPD"
  - "(2S)-2-Hydroxy-3,4-dioxopentyl phosphate"
  - "Phospho-AI-2"
---

# (4S)-4-Hydroxy-5-phosphooxypentane-2,3-dione

`molecule.C20959`

## Static

- Type: `small_molecule`
- Source: `KEGG:C20959`
- Default state: `low`
- Allowed states: `absent|low|medium|high`

## Enriched Summary

KEGG compound: (4S)-4-Hydroxy-5-phosphooxypentane-2,3-dione; (4S)-4-Hydroxy-5-phosphonooxypentane-2,3-dione; Phospho-DPD; P-DPD; (2S)-2-Hydroxy-3,4-dioxopentyl phosphate; Phospho-AI-2 EcoCyc common name: (2S)-2-hydroxy-3,4-dioxopentyl phosphate. This compound is a C5-phosphorylated derivative of the open form of DIHYDROXYPENTANEDIONE .

## Biological Role

Consumed as substrate in 2 reaction(s). Produced in 1 reaction(s).

## Enriched Pathways

- `eco02024` Quorum sensing (KEGG)

## Annotation

KEGG compound: (4S)-4-Hydroxy-5-phosphooxypentane-2,3-dione; (4S)-4-Hydroxy-5-phosphonooxypentane-2,3-dione; Phospho-DPD; P-DPD; (2S)-2-Hydroxy-3,4-dioxopentyl phosphate; Phospho-AI-2

## Pathways

- `eco02024` Quorum sensing (KEGG)

## Outgoing Edges (4)

- `is_component_of` --> [[complex.ecocyc.CPLX0-7750|complex.ecocyc.CPLX0-7750]] `EcoCyc` `database` - EcoCyc component coefficient=
- `is_product_of` --> [[reaction.ecocyc.RXN0-5461|reaction.ecocyc.RXN0-5461]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` --> [[reaction.R10939|reaction.R10939]] `KEGG` `database` - C20959 <=> C20960
- `is_substrate_of` --> [[reaction.ecocyc.RXN-15216|reaction.ecocyc.RXN-15216]] `EcoCyc` `database` - EcoCyc reaction LEFT

## Incoming Edges (0)

_None._

## External IDs

- `KEGG:C20959`

## Notes

Included because it appears in at least one E. coli KEGG pathway.
