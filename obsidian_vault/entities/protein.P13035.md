---
entity_id: "protein.P13035"
entity_type: "protein"
name: "glpD"
source_database: "UniProt"
source_id: "P13035"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cytoplasm."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "glpD glyD b3426 JW3389"
---

# glpD

`protein.P13035`

## Static

- Type: `protein`
- Source: `UniProt:P13035`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cytoplasm.

## Enriched Summary

FUNCTION: Conversion of glycerol 3-phosphate to dihydroxyacetone. Uses molecular oxygen or nitrate as electron acceptor.

## Biological Role

Catalyzes sn-glycerol-3-phosphate:(acceptor) 2-oxidoreductase (reaction.R00848), sn-glycerol 3-phosphate:quinone oxidoreductase (reaction.R00849). Component of aerobic glycerol 3-phosphate dehydrogenase (complex.ecocyc.AERGLYC3PDEHYDROG-CPLX).

## Enriched Pathways

- `eco00564` Glycerophospholipid metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01110` Biosynthesis of secondary metabolites (KEGG)

## Annotation

FUNCTION: Conversion of glycerol 3-phosphate to dihydroxyacetone. Uses molecular oxygen or nitrate as electron acceptor.

## Pathways

- `eco00564` Glycerophospholipid metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01110` Biosynthesis of secondary metabolites (KEGG)

## Outgoing Edges (3)

- `catalyzes` --> [[reaction.R00848|reaction.R00848]] `KEGG` `database` - via EC:1.1.5.3
- `catalyzes` --> [[reaction.R00849|reaction.R00849]] `KEGG` `database` - via EC:1.1.5.3
- `is_component_of` --> [[complex.ecocyc.AERGLYC3PDEHYDROG-CPLX|complex.ecocyc.AERGLYC3PDEHYDROG-CPLX]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2

## Incoming Edges (1)

- `encodes` <-- [[gene.b3426|gene.b3426]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P13035`
- `KEGG:ecj:JW3389;eco:b3426;ecoc:C3026_18575;`
- `GeneID:947934;`
- `GO:GO:0004368; GO:0005886; GO:0009055; GO:0009060; GO:0009061; GO:0009331; GO:0019563; GO:0042803; GO:0046168; GO:0071949`
- `EC:1.1.5.3`

## Notes

Aerobic glycerol-3-phosphate dehydrogenase (EC 1.1.5.3)
