---
entity_id: "protein.P52647"
entity_type: "protein"
name: "ydbK"
source_database: "UniProt"
source_id: "P52647"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "ydbK b1378 JW1372"
---

# ydbK

`protein.P52647`

## Static

- Type: `protein`
- Source: `UniProt:P52647`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`

## Enriched Summary

FUNCTION: Oxidoreductase required for the transfer of electrons from pyruvate to flavodoxin. {ECO:0000305}. Based on sequence similarity, YdbK is predicted to function as a pyruvate:flavodoxin oxidoreductase and/or pyruvate synthase . The activity has been assayed in crude extracts with methyl viologen as the electron acceptor . Coexpression of YdbK with a heterologous hydrogenase enzyme enhances the production of hydrogen; the effect depends on the coexpression of an E. coli flavodoxin or a heterologous ferredoxin . Overexpression of YdbK in an engineered strain that utilizes ethanol aerobically as the sole source of carbon and secretes valine enables better growth and higher valine production, suggesting enhanced availability of pyruvate . The authors of suggest that YdbK is most likely the enzyme characterized by , PYRUFLAVREDUCT-MONOMER. Under the conditions employed by , the enzyme may function in the direction of pyruvate synthesis. A ydbK mutant is unable to grow on glucose under oxidative stress conditions . ydbK is needed for superoxide resistance during growth on minimal medium , and a ydbK fpr double mutant is sensitive to methyl viologen . Expression of ydbK is induced by superoxide and is SoxS-dependent .

## Biological Role

Catalyzes pyruvate:flavodoxin 2-oxidoreductase (CoA-acetylating) (reaction.R10866), PYFLAVOXRE-RXN (reaction.ecocyc.PYFLAVOXRE-RXN). Bound by Thiamin diphosphate (molecule.C00068), a [4Fe-4S] iron-sulfur cluster (molecule.ecocyc.CPD-7).

## Enriched Pathways

- `eco00010` Glycolysis / Gluconeogenesis (KEGG)
- `eco00020` Citrate cycle (TCA cycle) (KEGG)
- `eco00620` Pyruvate metabolism (KEGG)
- `eco00650` Butanoate metabolism (KEGG)
- `eco00720` Other carbon fixation pathways (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01110` Biosynthesis of secondary metabolites (KEGG)
- `eco01120` Microbial metabolism in diverse environments (KEGG)
- `eco01200` Carbon metabolism (KEGG)
- `eco01210` 2-Oxocarboxylic acid metabolism (KEGG)

## Annotation

FUNCTION: Oxidoreductase required for the transfer of electrons from pyruvate to flavodoxin. {ECO:0000305}.

## Pathways

- `eco00010` Glycolysis / Gluconeogenesis (KEGG)
- `eco00020` Citrate cycle (TCA cycle) (KEGG)
- `eco00620` Pyruvate metabolism (KEGG)
- `eco00650` Butanoate metabolism (KEGG)
- `eco00720` Other carbon fixation pathways (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01110` Biosynthesis of secondary metabolites (KEGG)
- `eco01120` Microbial metabolism in diverse environments (KEGG)
- `eco01200` Carbon metabolism (KEGG)
- `eco01210` 2-Oxocarboxylic acid metabolism (KEGG)

## Outgoing Edges (2)

- `catalyzes` --> [[reaction.R10866|reaction.R10866]] `KEGG` `database` - via EC:1.2.8.1
- `catalyzes` --> [[reaction.ecocyc.PYFLAVOXRE-RXN|reaction.ecocyc.PYFLAVOXRE-RXN]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (3)

- `binds` <-- [[molecule.C00068|molecule.C00068]] `EcoCyc` `database` - EcoCyc enzymatic reaction cofactor
- `binds` <-- [[molecule.ecocyc.CPD-7|molecule.ecocyc.CPD-7]] `EcoCyc` `database` - EcoCyc enzymatic reaction cofactor
- `encodes` <-- [[gene.b1378|gene.b1378]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P52647`
- `KEGG:ecj:JW1372;eco:b1378;ecoc:C3026_08050;`
- `GeneID:946587;`
- `GO:GO:0005506; GO:0006979; GO:0022900; GO:0043873; GO:0051539`
- `EC:1.2.7.-`

## Notes

Probable pyruvate-flavodoxin oxidoreductase (EC 1.2.7.-)
