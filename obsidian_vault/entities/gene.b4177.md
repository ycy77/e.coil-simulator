---
entity_id: "gene.b4177"
entity_type: "gene"
name: "purA"
source_database: "NCBI RefSeq"
source_id: "gene-b4177"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b4177"
  - "purA"
---

# purA

`gene.b4177`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b4177`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

purA (gene.b4177) is a gene entity. It encodes purA (protein.P0A7D4). Encoded protein function: FUNCTION: Plays an important role in the de novo pathway of purine nucleotide biosynthesis. Catalyzes the first committed step in the biosynthesis of AMP from IMP. {ECO:0000255|HAMAP-Rule:MF_00011}. EcoCyc product frame: ADENYLOSUCCINATE-SYN-MONOMER. EcoCyc synonyms: adeK. Genomic coordinates: 4404687-4405985.

## Biological Role

Repressed by marA (protein.P0ACH5), purR (protein.P0ACP7).

## Enriched Pathways

- `eco00230` Purine metabolism (KEGG)
- `eco00250` Alanine, aspartate and glutamate metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01232` Nucleotide metabolism (KEGG)
- `eco01240` Biosynthesis of cofactors (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0A7D4|protein.P0A7D4]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (2)

- `represses` <-- [[protein.P0ACH5|protein.P0ACH5]] `RegulonDB` `C` - regulator=MarA; target=purA; function=-
- `represses` <-- [[protein.P0ACP7|protein.P0ACP7]] `RegulonDB` `S` - regulator=PurR; target=purA; function=-

## External IDs

- `Dbxref:ASAP:ABE-0013672,ECOCYC:EG10790,GeneID:948695`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:4404687-4405985:+; feature_type=gene
