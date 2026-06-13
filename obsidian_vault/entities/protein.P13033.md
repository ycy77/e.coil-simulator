---
entity_id: "protein.P13033"
entity_type: "protein"
name: "glpB"
source_database: "UniProt"
source_id: "P13033"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cell inner membrane; Peripheral membrane protein. Note=Loosely bound to the cytoplasmic membrane often occurring in vesicles associated with fumarate reductase."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "glpB b2242 JW2236"
---

# glpB

`protein.P13033`

## Static

- Type: `protein`
- Source: `UniProt:P13033`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cell inner membrane; Peripheral membrane protein. Note=Loosely bound to the cytoplasmic membrane often occurring in vesicles associated with fumarate reductase.

## Enriched Summary

FUNCTION: Conversion of glycerol 3-phosphate to dihydroxyacetone. Uses fumarate or nitrate as electron acceptor. glpB encodes a subunit of the heterotrimeric glycerol-3-phosphate dehydrogenase complex. In anaerobic conditions this respiratory enzyme converts glycerol-3-phosphate to dihydroxyacetone phosphate (DHAP) using fumarate as a terminal electron acceptor. GlpB contains a predicted flavin mononucleotide-binding domain glpB was among the genes induced during phosphate starvation .

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

- `encodes` <-- [[gene.b2242|gene.b2242]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P13033`
- `KEGG:ecj:JW2236;eco:b2242;ecoc:C3026_12525;`
- `GeneID:946733;`
- `GO:GO:0004368; GO:0005829; GO:0005886; GO:0009061; GO:0009331; GO:0010181; GO:0019563; GO:0046168`
- `EC:1.1.5.3`

## Notes

Anaerobic glycerol-3-phosphate dehydrogenase subunit B (Anaerobic G-3-P dehydrogenase subunit B) (Anaerobic G3Pdhase B) (EC 1.1.5.3)
