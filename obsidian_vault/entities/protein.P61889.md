---
entity_id: "protein.P61889"
entity_type: "protein"
name: "mdh"
source_database: "UniProt"
source_id: "P61889"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "mdh b3236 JW3205"
---

# mdh

`protein.P61889`

## Static

- Type: `protein`
- Source: `UniProt:P61889`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`

## Enriched Summary

FUNCTION: Catalyzes the reversible oxidation of malate to oxaloacetate. {ECO:0000255|HAMAP-Rule:MF_01516, ECO:0000269|PubMed:2993232, ECO:0000269|PubMed:7028159}.

## Biological Role

Catalyzes (S)-malate:NAD+ oxidoreductase (reaction.R00342), 3-(3,5-diiodo-4-hydroxyphenyl)lactate:NAD+ oxidoreductase (reaction.R03431). Component of malate dehydrogenase (complex.ecocyc.MALATE-DEHASE).

## Enriched Pathways

- `eco00020` Citrate cycle (TCA cycle) (KEGG)
- `eco00270` Cysteine and methionine metabolism (KEGG)
- `eco00566` Sulfoquinovose metabolism (KEGG)
- `eco00620` Pyruvate metabolism (KEGG)
- `eco00630` Glyoxylate and dicarboxylate metabolism (KEGG)
- `eco00680` Methane metabolism (KEGG)
- `eco00710` Carbon fixation by Calvin cycle (KEGG)
- `eco00720` Other carbon fixation pathways (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01110` Biosynthesis of secondary metabolites (KEGG)
- `eco01120` Microbial metabolism in diverse environments (KEGG)
- `eco01200` Carbon metabolism (KEGG)

## Annotation

FUNCTION: Catalyzes the reversible oxidation of malate to oxaloacetate. {ECO:0000255|HAMAP-Rule:MF_01516, ECO:0000269|PubMed:2993232, ECO:0000269|PubMed:7028159}.

## Pathways

- `eco00020` Citrate cycle (TCA cycle) (KEGG)
- `eco00270` Cysteine and methionine metabolism (KEGG)
- `eco00566` Sulfoquinovose metabolism (KEGG)
- `eco00620` Pyruvate metabolism (KEGG)
- `eco00630` Glyoxylate and dicarboxylate metabolism (KEGG)
- `eco00680` Methane metabolism (KEGG)
- `eco00710` Carbon fixation by Calvin cycle (KEGG)
- `eco00720` Other carbon fixation pathways (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01110` Biosynthesis of secondary metabolites (KEGG)
- `eco01120` Microbial metabolism in diverse environments (KEGG)
- `eco01200` Carbon metabolism (KEGG)

## Outgoing Edges (3)

- `catalyzes` --> [[reaction.R00342|reaction.R00342]] `KEGG` `database` - via EC:1.1.1.37
- `catalyzes` --> [[reaction.R03431|reaction.R03431]] `KEGG` `database` - via EC:1.1.1.37
- `is_component_of` --> [[complex.ecocyc.MALATE-DEHASE|complex.ecocyc.MALATE-DEHASE]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2

## Incoming Edges (1)

- `encodes` <-- [[gene.b3236|gene.b3236]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P61889`
- `KEGG:ecj:JW3205;eco:b3236;ecoc:C3026_17605;`
- `GeneID:86862375;93778749;947854;`
- `GO:GO:0005737; GO:0005829; GO:0006096; GO:0006099; GO:0006108; GO:0006113; GO:0009061; GO:0016020; GO:0016491; GO:0016615; GO:0019898; GO:0030060; GO:0042803`
- `EC:1.1.1.37`

## Notes

Malate dehydrogenase (EC 1.1.1.37)
