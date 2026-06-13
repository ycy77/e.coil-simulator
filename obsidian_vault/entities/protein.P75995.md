---
entity_id: "protein.P75995"
entity_type: "protein"
name: "pdeG"
source_database: "UniProt"
source_id: "P75995"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cell membrane {ECO:0000305}; Multi-pass membrane protein {ECO:0000255}. Note=Found associated with the RNA degradosome. {ECO:0000269|PubMed:16139413}."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "pdeG ycgG b1168 JW5174"
---

# pdeG

`protein.P75995`

## Static

- Type: `protein`
- Source: `UniProt:P75995`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cell membrane {ECO:0000305}; Multi-pass membrane protein {ECO:0000255}. Note=Found associated with the RNA degradosome. {ECO:0000269|PubMed:16139413}.

## Enriched Summary

FUNCTION: Phosphodiesterase (PDE) that catalyzes the hydrolysis of cyclic-di-GMP (c-di-GMP) to 5'-pGpG. {ECO:0000250|UniProtKB:P21514}. PdeG is a predicted c-di-GMP phosphodiesterase. PdeG is predicted to contain two transmembrane domains which flank a periplasmic CSS domain containing two highly conserved cysteines, followed by a cytoplasmic C-terminal EAL domain with predicted phosphodiesterase activity . PdeG consistently copurifies with the degradosome . PdeG is one of 5 CSS domain containing c-di-GMP phosphodiesterases in E. coli K-12; redox control and proteolysis of these enzymes is believed to modulate their activity and affect matrix production in biofilm (see ). No expression of pdeG was seen during growth in LB . PdeG is present at very low levels in wild-type cells grown in tryptone broth at 37 °C and is absent in ΔpdeH cells . PdeG: "phosphodiesterase G"

## Biological Role

Catalyzes cyclic bis(3->5')diguanylate 3-guanylylhydrolase (reaction.R08991).

## Annotation

FUNCTION: Phosphodiesterase (PDE) that catalyzes the hydrolysis of cyclic-di-GMP (c-di-GMP) to 5'-pGpG. {ECO:0000250|UniProtKB:P21514}.

## Outgoing Edges (1)

- `catalyzes` --> [[reaction.R08991|reaction.R08991]] `KEGG` `database` - via EC:3.1.4.52

## Incoming Edges (1)

- `encodes` <-- [[gene.b1168|gene.b1168]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P75995`
- `KEGG:ecj:JW5174;eco:b1168;ecoc:C3026_06880;`
- `GeneID:945738;`
- `GO:GO:0005886; GO:0071111; GO:1900190`
- `EC:3.1.4.52`

## Notes

Probable cyclic di-GMP phosphodiesterase PdeG (EC 3.1.4.52)
