---
entity_id: "protein.P39306"
entity_type: "protein"
name: "ulaF"
source_database: "UniProt"
source_id: "P39306"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "ulaF sgaE yjfX b4198 JW4156"
---

# ulaF

`protein.P39306`

## Static

- Type: `protein`
- Source: `UniProt:P39306`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`

## Enriched Summary

FUNCTION: Catalyzes the isomerization of L-ribulose 5-phosphate to D-xylulose 5-phosphate. Is involved in the anaerobic L-ascorbate utilization. {ECO:0000255|HAMAP-Rule:MF_01952, ECO:0000269|PubMed:11741871}. L-ribulose 5-phosphate 4-epimerase is an enzyme in the pathway of anaerobic L-ascorbate degradation . UlaF: "utilization of L-ascorbate"

## Biological Role

Catalyzes L-ribulose-5-phosphate 4-epimerase (reaction.R05850), RIBULPEPIM-RXN (reaction.ecocyc.RIBULPEPIM-RXN).

## Enriched Pathways

- `eco00040` Pentose and glucuronate interconversions (KEGG)
- `eco00053` Ascorbate and aldarate metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01120` Microbial metabolism in diverse environments (KEGG)

## Annotation

FUNCTION: Catalyzes the isomerization of L-ribulose 5-phosphate to D-xylulose 5-phosphate. Is involved in the anaerobic L-ascorbate utilization. {ECO:0000255|HAMAP-Rule:MF_01952, ECO:0000269|PubMed:11741871}.

## Pathways

- `eco00040` Pentose and glucuronate interconversions (KEGG)
- `eco00053` Ascorbate and aldarate metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01120` Microbial metabolism in diverse environments (KEGG)

## Outgoing Edges (2)

- `catalyzes` --> [[reaction.R05850|reaction.R05850]] `KEGG` `database` - via EC:5.1.3.4
- `catalyzes` --> [[reaction.ecocyc.RIBULPEPIM-RXN|reaction.ecocyc.RIBULPEPIM-RXN]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (1)

- `encodes` <-- [[gene.b4198|gene.b4198]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P39306`
- `KEGG:ecj:JW4156;eco:b4198;ecoc:C3026_22675;`
- `GeneID:948711;`
- `GO:GO:0005829; GO:0008270; GO:0008742; GO:0016832; GO:0019323; GO:0019852; GO:0019854`
- `EC:5.1.3.4`

## Notes

L-ribulose-5-phosphate 4-epimerase UlaF (EC 5.1.3.4) (L-ascorbate utilization protein F) (Phosphoribulose isomerase)
