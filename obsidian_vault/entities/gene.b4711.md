---
entity_id: "gene.b4711"
entity_type: "gene"
name: "insH21"
source_database: "NCBI RefSeq"
source_id: "gene-b4711"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b4711"
  - "insH21"
---

# insH21

`gene.b4711`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b4711`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

insH21 (gene.b4711) is a gene entity. It encodes insH21 (protein.A0A385XJE6). Encoded protein function: FUNCTION: Involved in the transposition of the insertion sequence IS5. {ECO:0000305}. EcoCyc product frame: MONOMER0-4347. Genomic coordinates: 1299567-1300547. EcoCyc protein note: InsH is believed to be the transposase for the insertion sequence element IS5. insH spans the length of IS5 . IS5 can enhance gene transcription when it is placed on either side of the promoter for a target gene. This enhancement depends specifically on InsH and its interaction with the termini of the IS5 sequence . The consensus target for IS5 insertion is C(T/A)A(G/A) . Many copies of IS5, and thus InsH, are present in typical E. coli strains .

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.A0A385XJE6|protein.A0A385XJE6]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (0)

_None._

## External IDs

- `Dbxref:ASAP:ABE-0285316,ECOCYC:G0-16639,GeneID:38094952`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:1299567-1300547:+; feature_type=gene
