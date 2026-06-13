---
entity_id: "gene.b0030"
entity_type: "gene"
name: "rihC"
source_database: "NCBI RefSeq"
source_id: "gene-b0030"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b0030"
  - "rihC"
---

# rihC

`gene.b0030`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b0030`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

rihC (gene.b0030) is a gene entity. It encodes rihC (protein.P22564). Encoded protein function: FUNCTION: Hydrolyzes both purine and pyrimidine ribonucleosides with a broad-substrate specificity with decreasing activity in the order uridine, xanthosine, inosine, adenosine, cytidine, guanosine. EcoCyc product frame: EG11082-MONOMER. EcoCyc synonyms: yaaF. Genomic coordinates: 27293-28207. EcoCyc protein note: rihC encodes a ribonucleoside hydrolase with a broad substrate specificity. It has decreasing activity on substrates in the order uridine > xanthosine > inosine > adenosine > cytidine . The enzyme has no activity with deoxyribonucleosides . E. coli contains two other nucleoside hydrolases with differing specificities, encoded by rihA and rihB . The transition state of the enzyme has been modeled based on kinetic isotope effects . Potential active and catalytic sites and the catalytic mechanism of RihC have been computationally predicted . An rihA rihB rihC triple mutant does not exhibit an obvious growth defect . The rihA and rihC genes are subject to catabolite repression . Transcription is induced by nalidixic acid, but not by mitomycin C, and induction does not require LexA .

## Enriched Pathways

- `eco00240` Pyrimidine metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01232` Nucleotide metabolism (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P22564|protein.P22564]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (0)

_None._

## External IDs

- `Dbxref:ASAP:ABE-0000109,ECOCYC:EG11082,GeneID:944796`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:27293-28207:+; feature_type=gene
