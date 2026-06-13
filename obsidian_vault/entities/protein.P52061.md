---
entity_id: "protein.P52061"
entity_type: "protein"
name: "rdgB"
source_database: "UniProt"
source_id: "P52061"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "rdgB yggV b2954 JW2921"
---

# rdgB

`protein.P52061`

## Static

- Type: `protein`
- Source: `UniProt:P52061`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`

## Enriched Summary

FUNCTION: Pyrophosphatase that catalyzes the hydrolysis of nucleoside triphosphates to their monophosphate derivatives, with a high preference for the non-canonical purine nucleotides XTP (xanthosine triphosphate), dITP (deoxyinosine triphosphate) and ITP (PubMed:12297000, PubMed:17976651). Can also efficiently hydrolyze 2'-deoxy-N-6-hydroxylaminopurine triphosphate (dHAPTP) (PubMed:17090528). Seems to function as a house-cleaning enzyme that removes non-canonical purine nucleotides from the nucleotide pool, thus preventing their incorporation into DNA/RNA and avoiding chromosomal lesions (PubMed:12297000, PubMed:12730170, PubMed:17090528). To a much lesser extent, is also able to hydrolyze GTP, dGTP and dUTP, but shows very low activity toward the canonical nucleotides dATP, dCTP and dTTP and toward 8-oxo-dGTP, purine deoxyribose triphosphate, 2-aminopurine deoxyribose triphosphate and 2,6-diaminopurine deoxyribose triphosphate (PubMed:12297000, PubMed:17090528). {ECO:0000255|HAMAP-Rule:MF_01405, ECO:0000269|PubMed:12297000, ECO:0000269|PubMed:12730170, ECO:0000269|PubMed:17090528, ECO:0000269|PubMed:17976651}.; FUNCTION: Genetic interactions among priB, dam, lexA, nagC, polA, rdgB, rdgB, rep and uup link the PriA-PriB replication restart pathway to DNA double-strand break repair (PubMed:36326440). {ECO:0000269|PubMed:36326440}.

## Biological Role

Catalyzes inosine 5'-triphosphate pyrophosphohydrolase (reaction.R00720). Component of dITP/XTP pyrophosphatase (complex.ecocyc.CPLX0-7826).

## Enriched Pathways

- `eco00230` Purine metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01232` Nucleotide metabolism (KEGG)

## Annotation

FUNCTION: Pyrophosphatase that catalyzes the hydrolysis of nucleoside triphosphates to their monophosphate derivatives, with a high preference for the non-canonical purine nucleotides XTP (xanthosine triphosphate), dITP (deoxyinosine triphosphate) and ITP (PubMed:12297000, PubMed:17976651). Can also efficiently hydrolyze 2'-deoxy-N-6-hydroxylaminopurine triphosphate (dHAPTP) (PubMed:17090528). Seems to function as a house-cleaning enzyme that removes non-canonical purine nucleotides from the nucleotide pool, thus preventing their incorporation into DNA/RNA and avoiding chromosomal lesions (PubMed:12297000, PubMed:12730170, PubMed:17090528). To a much lesser extent, is also able to hydrolyze GTP, dGTP and dUTP, but shows very low activity toward the canonical nucleotides dATP, dCTP and dTTP and toward 8-oxo-dGTP, purine deoxyribose triphosphate, 2-aminopurine deoxyribose triphosphate and 2,6-diaminopurine deoxyribose triphosphate (PubMed:12297000, PubMed:17090528). {ECO:0000255|HAMAP-Rule:MF_01405, ECO:0000269|PubMed:12297000, ECO:0000269|PubMed:12730170, ECO:0000269|PubMed:17090528, ECO:0000269|PubMed:17976651}.; FUNCTION: Genetic interactions among priB, dam, lexA, nagC, polA, rdgB, rdgB, rep and uup link the PriA-PriB replication restart pathway to DNA double-strand break repair (PubMed:36326440). {ECO:0000269|PubMed:36326440}.

## Pathways

- `eco00230` Purine metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01232` Nucleotide metabolism (KEGG)

## Outgoing Edges (2)

- `catalyzes` --> [[reaction.R00720|reaction.R00720]] `KEGG` `database` - via EC:3.6.1.66
- `is_component_of` --> [[complex.ecocyc.CPLX0-7826|complex.ecocyc.CPLX0-7826]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2

## Incoming Edges (1)

- `encodes` <-- [[gene.b2954|gene.b2954]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P52061`
- `KEGG:ecj:JW2921;eco:b2954;ecoc:C3026_16165;`
- `GeneID:947429;`
- `GO:GO:0000166; GO:0000287; GO:0005737; GO:0005829; GO:0009117; GO:0009143; GO:0009146; GO:0017111; GO:0035870; GO:0036220; GO:0036222; GO:0042803; GO:0047429`
- `EC:3.6.1.66`

## Notes

dITP/XTP pyrophosphatase (EC 3.6.1.66) (Deoxyribonucleoside triphosphate pyrophosphohydrolase) (Inosine triphosphate pyrophosphatase) (ITPase) (Non-canonical purine NTP pyrophosphatase) (Non-standard purine NTP pyrophosphatase) (Nucleoside-triphosphate diphosphatase) (Nucleoside-triphosphate pyrophosphatase) (NTPase)
