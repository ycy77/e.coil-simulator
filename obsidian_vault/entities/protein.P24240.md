---
entity_id: "protein.P24240"
entity_type: "protein"
name: "ascB"
source_database: "UniProt"
source_id: "P24240"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "ascB b2716 JW2686"
---

# ascB

`protein.P24240`

## Static

- Type: `protein`
- Source: `UniProt:P24240`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`

## Enriched Summary

FUNCTION: Can hydrolyze salicin, cellobiose, and probably arbutin. ascB is thought to encode phospho-β-glucosidase as part of the cryptic asc operon . In a strain evolved for efficient cellobiose utilization , duplication of the ascB ribosome binding site leads to increased expression of AscB . sac: "salicin-arbutin-cellobiose" AscB: "arbutin, salicin, cellobiose"

## Biological Role

Catalyzes 6-phospho-beta-D-glucosyl-(1->4)-D-glucose 6-phosphoglucohydrolase (reaction.R00839), 6-PHOSPHO-BETA-GLUCOSIDASE-RXN (reaction.ecocyc.6-PHOSPHO-BETA-GLUCOSIDASE-RXN), RXN0-5295 (reaction.ecocyc.RXN0-5295).

## Enriched Pathways

- `eco00010` Glycolysis / Gluconeogenesis (KEGG)
- `eco00500` Starch and sucrose metabolism (KEGG)

## Annotation

FUNCTION: Can hydrolyze salicin, cellobiose, and probably arbutin.

## Pathways

- `eco00010` Glycolysis / Gluconeogenesis (KEGG)
- `eco00500` Starch and sucrose metabolism (KEGG)

## Outgoing Edges (3)

- `catalyzes` --> [[reaction.R00839|reaction.R00839]] `KEGG` `database` - via EC:3.2.1.86
- `catalyzes` --> [[reaction.ecocyc.6-PHOSPHO-BETA-GLUCOSIDASE-RXN|reaction.ecocyc.6-PHOSPHO-BETA-GLUCOSIDASE-RXN]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` --> [[reaction.ecocyc.RXN0-5295|reaction.ecocyc.RXN0-5295]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (1)

- `encodes` <-- [[gene.b2716|gene.b2716]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P24240`
- `KEGG:ecj:JW2686;eco:b2716;`
- `GeneID:947460;`
- `GO:GO:0005829; GO:0008422; GO:0008706; GO:0016052; GO:2000892`
- `EC:3.2.1.86`

## Notes

6-phospho-beta-glucosidase AscB (EC 3.2.1.86)
