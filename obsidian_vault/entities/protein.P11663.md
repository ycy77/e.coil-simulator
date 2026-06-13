---
entity_id: "protein.P11663"
entity_type: "protein"
name: "fumE"
source_database: "UniProt"
source_id: "P11663"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "fumE yggD b2929 JW2896"
---

# fumE

`protein.P11663`

## Static

- Type: `protein`
- Source: `UniProt:P11663`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`

## Enriched Summary

FUNCTION: In vitro catalyzes the addition of water to fumarate, forming malate. Cannot catalyze the reverse reaction. Cannot use the cis-isomer maleate as substrate. {ECO:0000269|PubMed:27941785}. The fumarase activity of FumE was discovered in a large-scale metabolomics screen for enzymatic activities of uncharacterized proteins in E. coli . FumE: "fumarase E"

## Biological Role

Catalyzes FUMHYDR-RXN (reaction.ecocyc.FUMHYDR-RXN).

## Enriched Pathways

- `eco00020` Citrate cycle (TCA cycle) (KEGG)
- `eco00620` Pyruvate metabolism (KEGG)
- `eco00720` Other carbon fixation pathways (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01110` Biosynthesis of secondary metabolites (KEGG)
- `eco01120` Microbial metabolism in diverse environments (KEGG)

## Annotation

FUNCTION: In vitro catalyzes the addition of water to fumarate, forming malate. Cannot catalyze the reverse reaction. Cannot use the cis-isomer maleate as substrate. {ECO:0000269|PubMed:27941785}.

## Pathways

- `eco00020` Citrate cycle (TCA cycle) (KEGG)
- `eco00620` Pyruvate metabolism (KEGG)
- `eco00720` Other carbon fixation pathways (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01110` Biosynthesis of secondary metabolites (KEGG)
- `eco01120` Microbial metabolism in diverse environments (KEGG)

## Outgoing Edges (1)

- `catalyzes` --> [[reaction.ecocyc.FUMHYDR-RXN|reaction.ecocyc.FUMHYDR-RXN]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (1)

- `encodes` <-- [[gene.b2929|gene.b2929]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P11663`
- `KEGG:ecj:JW2896;eco:b2929;ecoc:C3026_16045;`
- `GeneID:946861;`
- `GO:GO:0004333`
- `EC:4.2.1.2`

## Notes

Fumarase E (EC 4.2.1.2)
