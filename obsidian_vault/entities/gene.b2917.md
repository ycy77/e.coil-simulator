---
entity_id: "gene.b2917"
entity_type: "gene"
name: "scpA"
source_database: "NCBI RefSeq"
source_id: "gene-b2917"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b2917"
  - "scpA"
---

# scpA

`gene.b2917`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b2917`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

scpA (gene.b2917) is a gene entity. It encodes scpA (protein.P27253). Encoded protein function: FUNCTION: Catalyzes the interconversion of succinyl-CoA and methylmalonyl-CoA. Could be part of a pathway that converts succinate to propionate. {ECO:0000269|PubMed:10769117, ECO:0000269|PubMed:11955068}. EcoCyc product frame: METHYLMALONYL-COA-MUT-MONOMER. EcoCyc synonyms: yliK, sbm. Genomic coordinates: 3060850-3062994. EcoCyc protein note: Methylmalonyl-CoA mutase (MCM) catalyzes the reversible, stereospecific interconversion of methylmalonyl-CoA to succinyl-CoA . The enzyme may participate in a pathway of succinate decarboxylation whose metabolic role is unknown . MCM and the YgfD (ArgK) protein interact both in vivo and in vitro . Sbm: "sleeping beauty mutase"

## Enriched Pathways

- `eco00280` Valine, leucine and isoleucine degradation (KEGG)
- `eco00630` Glyoxylate and dicarboxylate metabolism (KEGG)
- `eco00640` Propanoate metabolism (KEGG)
- `eco00720` Other carbon fixation pathways (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01120` Microbial metabolism in diverse environments (KEGG)
- `eco01200` Carbon metabolism (KEGG)
- `eco04980` Cobalamin transport and metabolism (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P27253|protein.P27253]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (0)

_None._

## External IDs

- `Dbxref:ASAP:ABE-0009577,ECOCYC:EG11444,GeneID:945576`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:3060850-3062994:+; feature_type=gene
