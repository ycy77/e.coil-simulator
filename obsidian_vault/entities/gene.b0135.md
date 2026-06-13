---
entity_id: "gene.b0135"
entity_type: "gene"
name: "yadC"
source_database: "NCBI RefSeq"
source_id: "gene-b0135"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b0135"
  - "yadC"
---

# yadC

`gene.b0135`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b0135`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

yadC (gene.b0135) is a gene entity. It encodes yadC (protein.P31058). Encoded protein function: FUNCTION: Part of the yadCKLM-htrE-yadVN fimbrial operon. Could contribute to adhesion to various surfaces in specific environmental niches. {ECO:0000269|PubMed:20345943}. EcoCyc product frame: EG11678-MONOMER. Genomic coordinates: 149715-150953. EcoCyc protein note: yadNVhtrEyadMLKC is a putative chaperone-usher fimbrial operon in E. coli K-12 . The operon is cryptic under normal laboratory conditions but when constitutive expression is induced in a strain that lacks the type 1 fimbrial complex the yad operon promotes biofilm formation in minimal media on a variety of abiotic surfaces and produces surface fimbrial structures that can be observed microscopically . Constitutive expression of the yad operon results in increased adhesion of cells to xylose; constitutive expression of the yad operon results in increased adherence to intestinal epithelial cells and can modulate the inflammatory reponse of host cells . A strain producing Yad fimbriae outcompetes both the wild type and a Δyad strain for corn rhizosphere colonisation YadC is predicted to contain two domains (a C-terminal pilin domain and an N-terminal lectin domain) similar to the type 1 fimbrial tip-adhesin FimH. Constitutive expression of the yad operon results in increased adhesion to xylose; YadC binds to xylose...

## Biological Role

Repressed by hns (protein.P0ACF8), nac (protein.Q47005).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P31058|protein.P31058]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (2)

- `represses` <-- [[protein.P0ACF8|protein.P0ACF8]] `EcoCyc` `database` - EcoCyc regulation TYPES=Transcription-Factor-Binding
- `represses` <-- [[protein.Q47005|protein.Q47005]] `RegulonDB|EcoCyc` `S` - regulator=Nac; target=yadC; function=- | EcoCyc regulation TYPES=Transcription-Factor-Binding

## External IDs

- `Dbxref:ASAP:ABE-0000470,ECOCYC:EG11678,GeneID:944837`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:149715-150953:-; feature_type=gene
