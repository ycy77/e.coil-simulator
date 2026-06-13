---
entity_id: "gene.b4837"
entity_type: "gene"
name: "spfP"
source_database: "NCBI RefSeq"
source_id: "gene-b4837"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b4837"
  - "spfP"
---

# spfP

`gene.b4837`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b4837`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

spfP (gene.b4837) is a gene entity. It encodes spfP (protein.P0DW56). Encoded protein function: FUNCTION: Plays a role in carbon catabolite repression (CCR), which prevents expression of genes involved in catabolism of nonpreferred carbon sources when glucose is present. Encoded in dual-function Spot 42 sRNA (spf gene), it inhibits CRP-mediated gene activation when cells are grown in glucose, especially at higher than 30 degrees Celsius (when Spot 42 sRNA base pairing may be less efficient). Overexpression of this protein leads to decreased cell growth on non-glucose carbon sources, with particularly poor growth on galactose. Its overexpression blocks expression of some but not all CRP-dependent operons when grown on the appropriate sugar (blocks galactose- and maltose- but not sorbitol-specific operons), decreases the ability of CRP to activate transcription from the galE P1 promoter. Overexpression has no effect on CRP levels. The base-pairing activity of Spot 42 and the protein-coding activity of SpfP can be genetically separated. {ECO:0000269|PubMed:35239441}. EcoCyc product frame: MONOMER0-4560. Genomic coordinates: 4049917-4049964. EcoCyc protein note: The small protein SpfP coding sequence was found within a small RNA coding sequence called EG30098...

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0DW56|protein.P0DW56]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (0)

_None._

## External IDs

- `Dbxref:ECOCYC:G0-17114,GeneID:302211668`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:4049917-4049964:+; feature_type=gene
