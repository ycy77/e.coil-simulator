---
entity_id: "protein.P07023"
entity_type: "protein"
name: "tyrA"
source_database: "UniProt"
source_id: "P07023"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cytoplasm."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "tyrA b2600 JW2581"
---

# tyrA

`protein.P07023`

## Static

- Type: `protein`
- Source: `UniProt:P07023`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cytoplasm.

## Enriched Summary

T-protein [Includes: Chorismate mutase (CM) (EC 5.4.99.5); Prephenate dehydrogenase (PDH) (EC 1.3.1.12)]

## Biological Role

Catalyzes prephenate:NAD+ oxidoreductase(decarboxylating) (reaction.R01728). Component of fused chorismate mutase/prephenate dehydrogenase (complex.ecocyc.CHORISMUTPREPHENDEHYDROG-CPLX).

## Enriched Pathways

- `eco00400` Phenylalanine, tyrosine and tryptophan biosynthesis (KEGG)
- `eco00401` Novobiocin biosynthesis (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01110` Biosynthesis of secondary metabolites (KEGG)
- `eco01230` Biosynthesis of amino acids (KEGG)

## Annotation

T-protein [Includes: Chorismate mutase (CM) (EC 5.4.99.5); Prephenate dehydrogenase (PDH) (EC 1.3.1.12)]

## Pathways

- `eco00400` Phenylalanine, tyrosine and tryptophan biosynthesis (KEGG)
- `eco00401` Novobiocin biosynthesis (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01110` Biosynthesis of secondary metabolites (KEGG)
- `eco01230` Biosynthesis of amino acids (KEGG)

## Outgoing Edges (2)

- `catalyzes` --> [[reaction.R01728|reaction.R01728]] `KEGG` `database` - via EC:1.3.1.12
- `is_component_of` --> [[complex.ecocyc.CHORISMUTPREPHENDEHYDROG-CPLX|complex.ecocyc.CHORISMUTPREPHENDEHYDROG-CPLX]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2

## Incoming Edges (1)

- `encodes` <-- [[gene.b2600|gene.b2600]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P07023`
- `KEGG:ecj:JW2581;eco:b2600;ecoc:C3026_14400;`
- `GeneID:947115;`
- `GO:GO:0004106; GO:0004665; GO:0005737; GO:0006571; GO:0008977; GO:0009094; GO:0042803; GO:0046417; GO:0070403`
- `EC:1.3.1.12; 5.4.99.5`

## Notes

T-protein [Includes: Chorismate mutase (CM) (EC 5.4.99.5); Prephenate dehydrogenase (PDH) (EC 1.3.1.12)]
