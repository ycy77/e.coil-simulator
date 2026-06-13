---
entity_id: "protein.P75897"
entity_type: "protein"
name: "rutB"
source_database: "UniProt"
source_id: "P75897"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "rutB ycdL b1011 JW5139"
---

# rutB

`protein.P75897`

## Static

- Type: `protein`
- Source: `UniProt:P75897`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`

## Enriched Summary

FUNCTION: Hydrolyzes ureidoacrylate to form aminoacrylate and carbamate. The carbamate hydrolyzes spontaneously, thereby releasing one of the nitrogen atoms of the pyrimidine ring as ammonia and one of its carbon atoms as CO2. {ECO:0000269|PubMed:16540542, ECO:0000269|PubMed:20400551}. E. coli K-12 contains a pathway for pyrimidine degradation (PWY0-1471). RutB, which belongs to the isochorismatase family, hydrolyzes ureidoacrylate, the product of the first enzymatic step of the pathway, to generate the unstable intermediates carbamate and aminoacrylate . RutB from E. coli W was purified and appears to be homooctameric in solution . (Note: RutB from E. coli W is 99% identical to RutB from K-12 MG1655.) The enzyme from the K12 strain JM109 was shown to act as a (+)-γ-lactamase, hydrolyzing CPD-26603 efficiently, making it a promising candidate for industrial processes (see CPLX-85455 "enzyme in MetaCyc"). Active site residues were identified and confirmed by alanine scanning mutagenesis . Expression of the rutABCDEFG operon is under the control of nitrogen regulatory protein C (NtrC) . A rutB insertion mutant loses the ability to utilize pyrimidine nucleosides and bases as the sole source of nitrogen at room temperature . A crystal structure of RutB was solved at a resolution of 1.9 Å, showing that it iwith six-stranded parallel β-sheet surrounded by five α-helices...

## Biological Role

Catalyzes (Z)-2-methylureidoacrylate amidohydrolase (reaction.R12623), R12624 (reaction.R12624), (Z)-3-ureidoacrylate amidohydrolase (reaction.R12625), RXN-12896 (reaction.ecocyc.RXN-12896), peroxyureidoacrylate/ureidoacrylate amidohydrolase (reaction.ecocyc.RXN0-6460).

## Enriched Pathways

- `eco00240` Pyrimidine metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)

## Annotation

FUNCTION: Hydrolyzes ureidoacrylate to form aminoacrylate and carbamate. The carbamate hydrolyzes spontaneously, thereby releasing one of the nitrogen atoms of the pyrimidine ring as ammonia and one of its carbon atoms as CO2. {ECO:0000269|PubMed:16540542, ECO:0000269|PubMed:20400551}.

## Pathways

- `eco00240` Pyrimidine metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)

## Outgoing Edges (5)

- `catalyzes` --> [[reaction.R12623|reaction.R12623]] `KEGG` `database` - via EC:3.5.1.110
- `catalyzes` --> [[reaction.R12624|reaction.R12624]] `KEGG` `database` - via EC:3.5.1.110
- `catalyzes` --> [[reaction.R12625|reaction.R12625]] `KEGG` `database` - via EC:3.5.1.110
- `catalyzes` --> [[reaction.ecocyc.RXN-12896|reaction.ecocyc.RXN-12896]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` --> [[reaction.ecocyc.RXN0-6460|reaction.ecocyc.RXN0-6460]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (1)

- `encodes` <-- [[gene.b1011|gene.b1011]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P75897`
- `KEGG:ecj:JW5139;eco:b1011;ecoc:C3026_06150;`
- `GeneID:945699;`
- `GO:GO:0006208; GO:0006212; GO:0016811; GO:0019740`
- `EC:3.5.1.110`

## Notes

Ureidoacrylate amidohydrolase RutB (EC 3.5.1.110)
