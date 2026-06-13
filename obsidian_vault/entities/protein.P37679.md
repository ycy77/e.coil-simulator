---
entity_id: "protein.P37679"
entity_type: "protein"
name: "sgbU"
source_database: "UniProt"
source_id: "P37679"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "sgbU yiaR b3582 JW5650"
---

# sgbU

`protein.P37679`

## Static

- Type: `protein`
- Source: `UniProt:P37679`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`

## Enriched Summary

FUNCTION: Catalyzes the isomerization of L-xylulose-5-phosphate to L-ribulose-5-phosphate (Potential). May be involved in the utilization of 2,3-diketo-L-gulonate. {ECO:0000305}. SgbU appears to be required for the utilization of L-lyxose . Despite similarity to UlaE, no SgbU L-xylulose 5-phosphate 3-epimerase activity has yet been detected directly . Review:

## Biological Role

Catalyzes LXULRU5P-RXN (reaction.ecocyc.LXULRU5P-RXN).

## Enriched Pathways

- `eco00040` Pentose and glucuronate interconversions (KEGG)
- `eco00053` Ascorbate and aldarate metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01120` Microbial metabolism in diverse environments (KEGG)

## Annotation

FUNCTION: Catalyzes the isomerization of L-xylulose-5-phosphate to L-ribulose-5-phosphate (Potential). May be involved in the utilization of 2,3-diketo-L-gulonate. {ECO:0000305}.

## Pathways

- `eco00040` Pentose and glucuronate interconversions (KEGG)
- `eco00053` Ascorbate and aldarate metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01120` Microbial metabolism in diverse environments (KEGG)

## Outgoing Edges (1)

- `catalyzes` --> [[reaction.ecocyc.LXULRU5P-RXN|reaction.ecocyc.LXULRU5P-RXN]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (1)

- `encodes` <-- [[gene.b3582|gene.b3582]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P37679`
- `KEGG:ecj:JW5650;eco:b3582;ecoc:C3026_19420;`
- `GeneID:948100;`
- `GO:GO:0003677; GO:0006281; GO:0008270; GO:0016861; GO:0019324; GO:0019852; GO:0034015`
- `EC:5.1.3.22`

## Notes

Putative L-ribulose-5-phosphate 3-epimerase SgbU (EC 5.1.3.22) (L-xylulose-5-phosphate 3-epimerase)
