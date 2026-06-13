---
entity_id: "molecule.C01013"
entity_type: "small_molecule"
name: "3-Hydroxypropanoate"
source_database: "KEGG"
source_id: "C01013"
default_state: "low"
allowed_states: "absent|low|medium|high"
subcellular_location: ""
enriched_summary_quality: "placeholder"
tags:
  - entity/small_molecule
  - source/KEGG
aliases:
  - "3-Hydroxypropanoate"
  - "3-Hydroxypropanoic acid"
  - "3-Hydroxypropionate"
  - "3-Hydroxypropionic acid"
  - "Hydracrylic acid"
---

# 3-Hydroxypropanoate

`molecule.C01013`

## Static

- Type: `small_molecule`
- Source: `KEGG:C01013`
- Default state: `low`
- Allowed states: `absent|low|medium|high`

## Enriched Summary

KEGG compound: 3-Hydroxypropanoate; 3-Hydroxypropanoic acid; 3-Hydroxypropionate; 3-Hydroxypropionic acid; Hydracrylic acid

## Biological Role

Consumed as substrate in 2 reaction(s). Produced in 2 reaction(s).

## Enriched Pathways

- `eco00240` Pyrimidine metabolism (KEGG)
- `eco00410` beta-Alanine metabolism (KEGG)
- `eco00640` Propanoate metabolism (KEGG)
- `eco00720` Other carbon fixation pathways (KEGG)
- `eco00920` Sulfur metabolism (KEGG)

## Annotation

KEGG compound: 3-Hydroxypropanoate; 3-Hydroxypropanoic acid; 3-Hydroxypropionate; 3-Hydroxypropionic acid; Hydracrylic acid

## Pathways

- `eco00240` Pyrimidine metabolism (KEGG)
- `eco00410` beta-Alanine metabolism (KEGG)
- `eco00640` Propanoate metabolism (KEGG)
- `eco00720` Other carbon fixation pathways (KEGG)
- `eco00920` Sulfur metabolism (KEGG)

## Outgoing Edges (4)

- `is_product_of` --> [[reaction.ecocyc.RXN0-5455|reaction.ecocyc.RXN0-5455]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.TRANS-RXN0-465|reaction.ecocyc.TRANS-RXN0-465]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` --> [[reaction.ecocyc.RXN-8974|reaction.ecocyc.RXN-8974]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.TRANS-RXN0-465|reaction.ecocyc.TRANS-RXN0-465]] `EcoCyc` `database` - EcoCyc reaction LEFT

## Incoming Edges (0)

_None._

## External IDs

- `KEGG:C01013`

## Notes

Included because it appears in at least one E. coli KEGG pathway.
