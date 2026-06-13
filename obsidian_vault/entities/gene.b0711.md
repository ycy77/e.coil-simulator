---
entity_id: "gene.b0711"
entity_type: "gene"
name: "pxpB"
source_database: "NCBI RefSeq"
source_id: "gene-b0711"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b0711"
  - "pxpB"
---

# pxpB

`gene.b0711`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b0711`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

pxpB (gene.b0711) is a gene entity. It encodes pxpB (protein.P0AAV4). Encoded protein function: FUNCTION: Catalyzes the cleavage of 5-oxoproline to form L-glutamate coupled to the hydrolysis of ATP to ADP and inorganic phosphate. {ECO:0000269|PubMed:28830929}. EcoCyc product frame: G6380-MONOMER. EcoCyc synonyms: ybgJ. Genomic coordinates: 743593-744249. EcoCyc protein note: Overexpression of pxpBCA leads to the presence of detectable oxoprolinase activity in cell lysates. A pxpB deletion mutant grows to a lower OD than wild type in minimal medium with ammonium as the sole source of nitrogen . A ΔpxpB mutant has aggravating genetic interactions with genes involved in DNA recombination . PxpB: "prokaryotic 5-oxoprolinase B"

## Enriched Pathways

- `eco00480` Glutathione metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0AAV4|protein.P0AAV4]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (0)

_None._

## External IDs

- `Dbxref:ASAP:ABE-0002426,ECOCYC:G6380,GeneID:945311`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:743593-744249:+; feature_type=gene
