---
entity_id: "gene.b0916"
entity_type: "gene"
name: "ycaQ"
source_database: "NCBI RefSeq"
source_id: "gene-b0916"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b0916"
  - "ycaQ"
---

# ycaQ

`gene.b0916`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b0916`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

ycaQ (gene.b0916) is a gene entity. It encodes ycaQ (protein.P75843). Encoded protein function: FUNCTION: DNA glycosylase involved in the repair of interstrand DNA cross-links (ICLs), which are highly toxic DNA lesions that covalently tether the opposing strands of DNA, thereby inhibiting essential cellular processes such as DNA replication and transcription (PubMed:32409837). Acts by unhooking both sides of the ICLs, forming abasic (AP) sites on both strands (PubMed:32409837). Unhooks ICLs derived from various cross-linking agents, including azinomycin B (AZB) and mechlorethamine, also known as nitrogen mustard (NM), protecting cells from the toxicity of these cross-linking agents (PubMed:32409837). In vitro, also acts on monoadducts and can catalyze the excision of N7-methylguanine (7mGua) from an oligonucleotide containing N7-methyldeoxyguanosine (d7mG) (PubMed:32409837). Shows no unhooking activity toward FaPy-ICLs (PubMed:32409837). {ECO:0000269|PubMed:32409837}. EcoCyc product frame: G6471-MONOMER. EcoCyc synonyms: alkZ. Genomic coordinates: 969389-970621. EcoCyc protein note: YcaQ is an alkylpurine DNA glycosylase which acts on interstrand cross-links (ICLs) formed by alkylation at purine N3 or N7 positions...

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P75843|protein.P75843]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (0)

_None._

## External IDs

- `Dbxref:ASAP:ABE-0003117,ECOCYC:G6471,GeneID:945524`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:969389-970621:+; feature_type=gene
