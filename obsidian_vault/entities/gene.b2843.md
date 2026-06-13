---
entity_id: "gene.b2843"
entity_type: "gene"
name: "kduI"
source_database: "NCBI RefSeq"
source_id: "gene-b2843"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b2843"
  - "kduI"
---

# kduI

`gene.b2843`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b2843`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

kduI (gene.b2843) is a gene entity. It encodes kduI (protein.Q46938). Encoded protein function: FUNCTION: Catalyzes the isomerization of 5-dehydro-4-deoxy-D-glucuronate to 3-deoxy-D-glycero-2,5-hexodiulosonate (By similarity). Plays a role in the catabolism of hexuronates under osmotic stress conditions, likely substituting for the regular hexuronate degrading enzyme UxaC whose expression is repressed in these conditions (PubMed:23437267). {ECO:0000250|UniProtKB:Q05529, ECO:0000269|PubMed:23437267}. EcoCyc product frame: G7463-MONOMER. EcoCyc synonyms: yqeE. Genomic coordinates: 2983288-2984124. EcoCyc protein note: KduI was a predicted 5-keto 4-deoxyuronate isomerase due to its high sequence similarity to the enzyme from Erwinia chrysanthemi. In unpurified form, the enzyme appeares to be able to utilize both glucuronate and galacturonate, perhaps catalyzing the same reaction as UXAC-MONOMER "UxaC". While UxaC expression is repressed under osmotic stress conditions, KduI expression appears to be unaffected, and it could therefore substitute for UxaC . The purified protein was recently shown to catalyze the activity of EC-5.3.1.17 in coupled assays with KduD from Pectobacterium carotovorum or Streptococcus agalactiae...

## Biological Role

Repressed by nac (protein.Q47005).

## Enriched Pathways

- `eco00040` Pentose and glucuronate interconversions (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01120` Microbial metabolism in diverse environments (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.Q46938|protein.Q46938]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (1)

- `represses` <-- [[protein.Q47005|protein.Q47005]] `RegulonDB` `S` - regulator=Nac; target=kduI; function=-

## External IDs

- `Dbxref:ASAP:ABE-0009332,ECOCYC:G7463,GeneID:947319`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:2983288-2984124:-; feature_type=gene
