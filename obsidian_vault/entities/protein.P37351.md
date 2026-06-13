---
entity_id: "protein.P37351"
entity_type: "protein"
name: "rpiB"
source_database: "UniProt"
source_id: "P37351"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "rpiB yjcA b4090 JW4051"
---

# rpiB

`protein.P37351`

## Static

- Type: `protein`
- Source: `UniProt:P37351`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`

## Enriched Summary

FUNCTION: Catalyzes the interconversion of ribulose-5-P and ribose-5-P. It probably also has activity on D-allose 6-phosphate. {ECO:0000269|PubMed:1104357, ECO:0000269|PubMed:18640127, ECO:0000269|PubMed:4909663, ECO:0000269|PubMed:8576032}. There are two physically and genetically distinct ribose-5-phosphate isomerases present in E. coli . The constitutive ribose-5-phosphate isomerase A, encoded by the rpiA gene, functions in the NONOXIPENT-PWY. The inducible ribose-5-phosphate isomerase B can substitute for RpiA's function if its expression is induced . There is no sequence similarity between the two enzymes . A crystal structure of RpiB has been solved at 2.2 Å resolution. The enzyme is present as a dimer of dimers in the crystal, and active site residues are located at the dimer interface . A crystal structure of the active site mutant H99N has been solved at 2.1 Å resolution . Expression of rpiB is induced by allose, and an rpiB mutant is unable to catabolize allose . RpiB: "ribosephosphate isomerase B" AlsI: "allose 6-phosphate isomerase" Review:

## Biological Role

Catalyzes D-allose-6-phosphate aldose-ketose-isomerase (reaction.R09030). Component of allose-6-phosphate isomerase / ribose-5-phosphate isomerase B (complex.ecocyc.RIB5PISOMB-CPLX).

## Enriched Pathways

- `eco00030` Pentose phosphate pathway (KEGG)
- `eco00051` Fructose and mannose metabolism (KEGG)
- `eco00710` Carbon fixation by Calvin cycle (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01110` Biosynthesis of secondary metabolites (KEGG)
- `eco01120` Microbial metabolism in diverse environments (KEGG)
- `eco01200` Carbon metabolism (KEGG)
- `eco01230` Biosynthesis of amino acids (KEGG)

## Annotation

FUNCTION: Catalyzes the interconversion of ribulose-5-P and ribose-5-P. It probably also has activity on D-allose 6-phosphate. {ECO:0000269|PubMed:1104357, ECO:0000269|PubMed:18640127, ECO:0000269|PubMed:4909663, ECO:0000269|PubMed:8576032}.

## Pathways

- `eco00030` Pentose phosphate pathway (KEGG)
- `eco00051` Fructose and mannose metabolism (KEGG)
- `eco00710` Carbon fixation by Calvin cycle (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01110` Biosynthesis of secondary metabolites (KEGG)
- `eco01120` Microbial metabolism in diverse environments (KEGG)
- `eco01200` Carbon metabolism (KEGG)
- `eco01230` Biosynthesis of amino acids (KEGG)

## Outgoing Edges (2)

- `catalyzes` --> [[reaction.R09030|reaction.R09030]] `KEGG` `database` - via EC:5.3.1.6
- `is_component_of` --> [[complex.ecocyc.RIB5PISOMB-CPLX|complex.ecocyc.RIB5PISOMB-CPLX]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2

## Incoming Edges (1)

- `encodes` <-- [[gene.b4090|gene.b4090]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P37351`
- `KEGG:ecj:JW4051;eco:b4090;ecoc:C3026_22110;`
- `GeneID:948602;`
- `GO:GO:0004751; GO:0008786; GO:0009052; GO:0019316`
- `EC:5.3.1.6`

## Notes

Ribose-5-phosphate isomerase B (EC 5.3.1.6) (Phosphoriboisomerase B)
