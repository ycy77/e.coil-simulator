---
entity_id: "protein.P09151"
entity_type: "protein"
name: "leuA"
source_database: "UniProt"
source_id: "P09151"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cytoplasm {ECO:0000255|HAMAP-Rule:MF_01025}."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "leuA b0074 JW0073"
---

# leuA

`protein.P09151`

## Static

- Type: `protein`
- Source: `UniProt:P09151`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cytoplasm {ECO:0000255|HAMAP-Rule:MF_01025}.

## Enriched Summary

FUNCTION: Catalyzes the condensation of the acetyl group of acetyl-CoA with 3-methyl-2-oxobutanoate (2-ketoisovalerate) to form 3-carboxy-3-hydroxy-4-methylpentanoate (2-isopropylmalate). {ECO:0000255|HAMAP-Rule:MF_01025}. 2-Isopropylmalate synthase (IPMS, LeuA) catalyzes the first committed step in leucine biosynthesis, the conversion of 2-keto-isovalerate and acetyl-CoA to 2-isopropylmalate . A mutant enzyme that is not feedback-inhibited by leucine and contains the G462D substitution was described in a US patent . leuA mutants are leucine auxotrophs . Enzyme analysis showed that strains with a mutation in leuA lacked IPMS activity . Overexpression of leuA from an ASKA plasmid leads to a more than 3-fold increase in the MIC of hydrogen peroxide . LeuA:

## Biological Role

Catalyzes 2-ISOPROPYLMALATESYN-RXN (reaction.ecocyc.2-ISOPROPYLMALATESYN-RXN).

## Enriched Pathways

- `eco00290` Valine, leucine and isoleucine biosynthesis (KEGG)
- `eco00620` Pyruvate metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01110` Biosynthesis of secondary metabolites (KEGG)
- `eco01210` 2-Oxocarboxylic acid metabolism (KEGG)
- `eco01230` Biosynthesis of amino acids (KEGG)

## Annotation

FUNCTION: Catalyzes the condensation of the acetyl group of acetyl-CoA with 3-methyl-2-oxobutanoate (2-ketoisovalerate) to form 3-carboxy-3-hydroxy-4-methylpentanoate (2-isopropylmalate). {ECO:0000255|HAMAP-Rule:MF_01025}.

## Pathways

- `eco00290` Valine, leucine and isoleucine biosynthesis (KEGG)
- `eco00620` Pyruvate metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01110` Biosynthesis of secondary metabolites (KEGG)
- `eco01210` 2-Oxocarboxylic acid metabolism (KEGG)
- `eco01230` Biosynthesis of amino acids (KEGG)

## Outgoing Edges (1)

- `catalyzes` --> [[reaction.ecocyc.2-ISOPROPYLMALATESYN-RXN|reaction.ecocyc.2-ISOPROPYLMALATESYN-RXN]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (1)

- `encodes` <-- [[gene.b0074|gene.b0074]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P09151`
- `KEGG:ecj:JW0073;eco:b0074;`
- `GeneID:947465;`
- `GO:GO:0003852; GO:0003985; GO:0005829; GO:0009098; GO:0030145`
- `EC:2.3.3.13`

## Notes

2-isopropylmalate synthase (EC 2.3.3.13) (Alpha-IPM synthase) (Alpha-isopropylmalate synthase)
