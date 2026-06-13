---
entity_id: "gene.b3657"
entity_type: "gene"
name: "yicJ"
source_database: "NCBI RefSeq"
source_id: "gene-b3657"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b3657"
  - "yicJ"
---

# yicJ

`gene.b3657`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b3657`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

yicJ (gene.b3657) is a gene entity. It encodes yicJ (protein.P31435). Encoded protein function: Inner membrane symporter YicJ EcoCyc product frame: YICJ-MONOMER. Genomic coordinates: 3834547-3835929. EcoCyc protein note: yicJI is predicted to be a member of the EG20253-MONOMER "XylR" regulon; its products may mediate transport (YicJ) and hydrolysis (YicI) of xylooligosaccharides; putative XylR and CRP binding sites are identified upstream of yicJI YicJ is a member of the GPH family of glycoside-pentoside-hexuronide transporters .

## Biological Role

Activated by rpoE (protein.P0AGB6), nac (protein.Q47005).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P31435|protein.P31435]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (2)

- `activates` <-- [[protein.P0AGB6|protein.P0AGB6]] `RegulonDB` `S` - sigma=sigma24; target=yicJ; function=+
- `activates` <-- [[protein.Q47005|protein.Q47005]] `RegulonDB|EcoCyc` `S` - regulator=Nac; target=yicJ; function=+ | EcoCyc regulation TYPES=Transcription-Factor-Binding

## External IDs

- `Dbxref:ASAP:ABE-0011953,ECOCYC:EG11686,GeneID:948168`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:3834547-3835929:-; feature_type=gene
