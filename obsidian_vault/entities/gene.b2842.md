---
entity_id: "gene.b2842"
entity_type: "gene"
name: "kduD"
source_database: "NCBI RefSeq"
source_id: "gene-b2842"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b2842"
  - "kduD"
---

# kduD

`gene.b2842`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b2842`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

kduD (gene.b2842) is a gene entity. It encodes kduD (protein.P37769). Encoded protein function: FUNCTION: Catalyzes the reversible reduction of 2,5-diketo-3-deoxygluconate (DKII or 4,6-dihydroxy-2,5-dioxohexanoate) into 2-keto-3-deoxygluconate (KDG or 2-dehydro-3-deoxygluconate) with a concomitant oxidation of NADH (Ref.4). To a lesser extent, can also reduce 5-keto-D-gluconate and oxidize D-gluconate and 1,2-propanediol (PubMed:24509771). Together with KduI, seems to play a role in the catabolism of hexuronates under osmotic stress conditions, substituting for the regular hexuronate degrading enzymes UxaABC and UxuAB whose expression is repressed in these conditions (PubMed:23437267). In vitro, also exhibits NADH-dependent 20-ketosteroid reductase activity against eukaryotic steroid hormone 11-deoxycorticosterone (11-DOC), which is converted into the product 4-pregnen-20,21-diol-3-one. In addition to 11-DOC, five other C21 steroid compounds (11-deoxycortisol, cortisol, corticosterone, cortisone, and 21-hydroxypregnenolone) are reduced by KduD, but steroids lacking the hydroxyl group at C21 position, such as pregnenolone, testosterone propionate, cortisone acetate, or progesterone, cannot be used as substrate (PubMed:24509771). {ECO:0000269|PubMed:23437267, ECO:0000269|PubMed:24509771, ECO:0000269|Ref.4}. EcoCyc product frame: KDUD-MONOMER. EcoCyc synonyms: yqeD, ygeC...

## Enriched Pathways

- `eco00040` Pentose and glucuronate interconversions (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01120` Microbial metabolism in diverse environments (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P37769|protein.P37769]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (0)

_None._

## External IDs

- `Dbxref:ASAP:ABE-0009330,ECOCYC:EG12361,GeneID:947323`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:2982497-2983258:-; feature_type=gene
