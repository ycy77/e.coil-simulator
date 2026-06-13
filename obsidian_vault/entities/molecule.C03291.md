---
entity_id: "molecule.C03291"
entity_type: "small_molecule"
name: "L-Xylulose 5-phosphate"
source_database: "KEGG"
source_id: "C03291"
default_state: "low"
allowed_states: "absent|low|medium|high"
subcellular_location: ""
enriched_summary_quality: "placeholder"
tags:
  - entity/small_molecule
  - source/KEGG
aliases:
  - "L-Xylulose 5-phosphate"
---

# L-Xylulose 5-phosphate

`molecule.C03291`

## Static

- Type: `small_molecule`
- Source: `KEGG:C03291`
- Default state: `low`
- Allowed states: `absent|low|medium|high`

## Enriched Summary

KEGG compound: L-Xylulose 5-phosphate

## Biological Role

Produced in 4 reaction(s).

## Enriched Pathways

- `eco00040` Pentose and glucuronate interconversions (KEGG)
- `eco00053` Ascorbate and aldarate metabolism (KEGG)

## Annotation

KEGG compound: L-Xylulose 5-phosphate

## Pathways

- `eco00040` Pentose and glucuronate interconversions (KEGG)
- `eco00053` Ascorbate and aldarate metabolism (KEGG)

## Outgoing Edges (4)

- `is_product_of` --> [[reaction.R01901|reaction.R01901]] `KEGG` `database` - C00002 + C00312 <=> C00008 + C03291
- `is_product_of` --> [[reaction.ecocyc.LXULRU5P-RXN|reaction.ecocyc.LXULRU5P-RXN]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.LYXK-RXN|reaction.ecocyc.LYXK-RXN]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.RXN0-705|reaction.ecocyc.RXN0-705]] `EcoCyc` `database` - EcoCyc reaction RIGHT

## Incoming Edges (0)

_None._

## External IDs

- `KEGG:C03291`

## Notes

Included because it appears in at least one E. coli KEGG pathway.
