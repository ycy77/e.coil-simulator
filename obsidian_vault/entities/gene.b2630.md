---
entity_id: "gene.b2630"
entity_type: "gene"
name: "rnlA"
source_database: "NCBI RefSeq"
source_id: "gene-b2630"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b2630"
  - "rnlA"
---

# rnlA

`gene.b2630`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b2630`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

rnlA (gene.b2630) is a gene entity. It encodes rnlA (protein.P52129). Encoded protein function: FUNCTION: Toxic component of a type II toxin-antitoxin (TA) system (PubMed:20980243, PubMed:24112600). A stable (half-life 27.6 minutes) endoribonuclease that in the absence of cognate antitoxin RnlB causes generalized RNA degradation. Degrades late enterobacteria phage T4 mRNAs, protecting the host against T4 reproduction. Activity is inhibited by cognate antitoxin RnlB and by enterobacteria phage T4 protein Dmd (PubMed:20980243, PubMed:22403819). Targets cyaA mRNA (PubMed:19019153). {ECO:0000269|PubMed:17895580, ECO:0000269|PubMed:19019153, ECO:0000269|PubMed:20980243, ECO:0000269|PubMed:22403819, ECO:0000269|PubMed:24112600}. EcoCyc product frame: G7365-MONOMER. EcoCyc synonyms: yfjN, std. Genomic coordinates: 2765918-2766991.

## Biological Role

Repressed by iscR (protein.P0AGK8).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P52129|protein.P52129]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (1)

- `represses` <-- [[protein.P0AGK8|protein.P0AGK8]] `RegulonDB` `S` - regulator=IscR; target=rnlA; function=-

## External IDs

- `Dbxref:ASAP:ABE-0008659,ECOCYC:G7365,GeneID:947107`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:2765918-2766991:+; feature_type=gene
