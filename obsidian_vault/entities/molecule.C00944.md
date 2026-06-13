---
entity_id: "molecule.C00944"
entity_type: "small_molecule"
name: "3-Dehydroquinate"
source_database: "KEGG"
source_id: "C00944"
default_state: "low"
allowed_states: "absent|low|medium|high"
subcellular_location: ""
enriched_summary_quality: "placeholder"
tags:
  - entity/small_molecule
  - source/KEGG
aliases:
  - "3-Dehydroquinate"
  - "3-Dehydroquinic acid"
  - "5-Dehydroquinate"
  - "5-Dehydroquinic acid"
---

# 3-Dehydroquinate

`molecule.C00944`

## Static

- Type: `small_molecule`
- Source: `KEGG:C00944`
- Default state: `low`
- Allowed states: `absent|low|medium|high`

## Enriched Summary

KEGG compound: 3-Dehydroquinate; 3-Dehydroquinic acid; 5-Dehydroquinate; 5-Dehydroquinic acid The numbering system used in the naming of 3-dehydroquinate is that of the recommendations on cyclitols, sections I-8 and I-9. The use of the term '5-dehydroquinate' for this compound is based on an earlier system of numbering.

## Biological Role

Consumed as substrate in 1 reaction(s). Produced in 3 reaction(s).

## Enriched Pathways

- `eco00400` Phenylalanine, tyrosine and tryptophan biosynthesis (KEGG)

## Annotation

KEGG compound: 3-Dehydroquinate; 3-Dehydroquinic acid; 5-Dehydroquinate; 5-Dehydroquinic acid

## Pathways

- `eco00400` Phenylalanine, tyrosine and tryptophan biosynthesis (KEGG)

## Outgoing Edges (5)

- `is_product_of` --> [[reaction.ecocyc.3-DEHYDROQUINATE-SYNTHASE-RXN|reaction.ecocyc.3-DEHYDROQUINATE-SYNTHASE-RXN]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.QUINATE-5-DEHYDROGENASE-RXN|reaction.ecocyc.QUINATE-5-DEHYDROGENASE-RXN]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.RXN-20674|reaction.ecocyc.RXN-20674]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` --> [[reaction.ecocyc.3-DEHYDROQUINATE-DEHYDRATASE-RXN|reaction.ecocyc.3-DEHYDROQUINATE-DEHYDRATASE-RXN]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `represses` --> [[reaction.ecocyc.3-DEHYDROQUINATE-DEHYDRATASE-RXN|reaction.ecocyc.3-DEHYDROQUINATE-DEHYDRATASE-RXN]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity

## Incoming Edges (0)

_None._

## External IDs

- `KEGG:C00944`

## Notes

Included because it appears in at least one E. coli KEGG pathway.
