---
entity_id: "gene.b4096"
entity_type: "gene"
name: "phnL"
source_database: "NCBI RefSeq"
source_id: "gene-b4096"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b4096"
  - "phnL"
---

# phnL

`gene.b4096`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b4096`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

phnL (gene.b4096) is a gene entity. It encodes phnL (protein.P16679). Encoded protein function: FUNCTION: Together with PhnG, PhnH and PhnI is required for the transfer of the ribose triphosphate moiety from ATP to methyl phosphonate. {ECO:0000269|PubMed:22089136}. EcoCyc product frame: PHNL-MONOMER. Genomic coordinates: 4317215-4317895.

## Biological Role

Activated by rpoD (protein.P00579), phoB (protein.P0AFJ5).

## Enriched Pathways

- `eco00440` Phosphonate and phosphinate metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P16679|protein.P16679]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (2)

- `activates` <-- [[protein.P00579|protein.P00579]] `RegulonDB` `S` - sigma=sigma70; target=phnL; function=+
- `activates` <-- [[protein.P0AFJ5|protein.P0AFJ5]] `RegulonDB` `S` - regulator=PhoB; target=phnL; function=+

## External IDs

- `Dbxref:ASAP:ABE-0013421,ECOCYC:EG10721,GeneID:948612`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:4317215-4317895:-; feature_type=gene
