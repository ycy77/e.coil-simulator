---
entity_id: "molecule.C03033"
entity_type: "small_molecule"
name: "beta-D-Glucuronoside"
source_database: "KEGG"
source_id: "C03033"
default_state: "low"
allowed_states: "absent|low|medium|high"
subcellular_location: ""
enriched_summary_quality: "placeholder"
tags:
  - entity/small_molecule
  - source/KEGG
aliases:
  - "beta-D-Glucuronoside"
  - "O-beta-D-Glucuronoside"
  - "Glucuronide"
  - "beta-D-Glucuronide"
---

# beta-D-Glucuronoside

`molecule.C03033`

## Static

- Type: `small_molecule`
- Source: `KEGG:C03033`
- Default state: `low`
- Allowed states: `absent|low|medium|high`

## Enriched Summary

KEGG compound: beta-D-Glucuronoside; O-beta-D-Glucuronoside; Glucuronide; beta-D-Glucuronide EcoCyc common name: a β-D-glucuronide.

## Biological Role

Consumed as substrate in 1 reaction(s).

## Enriched Pathways

- `eco00040` Pentose and glucuronate interconversions (KEGG)
- `eco00053` Ascorbate and aldarate metabolism (KEGG)

## Annotation

KEGG compound: beta-D-Glucuronoside; O-beta-D-Glucuronoside; Glucuronide; beta-D-Glucuronide

## Pathways

- `eco00040` Pentose and glucuronate interconversions (KEGG)
- `eco00053` Ascorbate and aldarate metabolism (KEGG)

## Outgoing Edges (1)

- `is_substrate_of` --> [[reaction.ecocyc.BETA-GLUCURONID-RXN|reaction.ecocyc.BETA-GLUCURONID-RXN]] `EcoCyc` `database` - EcoCyc reaction LEFT

## Incoming Edges (1)

- `transports` <-- [[protein.P0CE44|protein.P0CE44]] `EcoCyc` `database` - EcoCyc transporters.col equation

## External IDs

- `KEGG:C03033`

## Notes

Included because it appears in at least one E. coli KEGG pathway.
