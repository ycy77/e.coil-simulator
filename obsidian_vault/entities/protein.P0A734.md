---
entity_id: "protein.P0A734"
entity_type: "protein"
name: "minE"
source_database: "UniProt"
source_id: "P0A734"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "minE b1174 JW1163"
---

# minE

`protein.P0A734`

## Static

- Type: `protein`
- Source: `UniProt:P0A734`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`

## Enriched Summary

FUNCTION: Prevents the cell division inhibition by proteins MinC and MinD at internal division sites while permitting inhibition at polar sites. This ensures cell division at the proper site by restricting the formation of a division septum at the midpoint of the long axis of the cell. {ECO:0000269|PubMed:22380631}. The EG10596-MONOMER "MinC"-EG10597-MONOMER "MinD"-MinE system acts to direct septation to the proper (central) site in the dividing E. coli cell; the Min proteins are involved in a pole-to-pole oscillating system that restricts Z-ring formation to midcell. MinE is considered to be the 'topological specificity factor' that relieves MinCD inhibition of cell division specifically at mid-cell. MinDE is also implicated in a generic mechanism which regulates the positioning of membrane proteins in cells; MinDE form a propagating diffusion barrier which regulates the positioning of functionally unrelated membrane-bound molecules in vitro . MinDE constitutes the minimal set of proteins to drive the formation of FtsA-FtsZ cytoskeletal patterns on supported lipid bilayers . The Min proteins play a role in determining cell size; increasing the minE/minD expression ratio delays FtsZ binding to the membrane and subsequent Z-ring formation leading to an increase in average cell size...

## Annotation

FUNCTION: Prevents the cell division inhibition by proteins MinC and MinD at internal division sites while permitting inhibition at polar sites. This ensures cell division at the proper site by restricting the formation of a division septum at the midpoint of the long axis of the cell. {ECO:0000269|PubMed:22380631}.

## Outgoing Edges (0)

_None._

## Incoming Edges (1)

- `encodes` <-- [[gene.b1174|gene.b1174]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P0A734`
- `KEGG:ecj:JW1163;eco:b1174;ecoc:C3026_06920;`
- `GeneID:86859375;93776260;945740;`
- `GO:GO:0000918; GO:0001671; GO:0005829; GO:0005886; GO:0032955; GO:0042802`

## Notes

Cell division topological specificity factor
