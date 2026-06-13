---
entity_id: "gene.b1323"
entity_type: "gene"
name: "tyrR"
source_database: "NCBI RefSeq"
source_id: "gene-b1323"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b1323"
  - "tyrR"
---

# tyrR

`gene.b1323`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b1323`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

tyrR (gene.b1323) is a gene entity. It encodes tyrR (protein.P07604). Encoded protein function: FUNCTION: Dual transcriptional regulator of the TyrR regulon, which includes a number of genes coding for proteins involved in the biosynthesis or transport of the three aromatic amino acids, phenylalanine, tyrosine and tryptophan (PubMed:14614536, PubMed:15049824, PubMed:1860819, PubMed:334742, PubMed:4399341, PubMed:4887504, PubMed:7798138, PubMed:7961453, PubMed:8449883). These three aromatic amino acids act as effectors which bind to the TyrR protein to form an active regulatory protein (PubMed:1860819, PubMed:334742, PubMed:4399341, PubMed:7961453, PubMed:8106498). Modulates the expression of at least eight unlinked transcription units, including aroF, aroG, aroLM, aroP, mtr, tyrA, tyrB and tyrP (PubMed:14614536, PubMed:15049824, PubMed:1860819, PubMed:334742, PubMed:4399341, PubMed:4887504, PubMed:7798138, PubMed:7961453, PubMed:8449883). In most cases TyrR acts as a repressor, but positive effects have been observed on the tyrP gene, which is repressed in the presence of tyrosine and activated at high phenylalanine concentrations (PubMed:15049824, PubMed:1860819, PubMed:334742, PubMed:7798138, PubMed:8407813, PubMed:8449883)...

## Biological Role

Repressed by lrp (protein.P0ACJ0), pgrR (protein.P77333). Activated by lrp (protein.P0ACJ0), rpoH (protein.P0AGB3).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P07604|protein.P07604]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (4)

- `activates` <-- [[protein.P0ACJ0|protein.P0ACJ0]] `EcoCyc` `database` - EcoCyc regulation TYPES=Transcription-Factor-Binding
- `activates` <-- [[protein.P0AGB3|protein.P0AGB3]] `RegulonDB` `S` - sigma=sigma32; target=tyrR; function=+
- `represses` <-- [[protein.P0ACJ0|protein.P0ACJ0]] `EcoCyc` `database` - EcoCyc regulation TYPES=Transcription-Factor-Binding
- `represses` <-- [[protein.P77333|protein.P77333]] `RegulonDB` `S` - regulator=PgrR; target=tyrR; function=-

## External IDs

- `Dbxref:ASAP:ABE-0004440,ECOCYC:EG11042,GeneID:945879`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:1386720-1388261:+; feature_type=gene
