---
entity_id: "protein.P0A9C0"
entity_type: "protein"
name: "glpA"
source_database: "UniProt"
source_id: "P0A9C0"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cell inner membrane; Peripheral membrane protein. Note=Loosely bound to the cytoplasmic membrane often occurring in vesicles associated with fumarate reductase."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "glpA b2241 JW2235"
---

# glpA

`protein.P0A9C0`

## Static

- Type: `protein`
- Source: `UniProt:P0A9C0`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cell inner membrane; Peripheral membrane protein. Note=Loosely bound to the cytoplasmic membrane often occurring in vesicles associated with fumarate reductase.

## Enriched Summary

FUNCTION: Conversion of glycerol 3-phosphate to dihydroxyacetone. Uses fumarate or nitrate as electron acceptor. GlpA is the large subunit of a three subunit glycerol-3-phosphate dehydrogenase complex. In anaerobic conditions this respiratory enzyme converts glycerol-3-phosphate to dihydroxyacetone phosphate (DHAP) using fumarate as a terminal electron acceptor. The GlpA subunit contains noncovalently bound FAD. .

## Biological Role

Catalyzes sn-glycerol-3-phosphate:(acceptor) 2-oxidoreductase (reaction.R00848), sn-glycerol 3-phosphate:quinone oxidoreductase (reaction.R00849). Component of anaerobic glycerol-3-phosphate dehydrogenase (complex.ecocyc.ANGLYC3PDEHYDROG-CPLX).

## Enriched Pathways

- `eco00564` Glycerophospholipid metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01110` Biosynthesis of secondary metabolites (KEGG)

## Annotation

FUNCTION: Conversion of glycerol 3-phosphate to dihydroxyacetone. Uses fumarate or nitrate as electron acceptor.

## Pathways

- `eco00564` Glycerophospholipid metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01110` Biosynthesis of secondary metabolites (KEGG)

## Outgoing Edges (3)

- `catalyzes` --> [[reaction.R00848|reaction.R00848]] `KEGG` `database` - via EC:1.1.5.3
- `catalyzes` --> [[reaction.R00849|reaction.R00849]] `KEGG` `database` - via EC:1.1.5.3
- `is_component_of` --> [[complex.ecocyc.ANGLYC3PDEHYDROG-CPLX|complex.ecocyc.ANGLYC3PDEHYDROG-CPLX]] `EcoCyc` `database` - EcoCyc component coefficient=1 | EcoCyc protcplxs.col coefficient=1

## Incoming Edges (1)

- `encodes` <-- [[gene.b2241|gene.b2241]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P0A9C0`
- `KEGG:ecj:JW2235;eco:b2241;ecoc:C3026_12520;`
- `GeneID:93774933;946713;`
- `GO:GO:0004368; GO:0005829; GO:0005886; GO:0009061; GO:0009331; GO:0010181; GO:0019563; GO:0046168; GO:0050660`
- `EC:1.1.5.3`

## Notes

Anaerobic glycerol-3-phosphate dehydrogenase subunit A (G-3-P dehydrogenase) (EC 1.1.5.3)
