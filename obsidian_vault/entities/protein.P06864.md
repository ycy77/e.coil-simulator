---
entity_id: "protein.P06864"
entity_type: "protein"
name: "ebgA"
source_database: "UniProt"
source_id: "P06864"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "ebgA b3076 JW5511"
---

# ebgA

`protein.P06864`

## Static

- Type: `protein`
- Source: `UniProt:P06864`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`

## Enriched Summary

FUNCTION: The wild-type enzyme is an ineffective lactase. Two classes of point mutations dramatically improve activity of the enzyme.

## Biological Role

Catalyzes R07807 (reaction.R07807). Component of evolved β-D-galactosidase (complex.ecocyc.CPLX0-3937).

## Enriched Pathways

- `eco00052` Galactose metabolism (KEGG)
- `eco00511` Other glycan degradation (KEGG)
- `eco01100` Metabolic pathways (KEGG)

## Annotation

FUNCTION: The wild-type enzyme is an ineffective lactase. Two classes of point mutations dramatically improve activity of the enzyme.

## Pathways

- `eco00052` Galactose metabolism (KEGG)
- `eco00511` Other glycan degradation (KEGG)
- `eco01100` Metabolic pathways (KEGG)

## Outgoing Edges (2)

- `catalyzes` --> [[reaction.R07807|reaction.R07807]] `KEGG` `database` - via EC:3.2.1.23
- `is_component_of` --> [[complex.ecocyc.CPLX0-3937|complex.ecocyc.CPLX0-3937]] `EcoCyc` `database` - EcoCyc component coefficient=4 | EcoCyc protcplxs.col coefficient=4

## Incoming Edges (1)

- `encodes` <-- [[gene.b3076|gene.b3076]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P06864`
- `KEGG:ecj:JW5511;eco:b3076;ecoc:C3026_16800;`
- `GeneID:947583;`
- `GO:GO:0004565; GO:0005990; GO:0009341; GO:0030246`
- `EC:3.2.1.23`

## Notes

Evolved beta-galactosidase subunit alpha (Beta-gal) (EC 3.2.1.23) (Lactase)
