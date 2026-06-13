---
entity_id: "molecule.C06251"
entity_type: "small_molecule"
name: "Lauroyl-KDO2-lipid IV(A)"
source_database: "KEGG"
source_id: "C06251"
default_state: "low"
allowed_states: "absent|low|medium|high"
subcellular_location: ""
enriched_summary_quality: "placeholder"
tags:
  - entity/small_molecule
  - source/KEGG
aliases:
  - "Lauroyl-KDO2-lipid IV(A)"
  - "Dodecanoyl-KDO2-lipid IV(A)"
---

# Lauroyl-KDO2-lipid IV(A)

`molecule.C06251`

## Static

- Type: `small_molecule`
- Source: `KEGG:C06251`
- Default state: `low`
- Allowed states: `absent|low|medium|high`

## Enriched Summary

KEGG compound: Lauroyl-KDO2-lipid IV(A); Dodecanoyl-KDO2-lipid IV(A) EcoCyc common name: α-Kdo-(2->4)-α-Kdo-(2->6)-(lauroyl)-lipid IVA (E. coli).

## Biological Role

Consumed as substrate in 1 reaction(s). Produced in 1 reaction(s).

## Enriched Pathways

- `eco00540` Lipopolysaccharide biosynthesis (KEGG)

## Annotation

KEGG compound: Lauroyl-KDO2-lipid IV(A); Dodecanoyl-KDO2-lipid IV(A)

## Pathways

- `eco00540` Lipopolysaccharide biosynthesis (KEGG)

## Outgoing Edges (2)

- `is_product_of` --> [[reaction.ecocyc.LAUROYLACYLTRAN-RXN|reaction.ecocyc.LAUROYLACYLTRAN-RXN]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` --> [[reaction.ecocyc.MYRISTOYLACYLTRAN-RXN|reaction.ecocyc.MYRISTOYLACYLTRAN-RXN]] `EcoCyc` `database` - EcoCyc reaction LEFT

## Incoming Edges (0)

_None._

## External IDs

- `KEGG:C06251`

## Notes

Included because it appears in at least one E. coli KEGG pathway.
