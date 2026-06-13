---
entity_id: "gene.b1207"
entity_type: "gene"
name: "prs"
source_database: "NCBI RefSeq"
source_id: "gene-b1207"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b1207"
  - "prs"
---

# prs

`gene.b1207`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b1207`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

prs (gene.b1207) is a gene entity. It encodes prs (protein.P0A717). Encoded protein function: FUNCTION: Involved in the biosynthesis of the central metabolite phospho-alpha-D-ribosyl-1-pyrophosphate (PRPP) via the transfer of pyrophosphoryl group from ATP to 1-hydroxyl of ribose-5-phosphate (Rib-5-P). {ECO:0000255|HAMAP-Rule:MF_00583, ECO:0000269|PubMed:10954724, ECO:0000269|PubMed:2542328, ECO:0000269|PubMed:3009477, ECO:0000269|PubMed:6290219, ECO:0000269|PubMed:7657655, ECO:0000269|PubMed:8679571, ECO:0000269|PubMed:9125530}. EcoCyc product frame: PRPPSYN-MONOMER. EcoCyc synonyms: dnaR, prsA. Genomic coordinates: 1260928-1261875.

## Biological Role

Repressed by purR (protein.P0ACP7). Activated by rpoD (protein.P00579).

## Enriched Pathways

- `eco00030` Pentose phosphate pathway (KEGG)
- `eco00230` Purine metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01110` Biosynthesis of secondary metabolites (KEGG)
- `eco01120` Microbial metabolism in diverse environments (KEGG)
- `eco01200` Carbon metabolism (KEGG)
- `eco01230` Biosynthesis of amino acids (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0A717|protein.P0A717]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (2)

- `activates` <-- [[protein.P00579|protein.P00579]] `RegulonDB` `S` - sigma=sigma70; target=prs; function=+
- `represses` <-- [[protein.P0ACP7|protein.P0ACP7]] `RegulonDB` `S` - regulator=PurR; target=prs; function=-

## External IDs

- `Dbxref:ASAP:ABE-0004054,ECOCYC:EG10774,GeneID:945772`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:1260928-1261875:-; feature_type=gene
