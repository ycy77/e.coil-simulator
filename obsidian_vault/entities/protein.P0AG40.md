---
entity_id: "protein.P0AG40"
entity_type: "protein"
name: "ribF"
source_database: "UniProt"
source_id: "P0AG40"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "ribF yaaC b0025 JW0023"
---

# ribF

`protein.P0AG40`

## Static

- Type: `protein`
- Source: `UniProt:P0AG40`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`

## Enriched Summary

FUNCTION: Catalyzes the phosphorylation of riboflavin to FMN followed by the adenylation of FMN to FAD. {ECO:0000250|UniProtKB:Q59263}. It is thought that ribF encodes a bifunctional protein with riboflavin kinase and FMN adenylyltransferase activities. These enzymes transform riboflavin into the coenzyme forms of FMN and FAD, respectively . A published patent contains experimental evidence that partial deletions or point mutations in the N-terminal domain of RibF ("protein X") selectively affect the FMN adenylyltransferase activity of the enzyme . ribF can complement the lethal defect of a ribC mutant (lacking riboflavin kinase and FMN adenylyltransferase activities) in Bacillus subtilis . The G23 residue appears to be essential for the FMN adenylyltrasferase, but not the riboflavin kinase activity . ribF is likely essential for growth in E. coli .

## Biological Role

Catalyzes ATP:FMN adenylyltransferase (reaction.R00161), ATP:riboflavin 5'-phosphotransferase (reaction.R00549), FADSYN-RXN (reaction.ecocyc.FADSYN-RXN), RIBOFLAVINKIN-RXN (reaction.ecocyc.RIBOFLAVINKIN-RXN).

## Enriched Pathways

- `eco00740` Riboflavin metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01110` Biosynthesis of secondary metabolites (KEGG)
- `eco01240` Biosynthesis of cofactors (KEGG)

## Annotation

FUNCTION: Catalyzes the phosphorylation of riboflavin to FMN followed by the adenylation of FMN to FAD. {ECO:0000250|UniProtKB:Q59263}.

## Pathways

- `eco00740` Riboflavin metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01110` Biosynthesis of secondary metabolites (KEGG)
- `eco01240` Biosynthesis of cofactors (KEGG)

## Outgoing Edges (4)

- `catalyzes` --> [[reaction.R00161|reaction.R00161]] `KEGG` `database` - via EC:2.7.7.2
- `catalyzes` --> [[reaction.R00549|reaction.R00549]] `KEGG` `database` - via EC:2.7.1.26
- `catalyzes` --> [[reaction.ecocyc.FADSYN-RXN|reaction.ecocyc.FADSYN-RXN]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` --> [[reaction.ecocyc.RIBOFLAVINKIN-RXN|reaction.ecocyc.RIBOFLAVINKIN-RXN]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (1)

- `encodes` <-- [[gene.b0025|gene.b0025]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P0AG40`
- `KEGG:ecj:JW0023;eco:b0025;ecoc:C3026_00120;`
- `GeneID:93777411;949129;`
- `GO:GO:0003919; GO:0005524; GO:0006747; GO:0006771; GO:0008531; GO:0009231; GO:0009398`
- `EC:2.7.1.26; 2.7.7.2`

## Notes

Bifunctional riboflavin kinase/FMN adenylyltransferase (Riboflavin biosynthesis protein RibF) [Includes: Riboflavin kinase (EC 2.7.1.26) (Flavokinase); FMN adenylyltransferase (EC 2.7.7.2) (FAD pyrophosphorylase) (FAD synthase)]
