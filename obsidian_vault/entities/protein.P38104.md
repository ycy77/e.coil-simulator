---
entity_id: "protein.P38104"
entity_type: "protein"
name: "rspA"
source_database: "UniProt"
source_id: "P38104"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "rspA b1581 JW1573"
---

# rspA

`protein.P38104`

## Static

- Type: `protein`
- Source: `UniProt:P38104`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`

## Enriched Summary

FUNCTION: Probably involved in the degradation of homoserine lactone (HSL) or of a metabolite of HSL that signals starvation. The RspA protein may be a bifunctional dehydratase that utilizes both D-mannonate and D-altronate as substrates . However, the enzyme from E. coli CFT037 shows only low catalytic activity with D-mannonate in vitro . Overexpression of RspA prevents homoserine lactone-dependent synthesis of the stationary phase-specific sigma factor σS . Overexpression of HsrA relieves RspA-mediated suppression of σS levels . RspA is similar to Spa2 of Streptomyces ambofaciens and mandelate racemase and chloromuconate cycloisomerase from Pseudomonas putida . RspA: "regulatory in stationary phase"

## Enriched Pathways

- `eco00040` Pentose and glucuronate interconversions (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01120` Microbial metabolism in diverse environments (KEGG)

## Annotation

FUNCTION: Probably involved in the degradation of homoserine lactone (HSL) or of a metabolite of HSL that signals starvation.

## Pathways

- `eco00040` Pentose and glucuronate interconversions (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01120` Microbial metabolism in diverse environments (KEGG)

## Outgoing Edges (0)

_None._

## Incoming Edges (1)

- `encodes` <-- [[gene.b1581|gene.b1581]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P38104`
- `KEGG:ecj:JW1573;eco:b1581;ecoc:C3026_09115;`
- `GeneID:75171639;75204424;946126;`
- `GO:GO:0000287; GO:0008927; GO:0009063; GO:0016052; GO:0016836`

## Notes

Starvation-sensing protein RspA
