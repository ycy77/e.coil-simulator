---
entity_id: "gene.b4143"
entity_type: "gene"
name: "groL"
source_database: "NCBI RefSeq"
source_id: "gene-b4143"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b4143"
  - "groL"
---

# groL

`gene.b4143`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b4143`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

groL (gene.b4143) is a gene entity. It encodes groEL (protein.P0A6F5). Encoded protein function: FUNCTION: Together with its co-chaperonin GroES, plays an essential role in assisting protein folding (PubMed:10532860, PubMed:16751100, PubMed:1676490, PubMed:18418386, PubMed:18987317, PubMed:20603018, PubMed:24816391, PubMed:2573517, PubMed:2897629, PubMed:8104102, PubMed:9285593). The GroEL-GroES system forms a nano-cage that allows encapsulation of the non-native substrate proteins and provides a physical environment optimized to promote and accelerate protein folding, probably by preventing aggregation and by entropically destabilizing folding intermediates (PubMed:16751100, PubMed:18418386, PubMed:18987317, PubMed:20603018, PubMed:24816391). Rapid binding of ATP, followed by slower binding of the non-native substrate protein and GroES to the cis open ring of GroEL initiates productive folding of the non-native protein inside a highly stable GroEL-ATP-GroES complex (PubMed:19915138, PubMed:22445172, PubMed:9285585, PubMed:9285593). Binding of ATP and GroES induces conformational changes that result in the release of the substrate protein into a nano-cage compartment, within the GroEL central cavity, for folding in isolation (PubMed:16684774, PubMed:22445172, PubMed:8861908, PubMed:9285585)...

## Biological Role

Repressed by lrp (protein.P0ACJ0). Activated by lrp (protein.P0ACJ0).

## Enriched Pathways

- `eco03018` RNA degradation (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0A6F5|protein.P0A6F5]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (2)

- `activates` <-- [[protein.P0ACJ0|protein.P0ACJ0]] `EcoCyc` `database` - EcoCyc regulation TYPES=Transcription-Factor-Binding
- `represses` <-- [[protein.P0ACJ0|protein.P0ACJ0]] `EcoCyc` `database` - EcoCyc regulation TYPES=Transcription-Factor-Binding

## External IDs

- `Dbxref:ASAP:ABE-0013568,ECOCYC:EG10599,GeneID:948665`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:4371025-4372671:+; feature_type=gene
