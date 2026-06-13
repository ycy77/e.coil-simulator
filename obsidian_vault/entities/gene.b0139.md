---
entity_id: "gene.b0139"
entity_type: "gene"
name: "htrE"
source_database: "NCBI RefSeq"
source_id: "gene-b0139"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b0139"
  - "htrE"
---

# htrE

`gene.b0139`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b0139`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

htrE (gene.b0139) is a gene entity. It encodes htrE (protein.P33129). Encoded protein function: FUNCTION: Part of the yadCKLM-htrE-yadVN fimbrial operon. Could contribute to adhesion to various surfaces in specific environmental niches. Probably involved in the export and assembly of fimbrial subunits across the outer membrane. {ECO:0000269|PubMed:20345943}. EcoCyc product frame: EG11972-MONOMER. Genomic coordinates: 152829-155426. EcoCyc protein note: HtrE has similarity to PapC, which is a type II pilin porin . yadNVhtrEyadMLKC is a putative chaperone-usher fimbrial operon in E.coli K-12 . The operon is cryptic under normal laboratory conditions but when constitutive expression is induced in a strain that lacks the type 1 fimbrial complex the yad operon promotes biofilm formation in minimal media on a variety of abiotic surfaces and produces surface fimbrial structures that can be observed microscopically . Constitutive expression of the yad operon results in increased adhesion of cells to xylose; constitutive expression of the yad operon results in increased adherence to intestinal epithelial cells and can modulate the inflammatory reponse of host cells . A strain producing Yad fimbriae outcompetes both the wild type and a Δyad strain for corn rhizosphere colonisation...

## Biological Role

Repressed by nac (protein.Q47005). Activated by rpoD (protein.P00579), lrp (protein.P0ACJ0), rpoS (protein.P13445), glaR (protein.P37338).

## Enriched Pathways

- `eco02020` Two-component system (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P33129|protein.P33129]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (5)

- `activates` <-- [[protein.P00579|protein.P00579]] `RegulonDB` `S` - sigma=sigma70; target=htrE; function=+
- `activates` <-- [[protein.P0ACJ0|protein.P0ACJ0]] `EcoCyc` `database` - EcoCyc regulation TYPES=Transcription-Factor-Binding
- `activates` <-- [[protein.P13445|protein.P13445]] `RegulonDB` `S` - sigma=sigma38; target=htrE; function=+
- `activates` <-- [[protein.P37338|protein.P37338]] `RegulonDB|EcoCyc` `S` - regulator=GlaR; target=htrE; function=+ | EcoCyc regulation TYPES=Transcription-Factor-Binding
- `represses` <-- [[protein.Q47005|protein.Q47005]] `RegulonDB|EcoCyc` `S` - regulator=Nac; target=htrE; function=- | EcoCyc regulation TYPES=Transcription-Factor-Binding

## External IDs

- `Dbxref:ASAP:ABE-0000479,ECOCYC:EG11972,GeneID:944819`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:152829-155426:-; feature_type=gene
