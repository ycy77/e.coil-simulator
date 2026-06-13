---
entity_id: "protein.P37330"
entity_type: "protein"
name: "glcB"
source_database: "UniProt"
source_id: "P37330"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cytoplasm."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "glcB glc b2976 JW2943"
---

# glcB

`protein.P37330`

## Static

- Type: `protein`
- Source: `UniProt:P37330`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cytoplasm.

## Enriched Summary

FUNCTION: Involved in the glycolate utilization. Catalyzes the condensation and subsequent hydrolysis of acetyl-coenzyme A (acetyl-CoA) and glyoxylate to form malate and CoA. {ECO:0000255|HAMAP-Rule:MF_00641, ECO:0000269|PubMed:14336062, ECO:0000269|PubMed:4892366, ECO:0000269|PubMed:7925370}. Malate synthase catalyzes the Claisen condensation of glyoxylate and acetyl-CoA, initially forming a malyl-CoA intermediate that is hydrolyzed to the products malate and CoA. There are two isozymes of malate synthase in E. coli . Malate synthase G (the "glycolate form" of malate synthase described here) is responsible for almost all of the malate synthase activity in cells metabolizing glyoxylate that is formed during growth on glycolate . MALATE-SYNTHASE Malate synthase A is involved in the GLYOXYLATE-BYPASS "glyoxylate bypass", metabolizing glyoxylate formed in the dissimilation of acetate . Crystal and solution structures (as well as a cryo-EM structure) of malate synthase G in various conformations have been determined, and a reaction mechanism has been proposed . Active site residues were confirmed by site-directed mutagenesis . Refolding after denaturation of malate synthase G has been studied in detail . Expression of glcB is inducible by glycolate and during growth on glycerol as the sole source of carbon . The glc operon was also shown to be inducible by acetate...

## Biological Role

Catalyzes acetyl-CoA:glyoxylate C-acetyltransferase (thioester-hydrolysing, carboxymethyl-forming); (reaction.R00472), MALSYN-RXN (reaction.ecocyc.MALSYN-RXN). Bound by Magnesium cation (molecule.C00305).

## Enriched Pathways

- `eco00620` Pyruvate metabolism (KEGG)
- `eco00630` Glyoxylate and dicarboxylate metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01110` Biosynthesis of secondary metabolites (KEGG)
- `eco01120` Microbial metabolism in diverse environments (KEGG)
- `eco01200` Carbon metabolism (KEGG)

## Annotation

FUNCTION: Involved in the glycolate utilization. Catalyzes the condensation and subsequent hydrolysis of acetyl-coenzyme A (acetyl-CoA) and glyoxylate to form malate and CoA. {ECO:0000255|HAMAP-Rule:MF_00641, ECO:0000269|PubMed:14336062, ECO:0000269|PubMed:4892366, ECO:0000269|PubMed:7925370}.

## Pathways

- `eco00620` Pyruvate metabolism (KEGG)
- `eco00630` Glyoxylate and dicarboxylate metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01110` Biosynthesis of secondary metabolites (KEGG)
- `eco01120` Microbial metabolism in diverse environments (KEGG)
- `eco01200` Carbon metabolism (KEGG)

## Outgoing Edges (2)

- `catalyzes` --> [[reaction.R00472|reaction.R00472]] `KEGG` `database` - via EC:2.3.3.9
- `catalyzes` --> [[reaction.ecocyc.MALSYN-RXN|reaction.ecocyc.MALSYN-RXN]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (2)

- `binds` <-- [[molecule.C00305|molecule.C00305]] `EcoCyc` `database` - EcoCyc enzymatic reaction cofactor
- `encodes` <-- [[gene.b2976|gene.b2976]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P37330`
- `KEGG:ecj:JW2943;eco:b2976;ecoc:C3026_16280;`
- `GeneID:948857;`
- `GO:GO:0000287; GO:0004474; GO:0005829; GO:0006097; GO:0006099; GO:0009436`
- `EC:2.3.3.9`

## Notes

Malate synthase G (MSG) (EC 2.3.3.9)
