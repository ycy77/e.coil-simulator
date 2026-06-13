---
entity_id: "gene.b3835"
entity_type: "gene"
name: "ubiB"
source_database: "NCBI RefSeq"
source_id: "gene-b3835"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b3835"
  - "ubiB"
---

# ubiB

`gene.b3835`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b3835`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

ubiB (gene.b3835) is a gene entity. It encodes ubiB (protein.P0A6A0). Encoded protein function: FUNCTION: Is probably a protein kinase regulator of UbiI activity which is involved in aerobic coenzyme Q (ubiquinone) biosynthesis. {ECO:0000255|HAMAP-Rule:MF_00414, ECO:0000269|PubMed:10960098, ECO:0000269|PubMed:9422602}. EcoCyc product frame: 2-OCTAPRENYLPHENOL-HYDROX-MONOMER. EcoCyc synonyms: yigS, yigQ, yigR, aarF. Genomic coordinates: 4020226-4021866. EcoCyc protein note: UbiB is involved in the biosynthesis of ubiquinone-8. Until recently, it was thought to provide the 2-octaprenylphenol hydroxylase activity, which catalyzes the first hydroxylation step in the ubiquinone biosynthesis pathway. However, no direct biochemical evidence for the enzymatic function of UbiB is available, and the reaction is now thought to be catalyzed by EG11333-MONOMER "UbiI" . UbiB is part of an atypical protein kinase-like family and thus may function as a regulator . A ubiB insertion mutant does not grow on succinate as the sole source of carbon and has a slow growth phenotype . ubiB mutants accumulate 2-octaprenylphenol . The original ubiB allele of strain AN59 contains an IS1 insertion in ubiE, located upstream of ubiB, which appears to have a polar effect on ubiB . The human COQ8A protein is a member of the UbiB protein family and is associated with ubiquinone-10 biosynthesis...

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0A6A0|protein.P0A6A0]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (0)

_None._

## External IDs

- `Dbxref:ASAP:ABE-0012539,ECOCYC:EG11476,GeneID:948322`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:4020226-4021866:+; feature_type=gene
