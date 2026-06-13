---
entity_id: "molecule.C00957"
entity_type: "small_molecule"
name: "Mercaptopyruvate"
source_database: "KEGG"
source_id: "C00957"
default_state: "low"
allowed_states: "absent|low|medium|high"
subcellular_location: ""
enriched_summary_quality: "placeholder"
tags:
  - entity/small_molecule
  - source/KEGG
aliases:
  - "Mercaptopyruvate"
  - "2-Oxo-3-sulfanylpropanoate"
  - "3-Mercaptopyruvic acid"
  - "3-Mercaptopyruvate"
---

# Mercaptopyruvate

`molecule.C00957`

## Static

- Type: `small_molecule`
- Source: `KEGG:C00957`
- Default state: `low`
- Allowed states: `absent|low|medium|high`

## Enriched Summary

KEGG compound: Mercaptopyruvate; 2-Oxo-3-sulfanylpropanoate; 3-Mercaptopyruvic acid; 3-Mercaptopyruvate EcoCyc common name: 2-oxo-3-sulfanylpropanoate.

## Biological Role

Consumed as substrate in 2 reaction(s). Produced in 1 reaction(s).

## Enriched Pathways

- `eco00270` Cysteine and methionine metabolism (KEGG)

## Annotation

KEGG compound: Mercaptopyruvate; 2-Oxo-3-sulfanylpropanoate; 3-Mercaptopyruvic acid; 3-Mercaptopyruvate

## Pathways

- `eco00270` Cysteine and methionine metabolism (KEGG)

## Outgoing Edges (3)

- `is_product_of` --> [[reaction.ecocyc.CYSTEINE-AMINOTRANSFERASE-RXN|reaction.ecocyc.CYSTEINE-AMINOTRANSFERASE-RXN]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` --> [[reaction.ecocyc.MERCAPYSTRANS-RXN|reaction.ecocyc.MERCAPYSTRANS-RXN]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.RXN-18702|reaction.ecocyc.RXN-18702]] `EcoCyc` `database` - EcoCyc reaction LEFT

## Incoming Edges (0)

_None._

## External IDs

- `KEGG:C00957`

## Notes

Included because it appears in at least one E. coli KEGG pathway.
