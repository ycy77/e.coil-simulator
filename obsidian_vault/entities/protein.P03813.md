---
entity_id: "protein.P03813"
entity_type: "protein"
name: "ygeA"
source_database: "UniProt"
source_id: "P03813"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "ygeA b2840 JW2808"
---

# ygeA

`protein.P03813`

## Static

- Type: `protein`
- Source: `UniProt:P03813`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`

## Enriched Summary

FUNCTION: Amino-acid racemase able to utilize a broad range of substrates. Highest activity is observed with L-homoserine and D-homoserine. Has tenfold lower activity against L-methionine, L-leucine, L-valine and L-histidine. Has low activity with L-norvaline, L-asparagine, D-methionine, L-aminobutyric acid, L-isoleucine, L-serine, L-norleucine, L-alanine, L-glutamine, LL-diaminopimelic acid and L-phenylalanine. Has no activity against ten L-amino acids (Thr, Glu, Asp, Arg, Lys, Tyr, Trp, Orn, Cit and Aad) (PubMed:28894939). D-amino acids might be used as components of peptidoglycan and/or be involved in peptidoglycan metabolism and remodeling (PubMed:28894939). {ECO:0000269|PubMed:28894939}.

## Biological Role

Catalyzes lysine racemase (reaction.R00460), arginine racemase (reaction.R00567), glutamine racemase (reaction.R00579), serine racemase (reaction.R00589), ornithine racemase (reaction.R00672). Component of amino acid racemase YgeA (complex.ecocyc.CPLX0-8251).

## Enriched Pathways

- `eco00260` Glycine, serine and threonine metabolism (KEGG)
- `eco00270` Cysteine and methionine metabolism (KEGG)
- `eco00310` Lysine degradation (KEGG)
- `eco00470` D-Amino acid metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01120` Microbial metabolism in diverse environments (KEGG)

## Annotation

FUNCTION: Amino-acid racemase able to utilize a broad range of substrates. Highest activity is observed with L-homoserine and D-homoserine. Has tenfold lower activity against L-methionine, L-leucine, L-valine and L-histidine. Has low activity with L-norvaline, L-asparagine, D-methionine, L-aminobutyric acid, L-isoleucine, L-serine, L-norleucine, L-alanine, L-glutamine, LL-diaminopimelic acid and L-phenylalanine. Has no activity against ten L-amino acids (Thr, Glu, Asp, Arg, Lys, Tyr, Trp, Orn, Cit and Aad) (PubMed:28894939). D-amino acids might be used as components of peptidoglycan and/or be involved in peptidoglycan metabolism and remodeling (PubMed:28894939). {ECO:0000269|PubMed:28894939}.

## Pathways

- `eco00260` Glycine, serine and threonine metabolism (KEGG)
- `eco00270` Cysteine and methionine metabolism (KEGG)
- `eco00310` Lysine degradation (KEGG)
- `eco00470` D-Amino acid metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01120` Microbial metabolism in diverse environments (KEGG)

## Outgoing Edges (6)

- `catalyzes` --> [[reaction.R00460|reaction.R00460]] `KEGG` `database` - via EC:5.1.1.10
- `catalyzes` --> [[reaction.R00567|reaction.R00567]] `KEGG` `database` - via EC:5.1.1.10
- `catalyzes` --> [[reaction.R00579|reaction.R00579]] `KEGG` `database` - via EC:5.1.1.10
- `catalyzes` --> [[reaction.R00589|reaction.R00589]] `KEGG` `database` - via EC:5.1.1.10
- `catalyzes` --> [[reaction.R00672|reaction.R00672]] `KEGG` `database` - via EC:5.1.1.10
- `is_component_of` --> [[complex.ecocyc.CPLX0-8251|complex.ecocyc.CPLX0-8251]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2

## Incoming Edges (1)

- `encodes` <-- [[gene.b2840|gene.b2840]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P03813`
- `KEGG:ecj:JW2808;eco:b2840;ecoc:C3026_15595;`
- `GeneID:947348;`
- `GO:GO:0047661`
- `EC:5.1.1.10`

## Notes

Broad specificity amino-acid racemase YgeA (EC 5.1.1.10)
