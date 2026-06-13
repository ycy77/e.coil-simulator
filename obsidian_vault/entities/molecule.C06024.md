---
entity_id: "molecule.C06024"
entity_type: "small_molecule"
name: "3-Deoxy-D-manno-octulosonyl-lipid IV(A)"
source_database: "KEGG"
source_id: "C06024"
default_state: "low"
allowed_states: "absent|low|medium|high"
subcellular_location: ""
enriched_summary_quality: "placeholder"
tags:
  - entity/small_molecule
  - source/KEGG
aliases:
  - "3-Deoxy-D-manno-octulosonyl-lipid IV(A)"
  - "KDO-lipid IV(A)"
  - "3-Deoxy-D-manno-octulosonyl-2',3',2',3'-tetrakis(beta-hydroxymyristoyl)-D-glucosaminyl-1,6-beta-D-glucosamine 1,4'-bisphosphate"
  - "alpha-Kdo-(2->6)-[lipid IVA]"
---

# 3-Deoxy-D-manno-octulosonyl-lipid IV(A)

`molecule.C06024`

## Static

- Type: `small_molecule`
- Source: `KEGG:C06024`
- Default state: `low`
- Allowed states: `absent|low|medium|high`

## Enriched Summary

KEGG compound: 3-Deoxy-D-manno-octulosonyl-lipid IV(A); KDO-lipid IV(A); 3-Deoxy-D-manno-octulosonyl-2',3',2',3'-tetrakis(beta-hydroxymyristoyl)-D-glucosaminyl-1,6-beta-D-glucosamine 1,4'-bisphosphate; alpha-Kdo-(2->6)-[lipid IVA] EcoCyc common name: α-Kdo-(2→6)-lipid IVA (E. coli).

## Biological Role

Consumed as substrate in 1 reaction(s). Produced in 2 reaction(s).

## Enriched Pathways

- `eco00540` Lipopolysaccharide biosynthesis (KEGG)

## Annotation

KEGG compound: 3-Deoxy-D-manno-octulosonyl-lipid IV(A); KDO-lipid IV(A); 3-Deoxy-D-manno-octulosonyl-2',3',2',3'-tetrakis(beta-hydroxymyristoyl)-D-glucosaminyl-1,6-beta-D-glucosamine 1,4'-bisphosphate; alpha-Kdo-(2->6)-[lipid IVA]

## Pathways

- `eco00540` Lipopolysaccharide biosynthesis (KEGG)

## Outgoing Edges (3)

- `is_product_of` --> [[reaction.R04658|reaction.R04658]] `KEGG` `database` - C04919 + C04121 <=> C06024 + C00055
- `is_product_of` --> [[reaction.ecocyc.KDOTRANS-RXN|reaction.ecocyc.KDOTRANS-RXN]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` --> [[reaction.ecocyc.KDOTRANS2-RXN|reaction.ecocyc.KDOTRANS2-RXN]] `EcoCyc` `database` - EcoCyc reaction LEFT

## Incoming Edges (0)

_None._

## External IDs

- `KEGG:C06024`

## Notes

Included because it appears in at least one E. coli KEGG pathway.
