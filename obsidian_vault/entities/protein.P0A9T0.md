---
entity_id: "protein.P0A9T0"
entity_type: "protein"
name: "serA"
source_database: "UniProt"
source_id: "P0A9T0"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "serA b2913 JW2880"
---

# serA

`protein.P0A9T0`

## Static

- Type: `protein`
- Source: `UniProt:P0A9T0`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`

## Enriched Summary

FUNCTION: Catalyzes the reversible oxidation of 3-phospho-D-glycerate to 3-phosphonooxypyruvate, the first step of the phosphorylated L-serine biosynthesis pathway. Also catalyzes the reversible oxidation of 2-hydroxyglutarate to 2-oxoglutarate. {ECO:0000269|PubMed:8550422}. D-3-phosphoglycerate dehydrogenase (SerA, PHGDH) catalyzes the first committed step in the biosynthesis of L-serine. The enzyme is regulated by allosteric end-product inhibition that shows cooperativity. Inhibition by serine acts primarily through reduction of catalytic velocity and has only a small effect on the Kms of the substrates; SerA is thus classified as a type V allosteric enzyme. SerA also has an α-ketoglutarate reductase activity, producing 2-hydroxyglutarate. Kinetically, the best SerA substrates are 3-phosphohydroxypyruvate (3PHP) and α-ketoglutarate (αKG), i.e. in vitro, the reaction equilibrium is skewed towards production of 3-phosphoglycerate (3PG) rather than the 3PHP intermediate required for serine biosynthesis . The hypothesis that the activities and reaction equilibria of SerA may play a role in recycling NADH back to NAD+ is supported by experimental data . Unlike enzymes from some other organisms, E...

## Biological Role

Catalyzes R08198 (reaction.R08198), (R)-2-hydroxyglutarate:NAD+ 2-oxidireductase (reaction.R11337). Component of phosphoglycerate dehydrogenase (complex.ecocyc.PGLYCDEHYDROG-CPLX).

## Enriched Pathways

- `eco00260` Glycine, serine and threonine metabolism (KEGG)
- `eco00270` Cysteine and methionine metabolism (KEGG)
- `eco00680` Methane metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01110` Biosynthesis of secondary metabolites (KEGG)
- `eco01120` Microbial metabolism in diverse environments (KEGG)
- `eco01200` Carbon metabolism (KEGG)
- `eco01230` Biosynthesis of amino acids (KEGG)

## Annotation

FUNCTION: Catalyzes the reversible oxidation of 3-phospho-D-glycerate to 3-phosphonooxypyruvate, the first step of the phosphorylated L-serine biosynthesis pathway. Also catalyzes the reversible oxidation of 2-hydroxyglutarate to 2-oxoglutarate. {ECO:0000269|PubMed:8550422}.

## Pathways

- `eco00260` Glycine, serine and threonine metabolism (KEGG)
- `eco00270` Cysteine and methionine metabolism (KEGG)
- `eco00680` Methane metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01110` Biosynthesis of secondary metabolites (KEGG)
- `eco01120` Microbial metabolism in diverse environments (KEGG)
- `eco01200` Carbon metabolism (KEGG)
- `eco01230` Biosynthesis of amino acids (KEGG)

## Outgoing Edges (3)

- `catalyzes` --> [[reaction.R08198|reaction.R08198]] `KEGG` `database` - via EC:1.1.1.95
- `catalyzes` --> [[reaction.R11337|reaction.R11337]] `KEGG` `database` - via EC:1.1.1.399
- `is_component_of` --> [[complex.ecocyc.PGLYCDEHYDROG-CPLX|complex.ecocyc.PGLYCDEHYDROG-CPLX]] `EcoCyc` `database` - EcoCyc component coefficient=4 | EcoCyc protcplxs.col coefficient=4

## Incoming Edges (1)

- `encodes` <-- [[gene.b2913|gene.b2913]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P0A9T0`
- `KEGG:ecj:JW2880;eco:b2913;ecoc:C3026_15965;`
- `GeneID:93779086;945258;`
- `GO:GO:0004617; GO:0005829; GO:0006564; GO:0042802; GO:0047545; GO:0070403; GO:0070404; GO:0070905`
- `EC:1.1.1.399; 1.1.1.95`

## Notes

D-3-phosphoglycerate dehydrogenase (PGDH) (EC 1.1.1.95) (2-oxoglutarate reductase) (EC 1.1.1.399)
