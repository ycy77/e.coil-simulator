---
entity_id: "gene.b3963"
entity_type: "gene"
name: "fabR"
source_database: "NCBI RefSeq"
source_id: "gene-b3963"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b3963"
  - "fabR"
---

# fabR

`gene.b3963`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b3963`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

fabR (gene.b3963) is a gene entity. It encodes fabR (protein.P0ACU5). Encoded protein function: FUNCTION: Binds the promoter region of at least fabA and fabB, but probably not yqfA (PubMed:11160901, PubMed:19854834, PubMed:21276098). Represses the transcription of fabA and fabB, involved in unsaturated fatty acid (UFA) biosynthesis (PubMed:11859088). By controlling UFA production, FabR directly influences the physical properties of the membrane bilayer. {ECO:0000269|PubMed:11160901, ECO:0000269|PubMed:11859088, ECO:0000269|PubMed:19854834, ECO:0000269|PubMed:21276098}. EcoCyc product frame: EG11394-MONOMER. EcoCyc synonyms: yijC. Genomic coordinates: 4161067-4161771. EcoCyc protein note: FabR, "Fatty acid biosynthesis Regulator," represses expression of the fabA and fabB genes, which are essential for the synthesis of monounsaturated fatty acids . FabR directly influences membrane lipid homeostasis . It is a unique example of a transcription factor exclusively regulating expression of type II fatty acid synthase enzymes . The FabR consensus sequence has been identified as a palindromic sequence with a length of 18 bp . DNA binding and repression require the binding of unsaturated acyl-ACP (acyl-acyl carrier protein) or acyl-CoA. Saturated acyl-ACP or acyl-CoA competes with the unsaturated fatty acids for binding to FabR but does not trigger DNA binding...

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0ACU5|protein.P0ACU5]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (0)

_None._

## External IDs

- `Dbxref:ASAP:ABE-0012979,ECOCYC:EG11394,GeneID:948460`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:4161067-4161771:+; feature_type=gene
