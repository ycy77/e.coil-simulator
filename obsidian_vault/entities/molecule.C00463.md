---
entity_id: "molecule.C00463"
entity_type: "small_molecule"
name: "Indole"
source_database: "KEGG"
source_id: "C00463"
default_state: "low"
allowed_states: "absent|low|medium|high"
subcellular_location: ""
enriched_summary_quality: "placeholder"
tags:
  - entity/small_molecule
  - source/KEGG
aliases:
  - "Indole"
  - "2,3-Benzopyrrole"
---

# Indole

`molecule.C00463`

## Static

- Type: `small_molecule`
- Source: `KEGG:C00463`
- Default state: `low`
- Allowed states: `absent|low|medium|high`

## Enriched Summary

KEGG compound: Indole; 2,3-Benzopyrrole

## Biological Role

Consumed as substrate in 4 reaction(s). Produced in 7 reaction(s).

## Enriched Pathways

- `eco00380` Tryptophan metabolism (KEGG)
- `eco00400` Phenylalanine, tyrosine and tryptophan biosynthesis (KEGG)
- `eco00999` Biosynthesis of various plant secondary metabolites (KEGG)

## Annotation

KEGG compound: Indole; 2,3-Benzopyrrole

## Pathways

- `eco00380` Tryptophan metabolism (KEGG)
- `eco00400` Phenylalanine, tyrosine and tryptophan biosynthesis (KEGG)
- `eco00999` Biosynthesis of various plant secondary metabolites (KEGG)

## Outgoing Edges (11)

- `is_product_of` --> [[reaction.R00673|reaction.R00673]] `KEGG` `database` - C00078 + C00001 <=> C00463 + C00022 + C00014
- `is_product_of` --> [[reaction.R02340|reaction.R02340]] `KEGG` `database` - C03506 <=> C00463 + C00118
- `is_product_of` --> [[reaction.ecocyc.RXN-15578|reaction.ecocyc.RXN-15578]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.RXN0-2381|reaction.ecocyc.RXN0-2381]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.TRANS-RXN-142|reaction.ecocyc.TRANS-RXN-142]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.TRANS-RXN0-563|reaction.ecocyc.TRANS-RXN0-563]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.TRYPTOPHAN-RXN|reaction.ecocyc.TRYPTOPHAN-RXN]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` --> [[reaction.R00674|reaction.R00674]] `KEGG` `database` - C00065 + C00463 <=> C00078 + C00001
- `is_substrate_of` --> [[reaction.ecocyc.RXN0-2382|reaction.ecocyc.RXN0-2382]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.TRANS-RXN-142|reaction.ecocyc.TRANS-RXN-142]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.TRANS-RXN0-563|reaction.ecocyc.TRANS-RXN0-563]] `EcoCyc` `database` - EcoCyc reaction LEFT

## Incoming Edges (1)

- `transports` <-- [[protein.P0AAD2|protein.P0AAD2]] `EcoCyc` `database` - EcoCyc transporters.col equation

## External IDs

- `KEGG:C00463`

## Notes

Included because it appears in at least one E. coli KEGG pathway.
