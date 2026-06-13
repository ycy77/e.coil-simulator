---
entity_id: "gene.b0607"
entity_type: "gene"
name: "uspG"
source_database: "NCBI RefSeq"
source_id: "gene-b0607"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b0607"
  - "uspG"
---

# uspG

`gene.b0607`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b0607`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

uspG (gene.b0607) is a gene entity. It encodes uspG (protein.P39177). Encoded protein function: FUNCTION: Has intrinsic autoadenylation and autophosphorylation activities, probably on Ser or Thr residues. {ECO:0000269|PubMed:16460009}. EcoCyc product frame: G6334-MONOMER. EcoCyc synonyms: UP12, yzzU, ybdQ. Genomic coordinates: 641439-641867. EcoCyc protein note: UspG belongs to the class II (UspF/G) subfamily of universal stress proteins . Abundance of UspG is increased in response to nitrosative stress . UspG possesses intrinsic autophosphorylation and autoadenylation activity; the C-terminal domain of UspG is important for these activities and required for dimerization . UspG binds to GroEL . A ΔuspG mutant exhibits a defect in resumption of growth after reaching stationary phase and exhibits increased sensitivity to carbonyl cyanide m-chlorophenyl hydrazone (CCCP, a respiratory chain uncoupler), compared to wild type . Single deletions of uspF or uspG have a negative effect on fimbria-dependent adhesion and show enhanced motility. However, the uspFG double mutant shows no adhesion phenotype. A uspF uspG double mutant is more sensitive to oxidative stress and to the antibiotic streptonigrin . UspG abundance is increased in response to stresses including heat, stationary phase, carbon or phosphate starvation, and CCCP treatment . UP12: "unknown protein 12" Reviews:

## Biological Role

Repressed by nac (protein.Q47005).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P39177|protein.P39177]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (1)

- `represses` <-- [[protein.Q47005|protein.Q47005]] `RegulonDB|EcoCyc` `S` - regulator=Nac; target=uspG; function=- | EcoCyc regulation TYPES=Transcription-Factor-Binding

## External IDs

- `Dbxref:ASAP:ABE-0002095,ECOCYC:G6334,GeneID:945229`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:641439-641867:-; feature_type=gene
