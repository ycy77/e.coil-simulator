---
entity_id: "gene.b1885"
entity_type: "gene"
name: "tap"
source_database: "NCBI RefSeq"
source_id: "gene-b1885"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b1885"
  - "tap"
---

# tap

`gene.b1885`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b1885`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

tap (gene.b1885) is a gene entity. It encodes tap (protein.P07018). Encoded protein function: FUNCTION: Mediates taxis toward dipeptides via an interaction with the periplasmic dipeptide-binding protein.; FUNCTION: Chemotactic-signal transducers respond to changes in the concentration of attractants and repellents in the environment, transduce a signal from the outside to the inside of the cell, and facilitate sensory adaptation through the variation of the level of methylation. Attractants increase the level of methylation while repellents decrease the level of methylation, the methyl groups are added by the methyltransferase CheR and removed by the methylesterase CheB. EcoCyc product frame: TAP-MONOMER. Genomic coordinates: 1969383-1970984.

## Biological Role

Activated by fliA (protein.P0AEM6).

## Enriched Pathways

- `eco02020` Two-component system (KEGG)
- `eco02030` Bacterial chemotaxis (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P07018|protein.P07018]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (1)

- `activates` <-- [[protein.P0AEM6|protein.P0AEM6]] `RegulonDB` `S` - sigma=sigma28; target=tap; function=+

## External IDs

- `Dbxref:ASAP:ABE-0006288,ECOCYC:EG10987,GeneID:946397`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:1969383-1970984:-; feature_type=gene
