---
entity_id: "gene.b2501"
entity_type: "gene"
name: "ppk"
source_database: "NCBI RefSeq"
source_id: "gene-b2501"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b2501"
  - "ppk"
---

# ppk

`gene.b2501`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b2501`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

ppk (gene.b2501) is a gene entity. It encodes ppk (protein.P0A7B1). Encoded protein function: FUNCTION: Catalyzes the reversible transfer of the terminal phosphate of ATP to form a long-chain polyphosphate (polyP). Can form linear polymers of orthophosphate with chain lengths up to 1000 or more. Can use GTP instead of ATP, but the efficiency of GTP is 5% that of ATP. Also exhibits several other enzymatic activities, which include: ATP synthesis from polyP in the presence of excess ADP, general nucleoside-diphosphate kinase activity, linear guanosine 5'-tetraphosphate (ppppG) synthesis and autophosphorylation. {ECO:0000269|PubMed:10660553, ECO:0000269|PubMed:8962061}. EcoCyc product frame: PPK-MONOMER. Genomic coordinates: 2623044-2625110.

## Biological Role

Repressed by lrp (protein.P0ACJ0).

## Enriched Pathways

- `eco00190` Oxidative phosphorylation (KEGG)
- `eco03018` RNA degradation (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0A7B1|protein.P0A7B1]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (1)

- `represses` <-- [[protein.P0ACJ0|protein.P0ACJ0]] `EcoCyc` `database` - EcoCyc regulation TYPES=Transcription-Factor-Binding

## External IDs

- `Dbxref:ASAP:ABE-0008235,ECOCYC:EG11510,GeneID:946971`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:2623044-2625110:+; feature_type=gene
