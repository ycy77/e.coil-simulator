---
entity_id: "gene.b2395"
entity_type: "gene"
name: "pdeA"
source_database: "NCBI RefSeq"
source_id: "gene-b2395"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b2395"
  - "pdeA"
---

# pdeA

`gene.b2395`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b2395`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

pdeA (gene.b2395) is a gene entity. It encodes pdeA (protein.P23842). Encoded protein function: FUNCTION: Phosphodiesterase (PDE) that catalyzes the hydrolysis of cyclic-di-GMP (c-di-GMP) to 5'-pGpG. {ECO:0000250|UniProtKB:P21514}. EcoCyc product frame: EG11145-MONOMER. EcoCyc synonyms: yfeA. Genomic coordinates: 2515643-2517832. EcoCyc protein note: PdeA is a predicted c-di-GMP phosphodiesterase that consists of an N-terminal MASE1 (Membrane-Associated SEnsor) domain followed by a degenerate GGDEF domain and a C-terminal EAL domain . A screen for suppressors of the motility defect of a EG12252 ΔpdeH mutant identified activating mutations in E. coli's alternative c-di-GMP phosphodiesterases (PDEs), including PdeA. This supports a model whereby the signaling specificity of PDEs is the result of environmental signals required for their activation. The suppressor mutation in pdeA consisted of a single amino acid substitution in the N-terminal membrane sensory domain of PdeA and resulted in increased swimming motility and reduced levels of intracellular c-di-GMP . pdeA is expressed during exponential growth in rich medium . PdeA: "phosphodiesterase A"

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P23842|protein.P23842]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (0)

_None._

## External IDs

- `Dbxref:ASAP:ABE-0007899,ECOCYC:EG11145,GeneID:946864`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:2515643-2517832:-; feature_type=gene
