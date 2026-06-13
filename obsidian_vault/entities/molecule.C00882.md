---
entity_id: "molecule.C00882"
entity_type: "small_molecule"
name: "Dephospho-CoA"
source_database: "KEGG"
source_id: "C00882"
default_state: "low"
allowed_states: "absent|low|medium|high"
subcellular_location: ""
enriched_summary_quality: "placeholder"
tags:
  - entity/small_molecule
  - source/KEGG
aliases:
  - "Dephospho-CoA"
  - "Dephosphocoenzyme A"
  - "3'-Dephospho-CoA"
---

# Dephospho-CoA

`molecule.C00882`

## Static

- Type: `small_molecule`
- Source: `KEGG:C00882`
- Default state: `low`
- Allowed states: `absent|low|medium|high`

## Enriched Summary

KEGG compound: Dephospho-CoA; Dephosphocoenzyme A; 3'-Dephospho-CoA EcoCyc common name: 3'-dephospho-CoA.

## Biological Role

Consumed as substrate in 3 reaction(s). Produced in 1 reaction(s).

## Enriched Pathways

- `eco00770` Pantothenate and CoA biosynthesis (KEGG)

## Annotation

KEGG compound: Dephospho-CoA; Dephosphocoenzyme A; 3'-Dephospho-CoA

## Pathways

- `eco00770` Pantothenate and CoA biosynthesis (KEGG)

## Outgoing Edges (4)

- `is_product_of` --> [[reaction.ecocyc.PANTEPADENYLYLTRAN-RXN|reaction.ecocyc.PANTEPADENYLYLTRAN-RXN]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` --> [[reaction.R00130|reaction.R00130]] `KEGG` `database` - C00002 + C00882 <=> C00008 + C00010
- `is_substrate_of` --> [[reaction.ecocyc.2.7.8.25-RXN|reaction.ecocyc.2.7.8.25-RXN]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.DEPHOSPHOCOAKIN-RXN|reaction.ecocyc.DEPHOSPHOCOAKIN-RXN]] `EcoCyc` `database` - EcoCyc reaction LEFT

## Incoming Edges (0)

_None._

## External IDs

- `KEGG:C00882`

## Notes

Included because it appears in at least one E. coli KEGG pathway.
