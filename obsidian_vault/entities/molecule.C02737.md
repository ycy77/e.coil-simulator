---
entity_id: "molecule.C02737"
entity_type: "small_molecule"
name: "Phosphatidylserine"
source_database: "KEGG"
source_id: "C02737"
default_state: "low"
allowed_states: "absent|low|medium|high"
subcellular_location: ""
enriched_summary_quality: "placeholder"
tags:
  - entity/small_molecule
  - source/KEGG
aliases:
  - "Phosphatidylserine"
  - "Phosphatidyl-L-serine"
  - "1,2-Diacyl-sn-glycerol 3-phospho-L-serine"
  - "3-O-sn-Phosphatidyl-L-serine"
  - "O3-Phosphatidyl-L-serine"
  - "L-1-Phosphatidylserine"
---

# Phosphatidylserine

`molecule.C02737`

## Static

- Type: `small_molecule`
- Source: `KEGG:C02737`
- Default state: `low`
- Allowed states: `absent|low|medium|high`

## Enriched Summary

KEGG compound: Phosphatidylserine; Phosphatidyl-L-serine; 1,2-Diacyl-sn-glycerol 3-phospho-L-serine; 3-O-sn-Phosphatidyl-L-serine; O3-Phosphatidyl-L-serine; L-1-Phosphatidylserine EcoCyc common name: a phosphatidylserine. Phosphatidylserine (PS) is a phospholipid found in the cell membrane. It faces the cytosolic (inner) side of the cell membrane, and is held in place by the enzyme flippase. When a cell undergoes apoptosis, phospholipid scramblase catalyzes the rapid exchange of phosphatidylserine between the two sides. When PS flips to the extracellular (outer) surface, it acts as a signal for macrophages to engulf the cells . Phosphatidylserine also plays an important role in blood coagulation . In bacteria PS is biosynthesized by condensing SER with CDPDIACYLGLYCEROL by EC-2.7.8.8. In animalsPS is only produced by base-exchange reactions with phosphatidylcholine and phosphatidylethanolamine catalyzed by EC-2.7.8.29.

## Biological Role

Consumed as substrate in 1 reaction(s). Produced in 1 reaction(s).

## Enriched Pathways

- `eco00260` Glycine, serine and threonine metabolism (KEGG)
- `eco00564` Glycerophospholipid metabolism (KEGG)

## Annotation

KEGG compound: Phosphatidylserine; Phosphatidyl-L-serine; 1,2-Diacyl-sn-glycerol 3-phospho-L-serine; 3-O-sn-Phosphatidyl-L-serine; O3-Phosphatidyl-L-serine; L-1-Phosphatidylserine

## Pathways

- `eco00260` Glycine, serine and threonine metabolism (KEGG)
- `eco00564` Glycerophospholipid metabolism (KEGG)

## Outgoing Edges (3)

- `activates` --> [[reaction.ecocyc.CARDIOLIPSYN-RXN|reaction.ecocyc.CARDIOLIPSYN-RXN]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `is_product_of` --> [[reaction.ecocyc.PHOSPHASERSYN-RXN|reaction.ecocyc.PHOSPHASERSYN-RXN]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` --> [[reaction.ecocyc.PHOSPHASERDECARB-RXN|reaction.ecocyc.PHOSPHASERDECARB-RXN]] `EcoCyc` `database` - EcoCyc reaction LEFT

## Incoming Edges (0)

_None._

## External IDs

- `KEGG:C02737`

## Notes

Included because it appears in at least one E. coli KEGG pathway.
