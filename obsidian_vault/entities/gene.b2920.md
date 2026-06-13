---
entity_id: "gene.b2920"
entity_type: "gene"
name: "scpC"
source_database: "NCBI RefSeq"
source_id: "gene-b2920"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b2920"
  - "scpC"
---

# scpC

`gene.b2920`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b2920`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

scpC (gene.b2920) is a gene entity. It encodes scpC (protein.P52043). Encoded protein function: FUNCTION: Catalyzes the transfer of coenzyme A from propionyl-CoA to succinate (PubMed:10769117). Could be part of a pathway that converts succinate to propionate (PubMed:10769117). {ECO:0000269|PubMed:10769117}. EcoCyc product frame: G7517-MONOMER. EcoCyc synonyms: ygfH. Genomic coordinates: 3064802-3066280. EcoCyc protein note: The scpC-encoded enzyme is a CoA transferase. This reaction is suggested to be part of a pathway of succinate decarboxylation whose metabolic function is unknown . Deletion of scpC increases heterologous production of 6-deoxyerythronolide B (6dEB), the macrolactone precursor of erythromycin .

## Enriched Pathways

- `eco00640` Propanoate metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P52043|protein.P52043]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (0)

_None._

## External IDs

- `Dbxref:ASAP:ABE-0009583,ECOCYC:G7517,GeneID:947402`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:3064802-3066280:+; feature_type=gene
