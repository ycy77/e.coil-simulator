---
entity_id: "gene.b3243"
entity_type: "gene"
name: "aaeR"
source_database: "NCBI RefSeq"
source_id: "gene-b3243"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b3243"
  - "aaeR"
---

# aaeR

`gene.b3243`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b3243`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

aaeR (gene.b3243) is a gene entity. It encodes aaeR (protein.P67662). Encoded protein function: FUNCTION: Transcriptional regulator that activates expression of the aaeXAB operon, which is involved in the efflux of aromatic carboxylic acids such as p-hydroxybenzoic acid (pHBA) (PubMed:15489430, PubMed:34220787). In the presence of the effector pHBA, acts by binding to a single target within the aaeXAB-aaeR intergenic region (PubMed:34220787). In the absence of pHBA, binds more than 50 sites along the E.coli K12 genome, including genes related to biofilm formation and several genes involved in stress response, suggesting that it might play a role in quorum sensing in the absence of pHBA (PubMed:34220787). {ECO:0000269|PubMed:15489430, ECO:0000269|PubMed:34220787}. EcoCyc product frame: G7688-MONOMER. EcoCyc synonyms: yhcS, qseA. Genomic coordinates: 3389520-3390449. EcoCyc protein note: Based on Genomic SELEX screening it was suggested that AaeR could regulate genes involved in biofilm formation and genes encoding several TFs, such as NimR, Rob, SlyA, YcaN, YgaV, and YneJ . However, in the presence of some hydroxylated and nonhydroxylated aromatic carboxylic acids, such asp-hydroxybenzoic acid (pHBA), salicylate, benzoate, and 1-naphthoate, AaeR binds an intergenic region of its own gene (aaeR) and the aaeXAB operon to activate this operon...

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P67662|protein.P67662]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (0)

_None._

## External IDs

- `Dbxref:ASAP:ABE-0010639,ECOCYC:G7688,GeneID:947760`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:3389520-3390449:+; feature_type=gene
