---
entity_id: "gene.b3187"
entity_type: "gene"
name: "ispB"
source_database: "NCBI RefSeq"
source_id: "gene-b3187"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b3187"
  - "ispB"
---

# ispB

`gene.b3187`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b3187`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

ispB (gene.b3187) is a gene entity. It encodes ispB (protein.P0AD57). Encoded protein function: FUNCTION: Supplies octaprenyl diphosphate, the precursor for the side chain of the isoprenoid quinones ubiquinone and menaquinone. {ECO:0000269|PubMed:8037730}. EcoCyc product frame: OPPSYN-MONOMER. EcoCyc synonyms: cel, yhbD. Genomic coordinates: 3333710-3334681.

## Biological Role

Repressed by nac (protein.Q47005).

## Enriched Pathways

- `eco00900` Terpenoid backbone biosynthesis (KEGG)
- `eco01110` Biosynthesis of secondary metabolites (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0AD57|protein.P0AD57]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (1)

- `represses` <-- [[protein.Q47005|protein.Q47005]] `RegulonDB` `S` - regulator=Nac; target=ispB; function=-

## External IDs

- `Dbxref:ASAP:ABE-0010474,ECOCYC:EG10017,GeneID:947364`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:3333710-3334681:+; feature_type=gene
