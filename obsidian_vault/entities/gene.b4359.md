---
entity_id: "gene.b4359"
entity_type: "gene"
name: "opgB"
source_database: "NCBI RefSeq"
source_id: "gene-b4359"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b4359"
  - "opgB"
---

# opgB

`gene.b4359`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b4359`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

opgB (gene.b4359) is a gene entity. It encodes mdoB (protein.P39401). Encoded protein function: FUNCTION: Transfers a phosphoglycerol residue from phosphatidylglycerol to the membrane-bound nascent glucan backbones. {ECO:0000269|PubMed:2985566, ECO:0000269|PubMed:6094515}. EcoCyc product frame: PGLYCEROLTRANSII-MONOMER. EcoCyc synonyms: yjjO, mdoB. Genomic coordinates: 4597150-4599441. EcoCyc protein note: E. coli opgB encodes two phosphoglycerol transferases. Phosphoglycerol transferase I is a membrane bound enzyme which catalyzes the transfer of phosphoglycerol residues from phosphatidylglycerol to membrane derived oligosaccharides (MDOs), now known as osmoregulated periplasmic glucans (OPGs). Phosphoglycerol transferase II is a soluble periplasmic enzyme which catalyzes the transfer of phosphoglycerol residues between species of MDO leading to the formation of multiply substituted oligosaccharides. In addition, at low concentrations of acceptor, phosphoglycerol transferase II can act as a cyclase liberating free cyclic phosphoglycerol . EcoCyc protein note: Phosphoglycerol transferase II is the proteolytically processed form of PGLYCEROLTRANSI-MONOMER...

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P39401|protein.P39401]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (0)

_None._

## External IDs

- `Dbxref:ASAP:ABE-0014297,ECOCYC:EG12591,GeneID:948888`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:4597150-4599441:-; feature_type=gene
