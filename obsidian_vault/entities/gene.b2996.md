---
entity_id: "gene.b2996"
entity_type: "gene"
name: "hybA"
source_database: "NCBI RefSeq"
source_id: "gene-b2996"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b2996"
  - "hybA"
---

# hybA

`gene.b2996`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b2996`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

hybA (gene.b2996) is a gene entity. It encodes hybA (protein.P0AAJ8). Encoded protein function: FUNCTION: Participates in the periplasmic electron-transferring activity of hydrogenase 2 during its catalytic turnover. EcoCyc product frame: HYBA-MONOMER. EcoCyc synonyms: hydL. Genomic coordinates: 3144154-3145140. EcoCyc protein note: The hybA-encoded protein may be involved in the periplasmic electron-transferring activity of hydrogenase 2 during catalytic turnover . hybA contains a single C-terminal transmembrane helix; HybA is assembled in a Tat-dependent manner . hybA contains 16 cysteines and contains 4 predicted [Fe-S] binding sites (see also ). An hybA in-frame deletion mutant can not grow on glycerol and fumarate as the sole energy sources, and its reduced fumarate-dependent hydrogen uptake activity is comparable to a hybC deletion mutant; however, the HybOHybC complex is correctly targeted to the membrane . HybA is essential for electron transfer from H(2) to the quinone pool; it is also essential for the H(2) evolving redox reaction; it is not required for electron transfer to and from redox active viologen dyes in whole cells of E. coli .

## Biological Role

Activated by rpoD (protein.P00579).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0AAJ8|protein.P0AAJ8]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (1)

- `activates` <-- [[protein.P00579|protein.P00579]] `RegulonDB` `C` - sigma=sigma70; target=hybA; function=+

## External IDs

- `Dbxref:ASAP:ABE-0009832,ECOCYC:EG11799,GeneID:944842`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:3144154-3145140:-; feature_type=gene
