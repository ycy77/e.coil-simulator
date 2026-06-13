---
entity_id: "gene.b2514"
entity_type: "gene"
name: "hisS"
source_database: "NCBI RefSeq"
source_id: "gene-b2514"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b2514"
  - "hisS"
---

# hisS

`gene.b2514`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b2514`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

hisS (gene.b2514) is a gene entity. It encodes hisS (protein.P60906). Encoded protein function: Histidine--tRNA ligase (EC 6.1.1.21) (Histidyl-tRNA synthetase) (HisRS) EcoCyc product frame: HISS-MONOMER. Genomic coordinates: 2639301-2640575. EcoCyc protein note: Histidine-tRNA ligase (HisRS) is a member of the family of aminoacyl-tRNA synthetases, which interpret the genetic code by covalently linking amino acids to their specific tRNA molecules. The reaction is driven by ATP hydrolysis. HisRS belongs to the Class II aminoacyl tRNA synthetases, which share three regions of homology . HisRS is a dimer in solution . The C-terminal domain of the protein is required for dimerization, while the N-terminal domain contains most of the catalytic activity. The two domains do not complement each other in trans . Minimal active site fragments likely representing the ancestral "urzyme" have been studied . Specificity determinants within tRNAHis that are important for recognition by HisRS have been identified; the unique G-1:C73 base pair was found to play a crucial role . Specificity determinants and residues within HisRS that are important for catalytic activity have been investigated , and a model for the catalytic cycle was proposed . The C-terminal domain of HisRS was found to be largely responsible for recognition of the tRNAHis anticodon...

## Enriched Pathways

- `eco00970` Aminoacyl-tRNA biosynthesis (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P60906|protein.P60906]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (0)

_None._

## External IDs

- `Dbxref:ASAP:ABE-0008278,ECOCYC:EG10453,GeneID:946989`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:2639301-2640575:-; feature_type=gene
