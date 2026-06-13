---
entity_id: "protein.P75913"
entity_type: "protein"
name: "ghrA"
source_database: "UniProt"
source_id: "P75913"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cytoplasm {ECO:0000305|PubMed:11237876}."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "ghrA ycdW b1033 JW5146"
---

# ghrA

`protein.P75913`

## Static

- Type: `protein`
- Source: `UniProt:P75913`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cytoplasm {ECO:0000305|PubMed:11237876}.

## Enriched Summary

FUNCTION: Catalyzes the NADPH-dependent reduction of glyoxylate and hydroxypyruvate into glycolate and glycerate, respectively. Inactive towards 2-oxo-D-gluconate, 2-oxoglutarate, oxaloacetate and pyruvate. Only D- and L-glycerate are involved in the oxidative activity with NADP. Activity with NAD is very low. GhrA is one of two enzymes with glyoxylate reductase activity. GhrA prefers NADPH as the electron donor and also catalyzes reduction of hydroxypyruvate, although at lower catalytic efficiency. In contrast, the ghrB-encoded enzyme prefers hydroxypyruvate as the substrate . Expression of ghrA is slightly increased by growth on medium containing hydroxypyruvate . ghrA was one of only three genes whose expression changed under all stress conditions tested by . Inactivation of ghrA was investigated as a means to improve production of 1,2,4-butanetriol in a metabolically engineered strain .

## Biological Role

Catalyzes glycolate:NADP+ oxidoreductase (reaction.R00465), GLYOXYLATE-REDUCTASE-NADP+-RXN (reaction.ecocyc.GLYOXYLATE-REDUCTASE-NADP_-RXN), hydroxypyruvate reductase (NADP+) (reaction.ecocyc.RXN0-300).

## Enriched Pathways

- `eco00260` Glycine, serine and threonine metabolism (KEGG)
- `eco00620` Pyruvate metabolism (KEGG)
- `eco00630` Glyoxylate and dicarboxylate metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01110` Biosynthesis of secondary metabolites (KEGG)
- `eco01120` Microbial metabolism in diverse environments (KEGG)

## Annotation

FUNCTION: Catalyzes the NADPH-dependent reduction of glyoxylate and hydroxypyruvate into glycolate and glycerate, respectively. Inactive towards 2-oxo-D-gluconate, 2-oxoglutarate, oxaloacetate and pyruvate. Only D- and L-glycerate are involved in the oxidative activity with NADP. Activity with NAD is very low.

## Pathways

- `eco00260` Glycine, serine and threonine metabolism (KEGG)
- `eco00620` Pyruvate metabolism (KEGG)
- `eco00630` Glyoxylate and dicarboxylate metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01110` Biosynthesis of secondary metabolites (KEGG)
- `eco01120` Microbial metabolism in diverse environments (KEGG)

## Outgoing Edges (3)

- `catalyzes` --> [[reaction.R00465|reaction.R00465]] `KEGG` `database` - via EC:1.1.1.79
- `catalyzes` --> [[reaction.ecocyc.GLYOXYLATE-REDUCTASE-NADP_-RXN|reaction.ecocyc.GLYOXYLATE-REDUCTASE-NADP_-RXN]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` --> [[reaction.ecocyc.RXN0-300|reaction.ecocyc.RXN0-300]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (1)

- `encodes` <-- [[gene.b1033|gene.b1033]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P75913`
- `KEGG:ecj:JW5146;eco:b1033;ecoc:C3026_06295;`
- `GeneID:93776385;946431;`
- `GO:GO:0005829; GO:0008465; GO:0016618; GO:0030267; GO:0033554; GO:0051287; GO:0120509`
- `EC:1.1.1.79; 1.1.1.81`

## Notes

Glyoxylate/hydroxypyruvate reductase A (EC 1.1.1.79) (EC 1.1.1.81) (2-ketoacid reductase)
