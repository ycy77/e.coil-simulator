---
entity_id: "protein.P37666"
entity_type: "protein"
name: "ghrB"
source_database: "UniProt"
source_id: "P37666"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cytoplasm {ECO:0000305}."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "ghrB tkrA yiaE b3553 JW5656"
---

# ghrB

`protein.P37666`

## Static

- Type: `protein`
- Source: `UniProt:P37666`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cytoplasm {ECO:0000305}.

## Enriched Summary

FUNCTION: Catalyzes the NADPH-dependent reduction of glyoxylate and hydroxypyruvate into glycolate and glycerate, respectively. Can also reduce 2,5-diketo-D-gluconate (25DKG) to 5-keto-D-gluconate (5KDG), 2-keto-D-gluconate (2KDG) to D-gluconate, and 2-keto-L-gulonate (2KLG) to L-idonate (IA), but it is not its physiological function. Inactive towards 2-oxoglutarate, oxaloacetate, pyruvate, 5-keto-D-gluconate, D-fructose and L-sorbose. Activity with NAD is very low.

## Biological Role

Catalyzes glycolate:NADP+ oxidoreductase (reaction.R00465), D-gluconate:NADP+ 2-oxidoreductase (reaction.R01739), 5-dehydro-D-gluconate:NADP+ 2-oxidoreductase (reaction.R08879), L-idonate:NADP+ 2-oxidoreductase (reaction.R08880). Component of glyoxylate reductase [multifunctional] (complex.ecocyc.CPLX0-235).

## Enriched Pathways

- `eco00030` Pentose phosphate pathway (KEGG)
- `eco00260` Glycine, serine and threonine metabolism (KEGG)
- `eco00620` Pyruvate metabolism (KEGG)
- `eco00630` Glyoxylate and dicarboxylate metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01110` Biosynthesis of secondary metabolites (KEGG)
- `eco01120` Microbial metabolism in diverse environments (KEGG)

## Annotation

FUNCTION: Catalyzes the NADPH-dependent reduction of glyoxylate and hydroxypyruvate into glycolate and glycerate, respectively. Can also reduce 2,5-diketo-D-gluconate (25DKG) to 5-keto-D-gluconate (5KDG), 2-keto-D-gluconate (2KDG) to D-gluconate, and 2-keto-L-gulonate (2KLG) to L-idonate (IA), but it is not its physiological function. Inactive towards 2-oxoglutarate, oxaloacetate, pyruvate, 5-keto-D-gluconate, D-fructose and L-sorbose. Activity with NAD is very low.

## Pathways

- `eco00030` Pentose phosphate pathway (KEGG)
- `eco00260` Glycine, serine and threonine metabolism (KEGG)
- `eco00620` Pyruvate metabolism (KEGG)
- `eco00630` Glyoxylate and dicarboxylate metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01110` Biosynthesis of secondary metabolites (KEGG)
- `eco01120` Microbial metabolism in diverse environments (KEGG)

## Outgoing Edges (5)

- `catalyzes` --> [[reaction.R00465|reaction.R00465]] `KEGG` `database` - via EC:1.1.1.79
- `catalyzes` --> [[reaction.R01739|reaction.R01739]] `KEGG` `database` - via EC:1.1.1.215
- `catalyzes` --> [[reaction.R08879|reaction.R08879]] `KEGG` `database` - via EC:1.1.1.215
- `catalyzes` --> [[reaction.R08880|reaction.R08880]] `KEGG` `database` - via EC:1.1.1.215
- `is_component_of` --> [[complex.ecocyc.CPLX0-235|complex.ecocyc.CPLX0-235]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2

## Incoming Edges (1)

- `encodes` <-- [[gene.b3553|gene.b3553]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P37666`
- `KEGG:ecj:JW5656;eco:b3553;ecoc:C3026_19260;`
- `GeneID:948074;`
- `GO:GO:0005829; GO:0005886; GO:0008465; GO:0008873; GO:0016618; GO:0019521; GO:0030267; GO:0046181; GO:0051287; GO:0120509`
- `EC:1.1.1.215; 1.1.1.79; 1.1.1.81`

## Notes

Glyoxylate/hydroxypyruvate reductase B (EC 1.1.1.79) (EC 1.1.1.81) (2-ketoaldonate reductase) (2-ketogluconate reductase) (2KR) (EC 1.1.1.215)
