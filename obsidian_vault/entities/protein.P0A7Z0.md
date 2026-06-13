---
entity_id: "protein.P0A7Z0"
entity_type: "protein"
name: "rpiA"
source_database: "UniProt"
source_id: "P0A7Z0"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "rpiA ygfC b2914 JW5475"
---

# rpiA

`protein.P0A7Z0`

## Static

- Type: `protein`
- Source: `UniProt:P0A7Z0`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`

## Enriched Summary

FUNCTION: Involved in the first step of the non-oxidative branch of the pentose phosphate pathway. It catalyzes the reversible conversion of ribose-5-phosphate to ribulose 5-phosphate. Can also act on D-ribose-5-diphosphate and D-ribose-5-triphosphate as substrate. {ECO:0000269|PubMed:1104357, ECO:0000269|PubMed:12517338, ECO:0000269|PubMed:4909663}. There are two physically and genetically distinct ribose-5-phosphate isomerases present in E. coli . The constitutive ribose-5-phosphate isomerase A (RpiA) normally accounts for more than 99% of the ribose-5-phosphate isomerase activity in the cell and functions in the NONOXIPENT-PWY . The inducible ribose-5-phosphate isomerase B can substitute for RpiA's function if its expression is induced . There is no sequence similarity between the two enzymes . Crystal structures of RpiA have been solved and active site residues and an acid-base catalytic mechanism were predicted . An rpiA mutant requires ribose for growth . RpiA: "ribosephosphate isomerase A" Review:

## Biological Role

Catalyzes D-allose-6-phosphate aldose-ketose-isomerase (reaction.R09030). Component of ribose-5-phosphate isomerase A (complex.ecocyc.RIB5PISOMA-CPLX).

## Enriched Pathways

- `eco00030` Pentose phosphate pathway (KEGG)
- `eco00710` Carbon fixation by Calvin cycle (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01110` Biosynthesis of secondary metabolites (KEGG)
- `eco01120` Microbial metabolism in diverse environments (KEGG)
- `eco01200` Carbon metabolism (KEGG)
- `eco01230` Biosynthesis of amino acids (KEGG)

## Annotation

FUNCTION: Involved in the first step of the non-oxidative branch of the pentose phosphate pathway. It catalyzes the reversible conversion of ribose-5-phosphate to ribulose 5-phosphate. Can also act on D-ribose-5-diphosphate and D-ribose-5-triphosphate as substrate. {ECO:0000269|PubMed:1104357, ECO:0000269|PubMed:12517338, ECO:0000269|PubMed:4909663}.

## Pathways

- `eco00030` Pentose phosphate pathway (KEGG)
- `eco00710` Carbon fixation by Calvin cycle (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01110` Biosynthesis of secondary metabolites (KEGG)
- `eco01120` Microbial metabolism in diverse environments (KEGG)
- `eco01200` Carbon metabolism (KEGG)
- `eco01230` Biosynthesis of amino acids (KEGG)

## Outgoing Edges (2)

- `catalyzes` --> [[reaction.R09030|reaction.R09030]] `KEGG` `database` - via EC:5.3.1.6
- `is_component_of` --> [[complex.ecocyc.RIB5PISOMA-CPLX|complex.ecocyc.RIB5PISOMA-CPLX]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2

## Incoming Edges (1)

- `encodes` <-- [[gene.b2914|gene.b2914]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P0A7Z0`
- `KEGG:ecj:JW5475;eco:b2914;ecoc:C3026_15970;`
- `GeneID:93779085;947407;`
- `GO:GO:0004751; GO:0005829; GO:0006014; GO:0009052; GO:0042802; GO:0042803`
- `EC:5.3.1.6`

## Notes

Ribose-5-phosphate isomerase A (EC 5.3.1.6) (Phosphoriboisomerase A) (PRI)
