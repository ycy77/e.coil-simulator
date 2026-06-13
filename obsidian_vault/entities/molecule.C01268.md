---
entity_id: "molecule.C01268"
entity_type: "small_molecule"
name: "5-Amino-6-(5'-phosphoribosylamino)uracil"
source_database: "KEGG"
source_id: "C01268"
default_state: "low"
allowed_states: "absent|low|medium|high"
subcellular_location: ""
enriched_summary_quality: "placeholder"
tags:
  - entity/small_molecule
  - source/KEGG
aliases:
  - "5-Amino-6-(5'-phosphoribosylamino)uracil"
  - "5-Amino-6-(ribosylamino)-2,4-(1H,3H)-pyrimidinedione 5'-phosphate"
  - "5-Amino-6-(5-phosphoribosylamino)uracil"
---

# 5-Amino-6-(5'-phosphoribosylamino)uracil

`molecule.C01268`

## Static

- Type: `small_molecule`
- Source: `KEGG:C01268`
- Default state: `low`
- Allowed states: `absent|low|medium|high`

## Enriched Summary

KEGG compound: 5-Amino-6-(5'-phosphoribosylamino)uracil; 5-Amino-6-(ribosylamino)-2,4-(1H,3H)-pyrimidinedione 5'-phosphate; 5-Amino-6-(5-phosphoribosylamino)uracil EcoCyc common name: 5-amino-6-(5-phospho-D-ribosylamino)uracil.

## Biological Role

Consumed as substrate in 1 reaction(s). Produced in 3 reaction(s).

## Enriched Pathways

- `eco00740` Riboflavin metabolism (KEGG)

## Annotation

KEGG compound: 5-Amino-6-(5'-phosphoribosylamino)uracil; 5-Amino-6-(ribosylamino)-2,4-(1H,3H)-pyrimidinedione 5'-phosphate; 5-Amino-6-(5-phosphoribosylamino)uracil

## Pathways

- `eco00740` Riboflavin metabolism (KEGG)

## Outgoing Edges (4)

- `is_product_of` --> [[reaction.R03458|reaction.R03458]] `KEGG` `database` - C04454 + C00006 <=> C01268 + C00005 + C00080
- `is_product_of` --> [[reaction.ecocyc.RIBOFLAVINSYNDEAM-RXN|reaction.ecocyc.RIBOFLAVINSYNDEAM-RXN]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.RIBOFLAVINSYNREDUC-RXN|reaction.ecocyc.RIBOFLAVINSYNREDUC-RXN]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` --> [[reaction.ecocyc.RXN-19407|reaction.ecocyc.RXN-19407]] `EcoCyc` `database` - EcoCyc reaction LEFT

## Incoming Edges (0)

_None._

## External IDs

- `KEGG:C01268`

## Notes

Included because it appears in at least one E. coli KEGG pathway.
