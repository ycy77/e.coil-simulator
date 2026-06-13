---
entity_id: "protein.P39300"
entity_type: "protein"
name: "ulaG"
source_database: "UniProt"
source_id: "P39300"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cytoplasm {ECO:0000305}."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "ulaG yjfR b4192 JW5868"
---

# ulaG

`protein.P39300`

## Static

- Type: `protein`
- Source: `UniProt:P39300`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cytoplasm {ECO:0000305}.

## Enriched Summary

FUNCTION: Probably catalyzes the hydrolysis of L-ascorbate-6-P into 3-keto-L-gulonate-6-P. Is essential for L-ascorbate utilization under anaerobic conditions. Also shows phosphodiesterase activity, hydrolyzing phosphodiester bond in the artificial chromogenic substrate bis-p-nitrophenyl phosphate (bis-pNPP). {ECO:0000269|PubMed:12644495, ECO:0000269|PubMed:15808744}.

## Biological Role

Component of L-ascorbate-6-phosphate lactonase (complex.ecocyc.CPLX0-7848).

## Enriched Pathways

- `eco00053` Ascorbate and aldarate metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01120` Microbial metabolism in diverse environments (KEGG)

## Annotation

FUNCTION: Probably catalyzes the hydrolysis of L-ascorbate-6-P into 3-keto-L-gulonate-6-P. Is essential for L-ascorbate utilization under anaerobic conditions. Also shows phosphodiesterase activity, hydrolyzing phosphodiester bond in the artificial chromogenic substrate bis-p-nitrophenyl phosphate (bis-pNPP). {ECO:0000269|PubMed:12644495, ECO:0000269|PubMed:15808744}.

## Pathways

- `eco00053` Ascorbate and aldarate metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01120` Microbial metabolism in diverse environments (KEGG)

## Outgoing Edges (1)

- `is_component_of` --> [[complex.ecocyc.CPLX0-7848|complex.ecocyc.CPLX0-7848]] `EcoCyc` `database` - EcoCyc component coefficient=6 | EcoCyc protcplxs.col coefficient=6

## Incoming Edges (1)

- `encodes` <-- [[gene.b4192|gene.b4192]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P39300`
- `KEGG:ecj:JW5868;eco:b4192;ecoc:C3026_22645;`
- `GeneID:86861414;93777632;948705;`
- `GO:GO:0005737; GO:0016787; GO:0019854; GO:0030145; GO:0035460`
- `EC:3.1.1.-`

## Notes

Probable L-ascorbate-6-phosphate lactonase UlaG (EC 3.1.1.-) (L-ascorbate utilization protein G)
