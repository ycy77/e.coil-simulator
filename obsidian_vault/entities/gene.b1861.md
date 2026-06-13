---
entity_id: "gene.b1861"
entity_type: "gene"
name: "ruvA"
source_database: "NCBI RefSeq"
source_id: "gene-b1861"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b1861"
  - "ruvA"
---

# ruvA

`gene.b1861`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b1861`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

ruvA (gene.b1861) is a gene entity. It encodes ruvA (protein.P0A809). Encoded protein function: FUNCTION: The RuvA-RuvB-RuvC complex processes Holliday junction (HJ) DNA during genetic recombination and DNA repair (PubMed:21531731, PubMed:6374379). The RuvA-RuvB complex plays an important role in the rescue of blocked DNA replication forks via replication fork reversal (RFR); RFR and homologous recombination required for UV light survival can be separated (PubMed:16424908, PubMed:18942176, PubMed:21531731, PubMed:9814711). The RuvA-RuvB complex promotes Holliday junction (HJ) branch migration. RuvA binds to HJ cruciform DNA, conferring on it an open structure (PubMed:10890893, PubMed:7885479, PubMed:9628481). In the presence of RuvB, ATP and Mg(2+) the junction is dissociated; hydrolyzable (d)NTPs can replace ATP but other analogs cannot (PubMed:10772859, PubMed:10890893, PubMed:1608954, PubMed:1617728, PubMed:1833759, PubMed:7885479, PubMed:8393934, PubMed:9628481). The RuvB hexamer acts as a pump, pulling dsDNA into and through the RuvAB complex (PubMed:9078376). Can bypass UV-induced lesions (PubMed:1617728) and physically cross-linked DNA strands (PubMed:10662672)...

## Biological Role

Repressed by lexA (protein.P0A7C2).

## Enriched Pathways

- `eco03440` Homologous recombination (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0A809|protein.P0A809]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (1)

- `represses` <-- [[protein.P0A7C2|protein.P0A7C2]] `RegulonDB` `S` - regulator=LexA; target=ruvA; function=-

## External IDs

- `Dbxref:ASAP:ABE-0006206,ECOCYC:RUVA,GeneID:946369`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:1945365-1945976:-; feature_type=gene
