---
entity_id: "gene.b3667"
entity_type: "gene"
name: "uhpC"
source_database: "NCBI RefSeq"
source_id: "gene-b3667"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b3667"
  - "uhpC"
---

# uhpC

`gene.b3667`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b3667`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

uhpC (gene.b3667) is a gene entity. It encodes uhpC (protein.P09836). Encoded protein function: FUNCTION: Part of the UhpABC signaling cascade that controls the expression of the hexose phosphate transporter UhpT. UhpC senses external glucose-6-phosphate and interacts with the histidine kinase UhpB, leading to the stimulation of the autokinase activity of UhpB. {ECO:0000269|PubMed:11053370, ECO:0000269|PubMed:11739766, ECO:0000269|PubMed:3038843, ECO:0000269|PubMed:8349544}. EcoCyc product frame: GLU-UHPC. Genomic coordinates: 3847305-3848624. EcoCyc protein note: UhpC belongs to the phosphorelay system UhpB-UhpC-UhpA |CITS [8349544], [3042748], [11325944]| which regulates the uptake of hexose phosphates |CITS [11325944]| (see PWY0-1492 ). UhpC is a membrane-bound protein that senses external glucose-6-phosphate (G-6-P) and interacts with the histidine kinase UhpB. Interaction of UhpC with UhpB stimulates the kinase activity of UhpB with subsequent phosphorylation of the response regulator UhpA |CITS [11739766], [11053370], [12107138], [11325944]|. Phosphorylated UhpA increases the affinity for its specific DNA binding sites and controls the transcriptional expression of the hexose phosphate transporter UhpT |CITS [12107138], [11325944 ]|...

## Enriched Pathways

- `eco02020` Two-component system (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P09836|protein.P09836]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (0)

_None._

## External IDs

- `Dbxref:ASAP:ABE-0011990,ECOCYC:EG11053,GeneID:948184`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:3847305-3848624:-; feature_type=gene
