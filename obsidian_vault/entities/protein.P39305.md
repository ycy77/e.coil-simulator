---
entity_id: "protein.P39305"
entity_type: "protein"
name: "ulaE"
source_database: "UniProt"
source_id: "P39305"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "ulaE sgaU yjfW b4197 JW4155"
---

# ulaE

`protein.P39305`

## Static

- Type: `protein`
- Source: `UniProt:P39305`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`

## Enriched Summary

FUNCTION: Catalyzes the isomerization of L-xylulose-5-phosphate to L-ribulose-5-phosphate. Is involved in the anaerobic L-ascorbate utilization. {ECO:0000255|HAMAP-Rule:MF_01951, ECO:0000269|PubMed:11741871}. L-xylulose 5-phosphate 3-epimerase is an enzyme in the pathway of anaerobic L-ascorbate degradation. The crystal structure of the enzyme from E. coli O157:H7 has been solved, showing a dimeric enzyme with a TIM-barrel fold . UlaE: "utilization of L-ascorbate"

## Biological Role

Catalyzes LXULRU5P-RXN (reaction.ecocyc.LXULRU5P-RXN).

## Enriched Pathways

- `eco00040` Pentose and glucuronate interconversions (KEGG)
- `eco00053` Ascorbate and aldarate metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01120` Microbial metabolism in diverse environments (KEGG)

## Annotation

FUNCTION: Catalyzes the isomerization of L-xylulose-5-phosphate to L-ribulose-5-phosphate. Is involved in the anaerobic L-ascorbate utilization. {ECO:0000255|HAMAP-Rule:MF_01951, ECO:0000269|PubMed:11741871}.

## Pathways

- `eco00040` Pentose and glucuronate interconversions (KEGG)
- `eco00053` Ascorbate and aldarate metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01120` Microbial metabolism in diverse environments (KEGG)

## Outgoing Edges (1)

- `catalyzes` --> [[reaction.ecocyc.LXULRU5P-RXN|reaction.ecocyc.LXULRU5P-RXN]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (1)

- `encodes` <-- [[gene.b4197|gene.b4197]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P39305`
- `KEGG:ecj:JW4155;eco:b4197;ecoc:C3026_22670;`
- `GeneID:948712;`
- `GO:GO:0016861; GO:0019852; GO:0019854; GO:0034015`
- `EC:5.1.3.22`

## Notes

L-ribulose-5-phosphate 3-epimerase UlaE (EC 5.1.3.22) (L-ascorbate utilization protein E) (L-xylulose-5-phosphate 3-epimerase)
