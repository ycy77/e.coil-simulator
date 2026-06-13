---
entity_id: "gene.b2891"
entity_type: "gene"
name: "prfB"
source_database: "NCBI RefSeq"
source_id: "gene-b2891"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b2891"
  - "prfB"
---

# prfB

`gene.b2891`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b2891`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

prfB (gene.b2891) is a gene entity. It encodes prfB (protein.P07012). Encoded protein function: FUNCTION: Peptide chain release factor 2 directs the termination of translation in response to the peptide chain termination codons UGA and UAA (PubMed:11118225, PubMed:17932046). Acts as a peptidyl-tRNA hydrolase (PubMed:22857598, PubMed:27934701). In the presence of truncated mRNA in the 70S ribosome, ArfA and RF2 interact such that the GGQ peptide hydrolysis motif of RF2 rises into the peptidyl-transferase center (PTC) and releases the ribosome (PubMed:27906160, PubMed:27906161, PubMed:27934701, PubMed:28077875). Recruited by ArfA to rescue stalled ribosomes in the absence of a normal stop codon (PubMed:22857598, PubMed:22922063, PubMed:25355516). A TnaC-stalled ribosome binds RF2, but the active GGQ motif is prevented from engaging with the PTC by TnaC (PubMed:34504068). {ECO:0000269|PubMed:11118225, ECO:0000269|PubMed:17932046, ECO:0000269|PubMed:22857598, ECO:0000269|PubMed:22922063, ECO:0000269|PubMed:25355516, ECO:0000269|PubMed:27906160, ECO:0000269|PubMed:27906161, ECO:0000269|PubMed:27934701, ECO:0000269|PubMed:28077875, ECO:0000269|PubMed:34504068, ECO:0000305|PubMed:22857598}. EcoCyc product frame: EG10762-MONOMER. EcoCyc synonyms: supK. Genomic coordinates: 3035184-3036282. EcoCyc protein note: Release factor 2 (RF2) is one of two class 1 codon-specific factors in E...

## Biological Role

Activated by rpoE (protein.P0AGB6).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P07012|protein.P07012]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (1)

- `activates` <-- [[protein.P0AGB6|protein.P0AGB6]] `RegulonDB` `S` - sigma=sigma24; target=prfB; function=+

## External IDs

- `Dbxref:ASAP:ABE-0009488,ECOCYC:EG10762,GeneID:947369`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:3035184-3036282:-; feature_type=gene
