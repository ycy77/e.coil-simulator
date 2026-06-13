---
entity_id: "protein.P09836"
entity_type: "protein"
name: "uhpC"
source_database: "UniProt"
source_id: "P09836"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cell inner membrane {ECO:0000269|PubMed:15919996}; Multi-pass membrane protein {ECO:0000255}."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "uhpC b3667 JW3642"
---

# uhpC

`protein.P09836`

## Static

- Type: `protein`
- Source: `UniProt:P09836`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cell inner membrane {ECO:0000269|PubMed:15919996}; Multi-pass membrane protein {ECO:0000255}.

## Enriched Summary

FUNCTION: Part of the UhpABC signaling cascade that controls the expression of the hexose phosphate transporter UhpT. UhpC senses external glucose-6-phosphate and interacts with the histidine kinase UhpB, leading to the stimulation of the autokinase activity of UhpB. {ECO:0000269|PubMed:11053370, ECO:0000269|PubMed:11739766, ECO:0000269|PubMed:3038843, ECO:0000269|PubMed:8349544}. UhpC belongs to the phosphorelay system UhpB-UhpC-UhpA |CITS [8349544], [3042748], [11325944]| which regulates the uptake of hexose phosphates |CITS [11325944]| (see PWY0-1492 ). UhpC is a membrane-bound protein that senses external glucose-6-phosphate (G-6-P) and interacts with the histidine kinase UhpB. Interaction of UhpC with UhpB stimulates the kinase activity of UhpB with subsequent phosphorylation of the response regulator UhpA |CITS [11739766], [11053370], [12107138], [11325944]|. Phosphorylated UhpA increases the affinity for its specific DNA binding sites and controls the transcriptional expression of the hexose phosphate transporter UhpT |CITS [12107138], [11325944 ]|. uhpB insertion mutants which are consititutive for expression of uhpT are dependent on the presence of uhpC suggesting that UhpB and UhpC may act as a complex in the signalling pathway . Deletion of uhpC results in the elevated expression of a uhpT-lacZ reporter construct that is not further induced by G-6-P...

## Enriched Pathways

- `eco02020` Two-component system (KEGG)

## Annotation

FUNCTION: Part of the UhpABC signaling cascade that controls the expression of the hexose phosphate transporter UhpT. UhpC senses external glucose-6-phosphate and interacts with the histidine kinase UhpB, leading to the stimulation of the autokinase activity of UhpB. {ECO:0000269|PubMed:11053370, ECO:0000269|PubMed:11739766, ECO:0000269|PubMed:3038843, ECO:0000269|PubMed:8349544}.

## Pathways

- `eco02020` Two-component system (KEGG)

## Outgoing Edges (0)

_None._

## Incoming Edges (1)

- `encodes` <-- [[gene.b3667|gene.b3667]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P09836`
- `KEGG:ecj:JW3642;eco:b3667;ecoc:C3026_19875;`
- `GeneID:948184;`
- `GO:GO:0000160; GO:0005886; GO:0015760; GO:0016020; GO:0035435; GO:0061513`

## Notes

Membrane sensor protein UhpC
