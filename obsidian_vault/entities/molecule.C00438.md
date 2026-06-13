---
entity_id: "molecule.C00438"
entity_type: "small_molecule"
name: "N-Carbamoyl-L-aspartate"
source_database: "KEGG"
source_id: "C00438"
default_state: "low"
allowed_states: "absent|low|medium|high"
subcellular_location: ""
enriched_summary_quality: "placeholder"
tags:
  - entity/small_molecule
  - source/KEGG
aliases:
  - "N-Carbamoyl-L-aspartate"
---

# N-Carbamoyl-L-aspartate

`molecule.C00438`

## Static

- Type: `small_molecule`
- Source: `KEGG:C00438`
- Default state: `low`
- Allowed states: `absent|low|medium|high`

## Enriched Summary

KEGG compound: N-Carbamoyl-L-aspartate

## Biological Role

Produced in 2 reaction(s).

## Enriched Pathways

- `eco00240` Pyrimidine metabolism (KEGG)
- `eco00250` Alanine, aspartate and glutamate metabolism (KEGG)

## Annotation

KEGG compound: N-Carbamoyl-L-aspartate

## Pathways

- `eco00240` Pyrimidine metabolism (KEGG)
- `eco00250` Alanine, aspartate and glutamate metabolism (KEGG)

## Outgoing Edges (3)

- `is_product_of` --> [[reaction.ecocyc.ASPCARBTRANS-RXN|reaction.ecocyc.ASPCARBTRANS-RXN]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.DIHYDROOROT-RXN|reaction.ecocyc.DIHYDROOROT-RXN]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `represses` --> [[reaction.ecocyc.RXN0-5359|reaction.ecocyc.RXN0-5359]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity

## Incoming Edges (0)

_None._

## External IDs

- `KEGG:C00438`

## Notes

Included because it appears in at least one E. coli KEGG pathway.
