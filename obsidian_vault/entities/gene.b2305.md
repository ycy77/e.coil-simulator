---
entity_id: "gene.b2305"
entity_type: "gene"
name: "rpnB"
source_database: "NCBI RefSeq"
source_id: "gene-b2305"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b2305"
  - "rpnB"
---

# rpnB

`gene.b2305`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b2305`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

rpnB (gene.b2305) is a gene entity. It encodes rpnB (protein.P77768). Encoded protein function: FUNCTION: A low activity DNA endonuclease yielding 3'-hydroxyl ends (Probable). Upon expression enhances RecA-independent DNA recombination 19-fold, concomitantly reducing viability by 98% and inducing DNA damage as measured by induction of the SOS repair response. {ECO:0000269|PubMed:28096446, ECO:0000305|PubMed:28096446}. EcoCyc product frame: G7197-MONOMER. EcoCyc synonyms: yfcI. Genomic coordinates: 2422649-2423539. EcoCyc protein note: RpnB is one of five proteins in E. coli that belong to the "transposase_31" family , which is distantly related to the PD-(D/E)XK nuclease superfamily . Overexpression of rpnB increases RecA-independent recombination, reduces cell viability, and induces expression of the DNA damage-inducible gene dinD . RpnB: "recombination-promoting nuclease B"

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P77768|protein.P77768]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (0)

_None._

## External IDs

- `Dbxref:ASAP:ABE-0007607,ECOCYC:G7197,GeneID:946787`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:2422649-2423539:-; feature_type=gene
