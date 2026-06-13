---
entity_id: "protein.P18956"
entity_type: "protein"
name: "ggt"
source_database: "UniProt"
source_id: "P18956"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Periplasm {ECO:0000269|PubMed:1360205, ECO:0000269|PubMed:2877974}."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "ggt b3447 JW3412"
---

# ggt

`protein.P18956`

## Static

- Type: `protein`
- Source: `UniProt:P18956`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Periplasm {ECO:0000269|PubMed:1360205, ECO:0000269|PubMed:2877974}.

## Enriched Summary

FUNCTION: Cleaves the gamma-glutamyl bond of periplasmic glutathione (gamma-Glu-Cys-Gly), glutathione conjugates, and other gamma-glutamyl compounds. The metabolism of glutathione releases free glutamate and the dipeptide cysteinyl-glycine, which is hydrolyzed to cysteine and glycine by dipeptidases; it may function in amino acid uptake/salvage, or possibly in peptidoglycan linkage. Catalyzes the hydrolysis and transpeptidation of many gamma-glutamyl compounds (including some D-gamma-glutamyl substrates), with a preference for basic and aromatic amino acids as acceptors (PubMed:2877974). The KM values for gamma-glutamyl acceptors are so high that it has been proposed transpeptidation is not the physiological role in E.coli (PubMed:2877974, PubMed:8104180). {ECO:0000269|PubMed:2877974, ECO:0000305|PubMed:8104180}. The glutathione hydrolase proenzyme undergoes autocatalytic processing to release a catalytic threonine (Thr391); processing generates a large (Ala26 → Gln390) and small (Thr391 → Tyr580) subunit which together form the active heterodimer. The glutathione hydrolase proenzyme undergoes autocatalytic processing to release a catalytic threonine (Thr391); processing generates a large (Ala26 → Gln390) and small (Thr391 → Tyr580) subunit which together form the active heterodimer. ggt encodes a periplasmic γ-glutamylhydrolase also known as γ-glutamyltranspeptidase (GGT)...

## Biological Role

Catalyzes glutathione gamma-glutamylaminopeptidase (reaction.R00494), (5-L-glutamyl)-peptide:amino-acid 5-glutamyltransferase (reaction.R04159). Component of glutathione hydrolase (complex.ecocyc.CPLX0-7885).

## Enriched Pathways

- `eco00430` Taurine and hypotaurine metabolism (KEGG)
- `eco00460` Cyanoamino acid metabolism (KEGG)
- `eco00480` Glutathione metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)

## Annotation

FUNCTION: Cleaves the gamma-glutamyl bond of periplasmic glutathione (gamma-Glu-Cys-Gly), glutathione conjugates, and other gamma-glutamyl compounds. The metabolism of glutathione releases free glutamate and the dipeptide cysteinyl-glycine, which is hydrolyzed to cysteine and glycine by dipeptidases; it may function in amino acid uptake/salvage, or possibly in peptidoglycan linkage. Catalyzes the hydrolysis and transpeptidation of many gamma-glutamyl compounds (including some D-gamma-glutamyl substrates), with a preference for basic and aromatic amino acids as acceptors (PubMed:2877974). The KM values for gamma-glutamyl acceptors are so high that it has been proposed transpeptidation is not the physiological role in E.coli (PubMed:2877974, PubMed:8104180). {ECO:0000269|PubMed:2877974, ECO:0000305|PubMed:8104180}.

## Pathways

- `eco00430` Taurine and hypotaurine metabolism (KEGG)
- `eco00460` Cyanoamino acid metabolism (KEGG)
- `eco00480` Glutathione metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)

## Outgoing Edges (3)

- `catalyzes` --> [[reaction.R00494|reaction.R00494]] `KEGG` `database` - via EC:3.4.19.13
- `catalyzes` --> [[reaction.R04159|reaction.R04159]] `KEGG` `database` - via EC:2.3.2.2
- `is_component_of` --> [[complex.ecocyc.CPLX0-7885|complex.ecocyc.CPLX0-7885]] `EcoCyc` `database` - EcoCyc component coefficient= | EcoCyc protcplxs.col coefficient=1

## Incoming Edges (1)

- `encodes` <-- [[gene.b3447|gene.b3447]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P18956`
- `KEGG:ecj:JW3412;eco:b3447;ecoc:C3026_18670;`
- `GeneID:947947;`
- `GO:GO:0006750; GO:0006751; GO:0030288; GO:0034722; GO:0036374; GO:0042597; GO:0043102; GO:0097264; GO:0103068`
- `EC:2.3.2.2; 3.4.19.13`

## Notes

Glutathione hydrolase proenzyme (EC 3.4.19.13) (Gamma-glutamyltranspeptidase proenzyme) (GGT) (EC 2.3.2.2) [Cleaved into: Glutathione hydrolase large chain; Glutathione hydrolase small chain]
