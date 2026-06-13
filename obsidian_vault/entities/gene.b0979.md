---
entity_id: "gene.b0979"
entity_type: "gene"
name: "appB"
source_database: "NCBI RefSeq"
source_id: "gene-b0979"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b0979"
  - "appB"
---

# appB

`gene.b0979`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b0979`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

appB (gene.b0979) is a gene entity. It encodes appB (protein.P26458). Encoded protein function: FUNCTION: A terminal oxidase that catalyzes quinol-dependent, Na(+)-independent oxygen uptake. Prefers menadiol over other quinols although ubiquinol was not tested (PubMed:8626304). Generates a proton motive force using protons and electrons from opposite sides of the membrane to generate H(2)O, transferring 1 proton/electron. {ECO:0000269|PubMed:19542282, ECO:0000269|PubMed:21987791, ECO:0000269|PubMed:22843529, ECO:0000269|PubMed:8626304}. EcoCyc product frame: APPB-MONOMER. EcoCyc synonyms: cbdB, cyxB. Genomic coordinates: 1039296-1040432. EcoCyc protein note: appB encodes subunit II of cytochrome bd-II. AppB has 57.5% homology with the CYDB-MONOMER "CydB" subunit of CYT-D-UBIOX-CPLX . The AppB subunit harbors a structural ubiquinone-8 or DEMETHYLMENAQUINONE demethylmenaquinone-8 molecule.

## Biological Role

Activated by ydeO (protein.P76135).

## Enriched Pathways

- `eco00190` Oxidative phosphorylation (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco02020` Two-component system (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P26458|protein.P26458]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (1)

- `activates` <-- [[protein.P76135|protein.P76135]] `RegulonDB` `S` - regulator=YdeO; target=appB; function=+

## External IDs

- `Dbxref:ASAP:ABE-0003302,ECOCYC:EG11379,GeneID:947547`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:1039296-1040432:+; feature_type=gene
