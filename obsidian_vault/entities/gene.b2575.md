---
entity_id: "gene.b2575"
entity_type: "gene"
name: "yfiC"
source_database: "NCBI RefSeq"
source_id: "gene-b2575"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b2575"
  - "yfiC"
---

# yfiC

`gene.b2575`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b2575`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

yfiC (gene.b2575) is a gene entity. It encodes yfiC (protein.P31825). Encoded protein function: FUNCTION: Specifically methylates the adenine in position 37 of tRNA(1)(Val) (anticodon cmo5UAC). {ECO:0000269|PubMed:19383770}. EcoCyc product frame: EG11538-MONOMER. EcoCyc synonyms: trmM. Genomic coordinates: 2712027-2712764. EcoCyc protein note: The 37th position of tRNA, located in the anticodon stem-loop 3'-adjacent to the third nucleotide of the anticodon, is generally occupied by a purine and is often modified. The YfiC protein, also known as TrmM, is responsible for methylation of the A37 nucleotide of tRNAVal1 at the N6 position . The m6A modification is relatively rare in tRNA and mostly observed in bacteria. Under standard growth conditions, a yfiC null mutant has no significant growth defect. However, under osmotic or oxidative stress conditions, the yfiC mutant shows decreased survival . X-ray crystal structures of the protein with and without ADENOSYL-HOMO-CYS were published for the orthologous protein from TAX-2095, which can substitute for YfiC. That protein was shown to require a divalent metal ion for activity .

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P31825|protein.P31825]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (0)

_None._

## External IDs

- `Dbxref:ASAP:ABE-0008473,ECOCYC:EG11538,GeneID:947047`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:2712027-2712764:-; feature_type=gene
