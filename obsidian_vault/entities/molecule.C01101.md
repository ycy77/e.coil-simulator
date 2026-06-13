---
entity_id: "molecule.C01101"
entity_type: "small_molecule"
name: "L-Ribulose 5-phosphate"
source_database: "KEGG"
source_id: "C01101"
default_state: "low"
allowed_states: "absent|low|medium|high"
subcellular_location: ""
enriched_summary_quality: "placeholder"
tags:
  - entity/small_molecule
  - source/KEGG
aliases:
  - "L-Ribulose 5-phosphate"
---

# L-Ribulose 5-phosphate

`molecule.C01101`

## Static

- Type: `small_molecule`
- Source: `KEGG:C01101`
- Default state: `low`
- Allowed states: `absent|low|medium|high`

## Enriched Summary

KEGG compound: L-Ribulose 5-phosphate

## Biological Role

Consumed as substrate in 3 reaction(s). Produced in 1 reaction(s).

## Enriched Pathways

- `eco00040` Pentose and glucuronate interconversions (KEGG)
- `eco00053` Ascorbate and aldarate metabolism (KEGG)

## Annotation

KEGG compound: L-Ribulose 5-phosphate

## Pathways

- `eco00040` Pentose and glucuronate interconversions (KEGG)
- `eco00053` Ascorbate and aldarate metabolism (KEGG)

## Outgoing Edges (4)

- `is_product_of` --> [[reaction.ecocyc.RXN0-5116|reaction.ecocyc.RXN0-5116]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` --> [[reaction.R05850|reaction.R05850]] `KEGG` `database` - C01101 <=> C00231
- `is_substrate_of` --> [[reaction.ecocyc.LXULRU5P-RXN|reaction.ecocyc.LXULRU5P-RXN]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.RIBULPEPIM-RXN|reaction.ecocyc.RIBULPEPIM-RXN]] `EcoCyc` `database` - EcoCyc reaction LEFT

## Incoming Edges (0)

_None._

## External IDs

- `KEGG:C01101`

## Notes

Included because it appears in at least one E. coli KEGG pathway.
