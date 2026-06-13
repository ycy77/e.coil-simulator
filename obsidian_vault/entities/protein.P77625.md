---
entity_id: "protein.P77625"
entity_type: "protein"
name: "hxpA"
source_database: "UniProt"
source_id: "P77625"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "hxpA yfbT b2293 JW5376"
---

# hxpA

`protein.P77625`

## Static

- Type: `protein`
- Source: `UniProt:P77625`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`

## Enriched Summary

FUNCTION: Sugar-phosphate phosphohydrolase that appears to contribute to butanol tolerance (PubMed:27941785). Catalyzes the dephosphorylation of D-mannitol 1-phosphate and D-sorbitol 6-phosphate (PubMed:27941785). Is also able to dephosphorylate other sugar phosphates in vitro including ribose-5-phosphate (Rib5P), 2-deoxyribose-5-phosphate, fructose-1-phosphate (Fru1P), fructose-6-phosphate (Fru6P), and glucose-6-phosphate (Glu6P) (PubMed:16990279). Selectively hydrolyzes beta-D-glucose-1-phosphate (bGlu1P) and has no activity with the alpha form (PubMed:16990279). {ECO:0000269|PubMed:15808744, ECO:0000269|PubMed:16990279, ECO:0000269|PubMed:27941785}. The hexitol phosphatase activity of HxpA was discovered in a large-scale metabolomics screen for enzymatic activities of uncharacterized proteins in E. coli . HxpA is a sugar phosphatase belonging to the superfamily of haloacid dehalogenase (HAD)-like hydrolases. It shows a low level of substrate discrimination among its preferred substrates, although it does selectively hydrolyze β-D-glucose-1-phosphate and has no activity with the α form . Overexpression of hxpA results in increased glycerol-3-phosphatase activity in crude extract . The phosphatase activity of HxpA was first discovered in a high-throughput screen of purified proteins...

## Biological Role

Catalyzes sugar-phosphate phosphohydrolase (reaction.R00804), sorbitol-6-phosphate phosphohydrolase (reaction.R02866), GLYCEROL-1-PHOSPHATASE-RXN (reaction.ecocyc.GLYCEROL-1-PHOSPHATASE-RXN), MANNITOL-1-PHOSPHATASE-RXN (reaction.ecocyc.MANNITOL-1-PHOSPHATASE-RXN), SORBITOL-6-PHOSPHATASE-RXN (reaction.ecocyc.SORBITOL-6-PHOSPHATASE-RXN), SUGAR-PHOSPHATASE-RXN (reaction.ecocyc.SUGAR-PHOSPHATASE-RXN). Bound by Magnesium cation (molecule.C00305).

## Enriched Pathways

- `eco00051` Fructose and mannose metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)

## Annotation

FUNCTION: Sugar-phosphate phosphohydrolase that appears to contribute to butanol tolerance (PubMed:27941785). Catalyzes the dephosphorylation of D-mannitol 1-phosphate and D-sorbitol 6-phosphate (PubMed:27941785). Is also able to dephosphorylate other sugar phosphates in vitro including ribose-5-phosphate (Rib5P), 2-deoxyribose-5-phosphate, fructose-1-phosphate (Fru1P), fructose-6-phosphate (Fru6P), and glucose-6-phosphate (Glu6P) (PubMed:16990279). Selectively hydrolyzes beta-D-glucose-1-phosphate (bGlu1P) and has no activity with the alpha form (PubMed:16990279). {ECO:0000269|PubMed:15808744, ECO:0000269|PubMed:16990279, ECO:0000269|PubMed:27941785}.

## Pathways

- `eco00051` Fructose and mannose metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)

## Outgoing Edges (6)

- `catalyzes` --> [[reaction.R00804|reaction.R00804]] `KEGG` `database` - via EC:3.1.3.23
- `catalyzes` --> [[reaction.R02866|reaction.R02866]] `KEGG` `database` - via EC:3.1.3.50
- `catalyzes` --> [[reaction.ecocyc.GLYCEROL-1-PHOSPHATASE-RXN|reaction.ecocyc.GLYCEROL-1-PHOSPHATASE-RXN]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` --> [[reaction.ecocyc.MANNITOL-1-PHOSPHATASE-RXN|reaction.ecocyc.MANNITOL-1-PHOSPHATASE-RXN]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` --> [[reaction.ecocyc.SORBITOL-6-PHOSPHATASE-RXN|reaction.ecocyc.SORBITOL-6-PHOSPHATASE-RXN]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` --> [[reaction.ecocyc.SUGAR-PHOSPHATASE-RXN|reaction.ecocyc.SUGAR-PHOSPHATASE-RXN]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (2)

- `binds` <-- [[molecule.C00305|molecule.C00305]] `EcoCyc` `database` - EcoCyc enzymatic reaction cofactor
- `encodes` <-- [[gene.b2293|gene.b2293]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P77625`
- `KEGG:ecj:JW5376;eco:b2293;ecoc:C3026_12790;`
- `GeneID:946777;`
- `GO:GO:0000287; GO:0005975; GO:0030145; GO:0043136; GO:0050084; GO:0050286; GO:0050308; GO:0050897`
- `EC:3.1.3.22; 3.1.3.23; 3.1.3.50`

## Notes

Hexitol phosphatase A (Mannitol-1-phosphatase) (EC 3.1.3.22) (Sorbitol-6-phosphatase) (EC 3.1.3.50) (Sugar-phosphatase) (EC 3.1.3.23)
