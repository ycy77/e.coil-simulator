---
entity_id: "gene.b1468"
entity_type: "gene"
name: "narZ"
source_database: "NCBI RefSeq"
source_id: "gene-b1468"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b1468"
  - "narZ"
---

# narZ

`gene.b1468`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b1468`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

narZ (gene.b1468) is a gene entity. It encodes narZ (protein.P19319). Encoded protein function: FUNCTION: This is a second nitrate reductase enzyme which can substitute for the NRA enzyme and allows E.coli to use nitrate as an electron acceptor during anaerobic growth.; FUNCTION: The alpha chain is the actual site of nitrate reduction. EcoCyc product frame: NARZ-MONOMER. EcoCyc synonyms: chlZ. Genomic coordinates: 1538850-1542590. EcoCyc protein note: narZ encodes the α subunit of nitrate reductase Z; sequence analysis shows it has 76% identity with narG (which encodes the α subunit of nitrate reductase A); it is predicted to be the site of nitrate reduction and to contain the molybdenum cofactor .

## Biological Role

Activated by ompR (protein.P0AA16), ygfI (protein.P52044).

## Enriched Pathways

- `eco00910` Nitrogen metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01120` Microbial metabolism in diverse environments (KEGG)
- `eco01310` Nitrogen cycle (KEGG)
- `eco02020` Two-component system (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P19319|protein.P19319]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (2)

- `activates` <-- [[protein.P0AA16|protein.P0AA16]] `RegulonDB` `S` - regulator=OmpR; target=narZ; function=+
- `activates` <-- [[protein.P52044|protein.P52044]] `EcoCyc` `database` - EcoCyc regulation TYPES=Transcription-Factor-Binding

## External IDs

- `Dbxref:ASAP:ABE-0004898,ECOCYC:EG10648,GeneID:945999`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:1538850-1542590:-; feature_type=gene
