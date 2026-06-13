---
entity_id: "gene.b3838"
entity_type: "gene"
name: "tatB"
source_database: "NCBI RefSeq"
source_id: "gene-b3838"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b3838"
  - "tatB"
---

# tatB

`gene.b3838`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b3838`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

tatB (gene.b3838) is a gene entity. It encodes tatB (protein.P69425). Encoded protein function: FUNCTION: Part of the twin-arginine translocation (Tat) system that transports large folded proteins containing a characteristic twin-arginine motif in their signal peptide across membranes. Together with TatC, TatB is part of a receptor directly interacting with Tat signal peptides. TatB may form an oligomeric binding site that transiently accommodates folded Tat precursor proteins before their translocation. {ECO:0000255|HAMAP-Rule:MF_00237, ECO:0000269|PubMed:10593889, ECO:0000269|PubMed:11922668, ECO:0000269|PubMed:14580344, ECO:0000269|PubMed:19666509, ECO:0000269|PubMed:20926683}. EcoCyc product frame: G7808-MONOMER. EcoCyc synonyms: ysgB, mttA2. Genomic coordinates: 4022218-4022733. EcoCyc protein note: TatB is an inner membrane component of the twin arginine translocation (Tat) complex for the export of folded proteins; TatB and TatC form a functional unit that is thought to act as the substrate receptor for the Tat complex. TatB is predicted to contain an N-terminal transmembrane domain followed by a cytoplasmic domain...

## Enriched Pathways

- `eco03060` Protein export (KEGG)
- `eco03070` Bacterial secretion system (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P69425|protein.P69425]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (0)

_None._

## External IDs

- `Dbxref:ASAP:ABE-0012545,ECOCYC:G7808,GeneID:948319`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:4022218-4022733:+; feature_type=gene
