---
entity_id: "molecule.C04824"
entity_type: "small_molecule"
name: "Lipid X"
source_database: "KEGG"
source_id: "C04824"
default_state: "low"
allowed_states: "absent|low|medium|high"
subcellular_location: ""
enriched_summary_quality: "placeholder"
tags:
  - entity/small_molecule
  - source/KEGG
aliases:
  - "Lipid X"
  - "2,3-Diacylglucosamine 1-phosphate"
  - "2,3-Bis[(3R)-3-hydroxymyristoyl]-alpha-D-glucosaminyl 1-phosphate"
  - "2,3-Bis(3-hydroxytetradecanoyl)-alpha-D-glucosaminyl 1-phosphate"
---

# Lipid X

`molecule.C04824`

## Static

- Type: `small_molecule`
- Source: `KEGG:C04824`
- Default state: `low`
- Allowed states: `absent|low|medium|high`

## Enriched Summary

KEGG compound: Lipid X; 2,3-Diacylglucosamine 1-phosphate; 2,3-Bis[(3R)-3-hydroxymyristoyl]-alpha-D-glucosaminyl 1-phosphate; 2,3-Bis(3-hydroxytetradecanoyl)-alpha-D-glucosaminyl 1-phosphate EcoCyc common name: lipid X (E. coli).

## Biological Role

Consumed as substrate in 1 reaction(s). Produced in 1 reaction(s).

## Enriched Pathways

- `eco00540` Lipopolysaccharide biosynthesis (KEGG)

## Annotation

KEGG compound: Lipid X; 2,3-Diacylglucosamine 1-phosphate; 2,3-Bis[(3R)-3-hydroxymyristoyl]-alpha-D-glucosaminyl 1-phosphate; 2,3-Bis(3-hydroxytetradecanoyl)-alpha-D-glucosaminyl 1-phosphate

## Pathways

- `eco00540` Lipopolysaccharide biosynthesis (KEGG)

## Outgoing Edges (2)

- `is_product_of` --> [[reaction.ecocyc.LIPIDXSYNTHESIS-RXN|reaction.ecocyc.LIPIDXSYNTHESIS-RXN]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` --> [[reaction.ecocyc.LIPIDADISACCHARIDESYNTH-RXN|reaction.ecocyc.LIPIDADISACCHARIDESYNTH-RXN]] `EcoCyc` `database` - EcoCyc reaction LEFT

## Incoming Edges (0)

_None._

## External IDs

- `KEGG:C04824`

## Notes

Included because it appears in at least one E. coli KEGG pathway.
