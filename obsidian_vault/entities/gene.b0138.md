---
entity_id: "gene.b0138"
entity_type: "gene"
name: "yadM"
source_database: "NCBI RefSeq"
source_id: "gene-b0138"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b0138"
  - "yadM"
---

# yadM

`gene.b0138`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b0138`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

yadM (gene.b0138) is a gene entity. It encodes yadM (protein.P37018). Encoded protein function: FUNCTION: Part of the yadCKLM-htrE-yadVN fimbrial operon. Could contribute to adhesion to various surfaces in specific environmental niches. {ECO:0000269|PubMed:20345943}. EcoCyc product frame: EG12327-MONOMER. Genomic coordinates: 152243-152812. EcoCyc protein note: yadNVhtrEyadMLKC is a putative chaperone-usher fimbrial operon in E.coli K-12 . The operon is cryptic under normal laboratory conditions but when constitutive expression is induced in a strain that lacks the type 1 fimbrial complex the yad operon promotes biofilm formation in minimal media on a variety of abiotic surfaces and produces surface fimbrial structures that can be observed microscopically . Constitutive expression of the yad operon results in increased adhesion of cells to xylose; constitutive expression of the yad operon results in increased adherence to intestinal epithelial cells and can modulate the inflammatory reponse of host cells . A strain producing Yad fimbriae outcompetes both the wild type and a Δyad strain for corn rhizosphere colonisation Expression of the yad operon is negatively regulated by PD00288 "H-NS" . yad operon expression is subject to complex regulation; affected by different environmental conditions (eg. temperature, oxygen and others) and involves multiple regulatory proteins (eg...

## Biological Role

Repressed by nac (protein.Q47005).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P37018|protein.P37018]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (1)

- `represses` <-- [[protein.Q47005|protein.Q47005]] `RegulonDB|EcoCyc` `S` - regulator=Nac; target=yadM; function=- | EcoCyc regulation TYPES=Transcription-Factor-Binding

## External IDs

- `Dbxref:ASAP:ABE-0000477,ECOCYC:EG12327,GeneID:944828`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:152243-152812:-; feature_type=gene
