---
entity_id: "gene.b0446"
entity_type: "gene"
name: "cof"
source_database: "NCBI RefSeq"
source_id: "gene-b0446"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b0446"
  - "cof"
---

# cof

`gene.b0446`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b0446`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

cof (gene.b0446) is a gene entity. It encodes cof (protein.P46891). Encoded protein function: FUNCTION: Catalyzes the hydrolysis of 4-amino-2-methyl-5-hydroxymethylpyrimidine pyrophosphate (HMP-PP) to 4-amino-2-methyl-5-hydroxymethylpyrimidine phosphate (HMP-P). Can also hydrolyze other substrates such as MeO-HMP-PP and 4-amino-2-trifluoromethyl 5-hydroxymethylpyrimidine pyrophosphate (CF3-HMP-PP) to give MeO-HMP-P and 4-amino-2-trifluoromethyl-5-hydroxymethylpyrimidine phosphate. This hydrolysis generates resistance to the antibiotics (bacimethrin, CF3-HMP) by reducing the formation of their toxic forms, 2'-methoxythiamin pyrophosphate (MeO-TPP) and CF3-HMP-PP. Also hydrolyzes pyridoxal-phosphate (PLP) and flavin mononucleotide (FMN), and purines (GMP and IMP) as secondary substrates. {ECO:0000255|HAMAP-Rule:MF_01847, ECO:0000269|PubMed:15292217, ECO:0000269|PubMed:16990279}. EcoCyc product frame: G6246-MONOMER. Genomic coordinates: 467412-468230. EcoCyc protein note: Cof is a phosphatase belonging to the superfamily of haloacid dehalogenase (HAD)-like hydrolases. The enzyme is involved in the hydrolysis of HMP-PP, an intermediate in thiamin biosynthesis . In a screen using a variety of compounds, its preferred substrate is pyridoxal phosphate; purine and pyrimidine nucleotides are secondary substrates...

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P46891|protein.P46891]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (0)

_None._

## External IDs

- `Dbxref:ASAP:ABE-0001548,ECOCYC:G6246,GeneID:945089`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:467412-468230:+; feature_type=gene
