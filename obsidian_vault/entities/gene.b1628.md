---
entity_id: "gene.b1628"
entity_type: "gene"
name: "rsxB"
source_database: "NCBI RefSeq"
source_id: "gene-b1628"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b1628"
  - "rsxB"
---

# rsxB

`gene.b1628`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b1628`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

rsxB (gene.b1628) is a gene entity. It encodes rsxB (protein.P77223). Encoded protein function: FUNCTION: Part of a membrane-bound complex that couples electron transfer with translocation of ions across the membrane (By similarity). Required to maintain the reduced state of SoxR. Probably transfers electron from NAD(P)H to SoxR (PubMed:12773378). {ECO:0000255|HAMAP-Rule:MF_00463, ECO:0000269|PubMed:12773378}. EcoCyc product frame: G6872-MONOMER. EcoCyc synonyms: ydgM. Genomic coordinates: 1706348-1706926. EcoCyc protein note: Products of the rsxABCDGE cluster and G7347 rseC are implicated in a pathway that functions to reduce the PD04132 SoxR iron-sulfur cluster; in-frame deletion of any gene within the cluster results in SoxR-mediated constitutive activation of EG10958 soxS transcription in the absence of oxidative stress . SoxR exists in a more oxidized form in rsx and rseC mutants . The periplasmic flavin transferase EG12073-MONOMER ApbE (renamed Ftp ) is also a component of this system; the RsxABCDGE, RseC and AbpE proteins likely form a complex that uses NAD(P)H to reduce SoxR . The proteins encoded by the rsxABCDGE gene cluster are predicted to form a membrane-associated complex . RsxB has an N-terminal hydrophobic region and two ferredoxin-like motifs (see also ). RsxB is predicted to be a bitopic inner membrane protein...

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P77223|protein.P77223]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (0)

_None._

## External IDs

- `Dbxref:ASAP:ABE-0005452,ECOCYC:G6872,GeneID:946146`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:1706348-1706926:+; feature_type=gene
