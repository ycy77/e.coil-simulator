---
entity_id: "gene.b2064"
entity_type: "gene"
name: "asmA"
source_database: "NCBI RefSeq"
source_id: "gene-b2064"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b2064"
  - "asmA"
---

# asmA

`gene.b2064`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b2064`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

asmA (gene.b2064) is a gene entity. It encodes asmA (protein.P28249). Encoded protein function: FUNCTION: Could be involved in the assembly of outer membrane proteins (PubMed:7476172, PubMed:8866482). May indirectly influence the assembly of outer membrane proteins, potentially by altering outer membrane fluidity (PubMed:8866482). Inhibits the assembly of mutant forms of outer membrane protein F (OmpF) (PubMed:7476172). {ECO:0000269|PubMed:7476172, ECO:0000269|PubMed:8866482}. EcoCyc product frame: EG11361-MONOMER. EcoCyc synonyms: yegA. Genomic coordinates: 2139759-2141612. EcoCyc protein note: AsmA is involved in the assembly of outer membrane proteins, possibly by affecting outer membrane structure. Null mutations of asmA suppress the assembly defects of mutant OmpF and OmpC outer membrane proteins . The OmpF assembly step that is affected by this suppression occurs in the outer membrane . LPS levels in the outer membrane are lowered in asmA null mutants . AsmA is predicted to be a bitopic inner membrane protein asmA null mutations do not affect the assembly of wild-type OmpF . An asmA nonsense mutation contributes to colistin resistance in a laboratory evolved strain .

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P28249|protein.P28249]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (0)

_None._

## External IDs

- `Dbxref:ASAP:ABE-0006833,ECOCYC:EG11361,GeneID:946582`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:2139759-2141612:-; feature_type=gene
