---
entity_id: "gene.b1822"
entity_type: "gene"
name: "rlmA"
source_database: "NCBI RefSeq"
source_id: "gene-b1822"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b1822"
  - "rlmA"
---

# rlmA

`gene.b1822`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b1822`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

rlmA (gene.b1822) is a gene entity. It encodes rlmA (protein.P36999). Encoded protein function: FUNCTION: Specifically methylates the guanosine in position 745 of 23S rRNA. {ECO:0000269|PubMed:9440525}. EcoCyc product frame: EG12207-MONOMER. EcoCyc synonyms: rrmA, yebH. Genomic coordinates: 1906251-1907060. EcoCyc protein note: RlmA is the methyltransferase responsible for methylation of 23S rRNA at the N1 position of the G745 nucleotide. RlmA activity is required for wild-type translation and cell growth . The methylated base is expected to reside near the peptide exit channel in the context of the ribosome . In vitro, RlmA is able to methylate free 23S rRNA, but not assembled 50S ribosomal subunits or 70S ribosomes. A 92 nt fragment of 23S rRNA consisting of stem-loops 33, 34 and 35 is efficiently methylated . Specificity for the target nucleotide is determined by the methyltransferase rather than the rRNA substrate . The location of the SAM-binding region and catalytic site have been predicted . RlmA is predicted to have an N-terminal zinc finger and a C-terminal substrate recognition region . The crystal structure of RlmA has been determined at 2.8 Å resolution, and RlmA appears to be an asymmetric dimer. The Zn2+-binding domains may be responsible for RNA recognition and binding . An rlmA mutant lacks 1-methylguanine in its rRNA...

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P36999|protein.P36999]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (0)

_None._

## External IDs

- `Dbxref:ASAP:ABE-0006067,ECOCYC:EG12207,GeneID:946340`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:1906251-1907060:-; feature_type=gene
