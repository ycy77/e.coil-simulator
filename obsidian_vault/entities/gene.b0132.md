---
entity_id: "gene.b0132"
entity_type: "gene"
name: "rpnC"
source_database: "NCBI RefSeq"
source_id: "gene-b0132"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b0132"
  - "rpnC"
---

# rpnC

`gene.b0132`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b0132`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

rpnC (gene.b0132) is a gene entity. It encodes rpnC (protein.P31665). Encoded protein function: FUNCTION: A low activity DNA endonuclease yielding 3'-hydroxyl ends (Probable). Upon expression enhances RecA-independent DNA recombination 2.9-fold, concomitantly reducing viability by 59% and inducing DNA damage as measured by induction of the SOS repair response. {ECO:0000269|PubMed:28096446}. EcoCyc product frame: EG11748-MONOMER. EcoCyc synonyms: yadD. Genomic coordinates: 146968-147870. EcoCyc protein note: RpnC is one of five proteins in E. coli that belong to the "transposase_31" family , which is distantly related to the PD-(D/E)XK nuclease superfamily . Overexpression of rpnC increases RecA-independent recombination, reduces cell viability, and induces expression of the DNA damage-inducible gene dinD . An insertion mutation in rpnC does not affect the ability to grow on glucose minimal medium . RpnC: "recombination-promoting nuclease C"

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P31665|protein.P31665]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (0)

_None._

## External IDs

- `Dbxref:ASAP:ABE-0000463,ECOCYC:EG11748,GeneID:944781`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:146968-147870:+; feature_type=gene
