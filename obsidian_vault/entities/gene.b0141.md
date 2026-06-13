---
entity_id: "gene.b0141"
entity_type: "gene"
name: "yadN"
source_database: "NCBI RefSeq"
source_id: "gene-b0141"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b0141"
  - "yadN"
---

# yadN

`gene.b0141`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b0141`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

yadN (gene.b0141) is a gene entity. It encodes yadN (protein.P37050). Encoded protein function: FUNCTION: Part of the yadCKLM-htrE-yadVN fimbrial operon. Could contribute to adhesion to various surfaces in specific environmental niches. {ECO:0000269|PubMed:20345943}. EcoCyc product frame: EG12328-MONOMER. Genomic coordinates: 156299-156883. EcoCyc protein note: yadNVhtrEyadMLKC is a putative chaperone-usher fimbrial operon in E.coli K-12 . The operon is cryptic under normal laboratory conditions but when constitutive expression is induced in a strain that lacks the type 1 fimbrial complex the yad operon promotes biofilm formation in minimal media on a variety of abiotic surfaces and produces surface fimbrial structures that can be observed microscopically . Constitutive expression of the yad operon results in increased adhesion of cells to xylose; constitutive expression of the yad operon results in increased adherence to intestinal epithelial cells and can modulate the inflammatory reponse of host cells...

## Biological Role

Activated by glaR (protein.P37338).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P37050|protein.P37050]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (1)

- `activates` <-- [[protein.P37338|protein.P37338]] `RegulonDB` `S` - regulator=GlaR; target=yadN; function=+

## External IDs

- `Dbxref:ASAP:ABE-0000487,ECOCYC:EG12328,GeneID:944841`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:156299-156883:-; feature_type=gene
