---
entity_id: "gene.b3101"
entity_type: "gene"
name: "yqjF"
source_database: "NCBI RefSeq"
source_id: "gene-b3101"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b3101"
  - "yqjF"
---

# yqjF

`gene.b3101`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b3101`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

yqjF (gene.b3101) is a gene entity. It encodes yqjF (protein.P42619). Encoded protein function: Inner membrane protein YqjF EcoCyc product frame: G7615-MONOMER. Genomic coordinates: 3250562-3250954. EcoCyc protein note: YqiF is predicted to be an inner membrane protein with four transmembrane domains; topology analysis suggests the C-terminus is located in the cytoplasm . Expression of yqjF is induced by 2,4-dinitrotoluene (2,4-DNT), 2,4,6-trinitrotoluene (2,4,6-TNT) and 1,3-dinitrobenzene (1,3-DNB). A degradation product of these compounds is most likely the actual inducer . The induction of yqjF by 2,4-DNT, 2,4,6-TNT, hydroquinone, 2-metoxy-5-nitroaniline, 1,2,4-trihydroxybenzene, and catechol is inhibited in a yhaJ mutant strain. Furthermore, the yhaJ mutant strain showed an accumulation of the 2,4-DNT inducer. The induction of yqjF by 2,4-DNT, hydroquinone, and catechol is enhanced in a yhaK mutant strain .

## Biological Role

Activated by yhaJ (protein.P67660).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P42619|protein.P42619]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (1)

- `activates` <-- [[protein.P67660|protein.P67660]] `RegulonDB` `S` - regulator=YhaJ; target=yqjF; function=+

## External IDs

- `Dbxref:ASAP:ABE-0010200,ECOCYC:G7615,GeneID:947608`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:3250562-3250954:+; feature_type=gene
