---
entity_id: "gene.b0920"
entity_type: "gene"
name: "elyC"
source_database: "NCBI RefSeq"
source_id: "gene-b0920"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b0920"
  - "elyC"
---

# elyC

`gene.b0920`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b0920`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

elyC (gene.b0920) is a gene entity. It encodes elyC (protein.P0AB01). Encoded protein function: FUNCTION: Plays a critical role in the metabolism of the essential lipid carrier used for cell wall synthesis. {ECO:0000269|PubMed:24391520}. EcoCyc product frame: EG12166-MONOMER. EcoCyc synonyms: ycbC. Genomic coordinates: 972622-973401. EcoCyc protein note: Cells lacking ElyC have a defect in peptidoglycan synthesis and genetic analysis suggests a role for ElyC in CPD-9646 metabolism . ΔelyC cells show an excess of protein aggregation; overproduction of the periplasmic chaperones, Spy or DsbG, reduces this to a wild-type level . ElyC and CPD0-2646 (ECACYC) are implicated in a pathway that regulates synthesis of CPD-21605 "phosphoglyceride-linked ECA" (ECAPG); ElyC inhibits production of ECAPG most likely at a posttranscriptional level; the full function of ElyC requires ECACYC (consider also ). A ΔelyC mutant grows poorly and forms small colonies at room temperature. In a screen developed to identify genes associated with envelope biogenesis disorders, a ΔelyC mutant has a positive phenotype (chlorophenyl red-β-D-galactopyranoside+ or CPRG+). The growth defect and CPRG+ phenotype can be complemented by expressing elyC in trans. Overproduction of UPPSYN-CPLX "UppS" also specifically suppresses the phenotype associated with loss of ElyC function...

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0AB01|protein.P0AB01]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (0)

_None._

## External IDs

- `Dbxref:ASAP:ABE-0003127,ECOCYC:EG12166,GeneID:945546`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:972622-973401:-; feature_type=gene
