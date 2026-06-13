---
entity_id: "molecule.C15547"
entity_type: "small_molecule"
name: "1,4-Dihydroxy-2-naphthoyl-CoA"
source_database: "KEGG"
source_id: "C15547"
default_state: "low"
allowed_states: "absent|low|medium|high"
subcellular_location: ""
enriched_summary_quality: "placeholder"
tags:
  - entity/small_molecule
  - source/KEGG
aliases:
  - "1,4-Dihydroxy-2-naphthoyl-CoA"
---

# 1,4-Dihydroxy-2-naphthoyl-CoA

`molecule.C15547`

## Static

- Type: `small_molecule`
- Source: `KEGG:C15547`
- Default state: `low`
- Allowed states: `absent|low|medium|high`

## Enriched Summary

KEGG compound: 1,4-Dihydroxy-2-naphthoyl-CoA

## Biological Role

Consumed as substrate in 1 reaction(s). Produced in 1 reaction(s).

## Enriched Pathways

- `eco00130` Ubiquinone and other terpenoid-quinone biosynthesis (KEGG)

## Annotation

KEGG compound: 1,4-Dihydroxy-2-naphthoyl-CoA

## Pathways

- `eco00130` Ubiquinone and other terpenoid-quinone biosynthesis (KEGG)

## Outgoing Edges (3)

- `is_product_of` --> [[reaction.ecocyc.NAPHTHOATE-SYN-RXN|reaction.ecocyc.NAPHTHOATE-SYN-RXN]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` --> [[reaction.ecocyc.RXN-9311|reaction.ecocyc.RXN-9311]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `represses` --> [[reaction.ecocyc.NAPHTHOATE-SYN-RXN|reaction.ecocyc.NAPHTHOATE-SYN-RXN]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity

## Incoming Edges (0)

_None._

## External IDs

- `KEGG:C15547`

## Notes

Included because it appears in at least one E. coli KEGG pathway.
