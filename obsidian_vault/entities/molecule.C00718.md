---
entity_id: "molecule.C00718"
entity_type: "small_molecule"
name: "Amylose"
source_database: "KEGG"
source_id: "C00718"
default_state: "low"
allowed_states: "absent|low|medium|high"
subcellular_location: ""
enriched_summary_quality: "placeholder"
tags:
  - entity/small_molecule
  - source/KEGG
aliases:
  - "Amylose"
  - "Amylose chain"
  - "(1,4-alpha-D-Glucosyl)n"
  - "(1,4-alpha-D-Glucosyl)n+1"
  - "(1,4-alpha-D-Glucosyl)n-1"
  - "4-{(1,4)-alpha-D-Glucosyl}(n-1)-D-glucose"
  - "1,4-alpha-D-Glucan"
---

# Amylose

`molecule.C00718`

## Static

- Type: `small_molecule`
- Source: `KEGG:C00718`
- Default state: `low`
- Allowed states: `absent|low|medium|high`

## Enriched Summary

KEGG compound: Amylose; Amylose chain; (1,4-alpha-D-Glucosyl)n; (1,4-alpha-D-Glucosyl)n+1; (1,4-alpha-D-Glucosyl)n-1; 4-{(1,4)-alpha-D-Glucosyl}(n-1)-D-glucose; 1,4-alpha-D-Glucan EcoCyc common name: a (1→4)-α-D-glucan.

## Biological Role

Consumed as substrate in 7 reaction(s). Produced in 6 reaction(s).

## Enriched Pathways

- `eco00500` Starch and sucrose metabolism (KEGG)

## Annotation

KEGG compound: Amylose; Amylose chain; (1,4-alpha-D-Glucosyl)n; (1,4-alpha-D-Glucosyl)n+1; (1,4-alpha-D-Glucosyl)n-1; 4-{(1,4)-alpha-D-Glucosyl}(n-1)-D-glucose; 1,4-alpha-D-Glucan

## Pathways

- `eco00500` Starch and sucrose metabolism (KEGG)

## Outgoing Edges (13)

- `is_product_of` --> [[reaction.R02111|reaction.R02111]] `KEGG` `database` - C00369 + C00009 <=> C00718 + C00103
- `is_product_of` --> [[reaction.ecocyc.ALPHA-AMYL-RXN|reaction.ecocyc.ALPHA-AMYL-RXN]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.GLYCOGENSYN-RXN|reaction.ecocyc.GLYCOGENSYN-RXN]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.MALTODEXGLUCOSID-RXN|reaction.ecocyc.MALTODEXGLUCOSID-RXN]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.RXN0-5181|reaction.ecocyc.RXN0-5181]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.RXN0-5184|reaction.ecocyc.RXN0-5184]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` --> [[reaction.R02110|reaction.R02110]] `KEGG` `database` - C00718 <=> C00369
- `is_substrate_of` --> [[reaction.ecocyc.ALPHA-AMYL-RXN|reaction.ecocyc.ALPHA-AMYL-RXN]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.GLYCOGEN-BRANCH-RXN|reaction.ecocyc.GLYCOGEN-BRANCH-RXN]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.GLYCOGENSYN-RXN|reaction.ecocyc.GLYCOGENSYN-RXN]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.MALTODEXGLUCOSID-RXN|reaction.ecocyc.MALTODEXGLUCOSID-RXN]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.RXN0-5181|reaction.ecocyc.RXN0-5181]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.RXN0-5184|reaction.ecocyc.RXN0-5184]] `EcoCyc` `database` - EcoCyc reaction LEFT

## Incoming Edges (0)

_None._

## External IDs

- `KEGG:C00718`

## Notes

Included because it appears in at least one E. coli KEGG pathway.
