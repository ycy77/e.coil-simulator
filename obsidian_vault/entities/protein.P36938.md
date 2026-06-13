---
entity_id: "protein.P36938"
entity_type: "protein"
name: "pgm"
source_database: "UniProt"
source_id: "P36938"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cytoplasm {ECO:0000269|PubMed:21778229}."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "pgm b0688 JW0675"
---

# pgm

`protein.P36938`

## Static

- Type: `protein`
- Source: `UniProt:P36938`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cytoplasm {ECO:0000269|PubMed:21778229}.

## Enriched Summary

FUNCTION: This enzyme participates in both the breakdown and synthesis of glucose. {ECO:0000269|PubMed:14216423}. Phosphoglucomutase is involved in the breakdown of glycogen and metabolism of galactose and maltose. Pgm forms a complex with GLU6PDEHYDROG-MONOMER, which uses the product of Pgm, GLC-1-P, to produce D-6-P-GLUCONO-DELTA-LACTONE . Phosphoglucomutase was found to be a modulator of chromosomal supercoiling. Its role in mediating chromosome topology may be indirect . pgm mutants are thought to accumulate maltodextrin due to reversal of the reaction catalyzed by MALDEXPHOSPHORYL-CPLX, leading to the Blu phenotype (blue color when stained with iodine) . Amylose begins to accumulate when the pgm expression level is below 10% of wild type levels . In a genome-wide screen of single-gene knockout mutants of E. coli K-12 (the Keio collection), a pgm mutant was shown to be defective in swarming and swimming ability, as expected for the role of this enzyme in energy production . In another genome-wide screen of the Keio collection, pgm mutants displayed a glycogen-less phenotype as expected from the role of α-D-glucose 1-phosphate in glycogen metabolism (see pathways GLYCOCAT-PWY and GLYCOGENSYNTH-PWY). A nonsense mutation (Y324*) suppresses the low-temperature vancomycin sensitivity of E...

## Biological Role

Catalyzes PHOSPHOGLUCMUT-RXN (reaction.ecocyc.PHOSPHOGLUCMUT-RXN). Bound by Magnesium cation (molecule.C00305).

## Enriched Pathways

- `eco00010` Glycolysis / Gluconeogenesis (KEGG)
- `eco00030` Pentose phosphate pathway (KEGG)
- `eco00052` Galactose metabolism (KEGG)
- `eco00230` Purine metabolism (KEGG)
- `eco00500` Starch and sucrose metabolism (KEGG)
- `eco00520` Amino sugar and nucleotide sugar metabolism (KEGG)
- `eco00521` Streptomycin biosynthesis (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01110` Biosynthesis of secondary metabolites (KEGG)
- `eco01120` Microbial metabolism in diverse environments (KEGG)
- `eco01250` Biosynthesis of nucleotide sugars (KEGG)

## Annotation

FUNCTION: This enzyme participates in both the breakdown and synthesis of glucose. {ECO:0000269|PubMed:14216423}.

## Pathways

- `eco00010` Glycolysis / Gluconeogenesis (KEGG)
- `eco00030` Pentose phosphate pathway (KEGG)
- `eco00052` Galactose metabolism (KEGG)
- `eco00230` Purine metabolism (KEGG)
- `eco00500` Starch and sucrose metabolism (KEGG)
- `eco00520` Amino sugar and nucleotide sugar metabolism (KEGG)
- `eco00521` Streptomycin biosynthesis (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01110` Biosynthesis of secondary metabolites (KEGG)
- `eco01120` Microbial metabolism in diverse environments (KEGG)
- `eco01250` Biosynthesis of nucleotide sugars (KEGG)

## Outgoing Edges (1)

- `catalyzes` --> [[reaction.ecocyc.PHOSPHOGLUCMUT-RXN|reaction.ecocyc.PHOSPHOGLUCMUT-RXN]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (2)

- `binds` <-- [[molecule.C00305|molecule.C00305]] `EcoCyc` `database` - EcoCyc enzymatic reaction cofactor
- `encodes` <-- [[gene.b0688|gene.b0688]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P36938`
- `KEGG:ecj:JW0675;eco:b0688;ecoc:C3026_03430;`
- `GeneID:86863196;945271;`
- `GO:GO:0000287; GO:0004614; GO:0005829; GO:0005975; GO:0006006`
- `EC:5.4.2.2`

## Notes

Phosphoglucomutase (PGM) (EC 5.4.2.2) (Glucose phosphomutase)
