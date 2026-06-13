---
entity_id: "gene.b3932"
entity_type: "gene"
name: "hslV"
source_database: "NCBI RefSeq"
source_id: "gene-b3932"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b3932"
  - "hslV"
---

# hslV

`gene.b3932`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b3932`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

hslV (gene.b3932) is a gene entity. It encodes hslV (protein.P0A7B8). Encoded protein function: FUNCTION: Protease subunit of a proteasome-like degradation complex believed to be a general protein degrading machinery. The complex has been shown to be involved in the specific degradation of heat shock induced transcription factors such as RpoH and SulA. In addition, small hydrophobic peptides are also hydrolyzed by HslV. HslV has weak protease activity even in the absence of HslU, but this activity is induced more than 100-fold in the presence of HslU. HslU recognizes protein substrates and unfolds these before guiding them to HslV for hydrolysis. HslV is not believed to degrade folded proteins. {ECO:0000255|HAMAP-Rule:MF_00248, ECO:0000269|PubMed:10419524, ECO:0000269|PubMed:10452560, ECO:0000269|PubMed:15696175, ECO:0000269|PubMed:8650174, ECO:0000269|PubMed:8662828, ECO:0000269|PubMed:9288941, ECO:0000269|PubMed:9393683}. EcoCyc product frame: EG11676-MONOMER. EcoCyc synonyms: yiiC, clpQ, htpO. Genomic coordinates: 4121757-4122287.

## Biological Role

Activated by rpoH (protein.P0AGB3).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0A7B8|protein.P0A7B8]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (1)

- `activates` <-- [[protein.P0AGB3|protein.P0AGB3]] `RegulonDB` `S` - sigma=sigma32; target=hslV; function=+

## External IDs

- `Dbxref:ASAP:ABE-0012845,ECOCYC:EG11676,GeneID:948429`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:4121757-4122287:-; feature_type=gene
