---
entity_id: "protein.P22259"
entity_type: "protein"
name: "pckA"
source_database: "UniProt"
source_id: "P22259"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cytoplasm."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "pckA pck b3403 JW3366"
---

# pckA

`protein.P22259`

## Static

- Type: `protein`
- Source: `UniProt:P22259`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cytoplasm.

## Enriched Summary

FUNCTION: Involved in the gluconeogenesis. Catalyzes the conversion of oxaloacetate (OAA) to phosphoenolpyruvate (PEP) through direct phosphoryl transfer between the nucleoside triphosphate and OAA. {ECO:0000255|HAMAP-Rule:MF_00453, ECO:0000269|PubMed:1701430, ECO:0000269|PubMed:6986370, ECO:0000269|PubMed:8226637}. Phosphoenolpyruvate (PEP) carboxykinase (Pck) is an enzyme involved in gluconeogenesis. Growth on succinate as the carbon and energy source is limited by the level of Pck in the cell . PEP carboxykinase is unusual in that it appears to be a monomeric enzyme with an allosteric site . Crystal structures of the enzyme have been solved , providing insight into the mechanistic details of the enzymatic reaction and into the mechanism of activation by Ca2+ . Transcription of pck is regulated by catabolite repression and is induced at the onset of stationary phase and is regulated by CsrA . Overexpression of pck during growth on glucose leads to reduced growth yield and increased excretion of fermentation products such as acetate . Expression of Pck is upregulated when acetate is used as the source of carbon . A double mutant defective in both PEP carboxykinase and PEPSYNTH-CPLX is unable to utilize C4-dicarboxylic acids such as succinate and malate as the sole source of carbon and energy . Reviews:

## Biological Role

Catalyzes ATP:oxaloacetate carboxy-lyase (transphosphorylating;phosphoenolpyruvate-forming) (reaction.R00341), PEPCARBOXYKIN-RXN (reaction.ecocyc.PEPCARBOXYKIN-RXN). Bound by Magnesium cation (molecule.C00305).

## Enriched Pathways

- `eco00010` Glycolysis / Gluconeogenesis (KEGG)
- `eco00020` Citrate cycle (TCA cycle) (KEGG)
- `eco00620` Pyruvate metabolism (KEGG)
- `eco00710` Carbon fixation by Calvin cycle (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01110` Biosynthesis of secondary metabolites (KEGG)
- `eco01120` Microbial metabolism in diverse environments (KEGG)
- `eco01200` Carbon metabolism (KEGG)

## Annotation

FUNCTION: Involved in the gluconeogenesis. Catalyzes the conversion of oxaloacetate (OAA) to phosphoenolpyruvate (PEP) through direct phosphoryl transfer between the nucleoside triphosphate and OAA. {ECO:0000255|HAMAP-Rule:MF_00453, ECO:0000269|PubMed:1701430, ECO:0000269|PubMed:6986370, ECO:0000269|PubMed:8226637}.

## Pathways

- `eco00010` Glycolysis / Gluconeogenesis (KEGG)
- `eco00020` Citrate cycle (TCA cycle) (KEGG)
- `eco00620` Pyruvate metabolism (KEGG)
- `eco00710` Carbon fixation by Calvin cycle (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01110` Biosynthesis of secondary metabolites (KEGG)
- `eco01120` Microbial metabolism in diverse environments (KEGG)
- `eco01200` Carbon metabolism (KEGG)

## Outgoing Edges (2)

- `catalyzes` --> [[reaction.R00341|reaction.R00341]] `KEGG` `database` - via EC:4.1.1.49
- `catalyzes` --> [[reaction.ecocyc.PEPCARBOXYKIN-RXN|reaction.ecocyc.PEPCARBOXYKIN-RXN]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (2)

- `binds` <-- [[molecule.C00305|molecule.C00305]] `EcoCyc` `database` - EcoCyc enzymatic reaction cofactor
- `encodes` <-- [[gene.b3403|gene.b3403]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P22259`
- `KEGG:ecj:JW3366;eco:b3403;ecoc:C3026_18465;`
- `GeneID:945667;`
- `GO:GO:0000287; GO:0004612; GO:0005509; GO:0005524; GO:0005829; GO:0006094`
- `EC:4.1.1.49`

## Notes

Phosphoenolpyruvate carboxykinase (ATP) (PCK) (PEP carboxykinase) (PEPCK) (EC 4.1.1.49)
