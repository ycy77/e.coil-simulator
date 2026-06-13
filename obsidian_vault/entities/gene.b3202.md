---
entity_id: "gene.b3202"
entity_type: "gene"
name: "rpoN"
source_database: "NCBI RefSeq"
source_id: "gene-b3202"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b3202"
  - "rpoN"
---

# rpoN

`gene.b3202`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b3202`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

rpoN (gene.b3202) is a gene entity. It encodes rpoN (protein.P24255). Encoded protein function: FUNCTION: Sigma factors are initiation factors that promote the attachment of RNA polymerase to specific initiation sites and are then released. This sigma factor is responsible for the expression of enzymes involved in arginine catabolism. The open complex (sigma-54 and core RNA polymerase) serves as the receptor for the receipt of the melting signal from the remotely bound activator protein GlnG(NtrC). EcoCyc product frame: RPON-MONOMER. EcoCyc synonyms: glnF, ntrA. Genomic coordinates: 3344717-3346150. EcoCyc protein note: Sigma 54 controls expression of nitrogen-related genes, directing RNAP54-CPLX to the consensus nitrogen promoter. Sigma 54 is the sigma factor controlling nitrogen-regulated and other nitrogen-related promoters . It copurifies with the RNA polymerase core enzyme and binds to the consensus nitrogen promoter . It is also involved in the nitric oxide stress response . Mutants lacking rpoN had a significant defect in polyP synthesis . During typical exponential and stationary phase growth, the amount of sigma 54 present in the cell is one tenth that of the amount of sigma 70 . The metabolic context of genes dependent on sigma54 for transcription is reviewed in...

## Biological Role

Repressed by lrp (protein.P0ACJ0). Activated by rpoE (protein.P0AGB6).

## Enriched Pathways

- `eco02020` Two-component system (KEGG)
- `eco02040` Flagellar assembly (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P24255|protein.P24255]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (2)

- `activates` <-- [[protein.P0AGB6|protein.P0AGB6]] `RegulonDB` `S` - sigma=sigma24; target=rpoN; function=+
- `represses` <-- [[protein.P0ACJ0|protein.P0ACJ0]] `EcoCyc` `database` - EcoCyc regulation TYPES=Transcription-Factor-Binding

## External IDs

- `Dbxref:ASAP:ABE-0010514,ECOCYC:EG10898,GeneID:947714`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:3344717-3346150:+; feature_type=gene
