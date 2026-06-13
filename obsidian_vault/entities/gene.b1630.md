---
entity_id: "gene.b1630"
entity_type: "gene"
name: "rsxD"
source_database: "NCBI RefSeq"
source_id: "gene-b1630"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b1630"
  - "rsxD"
---

# rsxD

`gene.b1630`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b1630`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

rsxD (gene.b1630) is a gene entity. It encodes rsxD (protein.P76182). Encoded protein function: FUNCTION: Part of a membrane-bound complex that couples electron transfer with translocation of ions across the membrane (By similarity). Required to maintain the reduced state of SoxR. Probably transfers electron from NAD(P)H to SoxR (PubMed:12773378). {ECO:0000255|HAMAP-Rule:MF_00462, ECO:0000269|PubMed:12773378}. EcoCyc product frame: G6874-MONOMER. EcoCyc synonyms: ydgO. Genomic coordinates: 1709142-1710200. EcoCyc protein note: Products of the rsxABCDGE cluster and G7347 rseC are implicated in a pathway that functions to reduce the PD04132 SoxR iron-sulfur cluster; in-frame deletion of any gene within the cluster results in SoxR-mediated constitutive activation of EG10958 soxS transcription in the absence of oxidative stress . SoxR exists in a more oxidized form in rsx and rseC mutants . The periplasmic flavin transferase EG12073-MONOMER ApbE (renamed Ftp ) is also a component of this system; the RsxABCDGE, RseC and AbpE proteins likely form a complex that uses NAD(P)H to reduce SoxR . rsxD is predicted to encode an integral inner membrane protein; the proteins encoded by the rsxABCDGE gene cluster are predicted to form a membrane-associated complex . RsxD is predicted to contain a periplasmic flavin-binding domain...

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P76182|protein.P76182]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (0)

_None._

## External IDs

- `Dbxref:ASAP:ABE-0005457,ECOCYC:G6874,GeneID:946134`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:1709142-1710200:+; feature_type=gene
