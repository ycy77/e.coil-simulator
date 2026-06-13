---
entity_id: "gene.b3576"
entity_type: "gene"
name: "yiaL"
source_database: "NCBI RefSeq"
source_id: "gene-b3576"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b3576"
  - "yiaL"
---

# yiaL

`gene.b3576`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b3576`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

yiaL (gene.b3576) is a gene entity. It encodes yiaL (protein.P37673). Encoded protein function: Protein YiaL EcoCyc product frame: EG12280-MONOMER. Genomic coordinates: 3743743-3744210. EcoCyc protein note: A yiaL deletion mutant is 5-fold more sensitive to X-radiation and 3-fold more sensitive to UV-radiation than wild type .

## Biological Role

Repressed by plaR (protein.P37671). Activated by rpoD (protein.P00579), crp (protein.P0ACJ8), rpoE (protein.P0AGB6).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P37673|protein.P37673]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (4)

- `activates` <-- [[protein.P00579|protein.P00579]] `RegulonDB` `S` - sigma=sigma70; target=yiaL; function=+
- `activates` <-- [[protein.P0ACJ8|protein.P0ACJ8]] `RegulonDB` `S` - regulator=CRP; target=yiaL; function=+
- `activates` <-- [[protein.P0AGB6|protein.P0AGB6]] `RegulonDB` `S` - sigma=sigma24; target=yiaL; function=+
- `represses` <-- [[protein.P37671|protein.P37671]] `RegulonDB` `C` - regulator=PlaR; target=yiaL; function=-

## External IDs

- `Dbxref:ASAP:ABE-0011684,ECOCYC:EG12280,GeneID:948094`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:3743743-3744210:+; feature_type=gene
