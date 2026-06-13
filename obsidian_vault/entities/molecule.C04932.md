---
entity_id: "molecule.C04932"
entity_type: "small_molecule"
name: "Lipid A disaccharide"
source_database: "KEGG"
source_id: "C04932"
default_state: "low"
allowed_states: "absent|low|medium|high"
subcellular_location: ""
enriched_summary_quality: "placeholder"
tags:
  - entity/small_molecule
  - source/KEGG
aliases:
  - "Lipid A disaccharide"
  - "Tetraacyldisaccharide 1-phosphate"
  - "[2-N,3-O-Bis(3-hydroxytetradecanoyl)-beta-D-glucosaminyl]-(1->6)-[2-N,3-O-bis(3-hydroxytetradecanoyl)-alpha-D-glucosaminyl phosphate]"
  - "2,3-Bis[(3R)-3-hydroxytetradecanoyl]-beta-D-glucosaminyl-(1->6)-2,3-bis[(3R)-3-hydroxytetradecanoyl]-alpha-D-glucosaminyl 1-phosphate"
---

# Lipid A disaccharide

`molecule.C04932`

## Static

- Type: `small_molecule`
- Source: `KEGG:C04932`
- Default state: `low`
- Allowed states: `absent|low|medium|high`

## Enriched Summary

KEGG compound: Lipid A disaccharide; Tetraacyldisaccharide 1-phosphate; [2-N,3-O-Bis(3-hydroxytetradecanoyl)-beta-D-glucosaminyl]-(1->6)-[2-N,3-O-bis(3-hydroxytetradecanoyl)-alpha-D-glucosaminyl phosphate]; 2,3-Bis[(3R)-3-hydroxytetradecanoyl]-beta-D-glucosaminyl-(1->6)-2,3-bis[(3R)-3-hydroxytetradecanoyl]-alpha-D-glucosaminyl 1-phosphate EcoCyc common name: lipid A disaccharide (E. coli).

## Biological Role

Consumed as substrate in 2 reaction(s). Produced in 1 reaction(s).

## Enriched Pathways

- `eco00540` Lipopolysaccharide biosynthesis (KEGG)

## Annotation

KEGG compound: Lipid A disaccharide; Tetraacyldisaccharide 1-phosphate; [2-N,3-O-Bis(3-hydroxytetradecanoyl)-beta-D-glucosaminyl]-(1->6)-[2-N,3-O-bis(3-hydroxytetradecanoyl)-alpha-D-glucosaminyl phosphate]; 2,3-Bis[(3R)-3-hydroxytetradecanoyl]-beta-D-glucosaminyl-(1->6)-2,3-bis[(3R)-3-hydroxytetradecanoyl]-alpha-D-glucosaminyl 1-phosphate

## Pathways

- `eco00540` Lipopolysaccharide biosynthesis (KEGG)

## Outgoing Edges (5)

- `is_product_of` --> [[reaction.ecocyc.LIPIDADISACCHARIDESYNTH-RXN|reaction.ecocyc.LIPIDADISACCHARIDESYNTH-RXN]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` --> [[reaction.R04657|reaction.R04657]] `KEGG` `database` - C00002 + C04932 <=> C00008 + C04919
- `is_substrate_of` --> [[reaction.ecocyc.TETRAACYLDISACC4KIN-RXN|reaction.ecocyc.TETRAACYLDISACC4KIN-RXN]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `represses` --> [[reaction.ecocyc.KDOTRANS-RXN|reaction.ecocyc.KDOTRANS-RXN]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` --> [[reaction.ecocyc.KDOTRANS2-RXN|reaction.ecocyc.KDOTRANS2-RXN]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity

## Incoming Edges (0)

_None._

## External IDs

- `KEGG:C04932`

## Notes

Included because it appears in at least one E. coli KEGG pathway.
