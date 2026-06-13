---
entity_id: "molecule.C00805"
entity_type: "small_molecule"
name: "Salicylate"
source_database: "KEGG"
source_id: "C00805"
default_state: "low"
allowed_states: "absent|low|medium|high"
subcellular_location: ""
enriched_summary_quality: "placeholder"
tags:
  - entity/small_molecule
  - source/KEGG
aliases:
  - "Salicylate"
  - "o-Hydroxybenzoic acid"
  - "Salicylic acid"
---

# Salicylate

`molecule.C00805`

## Static

- Type: `small_molecule`
- Source: `KEGG:C00805`
- Default state: `low`
- Allowed states: `absent|low|medium|high`

## Enriched Summary

KEGG compound: Salicylate; o-Hydroxybenzoic acid; Salicylic acid Salicylate is widely used in organic synthesis and functions as a plant hormone. The source of the name CPD-110 (salicylic acid) comes from the name of the willow tree, TAX-40685, from whose bark it can be obtained.

## Biological Role

Consumed as substrate in 2 reaction(s).

## Enriched Pathways

- `eco00621` Dioxin degradation (KEGG)
- `eco00626` Naphthalene degradation (KEGG)
- `eco01053` Biosynthesis of siderophore group nonribosomal peptides (KEGG)

## Annotation

KEGG compound: Salicylate; o-Hydroxybenzoic acid; Salicylic acid

## Pathways

- `eco00621` Dioxin degradation (KEGG)
- `eco00626` Naphthalene degradation (KEGG)
- `eco01053` Biosynthesis of siderophore group nonribosomal peptides (KEGG)

## Outgoing Edges (5)

- `is_component_of` --> [[complex.ecocyc.CPLX0-8579|complex.ecocyc.CPLX0-8579]] `EcoCyc` `database` - EcoCyc component coefficient=
- `is_component_of` --> [[complex.ecocyc.MONOMER-58|complex.ecocyc.MONOMER-58]] `EcoCyc` `database` - EcoCyc component coefficient=
- `is_substrate_of` --> [[reaction.ecocyc.RXN0-290|reaction.ecocyc.RXN0-290]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.RXN0-7384|reaction.ecocyc.RXN0-7384]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `represses` --> [[reaction.ecocyc.ARYLAMINE-N-ACETYLTRANSFERASE-RXN|reaction.ecocyc.ARYLAMINE-N-ACETYLTRANSFERASE-RXN]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity

## Incoming Edges (0)

_None._

## External IDs

- `KEGG:C00805`

## Notes

Included because it appears in at least one E. coli KEGG pathway.
