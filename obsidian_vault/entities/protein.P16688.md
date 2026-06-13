---
entity_id: "protein.P16688"
entity_type: "protein"
name: "phnJ"
source_database: "UniProt"
source_id: "P16688"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "phnJ b4098 JW4059"
---

# phnJ

`protein.P16688`

## Static

- Type: `protein`
- Source: `UniProt:P16688`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`

## Enriched Summary

FUNCTION: Catalyzes the breakage of the C-P bond in alpha-D-ribose 1-methylphosphonate 5-phosphate (PRPn) forming alpha-D-ribose 1,2-cyclic phosphate 5-phosphate (PRcP). {ECO:0000269|PubMed:22089136}. PhnJ is a radical SAM enzyme that catalyzes the cleavage of CPD0-2480 (PRPn) to CPD0-2463 (PRcP). Activity requires anaerobic reconstitution of a [4Fe-4S] cluster and the presence of dithionite . PhnJ was also found to be a component of a protein complex that was thought to catalyze the carbon-phosphorus lyase reaction . phnJ is part of an operon that is phosphate starvation-inducible and required for use of phosphonate and phosphite as phosphorous sources . PhnJ appears to be required for carbon-phosphorous lyase activity . A phnJ mutant accumulates presumed intermediates of the C-P lyase pathway of phosphonate degradation .

## Biological Role

Catalyzes RXN-17956 (reaction.ecocyc.RXN-17956), RXN0-6734 (reaction.ecocyc.RXN0-6734). Component of carbon-phosphorus lyase core complex (complex.ecocyc.CPLX0-10309), carbon-phosphorus lyase core complex (complex.ecocyc.CPLX0-7935), carbon-phosphorus lyase system (complex.ecocyc.CPLX0-7958). Bound by a [4Fe-4S] iron-sulfur cluster (molecule.ecocyc.CPD-7).

## Enriched Pathways

- `eco00440` Phosphonate and phosphinate metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)

## Annotation

FUNCTION: Catalyzes the breakage of the C-P bond in alpha-D-ribose 1-methylphosphonate 5-phosphate (PRPn) forming alpha-D-ribose 1,2-cyclic phosphate 5-phosphate (PRcP). {ECO:0000269|PubMed:22089136}.

## Pathways

- `eco00440` Phosphonate and phosphinate metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)

## Outgoing Edges (5)

- `catalyzes` --> [[reaction.ecocyc.RXN-17956|reaction.ecocyc.RXN-17956]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` --> [[reaction.ecocyc.RXN0-6734|reaction.ecocyc.RXN0-6734]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_component_of` --> [[complex.ecocyc.CPLX0-10309|complex.ecocyc.CPLX0-10309]] `EcoCyc` `database` - EcoCyc protcplxs.col coefficient=2
- `is_component_of` --> [[complex.ecocyc.CPLX0-7935|complex.ecocyc.CPLX0-7935]] `EcoCyc` `database` - EcoCyc component coefficient=1 | EcoCyc protcplxs.col coefficient=1
- `is_component_of` --> [[complex.ecocyc.CPLX0-7958|complex.ecocyc.CPLX0-7958]] `EcoCyc` `database` - EcoCyc protcplxs.col coefficient=2

## Incoming Edges (2)

- `binds` <-- [[molecule.ecocyc.CPD-7|molecule.ecocyc.CPD-7]] `EcoCyc` `database` - EcoCyc enzymatic reaction cofactor
- `encodes` <-- [[gene.b4098|gene.b4098]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P16688`
- `KEGG:ecj:JW4059;eco:b4098;ecoc:C3026_22150;`
- `GeneID:948606;`
- `GO:GO:0015716; GO:0016829; GO:0019634; GO:0019700; GO:0046872; GO:0051539; GO:0061694; GO:0098848; GO:1904176`
- `EC:4.7.1.1`

## Notes

Alpha-D-ribose 1-methylphosphonate 5-phosphate C-P lyase (PRPn C-P lyase) (EC 4.7.1.1)
