---
entity_id: "gene.b3249"
entity_type: "gene"
name: "mreD"
source_database: "NCBI RefSeq"
source_id: "gene-b3249"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b3249"
  - "mreD"
---

# mreD

`gene.b3249`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b3249`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

mreD (gene.b3249) is a gene entity. It encodes mreD (protein.P0ABH4). Encoded protein function: FUNCTION: Involved in formation of the rod shape of the cell. May also contribute to regulation of formation of penicillin-binding proteins. EcoCyc product frame: EG10610-MONOMER. Genomic coordinates: 3398387-3398875. EcoCyc protein note: mreD is implicated in the formation of cell shape . Cells depleted of MreD become spherical and eventually lyse . MreD is associated with the inner membrane; MreD interacts with EG10609-MONOMER "MreC". MreD is predicted to contain 5 transmembrane regions with the N-terminus in the periplasm and the C-terminus in the cytoplasm . The Mre proteins are conditionally essential; MreD- cells are viable under slow growth conditions and divide as small spheres, their death under fast growth conditions can be prevented by an increase in ppGpp levels or an increase in the FtsZ division protein. Cells depleted of MreD under fast growth conditions grow as large, non-dividing spheres . mreB, mreC and mreD form an operon in E. coli K-12, transcribed as monocistronic mreB and polycistronic mreBCD mRNA . mre: murein formation gene cluster E

## Biological Role

Repressed by bolA (protein.P0ABE2).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0ABH4|protein.P0ABH4]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (1)

- `represses` <-- [[protein.P0ABE2|protein.P0ABE2]] `RegulonDB` `S` - regulator=BolA; target=mreD; function=-

## External IDs

- `Dbxref:ASAP:ABE-0010656,ECOCYC:EG10610,GeneID:947756`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:3398387-3398875:-; feature_type=gene
