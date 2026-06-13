---
entity_id: "gene.b2455"
entity_type: "gene"
name: "eutE"
source_database: "NCBI RefSeq"
source_id: "gene-b2455"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b2455"
  - "eutE"
---

# eutE

`gene.b2455`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b2455`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

eutE (gene.b2455) is a gene entity. It encodes eutE (protein.P77445). Encoded protein function: FUNCTION: Acts as the second step in ethanolamine degradation by converting acetaldehyde into acetyl-CoA. May play a role in bacterial microcompartment (BMC) assembly or maintenance. Directly targeted to the BMC (By similarity). Its heterologous expression in S.cerevisiae increases the level of acetylating acetaldehyde dehydrogenase activity (PubMed:26384570). {ECO:0000250|UniProtKB:P41793, ECO:0000269|PubMed:26384570}. EcoCyc product frame: G7285-MONOMER. EcoCyc synonyms: yffX. Genomic coordinates: 2570348-2571751. EcoCyc protein note: Heterologous expression of EutE in various yeasts increases the level of acetylating acetaldehyde dehydrogenase activity in the cells and has been used in metabolic engineering .

## Enriched Pathways

- `eco00620` Pyruvate metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01120` Microbial metabolism in diverse environments (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P77445|protein.P77445]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (0)

_None._

## External IDs

- `Dbxref:ASAP:ABE-0008091,ECOCYC:G7285,GeneID:946943`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:2570348-2571751:-; feature_type=gene
