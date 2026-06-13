---
entity_id: "molecule.C00179"
entity_type: "small_molecule"
name: "Agmatine"
source_database: "KEGG"
source_id: "C00179"
default_state: "low"
allowed_states: "absent|low|medium|high"
subcellular_location: ""
enriched_summary_quality: "placeholder"
tags:
  - entity/small_molecule
  - source/KEGG
aliases:
  - "Agmatine"
  - "(4-Aminobutyl) guanidine"
---

# Agmatine

`molecule.C00179`

## Static

- Type: `small_molecule`
- Source: `KEGG:C00179`
- Default state: `low`
- Allowed states: `absent|low|medium|high`

## Enriched Summary

KEGG compound: Agmatine; (4-Aminobutyl) guanidine

## Biological Role

Consumed as substrate in 3 reaction(s). Produced in 3 reaction(s).

## Enriched Pathways

- `eco00330` Arginine and proline metabolism (KEGG)
- `eco00999` Biosynthesis of various plant secondary metabolites (KEGG)

## Annotation

KEGG compound: Agmatine; (4-Aminobutyl) guanidine

## Pathways

- `eco00330` Arginine and proline metabolism (KEGG)
- `eco00999` Biosynthesis of various plant secondary metabolites (KEGG)

## Outgoing Edges (6)

- `is_product_of` --> [[reaction.R00566|reaction.R00566]] `KEGG` `database` - C00062 <=> C00179 + C00011
- `is_product_of` --> [[reaction.ecocyc.ARGDECARBOX-RXN|reaction.ecocyc.ARGDECARBOX-RXN]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.RXN0-2162|reaction.ecocyc.RXN0-2162]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` --> [[reaction.R01157|reaction.R01157]] `KEGG` `database` - C00179 + C00001 <=> C00134 + C00086
- `is_substrate_of` --> [[reaction.ecocyc.AGMATIN-RXN|reaction.ecocyc.AGMATIN-RXN]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.RXN0-2162|reaction.ecocyc.RXN0-2162]] `EcoCyc` `database` - EcoCyc reaction LEFT

## Incoming Edges (1)

- `transports` <-- [[complex.ecocyc.CPLX0-7535|complex.ecocyc.CPLX0-7535]] `EcoCyc` `database` - EcoCyc transporters.col equation

## External IDs

- `KEGG:C00179`

## Notes

Included because it appears in at least one E. coli KEGG pathway.
