---
entity_id: "gene.b1670"
entity_type: "gene"
name: "ydhU"
source_database: "NCBI RefSeq"
source_id: "gene-b1670"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b1670"
  - "ydhU"
---

# ydhU

`gene.b1670`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b1670`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

ydhU (gene.b1670) is a gene entity. It encodes ydhU (protein.P77409). Encoded protein function: Putative cytochrome YdhU (Protein PhsC homolog) EcoCyc product frame: G6898-MONOMER. Genomic coordinates: 1749563-1750348. EcoCyc protein note: YdhU is a predicted cytochrome b-containing integral membrane protein. Based on sequence similarity, the ydhYVWXUT operon may encode components of an oxidoreductase . A ydhY-T mutant does not show a growth defect under anaerobic conditions, although utilization of certain sources of sulfur is impaired .

## Biological Role

Repressed by narL (protein.P0AF28), narP (protein.P31802). Activated by fnr (protein.P0A9E5), rpoS (protein.P13445).

## Enriched Pathways

- `eco00920` Sulfur metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01120` Microbial metabolism in diverse environments (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P77409|protein.P77409]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (4)

- `activates` <-- [[protein.P0A9E5|protein.P0A9E5]] `RegulonDB` `C` - regulator=FNR; target=ydhU; function=+
- `activates` <-- [[protein.P13445|protein.P13445]] `RegulonDB` `S` - sigma=sigma38; target=ydhU; function=+
- `represses` <-- [[protein.P0AF28|protein.P0AF28]] `RegulonDB` `C` - regulator=NarL; target=ydhU; function=-
- `represses` <-- [[protein.P31802|protein.P31802]] `RegulonDB` `C` - regulator=NarP; target=ydhU; function=-

## External IDs

- `Dbxref:ASAP:ABE-0005579,ECOCYC:G6898,GeneID:945608`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:1749563-1750348:-; feature_type=gene
