---
entity_id: "protein.P0A870"
entity_type: "protein"
name: "talB"
source_database: "UniProt"
source_id: "P0A870"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cytoplasm {ECO:0000305}."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "talB yaaK b0008 JW0007"
---

# talB

`protein.P0A870`

## Static

- Type: `protein`
- Source: `UniProt:P0A870`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cytoplasm {ECO:0000305}.

## Enriched Summary

FUNCTION: Transaldolase is important for the balance of metabolites in the pentose-phosphate pathway. {ECO:0000269|PubMed:18687684, ECO:0000269|PubMed:7592346}. Transaldolase B is an enzyme of the non-oxidative branch of the pentose phosphate pathway. Along with transketolase, transaldolase creates a reversible link between the pentose phosphate pathway and glycolysis. It catalyzes the interconversion of glyceraldehyde-3-phosphate and sedoheptulose-7-phosphate to fructose-6-phosphate and erythrose-4-phosphate. The reversibility of this reaction and carbon flux through the pentose phosphate pathway has been addressed both experimentally (summarized in ) and theoretically . There are two closely related transaldolases in E. coli, encoded by talA and talB. Only transaldolase B has been biochemically characterized. TalB is a dimer in solution and in the crystal structure . Mutation of the R300 residue leads to the formation of catalytically active monomers . Catalytically important active site residues have been identified by site-directed mutagenesis . Crystal structures of transaldolase B have been determined, confirming the presence of a Schiff-base intermediate at the active site and leading to a proposed reaction mechanism . A talB null mutant has no growth defect on minimal media with glucose as the carbon source...

## Biological Role

Component of transaldolase B (complex.ecocyc.TRANSALDOLB-CPLX).

## Enriched Pathways

- `eco00030` Pentose phosphate pathway (KEGG)
- `eco00710` Carbon fixation by Calvin cycle (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01110` Biosynthesis of secondary metabolites (KEGG)
- `eco01120` Microbial metabolism in diverse environments (KEGG)
- `eco01200` Carbon metabolism (KEGG)
- `eco01230` Biosynthesis of amino acids (KEGG)

## Annotation

FUNCTION: Transaldolase is important for the balance of metabolites in the pentose-phosphate pathway. {ECO:0000269|PubMed:18687684, ECO:0000269|PubMed:7592346}.

## Pathways

- `eco00030` Pentose phosphate pathway (KEGG)
- `eco00710` Carbon fixation by Calvin cycle (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01110` Biosynthesis of secondary metabolites (KEGG)
- `eco01120` Microbial metabolism in diverse environments (KEGG)
- `eco01200` Carbon metabolism (KEGG)
- `eco01230` Biosynthesis of amino acids (KEGG)

## Outgoing Edges (1)

- `is_component_of` --> [[complex.ecocyc.TRANSALDOLB-CPLX|complex.ecocyc.TRANSALDOLB-CPLX]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2

## Incoming Edges (1)

- `encodes` <-- [[gene.b0008|gene.b0008]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P0A870`
- `KEGG:ecj:JW0007;eco:b0008;ecoc:C3026_00045;`
- `GeneID:93777434;944748;`
- `GO:GO:0004801; GO:0005829; GO:0005975; GO:0009052; GO:0016020; GO:0016744`
- `EC:2.2.1.2`

## Notes

Transaldolase B (EC 2.2.1.2)
