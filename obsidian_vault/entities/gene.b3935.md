---
entity_id: "gene.b3935"
entity_type: "gene"
name: "priA"
source_database: "NCBI RefSeq"
source_id: "gene-b3935"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b3935"
  - "priA"
---

# priA

`gene.b3935`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b3935`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

priA (gene.b3935) is a gene entity. It encodes priA (protein.P17888). Encoded protein function: FUNCTION: Initiates the restart of stalled replication forks, which reloads the DnaB replicative helicase on sites other than the origin of replication (PubMed:11532137, PubMed:11929519). Recognizes abandoned replication forks and remodels them to uncover a loading site for DnaB (PubMed:24379377). Serves as the scaffold for primosome assembly (PubMed:1313026, PubMed:8663104, PubMed:8663105, PubMed:8663106). There are several restart pathways, the PriA-PriB pathway is the major replication restart pathway (PubMed:11532137, PubMed:37169801, PubMed:22636770). The PriA-PriB pathway is subdivided into 2 distinct pathways (PubMed:34423481). The PriA-PriC pathway is a minor restart pathway (PubMed:11532137, PubMed:22636770). Recognizes and binds the arrested nascent DNA chain at stalled replication forks. Unwinds the lagging strand at DNA replication forks in the presence of DNA single-stranded binding protein (SSB) (PubMed:10356325, PubMed:30201718). A 3'-5' DNA helicase that requires (d)ATP and is enhanced by DNA single-stranded binding protein (SSB) and/or PriB (PubMed:2825188, PubMed:2833507, PubMed:1313026, PubMed:16188886, PubMed:23193948, PubMed:34423481)...

## Enriched Pathways

- `eco03440` Homologous recombination (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P17888|protein.P17888]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (0)

_None._

## External IDs

- `Dbxref:ASAP:ABE-0012860,ECOCYC:EG10763,GeneID:948426`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:4124612-4126810:-; feature_type=gene
