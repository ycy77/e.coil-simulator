---
entity_id: "gene.b3813"
entity_type: "gene"
name: "uvrD"
source_database: "NCBI RefSeq"
source_id: "gene-b3813"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b3813"
  - "uvrD"
---

# uvrD

`gene.b3813`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b3813`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

uvrD (gene.b3813) is a gene entity. It encodes uvrD (protein.P03018). Encoded protein function: FUNCTION: A helicase with DNA-dependent ATPase activity (PubMed:6319401, PubMed:8419285). Unwinds DNA duplexes with 3'-5' polarity (PubMed:2170128, PubMed:8419285). Translocates on single-stranded DNA with 3'-5' polarity (PubMed:2942537). Initiates unwinding more efficiently from a nicked substrate than double-stranded DNA (PubMed:2170128, PubMed:8419285). Involved in the post-incision events of nucleotide excision repair and methyl-directed mismatch repair, and probably also in repair of alkylated DNA (Probable) (PubMed:25484163). {ECO:0000269|PubMed:2170128, ECO:0000269|PubMed:2942537, ECO:0000269|PubMed:8419285, ECO:0000305|PubMed:25484163}. EcoCyc product frame: EG11064-MONOMER. EcoCyc synonyms: uvr502, srjC, uvrE, dar-2, dda, mutU, pdeB, rad. Genomic coordinates: 3997983-4000145.

## Enriched Pathways

- `eco03420` Nucleotide excision repair (KEGG)
- `eco03430` Mismatch repair (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P03018|protein.P03018]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (0)

_None._

## External IDs

- `Dbxref:ASAP:ABE-0012455,ECOCYC:EG11064,GeneID:948347`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:3997983-4000145:+; feature_type=gene
