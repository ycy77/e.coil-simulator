---
entity_id: "gene.b3557"
entity_type: "gene"
name: "insJ"
source_database: "NCBI RefSeq"
source_id: "gene-b3557"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b3557"
  - "insJ"
---

# insJ

`gene.b3557`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b3557`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

insJ (gene.b3557) is a gene entity. It encodes insJ (protein.P19768). Encoded protein function: Insertion element IS150 protein InsJ (ORFA) EcoCyc product frame: G7776-MONOMER. EcoCyc synonyms: yi5A. Genomic coordinates: 3720680-3721201. EcoCyc protein note: InsA is one of three proteins coded for by the IS150 insertion element. It appears to prevent incomplete transposition by InsAB. The IS150 insertion element, which is found singly or in many copies in various E. coli isolates, codes for three proteins, InsA, InsB and InsAB . Although InsA is translated normally, both InsB and InsAB translation require -1 frameshifts. InsAB translation begins from the same start codon as InsA translation, but a -1 frameshift allows readthrough on the former InsA stop codon, yielding the much longer protein InsAB. InsB translation begins at an ATG within the InsA sequence, requiring a -1 frameshift to properly translate it. In vivo, InsB is generated at a much lower rate than InsA or InsAB. The frameshift that generates InsAB rather than InsA occurs about a third of the time. Disruption of a putative stem-loop region following the frameshift site reduces InsAB expression dramatically . InsAB is the transposase for the IS150 insertion element. Though a lack of InsB has no effect on the process, loss of separate InsA leads to a 5-fold increase in transposition of IS150...

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P19768|protein.P19768]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (0)

_None._

## External IDs

- `Dbxref:ASAP:ABE-0011620,ECOCYC:G7776,GeneID:948082`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:3720680-3721201:+; feature_type=gene
