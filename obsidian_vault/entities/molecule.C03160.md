---
entity_id: "molecule.C03160"
entity_type: "small_molecule"
name: "2-Succinylbenzoyl-CoA"
source_database: "KEGG"
source_id: "C03160"
default_state: "low"
allowed_states: "absent|low|medium|high"
subcellular_location: ""
enriched_summary_quality: "placeholder"
tags:
  - entity/small_molecule
  - source/KEGG
aliases:
  - "2-Succinylbenzoyl-CoA"
  - "o-Succinylbenzoyl-CoA"
  - "Succinylbenzoyl-CoA"
  - "4-(2-Carboxyphenyl)-4-oxobutanoyl-CoA"
---

# 2-Succinylbenzoyl-CoA

`molecule.C03160`

## Static

- Type: `small_molecule`
- Source: `KEGG:C03160`
- Default state: `low`
- Allowed states: `absent|low|medium|high`

## Enriched Summary

KEGG compound: 2-Succinylbenzoyl-CoA; o-Succinylbenzoyl-CoA; Succinylbenzoyl-CoA; 4-(2-Carboxyphenyl)-4-oxobutanoyl-CoA EcoCyc common name: 4-(2'-carboxyphenyl)-4-oxobutyryl-CoA.

## Biological Role

Consumed as substrate in 2 reaction(s). Produced in 1 reaction(s).

## Enriched Pathways

- `eco00130` Ubiquinone and other terpenoid-quinone biosynthesis (KEGG)

## Annotation

KEGG compound: 2-Succinylbenzoyl-CoA; o-Succinylbenzoyl-CoA; Succinylbenzoyl-CoA; 4-(2-Carboxyphenyl)-4-oxobutanoyl-CoA

## Pathways

- `eco00130` Ubiquinone and other terpenoid-quinone biosynthesis (KEGG)

## Outgoing Edges (3)

- `is_product_of` --> [[reaction.ecocyc.O-SUCCINYLBENZOATE-COA-LIG-RXN|reaction.ecocyc.O-SUCCINYLBENZOATE-COA-LIG-RXN]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` --> [[reaction.R04150|reaction.R04150]] `KEGG` `database` - C03160 <=> C03657 + C00010
- `is_substrate_of` --> [[reaction.ecocyc.NAPHTHOATE-SYN-RXN|reaction.ecocyc.NAPHTHOATE-SYN-RXN]] `EcoCyc` `database` - EcoCyc reaction LEFT

## Incoming Edges (0)

_None._

## External IDs

- `KEGG:C03160`

## Notes

Included because it appears in at least one E. coli KEGG pathway.
