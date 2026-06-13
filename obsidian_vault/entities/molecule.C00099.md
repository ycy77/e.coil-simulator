---
entity_id: "molecule.C00099"
entity_type: "small_molecule"
name: "beta-Alanine"
source_database: "KEGG"
source_id: "C00099"
default_state: "low"
allowed_states: "absent|low|medium|high"
subcellular_location: ""
enriched_summary_quality: "placeholder"
tags:
  - entity/small_molecule
  - source/KEGG
aliases:
  - "beta-Alanine"
  - "3-Aminopropionic acid"
  - "3-Aminopropanoate"
---

# beta-Alanine

`molecule.C00099`

## Static

- Type: `small_molecule`
- Source: `KEGG:C00099`
- Default state: `low`
- Allowed states: `absent|low|medium|high`

## Enriched Summary

KEGG compound: beta-Alanine; 3-Aminopropionic acid; 3-Aminopropanoate EcoCyc common name: β-alanine.

## Biological Role

Consumed as substrate in 2 reaction(s). Produced in 3 reaction(s).

## Enriched Pathways

- `eco00240` Pyrimidine metabolism (KEGG)
- `eco00410` beta-Alanine metabolism (KEGG)
- `eco00640` Propanoate metabolism (KEGG)
- `eco00770` Pantothenate and CoA biosynthesis (KEGG)

## Annotation

KEGG compound: beta-Alanine; 3-Aminopropionic acid; 3-Aminopropanoate

## Pathways

- `eco00240` Pyrimidine metabolism (KEGG)
- `eco00410` beta-Alanine metabolism (KEGG)
- `eco00640` Propanoate metabolism (KEGG)
- `eco00770` Pantothenate and CoA biosynthesis (KEGG)

## Outgoing Edges (6)

- `is_product_of` --> [[reaction.R00489|reaction.R00489]] `KEGG` `database` - C00049 <=> C00099 + C00011
- `is_product_of` --> [[reaction.ecocyc.ASPDECARBOX-RXN|reaction.ecocyc.ASPDECARBOX-RXN]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.RXN0-5201|reaction.ecocyc.RXN0-5201]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` --> [[reaction.ecocyc.PANTOATE-BETA-ALANINE-LIG-RXN|reaction.ecocyc.PANTOATE-BETA-ALANINE-LIG-RXN]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.RXN0-5201|reaction.ecocyc.RXN0-5201]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `represses` --> [[reaction.ecocyc.GLYRIBONUCSYN-RXN|reaction.ecocyc.GLYRIBONUCSYN-RXN]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity

## Incoming Edges (0)

_None._

## External IDs

- `KEGG:C00099`

## Notes

Included because it appears in at least one E. coli KEGG pathway.
