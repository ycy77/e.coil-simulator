---
entity_id: "molecule.C00631"
entity_type: "small_molecule"
name: "2-Phospho-D-glycerate"
source_database: "KEGG"
source_id: "C00631"
default_state: "low"
allowed_states: "absent|low|medium|high"
subcellular_location: ""
enriched_summary_quality: "placeholder"
tags:
  - entity/small_molecule
  - source/KEGG
aliases:
  - "2-Phospho-D-glycerate"
  - "D-Glycerate 2-phosphate"
  - "2-Phospho-(R)-glycerate"
---

# 2-Phospho-D-glycerate

`molecule.C00631`

## Static

- Type: `small_molecule`
- Source: `KEGG:C00631`
- Default state: `low`
- Allowed states: `absent|low|medium|high`

## Enriched Summary

KEGG compound: 2-Phospho-D-glycerate; D-Glycerate 2-phosphate; 2-Phospho-(R)-glycerate

## Biological Role

Consumed as substrate in 7 reaction(s). Produced in 1 reaction(s).

## Enriched Pathways

- `eco00010` Glycolysis / Gluconeogenesis (KEGG)
- `eco00030` Pentose phosphate pathway (KEGG)
- `eco00260` Glycine, serine and threonine metabolism (KEGG)
- `eco00561` Glycerolipid metabolism (KEGG)
- `eco00630` Glyoxylate and dicarboxylate metabolism (KEGG)
- `eco00680` Methane metabolism (KEGG)

## Annotation

KEGG compound: 2-Phospho-D-glycerate; D-Glycerate 2-phosphate; 2-Phospho-(R)-glycerate

## Pathways

- `eco00010` Glycolysis / Gluconeogenesis (KEGG)
- `eco00030` Pentose phosphate pathway (KEGG)
- `eco00260` Glycine, serine and threonine metabolism (KEGG)
- `eco00561` Glycerolipid metabolism (KEGG)
- `eco00630` Glyoxylate and dicarboxylate metabolism (KEGG)
- `eco00680` Methane metabolism (KEGG)

## Outgoing Edges (10)

- `is_product_of` --> [[reaction.ecocyc.GKI-RXN|reaction.ecocyc.GKI-RXN]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` --> [[reaction.R00658|reaction.R00658]] `KEGG` `database` - C00631 <=> C00074 + C00001
- `is_substrate_of` --> [[reaction.R01518|reaction.R01518]] `KEGG` `database` - C00631 <=> C00197
- `is_substrate_of` --> [[reaction.ecocyc.2PGADEHYDRAT-RXN|reaction.ecocyc.2PGADEHYDRAT-RXN]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.3PGAREARR-RXN|reaction.ecocyc.3PGAREARR-RXN]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.PHOSPHOGLYCERATE-PHOSPHATASE-RXN|reaction.ecocyc.PHOSPHOGLYCERATE-PHOSPHATASE-RXN]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.RXN-15510|reaction.ecocyc.RXN-15510]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.RXN-15513|reaction.ecocyc.RXN-15513]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `represses` --> [[reaction.ecocyc.DAHPSYN-RXN|reaction.ecocyc.DAHPSYN-RXN]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` --> [[reaction.ecocyc.RXN0-5260|reaction.ecocyc.RXN0-5260]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity

## Incoming Edges (0)

_None._

## External IDs

- `KEGG:C00631`

## Notes

Included because it appears in at least one E. coli KEGG pathway.
