---
entity_id: "gene.b3989"
entity_type: "gene"
name: "yjaZ"
source_database: "NCBI RefSeq"
source_id: "gene-b3989"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b3989"
  - "yjaZ"
---

# yjaZ

`gene.b3989`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b3989`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

yjaZ (gene.b3989) is a gene entity. It encodes yjaZ (protein.P27375). Encoded protein function: Protein YjaZ (Heat shock protein C) EcoCyc product frame: EG11429-MONOMER. EcoCyc synonyms: htrC. Genomic coordinates: 4189786-4190325. EcoCyc protein note: yjaZ is a gene of unknown function that was previously thought to code for a heat shock protein, HtrC. A prior study indicated that "htrC" expression was controlled by the heat-shock alternative sigma factor RPOH-MONOMER . Putative htrC mutants showed filamentation at intermediate temperatures, induction of other σ32-modulated heat shock proteins, and growth defects above 42°C . Subsequent reevaluation demonstrated that the original knockout was not in the htrC/yjaZ coding region. An actual yjaZ mutant has no growth effects at higher temperatures, nor does it induce expression of heat shock proteins. A yjaZ mutant does experience slowed growth during entrance to stationary phase . yjaZ expression increases 5-fold during entrance to stationary phase growth .

## Biological Role

Activated by rpoH (protein.P0AGB3).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P27375|protein.P27375]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (1)

- `activates` <-- [[protein.P0AGB3|protein.P0AGB3]] `RegulonDB` `S` - sigma=sigma32; target=yjaZ; function=+

## External IDs

- `Dbxref:ASAP:ABE-0013046,ECOCYC:EG11429,GeneID:948495`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:4189786-4190325:+; feature_type=gene
