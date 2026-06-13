---
entity_id: "gene.b2339"
entity_type: "gene"
name: "yfcV"
source_database: "NCBI RefSeq"
source_id: "gene-b2339"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b2339"
  - "yfcV"
---

# yfcV

`gene.b2339`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b2339`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

yfcV (gene.b2339) is a gene entity. It encodes yfcV (protein.P77288). Encoded protein function: FUNCTION: Part of the yfcOPQRSUV fimbrial operon. Could contribute to adhesion to various surfaces in specific environmental niches. Increases adhesion to eukaryotic T24 bladder epithelial cells in the absence of fim genes. {ECO:0000269|PubMed:20345943}. EcoCyc product frame: G7210-MONOMER. Genomic coordinates: 2455083-2455646. EcoCyc protein note: yfcOPQRSTUV is a putative chaperone-usher fimbrial operon . The operon is cryptic under normal laboratory conditions but when constitutive expression is induced in a strain that lacks the type 1 fimbrial complex the yfc operon promotes adhesion to eukaryotic epithelial cells (T4 bladder cells) . Expression of the yfc operon is regulated by the global regulators PD00288 "H-NS" and CPLX0-226 "CRP cAMP" . E. coli K-12 contains 12 chaperone-usher fimbrial operons, including yfcOPQRSTUV; a fimbria-lacking mutant - strain WQM026 - created by deleting all 12 operons has been characterised .

## Biological Role

Repressed by hns (protein.P0ACF8). Activated by CRP-cyclic-AMP DNA-binding transcriptional dual regulator (complex.ecocyc.CPLX0-226), [2Fe-2S] cluster DNA-binding transcriptional dual regulator (complex.ecocyc.CPLX0-7639), fur (protein.P0A9A9), glaR (protein.P37338).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P77288|protein.P77288]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (5)

- `activates` <-- [[complex.ecocyc.CPLX0-226|complex.ecocyc.CPLX0-226]] `EcoCyc` `database` - EcoCyc regulation TYPES=Transcription-Factor-Binding
- `activates` <-- [[complex.ecocyc.CPLX0-7639|complex.ecocyc.CPLX0-7639]] `EcoCyc` `database` - EcoCyc regulation TYPES=Transcription-Factor-Binding
- `activates` <-- [[protein.P0A9A9|protein.P0A9A9]] `RegulonDB` `S` - regulator=Fur; target=yfcV; function=+
- `activates` <-- [[protein.P37338|protein.P37338]] `RegulonDB|EcoCyc` `S` - regulator=GlaR; target=yfcV; function=+ | EcoCyc regulation TYPES=Transcription-Factor-Binding
- `represses` <-- [[protein.P0ACF8|protein.P0ACF8]] `EcoCyc` `database` - EcoCyc regulation TYPES=Transcription-Factor-Binding

## External IDs

- `Dbxref:ASAP:ABE-0007715,ECOCYC:G7210,GeneID:949109`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:2455083-2455646:-; feature_type=gene
