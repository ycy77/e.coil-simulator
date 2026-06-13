---
entity_id: "molecule.C00197"
entity_type: "small_molecule"
name: "3-Phospho-D-glycerate"
source_database: "KEGG"
source_id: "C00197"
default_state: "low"
allowed_states: "absent|low|medium|high"
subcellular_location: ""
enriched_summary_quality: "placeholder"
tags:
  - entity/small_molecule
  - source/KEGG
aliases:
  - "3-Phospho-D-glycerate"
  - "D-Glycerate 3-phosphate"
  - "3-Phospho-(R)-glycerate"
  - "3-Phosphoglycerate"
---

# 3-Phospho-D-glycerate

`molecule.C00197`

## Static

- Type: `small_molecule`
- Source: `KEGG:C00197`
- Default state: `low`
- Allowed states: `absent|low|medium|high`

## Enriched Summary

KEGG compound: 3-Phospho-D-glycerate; D-Glycerate 3-phosphate; 3-Phospho-(R)-glycerate; 3-Phosphoglycerate

## Biological Role

Consumed as substrate in 3 reaction(s). Produced in 5 reaction(s).

## Enriched Pathways

- `eco00010` Glycolysis / Gluconeogenesis (KEGG)
- `eco00030` Pentose phosphate pathway (KEGG)
- `eco00260` Glycine, serine and threonine metabolism (KEGG)
- `eco00270` Cysteine and methionine metabolism (KEGG)
- `eco00561` Glycerolipid metabolism (KEGG)
- `eco00630` Glyoxylate and dicarboxylate metabolism (KEGG)
- `eco00680` Methane metabolism (KEGG)
- `eco00710` Carbon fixation by Calvin cycle (KEGG)

## Annotation

KEGG compound: 3-Phospho-D-glycerate; D-Glycerate 3-phosphate; 3-Phospho-(R)-glycerate; 3-Phosphoglycerate

## Pathways

- `eco00010` Glycolysis / Gluconeogenesis (KEGG)
- `eco00030` Pentose phosphate pathway (KEGG)
- `eco00260` Glycine, serine and threonine metabolism (KEGG)
- `eco00270` Cysteine and methionine metabolism (KEGG)
- `eco00561` Glycerolipid metabolism (KEGG)
- `eco00630` Glyoxylate and dicarboxylate metabolism (KEGG)
- `eco00680` Methane metabolism (KEGG)
- `eco00710` Carbon fixation by Calvin cycle (KEGG)

## Outgoing Edges (16)

- `activates` --> [[reaction.ecocyc.DEPHOSICITDEHASE-RXN|reaction.ecocyc.DEPHOSICITDEHASE-RXN]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `is_product_of` --> [[reaction.R01518|reaction.R01518]] `KEGG` `database` - C00631 <=> C00197
- `is_product_of` --> [[reaction.ecocyc.3PGAREARR-RXN|reaction.ecocyc.3PGAREARR-RXN]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.GLY3KIN-RXN|reaction.ecocyc.GLY3KIN-RXN]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.RXN-15511|reaction.ecocyc.RXN-15511]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.RXN-15513|reaction.ecocyc.RXN-15513]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` --> [[reaction.ecocyc.3-PHOSPHOGLYCERATE-PHOSPHATASE-RXN|reaction.ecocyc.3-PHOSPHOGLYCERATE-PHOSPHATASE-RXN]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.PGLYCDEHYDROG-RXN|reaction.ecocyc.PGLYCDEHYDROG-RXN]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.PHOSGLYPHOS-RXN|reaction.ecocyc.PHOSGLYPHOS-RXN]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `represses` --> [[reaction.ecocyc.GSADENYLATION-RXN|reaction.ecocyc.GSADENYLATION-RXN]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` --> [[reaction.ecocyc.ISOCIT-CLEAV-RXN|reaction.ecocyc.ISOCIT-CLEAV-RXN]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` --> [[reaction.ecocyc.KETOGLUTREDUCT-RXN|reaction.ecocyc.KETOGLUTREDUCT-RXN]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` --> [[reaction.ecocyc.METHGLYSYN-RXN|reaction.ecocyc.METHGLYSYN-RXN]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` --> [[reaction.ecocyc.PHOSICITDEHASE-RXN|reaction.ecocyc.PHOSICITDEHASE-RXN]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` --> [[reaction.ecocyc.RXN-16701|reaction.ecocyc.RXN-16701]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` --> [[reaction.ecocyc.RXN0-5260|reaction.ecocyc.RXN0-5260]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity

## Incoming Edges (0)

_None._

## External IDs

- `KEGG:C00197`

## Notes

Included because it appears in at least one E. coli KEGG pathway.
