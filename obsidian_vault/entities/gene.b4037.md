---
entity_id: "gene.b4037"
entity_type: "gene"
name: "malM"
source_database: "NCBI RefSeq"
source_id: "gene-b4037"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b4037"
  - "malM"
---

# malM

`gene.b4037`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b4037`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

malM (gene.b4037) is a gene entity. It encodes malM (protein.P03841). Encoded protein function: FUNCTION: Not yet known. Might function in the uptake of a still unidentified substrate. EcoCyc product frame: EG10559-MONOMER. EcoCyc synonyms: molA. Genomic coordinates: 4249554-4250474. EcoCyc protein note: malM is the last gene in the malK-lamB-malM operon and is thus part of the maltose regulon. A signal sequence is cleaved, and the mature MalM protein localizes to the periplasm . The malM gene is conserved between species, but its function is unknown .

## Biological Role

Activated by malT (protein.P06993), crp (protein.P0ACJ8).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P03841|protein.P03841]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (2)

- `activates` <-- [[protein.P06993|protein.P06993]] `RegulonDB` `C` - regulator=MalT; target=malM; function=+
- `activates` <-- [[protein.P0ACJ8|protein.P0ACJ8]] `RegulonDB` `C` - regulator=CRP; target=malM; function=+

## External IDs

- `Dbxref:ASAP:ABE-0013221,ECOCYC:EG10559,GeneID:948547`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:4249554-4250474:+; feature_type=gene
