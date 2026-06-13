---
entity_id: "gene.b0353"
entity_type: "gene"
name: "mhpT"
source_database: "NCBI RefSeq"
source_id: "gene-b0353"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b0353"
  - "mhpT"
---

# mhpT

`gene.b0353`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b0353`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

mhpT (gene.b0353) is a gene entity. It encodes mhpT (protein.P77589). Encoded protein function: FUNCTION: Uptake of 3-(3-hydroxyphenyl)propionate (3HPP) across the cytoplasmic membrane (PubMed:23934492). Transport is driven by the proton motive force (PubMed:23934492). Does not transport benzoate, 3-hydroxybenzoate or gentisate (PubMed:23934492). {ECO:0000269|PubMed:23934492}. EcoCyc product frame: MHPT-MONOMER. EcoCyc synonyms: yaiK. Genomic coordinates: 375459-376670. EcoCyc protein note: MhpT is a putative 3-hydroxyphenylpropionic acid transporter. The mhpT gene is located immediately downstream of the mhpA-E operon, responsible for catabolism of 3-hydroxyphenylpropionate . MhpT is a member of the major facilitator superfamily of transporters and shares a high degree of sequence similarity with PcaK, a 4-hydroxybenzoate transporter from Pseudomonas putida . MhpT may function as a 3-hydroxyphenylpropionate/proton symporter. Imported 3-hydroxyphenylpropionate is converted to 2,3-dihydroxyphenylpropionate and ultimately degraded to Krebs cycle intermediates. MhpT has been implicated in arabinose efflux .

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P77589|protein.P77589]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (0)

_None._

## External IDs

- `Dbxref:ASAP:ABE-0001213,ECOCYC:G6206,GeneID:944997`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:375459-376670:+; feature_type=gene
