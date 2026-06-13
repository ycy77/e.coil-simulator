---
entity_id: "gene.b0171"
entity_type: "gene"
name: "pyrH"
source_database: "NCBI RefSeq"
source_id: "gene-b0171"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b0171"
  - "pyrH"
---

# pyrH

`gene.b0171`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b0171`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

pyrH (gene.b0171) is a gene entity. It encodes pyrH (protein.P0A7E9). Encoded protein function: FUNCTION: Catalyzes the reversible phosphorylation of UMP to UDP, with ATP as the most efficient phosphate donor. {ECO:0000269|PubMed:7711027}. EcoCyc product frame: UMPKI-MONOMER. EcoCyc synonyms: umk, smbA. Genomic coordinates: 191855-192580.

## Enriched Pathways

- `eco00240` Pyrimidine metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01232` Nucleotide metabolism (KEGG)
- `eco01240` Biosynthesis of cofactors (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0A7E9|protein.P0A7E9]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (0)

_None._

## External IDs

- `Dbxref:ASAP:ABE-0000582,ECOCYC:EG11539,GeneID:944989`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:191855-192580:+; feature_type=gene
