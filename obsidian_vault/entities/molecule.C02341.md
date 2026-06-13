---
entity_id: "molecule.C02341"
entity_type: "small_molecule"
name: "trans-Aconitate"
source_database: "KEGG"
source_id: "C02341"
default_state: "low"
allowed_states: "absent|low|medium|high"
subcellular_location: ""
enriched_summary_quality: "placeholder"
tags:
  - entity/small_molecule
  - source/KEGG
aliases:
  - "trans-Aconitate"
  - "trans-Aconitic acid"
---

# trans-Aconitate

`molecule.C02341`

## Static

- Type: `small_molecule`
- Source: `KEGG:C02341`
- Default state: `low`
- Allowed states: `absent|low|medium|high`

## Enriched Summary

KEGG compound: trans-Aconitate; trans-Aconitic acid

## Biological Role

Consumed as substrate in 3 reaction(s).

## Enriched Pathways

- `eco00660` C5-Branched dibasic acid metabolism (KEGG)

## Annotation

KEGG compound: trans-Aconitate; trans-Aconitic acid

## Pathways

- `eco00660` C5-Branched dibasic acid metabolism (KEGG)

## Outgoing Edges (4)

- `is_substrate_of` --> [[reaction.R05763|reaction.R05763]] `KEGG` `database` - C00019 + C02341 <=> C00021 + C11514
- `is_substrate_of` --> [[reaction.ecocyc.ACONITATE-DELTA-ISOMERASE-RXN|reaction.ecocyc.ACONITATE-DELTA-ISOMERASE-RXN]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.RXN0-2441|reaction.ecocyc.RXN0-2441]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `represses` --> [[reaction.ecocyc.PREPHENATEDEHYDRAT-RXN|reaction.ecocyc.PREPHENATEDEHYDRAT-RXN]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity

## Incoming Edges (0)

_None._

## External IDs

- `KEGG:C02341`

## Notes

Included because it appears in at least one E. coli KEGG pathway.
