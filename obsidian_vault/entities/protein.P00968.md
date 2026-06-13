---
entity_id: "protein.P00968"
entity_type: "protein"
name: "carB"
source_database: "UniProt"
source_id: "P00968"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "carB pyrA b0033 JW0031"
---

# carB

`protein.P00968`

## Static

- Type: `protein`
- Source: `UniProt:P00968`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`

## Enriched Summary

FUNCTION: Large subunit of the glutamine-dependent carbamoyl phosphate synthetase (CPSase). CPSase catalyzes the formation of carbamoyl phosphate from the ammonia moiety of glutamine, carbonate, and phosphate donated by ATP, constituting the first step of 2 biosynthetic pathways, one leading to arginine and/or urea and the other to pyrimidine nucleotides. The large subunit (synthetase) binds the substrates ammonia (free or transferred from glutamine from the small subunit), hydrogencarbonate and ATP and carries out an ATP-coupled ligase reaction, activating hydrogencarbonate by forming carboxy phosphate which reacts with ammonia to form carbamoyl phosphate. {ECO:0000255|HAMAP-Rule:MF_01210, ECO:0000269|PubMed:2658488, ECO:0000269|PubMed:2868386, ECO:0000269|PubMed:4944634, ECO:0000269|Ref.8}. The CarB subunit is the synthetase component of carbamoylphosphate synthetase. It binds the two required molecules of MgATP and catalyzes the two required phosphorylation events. The large subunit consists of four structural units: the carboxyphosphate synthetic component, the oligomerization domain, the carbamoyl phosphate synthetic component and the allosteric domain . The large subunit alone can catalyze carbamyl phosphate synthesis from ammonia, but not from glutamine . It uses NH3 and HCO3- in an ATP-dependent reaction to form carbamoyl phosphate...

## Biological Role

Catalyzes L-glutamine amidohydrolase (reaction.R00256), HCO3-:L-glutamine amido-ligase (ADP-forming, carbamate-phosphorylating) (reaction.R00575), ATP:HCO3- phosphotransferase (reaction.R10948), R10949 (reaction.R10949). Component of carbamoyl-phosphate synthetase, glutamine-hydrolyzing (complex.ecocyc.CARBPSYN-CPLX).

## Enriched Pathways

- `eco00220` Arginine biosynthesis (KEGG)
- `eco00240` Pyrimidine metabolism (KEGG)
- `eco00250` Alanine, aspartate and glutamate metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01110` Biosynthesis of secondary metabolites (KEGG)
- `eco01240` Biosynthesis of cofactors (KEGG)

## Annotation

FUNCTION: Large subunit of the glutamine-dependent carbamoyl phosphate synthetase (CPSase). CPSase catalyzes the formation of carbamoyl phosphate from the ammonia moiety of glutamine, carbonate, and phosphate donated by ATP, constituting the first step of 2 biosynthetic pathways, one leading to arginine and/or urea and the other to pyrimidine nucleotides. The large subunit (synthetase) binds the substrates ammonia (free or transferred from glutamine from the small subunit), hydrogencarbonate and ATP and carries out an ATP-coupled ligase reaction, activating hydrogencarbonate by forming carboxy phosphate which reacts with ammonia to form carbamoyl phosphate. {ECO:0000255|HAMAP-Rule:MF_01210, ECO:0000269|PubMed:2658488, ECO:0000269|PubMed:2868386, ECO:0000269|PubMed:4944634, ECO:0000269|Ref.8}.

## Pathways

- `eco00220` Arginine biosynthesis (KEGG)
- `eco00240` Pyrimidine metabolism (KEGG)
- `eco00250` Alanine, aspartate and glutamate metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01110` Biosynthesis of secondary metabolites (KEGG)
- `eco01240` Biosynthesis of cofactors (KEGG)

## Outgoing Edges (5)

- `catalyzes` --> [[reaction.R00256|reaction.R00256]] `KEGG` `database` - via EC:6.3.5.5
- `catalyzes` --> [[reaction.R00575|reaction.R00575]] `KEGG` `database` - via EC:6.3.5.5
- `catalyzes` --> [[reaction.R10948|reaction.R10948]] `KEGG` `database` - via EC:6.3.5.5
- `catalyzes` --> [[reaction.R10949|reaction.R10949]] `KEGG` `database` - via EC:6.3.5.5
- `is_component_of` --> [[complex.ecocyc.CARBPSYN-CPLX|complex.ecocyc.CARBPSYN-CPLX]] `EcoCyc` `database` - EcoCyc component coefficient=1 | EcoCyc protcplxs.col coefficient=1

## Incoming Edges (1)

- `encodes` <-- [[gene.b0033|gene.b0033]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P00968`
- `KEGG:ecj:JW0031;eco:b0033;ecoc:C3026_00170;`
- `GeneID:944775;`
- `GO:GO:0000166; GO:0004087; GO:0004088; GO:0005524; GO:0005737; GO:0005829; GO:0005951; GO:0006526; GO:0006541; GO:0008652; GO:0016597; GO:0019856; GO:0044205; GO:0046872`
- `EC:6.3.4.16; 6.3.5.5`

## Notes

Carbamoyl phosphate synthase large chain (EC 6.3.4.16) (EC 6.3.5.5) (Carbamoyl phosphate synthetase ammonia chain)
