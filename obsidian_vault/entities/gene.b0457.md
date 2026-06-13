---
entity_id: "gene.b0457"
entity_type: "gene"
name: "pdeB"
source_database: "NCBI RefSeq"
source_id: "gene-b0457"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b0457"
  - "pdeB"
---

# pdeB

`gene.b0457`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b0457`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

pdeB (gene.b0457) is a gene entity. It encodes pdeB (protein.P77473). Encoded protein function: FUNCTION: Phosphodiesterase (PDE) that catalyzes the hydrolysis of cyclic-di-GMP (c-di-GMP) to 5'-pGpG. {ECO:0000250|UniProtKB:P21514}. EcoCyc product frame: G6252-MONOMER. EcoCyc synonyms: ylaB. Genomic coordinates: 477067-478617. EcoCyc protein note: PdeB is a predicted c-di-GMP-specific phosphodiesterase whose activity is implicated in modulating matrix formation in E. coli biofilm. PdeB is an inner membrane protein with two predicted transmembrane domains which flank a predicted periplasmic CSS domain containing two highly conserved cysteines, followed by a cytoplasmic C-terminal EAL domain with predicted phosphodiesterase activity . PdeB belongs to the core set of eight GGDEF/EAL domain proteins that is absolutely conserved in a set of 61 E. coli genomes containing pathogenic, commensal and probiotic strains . PdeB, like EG11938-MONOMER "PdeC", is subject to redox control and and DegP/DegQ mediated proteolysis; PdeB variants which cannot form a disulphide bond in the periplasmic CSS domain have higher phosphodiesterase activity than the wild-type and interfere with macrocolony morphology when expressed in a cellulose and curli producing K-12 strain (AR3110) . A screen for suppressors of the motility defect of a EG12252 ΔpdeH mutant identified activating mutations in E...

## Biological Role

Repressed by DNA-binding transcriptional dual regulator CpxR-phosphorylated (complex.ecocyc.CPLX0-7748).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P77473|protein.P77473]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (1)

- `represses` <-- [[complex.ecocyc.CPLX0-7748|complex.ecocyc.CPLX0-7748]] `EcoCyc` `database` - EcoCyc regulation TYPES=Transcription-Factor-Binding

## External IDs

- `Dbxref:ASAP:ABE-0001584,ECOCYC:G6252,GeneID:948951`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:477067-478617:-; feature_type=gene
