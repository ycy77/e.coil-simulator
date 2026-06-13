---
entity_id: "molecule.C00565"
entity_type: "small_molecule"
name: "Trimethylamine"
source_database: "KEGG"
source_id: "C00565"
default_state: "low"
allowed_states: "absent|low|medium|high"
subcellular_location: ""
enriched_summary_quality: "placeholder"
tags:
  - entity/small_molecule
  - source/KEGG
aliases:
  - "Trimethylamine"
  - "(CH3)3N"
  - "N,N-Dimethylmethanamine"
  - "N,N,N-Trimethylamine"
---

# Trimethylamine

`molecule.C00565`

## Static

- Type: `small_molecule`
- Source: `KEGG:C00565`
- Default state: `low`
- Allowed states: `absent|low|medium|high`

## Enriched Summary

KEGG compound: Trimethylamine; (CH3)3N; N,N-Dimethylmethanamine; N,N,N-Trimethylamine

## Biological Role

Consumed as substrate in 3 reaction(s). Produced in 6 reaction(s).

## Enriched Pathways

- `eco00680` Methane metabolism (KEGG)

## Annotation

KEGG compound: Trimethylamine; (CH3)3N; N,N-Dimethylmethanamine; N,N,N-Trimethylamine

## Pathways

- `eco00680` Methane metabolism (KEGG)

## Outgoing Edges (9)

- `is_product_of` --> [[reaction.R11911|reaction.R11911]] `KEGG` `database` - C00318 + C00005 + C00080 + C00007 <=> C21761 + C00565 + C00006 + C00001
- `is_product_of` --> [[reaction.ecocyc.RXN-18258|reaction.ecocyc.RXN-18258]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.RXN-18376|reaction.ecocyc.RXN-18376]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.RXN-5921|reaction.ecocyc.RXN-5921]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.RXN0-5263|reaction.ecocyc.RXN0-5263]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.RXN0-5264|reaction.ecocyc.RXN0-5264]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` --> [[reaction.ecocyc.1.7.2.3-RXN|reaction.ecocyc.1.7.2.3-RXN]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.RXN-19618|reaction.ecocyc.RXN-19618]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.RXN-19619|reaction.ecocyc.RXN-19619]] `EcoCyc` `database` - EcoCyc reaction LEFT

## Incoming Edges (0)

_None._

## External IDs

- `KEGG:C00565`

## Notes

Included because it appears in at least one E. coli KEGG pathway.
