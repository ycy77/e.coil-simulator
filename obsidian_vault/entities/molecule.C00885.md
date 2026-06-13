---
entity_id: "molecule.C00885"
entity_type: "small_molecule"
name: "Isochorismate"
source_database: "KEGG"
source_id: "C00885"
default_state: "low"
allowed_states: "absent|low|medium|high"
subcellular_location: ""
enriched_summary_quality: "placeholder"
tags:
  - entity/small_molecule
  - source/KEGG
aliases:
  - "Isochorismate"
  - "Isochorismic acid"
---

# Isochorismate

`molecule.C00885`

## Static

- Type: `small_molecule`
- Source: `KEGG:C00885`
- Default state: `low`
- Allowed states: `absent|low|medium|high`

## Enriched Summary

KEGG compound: Isochorismate; Isochorismic acid

## Biological Role

Consumed as substrate in 2 reaction(s). Produced in 1 reaction(s).

## Enriched Pathways

- `eco00130` Ubiquinone and other terpenoid-quinone biosynthesis (KEGG)
- `eco01053` Biosynthesis of siderophore group nonribosomal peptides (KEGG)

## Annotation

KEGG compound: Isochorismate; Isochorismic acid

## Pathways

- `eco00130` Ubiquinone and other terpenoid-quinone biosynthesis (KEGG)
- `eco01053` Biosynthesis of siderophore group nonribosomal peptides (KEGG)

## Outgoing Edges (3)

- `is_product_of` --> [[reaction.ecocyc.ISOCHORSYN-RXN|reaction.ecocyc.ISOCHORSYN-RXN]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` --> [[reaction.ecocyc.2.5.1.64-RXN|reaction.ecocyc.2.5.1.64-RXN]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.ISOCHORMAT-RXN|reaction.ecocyc.ISOCHORMAT-RXN]] `EcoCyc` `database` - EcoCyc reaction LEFT

## Incoming Edges (0)

_None._

## External IDs

- `KEGG:C00885`

## Notes

Included because it appears in at least one E. coli KEGG pathway.
