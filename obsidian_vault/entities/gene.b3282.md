---
entity_id: "gene.b3282"
entity_type: "gene"
name: "tsaC"
source_database: "NCBI RefSeq"
source_id: "gene-b3282"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b3282"
  - "tsaC"
---

# tsaC

`gene.b3282`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b3282`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

tsaC (gene.b3282) is a gene entity. It encodes tsaC (protein.P45748). Encoded protein function: FUNCTION: Required for the formation of a threonylcarbamoyl group on adenosine at position 37 (t(6)A37) in tRNAs that read codons beginning with adenine. Catalyzes the conversion of L-threonine, HCO(3)(-)/CO(2) and ATP to give threonylcarbamoyl-AMP (TC-AMP) as the acyladenylate intermediate, with the release of diphosphate. Is also able to catalyze the reverse reaction in vitro, i.e. the formation of ATP from TC-AMP and PPi. Shows higher affinity for the full-length tRNA(Thr) lacking only the t(6)A37 modification than for its fully modified counterpart. Could also be required for the maturation of 16S rRNA. Binds to double-stranded RNA but does not interact tightly with either of the ribosomal subunits, or the 70S particles. {ECO:0000255|HAMAP-Rule:MF_01852, ECO:0000269|PubMed:15716138, ECO:0000269|PubMed:19287007, ECO:0000269|PubMed:21285948, ECO:0000269|PubMed:22378793, ECO:0000269|PubMed:23072323}. EcoCyc product frame: G7698-MONOMER. EcoCyc synonyms: yrdC, rimN. Genomic coordinates: 3430843-3431415. EcoCyc protein note: Threonylcarbamoyl-AMP synthase (TsaC) catalyzes the synthesis of threonylcarbamoyl-AMP, an intermediate in the biosynthesis of the threonylcarbamoyladenosine (t6A) modification at position 37 of ANN-decoding tRNAs...

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P45748|protein.P45748]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (0)

_None._

## External IDs

- `Dbxref:ASAP:ABE-0010766,ECOCYC:G7698,GeneID:947783`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:3430843-3431415:-; feature_type=gene
