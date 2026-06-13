---
entity_id: "gene.b1467"
entity_type: "gene"
name: "narY"
source_database: "NCBI RefSeq"
source_id: "gene-b1467"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b1467"
  - "narY"
---

# narY

`gene.b1467`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b1467`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

narY (gene.b1467) is a gene entity. It encodes narY (protein.P19318). Encoded protein function: FUNCTION: This is a second nitrate reductase enzyme which can substitute for the NRA enzyme and allows E.coli to use nitrate as an electron acceptor during anaerobic growth. The beta chain is an electron transfer unit containing four cysteine clusters involved in the formation of iron-sulfur centers. Electrons are transferred from the gamma chain to the molybdenum cofactor of the alpha subunit. EcoCyc product frame: NARY-MONOMER. EcoCyc synonyms: chlZ. Genomic coordinates: 1537309-1538853. EcoCyc protein note: narY encodes the β subunit of nitrate reductase Z; sequence analysis shows it has 75% identity with narH (which encodes the β subunit of nitrate reductase A); it is predicted to contain the iron-sulfur clusters (see also ) - one [3Fe-4S] cluster (FS4) and three [4Fe-4S] clusters (FS1, FS2 and FS3).

## Biological Role

Activated by ompR (protein.P0AA16).

## Enriched Pathways

- `eco00910` Nitrogen metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01120` Microbial metabolism in diverse environments (KEGG)
- `eco01310` Nitrogen cycle (KEGG)
- `eco02020` Two-component system (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P19318|protein.P19318]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (1)

- `activates` <-- [[protein.P0AA16|protein.P0AA16]] `RegulonDB` `S` - regulator=OmpR; target=narY; function=+

## External IDs

- `Dbxref:ASAP:ABE-0004896,ECOCYC:EG10647,GeneID:946034`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:1537309-1538853:-; feature_type=gene
