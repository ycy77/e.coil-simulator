---
entity_id: "molecule.C01606"
entity_type: "small_molecule"
name: "Phthalate"
source_database: "KEGG"
source_id: "C01606"
default_state: "low"
allowed_states: "absent|low|medium|high"
subcellular_location: ""
enriched_summary_quality: "placeholder"
tags:
  - entity/small_molecule
  - source/KEGG
aliases:
  - "Phthalate"
  - "o-Phthalic acid"
  - "1,2-Benzenedicarboxylic acid"
---

# Phthalate

`molecule.C01606`

## Static

- Type: `small_molecule`
- Source: `KEGG:C01606`
- Default state: `low`
- Allowed states: `absent|low|medium|high`

## Enriched Summary

KEGG compound: Phthalate; o-Phthalic acid; 1,2-Benzenedicarboxylic acid

## Biological Role

Produced in 1 reaction(s).

## Enriched Pathways

- `eco02010` ABC transporters (KEGG)

## Annotation

KEGG compound: Phthalate; o-Phthalic acid; 1,2-Benzenedicarboxylic acid

## Pathways

- `eco02010` ABC transporters (KEGG)

## Outgoing Edges (3)

- `is_product_of` --> [[reaction.ecocyc.RXN-11813|reaction.ecocyc.RXN-11813]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `represses` --> [[reaction.ecocyc.GLUTDECARBOX-RXN|reaction.ecocyc.GLUTDECARBOX-RXN]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` --> [[reaction.ecocyc.QUINOPRIBOTRANS-RXN|reaction.ecocyc.QUINOPRIBOTRANS-RXN]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity

## Incoming Edges (0)

_None._

## External IDs

- `KEGG:C01606`

## Notes

Included because it appears in at least one E. coli KEGG pathway.
