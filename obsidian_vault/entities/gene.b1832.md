---
entity_id: "gene.b1832"
entity_type: "gene"
name: "msrC"
source_database: "NCBI RefSeq"
source_id: "gene-b1832"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b1832"
  - "msrC"
---

# msrC

`gene.b1832`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b1832`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

msrC (gene.b1832) is a gene entity. It encodes msrC (protein.P76270). Encoded protein function: FUNCTION: Catalyzes the reversible oxidation-reduction of the R-enantiomer of free methionine sulfoxide to methionine. Specific for free L-methionine-(R)-S-oxide. {ECO:0000269|PubMed:17535911}. EcoCyc product frame: G7005-MONOMER. EcoCyc synonyms: yebR. Genomic coordinates: 1915631-1916128.

## Enriched Pathways

- `eco00270` Cysteine and methionine metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P76270|protein.P76270]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (0)

_None._

## External IDs

- `Dbxref:ASAP:ABE-0006095,ECOCYC:G7005,GeneID:946086`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:1915631-1916128:-; feature_type=gene
