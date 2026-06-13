---
entity_id: "gene.b0836"
entity_type: "gene"
name: "bssR"
source_database: "NCBI RefSeq"
source_id: "gene-b0836"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b0836"
  - "bssR"
---

# bssR

`gene.b0836`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b0836`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

bssR (gene.b0836) is a gene entity. It encodes bssR (protein.P0AAY1). Encoded protein function: FUNCTION: Represses biofilm formation in M9C glu and LB glu media but not in M9C and LB media. Seems to act as a global regulator of several genes involved in catabolite repression and stress response and regulation of the uptake and export of signaling pathways. Could be involved the regulation of indole as well as uptake and export of AI-2 through a cAMP-dependent pathway. {ECO:0000269|PubMed:16597943}. EcoCyc product frame: G6436-MONOMER. EcoCyc synonyms: yliH. Genomic coordinates: 878248-878631. EcoCyc protein note: A bssR deletion mutant does not have a significant growth defect. Deletion of bssR leads to increased biofilm formation in LB+glucose and MC9C+glucose media and increased motility in LB medium. Deletion of bssR affects the expression of more than 1000 genes significantly. Among the affected pathways are indole transport and AI-2 uptake and processing. A regulatory model has been proposed . Expression of the bssR gene is induced in stationary phase compared to log phase , and transcription is also induced upon biofilm formation . BssR: "regulator of biofilm through signal secretion"

## Biological Role

Activated by [2Fe-2S] cluster DNA-binding transcriptional dual regulator (complex.ecocyc.CPLX0-7639), fur (protein.P0A9A9).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0AAY1|protein.P0AAY1]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (2)

- `activates` <-- [[complex.ecocyc.CPLX0-7639|complex.ecocyc.CPLX0-7639]] `EcoCyc` `database` - EcoCyc regulation TYPES=Transcription-Factor-Binding
- `activates` <-- [[protein.P0A9A9|protein.P0A9A9]] `RegulonDB` `S` - regulator=Fur; target=bssR; function=+

## External IDs

- `Dbxref:ASAP:ABE-0002849,ECOCYC:G6436,GeneID:945466`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:878248-878631:+; feature_type=gene
