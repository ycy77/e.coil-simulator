---
entity_id: "gene.b1010"
entity_type: "gene"
name: "rutC"
source_database: "NCBI RefSeq"
source_id: "gene-b1010"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b1010"
  - "rutC"
---

# rutC

`gene.b1010`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b1010`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

rutC (gene.b1010) is a gene entity. It encodes rutC (protein.P0AFQ5). Encoded protein function: FUNCTION: Involved in pyrimidine catabolism (PubMed:16540542). Catalyzes the deamination of 3-aminoacrylate to malonic semialdehyde, a reaction that can also occur spontaneously (PubMed:33839153). RutC may facilitate the reaction and modulate the metabolic fitness, rather than catalyzing essential functions (PubMed:33839153). In vitro, can also deaminate 2-aminoacrylate (PubMed:33839153). {ECO:0000269|PubMed:16540542, ECO:0000269|PubMed:33839153}. EcoCyc product frame: G6521-MONOMER. EcoCyc synonyms: ycdK. Genomic coordinates: 1071773-1072159.

## Biological Role

Repressed by rutR (protein.P0ACU2). Activated by arcA (protein.P0A9Q1), glnG (protein.P0AFB8).

## Enriched Pathways

- `eco00240` Pyrimidine metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0AFQ5|protein.P0AFQ5]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (3)

- `activates` <-- [[protein.P0A9Q1|protein.P0A9Q1]] `RegulonDB` `S` - regulator=ArcA; target=rutC; function=+
- `activates` <-- [[protein.P0AFB8|protein.P0AFB8]] `RegulonDB` `S` - regulator=NtrC; target=rutC; function=+
- `represses` <-- [[protein.P0ACU2|protein.P0ACU2]] `RegulonDB` `C` - regulator=RutR; target=rutC; function=-

## External IDs

- `Dbxref:ASAP:ABE-0003412,ECOCYC:G6521,GeneID:945599`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:1071773-1072159:-; feature_type=gene
