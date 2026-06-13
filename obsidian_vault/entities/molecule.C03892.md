---
entity_id: "molecule.C03892"
entity_type: "small_molecule"
name: "Phosphatidylglycerophosphate"
source_database: "KEGG"
source_id: "C03892"
default_state: "low"
allowed_states: "absent|low|medium|high"
subcellular_location: ""
enriched_summary_quality: "placeholder"
tags:
  - entity/small_molecule
  - source/KEGG
aliases:
  - "Phosphatidylglycerophosphate"
  - "1-(3-sn-Phosphatidyl)-sn-glycerol 3-phosphate"
  - "3-(3-Phosphatidyl)-D-glycerol 1-phosphate"
  - "1,2-Diacyl-sn-glycero-3-phospho-sn-glycerol 3'-phosphate"
---

# Phosphatidylglycerophosphate

`molecule.C03892`

## Static

- Type: `small_molecule`
- Source: `KEGG:C03892`
- Default state: `low`
- Allowed states: `absent|low|medium|high`

## Enriched Summary

KEGG compound: Phosphatidylglycerophosphate; 1-(3-sn-Phosphatidyl)-sn-glycerol 3-phosphate; 3-(3-Phosphatidyl)-D-glycerol 1-phosphate; 1,2-Diacyl-sn-glycero-3-phospho-sn-glycerol 3'-phosphate EcoCyc common name: a phosphatidylglycerophosphate.

## Biological Role

Consumed as substrate in 1 reaction(s). Produced in 2 reaction(s).

## Enriched Pathways

- `eco00564` Glycerophospholipid metabolism (KEGG)

## Annotation

KEGG compound: Phosphatidylglycerophosphate; 1-(3-sn-Phosphatidyl)-sn-glycerol 3-phosphate; 3-(3-Phosphatidyl)-D-glycerol 1-phosphate; 1,2-Diacyl-sn-glycero-3-phospho-sn-glycerol 3'-phosphate

## Pathways

- `eco00564` Glycerophospholipid metabolism (KEGG)

## Outgoing Edges (4)

- `activates` --> [[reaction.ecocyc.MALATE-DEHYDROGENASE-ACCEPTOR-RXN|reaction.ecocyc.MALATE-DEHYDROGENASE-ACCEPTOR-RXN]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `is_product_of` --> [[reaction.ecocyc.PHOSPHAGLYPSYN-RXN|reaction.ecocyc.PHOSPHAGLYPSYN-RXN]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.RXN0-5223|reaction.ecocyc.RXN0-5223]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` --> [[reaction.ecocyc.PGPPHOSPHA-RXN|reaction.ecocyc.PGPPHOSPHA-RXN]] `EcoCyc` `database` - EcoCyc reaction LEFT

## Incoming Edges (0)

_None._

## External IDs

- `KEGG:C03892`

## Notes

Included because it appears in at least one E. coli KEGG pathway.
