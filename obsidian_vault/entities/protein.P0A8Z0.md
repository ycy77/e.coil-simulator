---
entity_id: "protein.P0A8Z0"
entity_type: "protein"
name: "yciA"
source_database: "UniProt"
source_id: "P0A8Z0"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "yciA b1253 JW1245"
---

# yciA

`protein.P0A8Z0`

## Static

- Type: `protein`
- Source: `UniProt:P0A8Z0`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`

## Enriched Summary

FUNCTION: Catalyzes the hydrolysis of the thioester bond in palmitoyl-CoA and malonyl-CoA. {ECO:0000269|PubMed:15808744}. YciA is an acyl-CoA thioesterase with broad substrate specificity . Esterase activity of YciA was first discovered in a high-throughput screen of purified proteins . YciA homologs exist in a wide variety of bacteria. The Haemophilus influenzae enzyme is a homohexamer and has been crystallized . A yciA null mutant does not have an obvious growth defect . A yciA deletion mutant in the EB228 strain background produces significantly less butyrate than its parent .

## Biological Role

Catalyzes ACYL-COA-HYDROLASE-RXN (reaction.ecocyc.ACYL-COA-HYDROLASE-RXN).

## Enriched Pathways

- `eco01040` Biosynthesis of unsaturated fatty acids (KEGG)

## Annotation

FUNCTION: Catalyzes the hydrolysis of the thioester bond in palmitoyl-CoA and malonyl-CoA. {ECO:0000269|PubMed:15808744}.

## Pathways

- `eco01040` Biosynthesis of unsaturated fatty acids (KEGG)

## Outgoing Edges (1)

- `catalyzes` --> [[reaction.ecocyc.ACYL-COA-HYDROLASE-RXN|reaction.ecocyc.ACYL-COA-HYDROLASE-RXN]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (1)

- `encodes` <-- [[gene.b1253|gene.b1253]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P0A8Z0`
- `KEGG:ecj:JW1245;eco:b1253;ecoc:C3026_07360;`
- `GeneID:93775322;946634;`
- `GO:GO:0005737; GO:0005829; GO:0006637; GO:0009062; GO:0044581; GO:0052816`
- `EC:3.1.2.-`

## Notes

Acyl-CoA thioester hydrolase YciA (EC 3.1.2.-) (Protein P14)
