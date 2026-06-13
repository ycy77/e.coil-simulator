---
entity_id: "protein.P75869"
entity_type: "protein"
name: "sxy"
source_database: "UniProt"
source_id: "P75869"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "sxy tfoX yccR b0959 JW0942"
---

# sxy

`protein.P75869`

## Static

- Type: `protein`
- Source: `UniProt:P75869`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`

## Enriched Summary

FUNCTION: Induces low levels of natural DNA uptake by inducing transcription of the competence genes (the CRP-S regulon) required for DNA transformation. Induction of the CRP-S regulon also requires Sxy-activated promoter (CRP-S), cAMP receptor protein (CRP) and cAMP (PubMed:17068078, PubMed:22532864). Induces CRP-S site-containing genes which are involved in genome maintenance and transcription or encoding transposases and toxin-antitoxin pairs (PubMed:19502395). {ECO:0000269|PubMed:17068078, ECO:0000269|PubMed:19502395, ECO:0000269|PubMed:22532864}. Sxy is required for transcription from a subset of PD00257 CRP-activated promoters. Sxy is not thought to bind to DNA itself . Genes that are differentially expressed upon overexpression of Sxy were identified by microarray analysis . Although expression of Sxy induces the expression of competence gene homologs, natural transformation was not detected . However, transformation occurs when Sxy is expressed while recombination functions are provided by the λ Red recombinase . Expression of sxy is autoregulated . The Sxy protein is unstable and is rapidly degraded by the Lon protease . A sxy null mutant shows reduced fitness in long-term competitive growth experiments...

## Biological Role

Component of DNA-binding transcriptional repressor CRP-Sxy (complex.ecocyc.CPLX0-8312).

## Annotation

FUNCTION: Induces low levels of natural DNA uptake by inducing transcription of the competence genes (the CRP-S regulon) required for DNA transformation. Induction of the CRP-S regulon also requires Sxy-activated promoter (CRP-S), cAMP receptor protein (CRP) and cAMP (PubMed:17068078, PubMed:22532864). Induces CRP-S site-containing genes which are involved in genome maintenance and transcription or encoding transposases and toxin-antitoxin pairs (PubMed:19502395). {ECO:0000269|PubMed:17068078, ECO:0000269|PubMed:19502395, ECO:0000269|PubMed:22532864}.

## Outgoing Edges (1)

- `is_component_of` --> [[complex.ecocyc.CPLX0-8312|complex.ecocyc.CPLX0-8312]] `EcoCyc` `database` - EcoCyc component coefficient= | EcoCyc protcplxs.col coefficient=1

## Incoming Edges (1)

- `encodes` <-- [[gene.b0959|gene.b0959]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P75869`
- `KEGG:ecj:JW0942;eco:b0959;ecoc:C3026_05865;`
- `GeneID:93776455;946504;`
- `GO:GO:0006355; GO:0009290; GO:0030420; GO:1903658`

## Notes

Protein Sxy (Competence activator Sxy)
