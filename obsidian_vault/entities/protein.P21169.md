---
entity_id: "protein.P21169"
entity_type: "protein"
name: "speC"
source_database: "UniProt"
source_id: "P21169"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "speC b2965 JW5482"
---

# speC

`protein.P21169`

## Static

- Type: `protein`
- Source: `UniProt:P21169`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`

## Enriched Summary

Constitutive ornithine decarboxylase (EC 4.1.1.17)

## Biological Role

Catalyzes L-ornithine carboxy-lyase (putrescine-forming) (reaction.R00670). Component of constitutive ornithine decarboxylase (complex.ecocyc.ORNDECARBOX-BIO-CPLX).

## Enriched Pathways

- `eco00330` Arginine and proline metabolism (KEGG)
- `eco00480` Glutathione metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01110` Biosynthesis of secondary metabolites (KEGG)

## Annotation

Constitutive ornithine decarboxylase (EC 4.1.1.17)

## Pathways

- `eco00330` Arginine and proline metabolism (KEGG)
- `eco00480` Glutathione metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01110` Biosynthesis of secondary metabolites (KEGG)

## Outgoing Edges (2)

- `catalyzes` --> [[reaction.R00670|reaction.R00670]] `KEGG` `database` - via EC:4.1.1.17
- `is_component_of` --> [[complex.ecocyc.ORNDECARBOX-BIO-CPLX|complex.ecocyc.ORNDECARBOX-BIO-CPLX]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2

## Incoming Edges (1)

- `encodes` <-- [[gene.b2965|gene.b2965]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P21169`
- `KEGG:ecj:JW5482;eco:b2965;ecoc:C3026_16225;`
- `GeneID:947457;`
- `GO:GO:0004586; GO:0005829; GO:0008295; GO:0030170; GO:0033387; GO:0097216`
- `EC:4.1.1.17`

## Notes

Constitutive ornithine decarboxylase (EC 4.1.1.17)
