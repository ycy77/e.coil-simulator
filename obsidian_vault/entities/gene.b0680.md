---
entity_id: "gene.b0680"
entity_type: "gene"
name: "glnS"
source_database: "NCBI RefSeq"
source_id: "gene-b0680"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b0680"
  - "glnS"
---

# glnS

`gene.b0680`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b0680`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

glnS (gene.b0680) is a gene entity. It encodes glnS (protein.P00962). Encoded protein function: Glutamine--tRNA ligase (EC 6.1.1.18) (Glutaminyl-tRNA synthetase) (GlnRS) EcoCyc product frame: GLNS-MONOMER. Genomic coordinates: 706093-707757. EcoCyc protein note: Glutamine-tRNA ligase (GlnRS) is a member of the family of aminoacyl tRNA synthetases, which interpret the genetic code by covalently linking amino acids to their specific tRNA molecules. The reaction is driven by ATP hydrolysis. GlnRS belongs to the Class I aminoacyl tRNA synthetases ; apart from sequence motifs within the active site, the different enzymes show little similarity in their primary amino acid sequences. Substrate recognition and discrimination by GlnRS has been studied extensively. Binding of tRNA and ATP to GlnRS is cooperative, and transfer of the aminoacyl adenylate to the tRNA is the rate determining step . Interactions between the tRNA identity nucleotides and GlnRS modulate the affinity of the enzyme for glutamine , and the terminal adenosine base of tRNAGln mediates amino acid recognition . tRNA binding to GlnRS results in conformational changes in the active site ; induced-fit changes in the active site structure by both amino acid and tRNA binding may contribute to enzyme specificity...

## Enriched Pathways

- `eco00970` Aminoacyl-tRNA biosynthesis (KEGG)
- `eco01100` Metabolic pathways (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P00962|protein.P00962]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (0)

_None._

## External IDs

- `Dbxref:ASAP:ABE-0002317,ECOCYC:EG10390,GeneID:945310`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:706093-707757:+; feature_type=gene
