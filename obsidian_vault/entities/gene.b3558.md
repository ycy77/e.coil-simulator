---
entity_id: "gene.b3558"
entity_type: "gene"
name: "insK"
source_database: "NCBI RefSeq"
source_id: "gene-b3558"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b3558"
  - "insK"
---

# insK

`gene.b3558`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b3558`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

insK (gene.b3558) is a gene entity. It encodes insK (protein.P19769). Encoded protein function: FUNCTION: Involved in the transposition of the insertion sequence IS150. EcoCyc product frame: G7777-MONOMER. EcoCyc synonyms: dinS, yi5B, t150. Genomic coordinates: 3721198-3722049. EcoCyc protein note: InsB is one of three proteins coded for by the IS150 insertion element. Its function is unknown. The IS150 insertion element, which is found singly or in many copies in various E. coli isolates, codes for three proteins, InsA, InsB and InsAB . Although InsA is translated normally, both InsB and InsAB translation require -1 frameshifts. InsAB translation begins from the same start codon as InsA translation, but a -1 frameshift allows readthrough on the former InsA stop codon, yielding the much longer protein InsAB. InsB translation begins at an ATG within the InsA sequence, requiring a -1 frameshift to properly translate it. In vivo, InsB is generated at a much lower rate than InsA or InsAB. The frameshift that generates InsAB rather than InsA occurs about a third of the time. Disruption of a putative stem-loop region following the frameshift site reduces InsAB expression dramatically . InsAB is the transposase for the IS150 insertion element. Though a lack of InsB has no effect on the process, loss of separate InsA leads to a 5-fold increase in transposition of IS150...

## Biological Role

Activated by nac (protein.Q47005).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P19769|protein.P19769]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (1)

- `activates` <-- [[protein.Q47005|protein.Q47005]] `RegulonDB|EcoCyc` `S` - regulator=Nac; target=insK; function=+ | EcoCyc regulation TYPES=Transcription-Factor-Binding

## External IDs

- `Dbxref:ASAP:ABE-0011622,ECOCYC:G7777,GeneID:948081`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:3721198-3722049:+; feature_type=gene
