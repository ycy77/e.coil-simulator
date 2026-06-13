---
entity_id: "gene.b0656"
entity_type: "gene"
name: "insH3"
source_database: "NCBI RefSeq"
source_id: "gene-b0656"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b0656"
  - "insH3"
---

# insH3

`gene.b0656`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b0656`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

insH3 (gene.b0656) is a gene entity. It encodes insH3 (protein.P0CE51). Encoded protein function: FUNCTION: Involved in the transposition of the insertion sequence IS5. EcoCyc product frame: MONOMER0-4235. EcoCyc synonyms: trs5-3, yi52_3. Genomic coordinates: 687997-688977. EcoCyc protein note: InsH is believed to be the transposase for the insertion sequence element IS5. insH spans the length of IS5 . IS5 can enhance gene transcription when it is placed on either side of the promoter for a target gene. This enhancement depends specifically on InsH and its interaction with the termini of the IS5 sequence . The consensus target for IS5 insertion is C(T/A)A(G/A) . Many copies of IS5, and thus InsH, are present in typical E. coli strains .

## Biological Role

Activated by lrp (protein.P0ACJ0).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0CE51|protein.P0CE51]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (1)

- `activates` <-- [[protein.P0ACJ0|protein.P0ACJ0]] `EcoCyc` `database` - EcoCyc regulation TYPES=Transcription-Factor-Binding

## External IDs

- `Dbxref:ASAP:ABE-0002246,ECOCYC:G6360,GeneID:944917`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:687997-688977:-; feature_type=gene
