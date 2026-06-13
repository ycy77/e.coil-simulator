---
entity_id: "gene.b4059"
entity_type: "gene"
name: "ssb"
source_database: "NCBI RefSeq"
source_id: "gene-b4059"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b4059"
  - "ssb"
---

# ssb

`gene.b4059`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b4059`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

ssb (gene.b4059) is a gene entity. It encodes ssb (protein.P0AGE0). Encoded protein function: FUNCTION: Plays an important role in DNA replication, recombination and repair. Binds to ssDNA and to an array of partner proteins to recruit them to their sites of action during DNA metabolism. Acts as a sliding platform that migrates on DNA via reptation. SSB or its 10 C-terminal amino acids stimulates the ATPase activity of RadD (PubMed:27519413). {ECO:0000255|HAMAP-Rule:MF_00984, ECO:0000269|PubMed:18937104, ECO:0000269|PubMed:20360609, ECO:0000269|PubMed:21784244, ECO:0000269|PubMed:27519413}. EcoCyc product frame: EG10976-MONOMER. EcoCyc synonyms: exrB, lexC. Genomic coordinates: 4274125-4274661.

## Biological Role

Repressed by arcA (protein.P0A9Q1). Activated by rpoD (protein.P00579).

## Enriched Pathways

- `eco03030` DNA replication (KEGG)
- `eco03430` Mismatch repair (KEGG)
- `eco03440` Homologous recombination (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0AGE0|protein.P0AGE0]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (2)

- `activates` <-- [[protein.P00579|protein.P00579]] `RegulonDB` `S` - sigma=sigma70; target=ssb; function=+
- `represses` <-- [[protein.P0A9Q1|protein.P0A9Q1]] `RegulonDB` `S` - regulator=ArcA; target=ssb; function=-

## External IDs

- `Dbxref:ASAP:ABE-0013298,ECOCYC:EG10976,GeneID:948570`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:4274125-4274661:+; feature_type=gene
