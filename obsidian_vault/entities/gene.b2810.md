---
entity_id: "gene.b2810"
entity_type: "gene"
name: "csdA"
source_database: "NCBI RefSeq"
source_id: "gene-b2810"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b2810"
  - "csdA"
---

# csdA

`gene.b2810`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b2810`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

csdA (gene.b2810) is a gene entity. It encodes csdA (protein.Q46925). Encoded protein function: FUNCTION: Catalyzes the removal of elemental sulfur and selenium atoms from L-cysteine, L-cystine, L-selenocysteine, and L-selenocystine to produce L-alanine, and transiently retains the released sulfur atom on a cysteine residue, in the form of a persulfide. Can also desulfinate L-cysteine sulfinate (3-sulfino-L-alanine), which is the best substrate of the enzyme. Functions as a selenium delivery protein in the pathway for the biosynthesis of selenophosphate. Seems to participate in Fe/S biogenesis by recruiting the SufBCD-SufE proteins. Transfers sulfur to CsdE that increases the cysteine desulfurase activity of CsdA. Can also transfer sulfur directly to TcdA/CsdL in vitro. Appears to support the function of TcdA in the generation of cyclic threonylcarbamoyladenosine at position 37 (ct(6)A37) in tRNAs that read codons beginning with adenine. {ECO:0000269|PubMed:10829016, ECO:0000269|PubMed:15901727, ECO:0000269|PubMed:20054882, ECO:0000269|PubMed:23242255, ECO:0000269|PubMed:9278392}. EcoCyc product frame: G7454-MONOMER. EcoCyc synonyms: ygdJ. Genomic coordinates: 2943337-2944542.

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.Q46925|protein.Q46925]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (0)

_None._

## External IDs

- `Dbxref:ASAP:ABE-0009218,ECOCYC:G7454,GeneID:947275`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:2943337-2944542:+; feature_type=gene
