---
entity_id: "gene.b3910"
entity_type: "gene"
name: "yiiM"
source_database: "NCBI RefSeq"
source_id: "gene-b3910"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b3910"
  - "yiiM"
---

# yiiM

`gene.b3910`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b3910`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

yiiM (gene.b3910) is a gene entity. It encodes yiiM (protein.P32157). Encoded protein function: FUNCTION: Reductase involved in the detoxification of N-hydroxylated base analogs (PubMed:18312271). Contributes to the detoxification of 6-N-hydroxylaminopurine (HAP) by catalyzing the reduction of HAP to adenine (PubMed:18312271, PubMed:34921810). Is specific for N-hydroxylated substrates over N-oxides or sulfoxides (PubMed:34921810). In the presence of methyl viologen as reduced electron donor, it preferentially reduces N-hydroxylated compounds such as hydroxylamines, amidoximes, N-hydroxypurines and N-hydroxyureas but shows little or no activity against amine-oxides or sulfoxides (PubMed:34921810). YiiM is not involved in molybdenum cofactor (MoCo) biosynthesis or in MoCo sulfuration (PubMed:18312271). {ECO:0000269|PubMed:18312271, ECO:0000269|PubMed:34921810}. EcoCyc product frame: EG11870-MONOMER. Genomic coordinates: 4102822-4103496.

## Biological Role

Repressed by lrp (protein.P0ACJ0).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P32157|protein.P32157]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (1)

- `represses` <-- [[protein.P0ACJ0|protein.P0ACJ0]] `EcoCyc` `database` - EcoCyc regulation TYPES=Transcription-Factor-Binding

## External IDs

- `Dbxref:ASAP:ABE-0012769,ECOCYC:EG11870,GeneID:948406`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:4102822-4103496:+; feature_type=gene
