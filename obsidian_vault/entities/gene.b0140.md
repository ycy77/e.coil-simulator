---
entity_id: "gene.b0140"
entity_type: "gene"
name: "yadV"
source_database: "NCBI RefSeq"
source_id: "gene-b0140"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b0140"
  - "yadV"
---

# yadV

`gene.b0140`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b0140`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

yadV (gene.b0140) is a gene entity. It encodes yadV (protein.P33128). Encoded protein function: FUNCTION: Part of the yadCKLM-htrE-yadVN fimbrial operon. Could contribute to adhesion to various surfaces in specific environmental niches. {ECO:0000269|PubMed:20345943}. EcoCyc product frame: EG11973-MONOMER. EcoCyc synonyms: ecpD. Genomic coordinates: 155461-156201. EcoCyc protein note: YadV (formerly EcpD) has similarity to PapD pilin chaperones . yadNVhtrEyadMLKC is a putative chaperone-usher fimbrial operon in E.coli K-12 . The operon is cryptic under normal laboratory conditions but when constitutive expression is induced in a strain that lacks the type 1 fimbrial complex the yad operon promotes biofilm formation in minimal media on a variety of abiotic surfaces and produces surface fimbrial structures that can be observed microscopically . Constitutive expression of the yad operon results in increased adhesion of cells to xylose; constitutive expression of the yad operon results in increased adherence to intestinal epithelial cells and can modulate the inflammatory reponse of host cells . A strain producing Yad fimbriae outcompetes both the wild type and a Δyad strain for corn rhizosphere colonisation Expression of the yad operon is negatively regulated by PD00288 "H-NS"...

## Biological Role

Activated by rpoD (protein.P00579), rpoS (protein.P13445).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P33128|protein.P33128]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (2)

- `activates` <-- [[protein.P00579|protein.P00579]] `RegulonDB` `S` - sigma=sigma70; target=yadV; function=+
- `activates` <-- [[protein.P13445|protein.P13445]] `RegulonDB` `S` - sigma=sigma38; target=yadV; function=+

## External IDs

- `Dbxref:ASAP:ABE-0000482,ECOCYC:EG11973,GeneID:944859`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:155461-156201:-; feature_type=gene
