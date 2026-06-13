---
entity_id: "gene.b1066"
entity_type: "gene"
name: "rimJ"
source_database: "NCBI RefSeq"
source_id: "gene-b1066"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b1066"
  - "rimJ"
---

# rimJ

`gene.b1066`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b1066`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

rimJ (gene.b1066) is a gene entity. It encodes rimJ (protein.P0A948). Encoded protein function: FUNCTION: Acetylates the N-terminal alanine of ribosomal protein uS5 (PubMed:2828880, PubMed:385889). Also plays a role in maturation of the 30S ribosomal subunit (PubMed:18466225, PubMed:20176963). Plays a role in the temperature regulation of pap pilin transcription (PubMed:1356970). {ECO:0000269|PubMed:1356970, ECO:0000269|PubMed:18466225, ECO:0000269|PubMed:20176963, ECO:0000269|PubMed:2828880, ECO:0000269|PubMed:385889}. EcoCyc product frame: EG10851-MONOMER. EcoCyc synonyms: tcp. Genomic coordinates: 1125562-1126146. EcoCyc protein note: RimJ is an alanine acetyltransferase that is specific for EG10904-MONOMER . RimJ also plays a role in maturation of the 30S ribosomal subunit . RimJ interacts with pre-30S, but not mature ribosomal subunits . RimJ has overall similarity to RimL and C-terminal similarity to RimI . Overexpression of RimJ, even when lacking its acetyltransferase activity, suppresses the 16S rRNA maturation defect of an RpsE G28D mutant . Overexpression of RimJ decreases the levels of the immature long precursor 16S rRNA (lp16S rRNA) in the RpsE G28D mutant . In a rimJ mutant, the ribosomal protein S5 is not acetylated at the N terminus . Mutation of the conserved cysteine residues C54 and/or C105 results in loss of RimJ acetyltransferase activity...

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0A948|protein.P0A948]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (0)

_None._

## External IDs

- `Dbxref:ASAP:ABE-0003622,ECOCYC:EG10851,GeneID:946910`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:1125562-1126146:+; feature_type=gene
