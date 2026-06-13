---
entity_id: "protein.P0ACX5"
entity_type: "protein"
name: "fumD"
source_database: "UniProt"
source_id: "P0ACX5"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "fumD ydhZ b1675 JW1665"
---

# fumD

`protein.P0ACX5`

## Static

- Type: `protein`
- Source: `UniProt:P0ACX5`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`

## Enriched Summary

FUNCTION: In vitro catalyzes the addition of water to fumarate, forming malate. Cannot catalyze the reverse reaction. Cannot use the cis-isomer maleate as substrate. {ECO:0000269|PubMed:27941785}. The fumarase activity of FumD was discovered in a large-scale metabolomics screen for enzymatic activities of uncharacterized proteins in E. coli . fumD is part of a functional interaction network that includes Fe-S cluster biosynthesis genes. A fumD mutant reaches slightly higher cell density in stationary phase than wild type when growing in media with sublethal levels of streptomycin, an aminoglycoside antibiotic . FumD: "fumarase D"

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

- `encodes` <-- [[gene.b1675|gene.b1675]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P0ACX5`
- `KEGG:ecj:JW1665;eco:b1675;ecoc:C3026_09600;`
- `GeneID:93775830;946180;`
- `GO:GO:0004333`
- `EC:4.2.1.2`

## Notes

Fumarase D (EC 4.2.1.2)
