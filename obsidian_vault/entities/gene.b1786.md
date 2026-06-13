---
entity_id: "gene.b1786"
entity_type: "gene"
name: "dgcJ"
source_database: "NCBI RefSeq"
source_id: "gene-b1786"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b1786"
  - "dgcJ"
---

# dgcJ

`gene.b1786`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b1786`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

dgcJ (gene.b1786) is a gene entity. It encodes dgcJ (protein.P76237). Encoded protein function: FUNCTION: Catalyzes the synthesis of cyclic-di-GMP (c-di-GMP) via the condensation of 2 GTP molecules. {ECO:0000250|UniProtKB:P31129}. EcoCyc product frame: G6972-MONOMER. EcoCyc synonyms: yeaJ. Genomic coordinates: 1872041-1873531. EcoCyc protein note: DgcJ contains an N-terminal GAPES (GAmma-proteobacterial PEriplasmic Sensory) domain predicted to be periplasmic and a C-terminal cytoplasmic GGDEF domain with predicted diguanylate cyclase activity . DgcJ interacts directly with the C-DI-GMP-activated glycosyltransferase EG11739-MONOMER NfrB and is required for NfrAB-dependent phage N4 infection; DgcJ functions to provide cyclic di-3',5'-guanylate to NrfB wth resultant activation of glycosyltransferase activity . The periplasmic domain of DgcJ likely senses a nutritional signal . A dgcJ null mutant partially suppresses the loss of motility phenotype of a pdeH mutant at 37°C . Deletion of dgcJ increases swimming motility ; complementation by overexpressing dgcJ reduced swimming and swarming back to wild-type levels . dgcJ is expressed during exponential growth . DgcJ is active during vegetative growth at at 37°C; DgcJ, G7049-MONOMER DgcQ, and CPLX0-8535 DgcE all contribute to inhibiting motility of a ΔpdeH mutant at 37°C . Deletion of dgcJ provides strong protection against phage N4...

## Biological Role

Repressed by hns (protein.P0ACF8), lrp (protein.P0ACJ0).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P76237|protein.P76237]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (2)

- `represses` <-- [[protein.P0ACF8|protein.P0ACF8]] `EcoCyc` `database` - EcoCyc regulation TYPES=Transcription-Factor-Binding
- `represses` <-- [[protein.P0ACJ0|protein.P0ACJ0]] `EcoCyc` `database` - EcoCyc regulation TYPES=Transcription-Factor-Binding

## External IDs

- `Dbxref:ASAP:ABE-0005943,ECOCYC:G6972,GeneID:946290`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:1872041-1873531:+; feature_type=gene
