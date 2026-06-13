---
entity_id: "molecule.C03657"
entity_type: "small_molecule"
name: "1,4-Dihydroxy-2-naphthoate"
source_database: "KEGG"
source_id: "C03657"
default_state: "low"
allowed_states: "absent|low|medium|high"
subcellular_location: ""
enriched_summary_quality: "placeholder"
tags:
  - entity/small_molecule
  - source/KEGG
aliases:
  - "1,4-Dihydroxy-2-naphthoate"
  - "1,4-Dihydroxy-2-naphthoic acid"
---

# 1,4-Dihydroxy-2-naphthoate

`molecule.C03657`

## Static

- Type: `small_molecule`
- Source: `KEGG:C03657`
- Default state: `low`
- Allowed states: `absent|low|medium|high`

## Enriched Summary

KEGG compound: 1,4-Dihydroxy-2-naphthoate; 1,4-Dihydroxy-2-naphthoic acid

## Biological Role

Consumed as substrate in 3 reaction(s). Produced in 2 reaction(s).

## Enriched Pathways

- `eco00130` Ubiquinone and other terpenoid-quinone biosynthesis (KEGG)

## Annotation

KEGG compound: 1,4-Dihydroxy-2-naphthoate; 1,4-Dihydroxy-2-naphthoic acid

## Pathways

- `eco00130` Ubiquinone and other terpenoid-quinone biosynthesis (KEGG)

## Outgoing Edges (5)

- `is_product_of` --> [[reaction.R04150|reaction.R04150]] `KEGG` `database` - C03160 <=> C03657 + C00010
- `is_product_of` --> [[reaction.ecocyc.RXN-9311|reaction.ecocyc.RXN-9311]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` --> [[reaction.ecocyc.DMK-RXN|reaction.ecocyc.DMK-RXN]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.RXN-17066|reaction.ecocyc.RXN-17066]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.RXN-23260|reaction.ecocyc.RXN-23260]] `EcoCyc` `database` - EcoCyc reaction LEFT

## Incoming Edges (0)

_None._

## External IDs

- `KEGG:C03657`

## Notes

Included because it appears in at least one E. coli KEGG pathway.
