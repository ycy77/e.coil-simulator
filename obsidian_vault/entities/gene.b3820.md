---
entity_id: "gene.b3820"
entity_type: "gene"
name: "yigI"
source_database: "NCBI RefSeq"
source_id: "gene-b3820"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b3820"
  - "yigI"
---

# yigI

`gene.b3820`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b3820`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

yigI (gene.b3820) is a gene entity. It encodes yigI (protein.P0ADP2). Encoded protein function: FUNCTION: Displays thioesterase activity against medium- to long-chain acyl-CoA substrates (PubMed:35876515). Is involved in the thioesterase-dependent beta-oxidation pathway of (9Z,11E)-octadecadienoate (conjugated linoleic acid or CLA), along with TesB and FadM (PubMed:35876515). In vitro, is active against decanoyl-CoA and palmitoyl-CoA (hexadecanoyl-CoA), but not with acetyl-, butyl- or benzoyl-CoA (PubMed:35876515). Lacks general lipase or amidase activity (PubMed:35876515). Likely plays an important and specific role under natural conditions in permitting the metabolism of unusual carbon sources (PubMed:35876515). {ECO:0000269|PubMed:35876515}. EcoCyc product frame: EG11467-MONOMER. Genomic coordinates: 4004230-4004697. EcoCyc protein note: This cytosolic acyl-CoA thioesterase is involved in thioesterase-dependent β-oxidation of fatty acids in E. coli . It participates in the degradation of conjugated linoleic acid (CLA), overlapping in its substrate specificities with two other cytosolic thioesterases in E. coli, EG10995 and G6244; the three genes differ in the conditions under which they are expressed...

## Biological Role

Repressed by arcA (protein.P0A9Q1). Activated by nac (protein.Q47005).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0ADP2|protein.P0ADP2]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (2)

- `activates` <-- [[protein.Q47005|protein.Q47005]] `RegulonDB|EcoCyc` `S` - regulator=Nac; target=yigI; function=+ | EcoCyc regulation TYPES=Transcription-Factor-Binding
- `represses` <-- [[protein.P0A9Q1|protein.P0A9Q1]] `RegulonDB|EcoCyc` `S` - regulator=ArcA; target=yigI; function=- | EcoCyc regulation TYPES=Transcription-Factor-Binding

## External IDs

- `Dbxref:ASAP:ABE-0012474,ECOCYC:EG11467,GeneID:948338`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:4004230-4004697:-; feature_type=gene
