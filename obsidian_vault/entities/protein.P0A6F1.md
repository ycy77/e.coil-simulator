---
entity_id: "protein.P0A6F1"
entity_type: "protein"
name: "carA"
source_database: "UniProt"
source_id: "P0A6F1"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "carA pyrA b0032 JW0030"
---

# carA

`protein.P0A6F1`

## Static

- Type: `protein`
- Source: `UniProt:P0A6F1`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`

## Enriched Summary

FUNCTION: Small subunit of the glutamine-dependent carbamoyl phosphate synthetase (CPSase). CPSase catalyzes the formation of carbamoyl phosphate from the ammonia moiety of glutamine, carbonate, and phosphate donated by ATP, constituting the first step of 2 biosynthetic pathways, one leading to arginine and/or urea and the other to pyrimidine nucleotides. The small subunit (glutamine amidotransferase) binds and cleaves glutamine to supply the large subunit with the substrate ammonia. {ECO:0000255|HAMAP-Rule:MF_01209, ECO:0000269|PubMed:2658488, ECO:0000269|PubMed:2868386, ECO:0000269|PubMed:4944634, ECO:0000269|Ref.10}. The small subunit encoded by carA is the amidotransferase component of the enzyme. It hydrolyzes glutamine to glutamate and ammonia. The small subunit contains a catalytic triad (Cys269, His353 and Glu355) situated between the two structural domains . The small subunit is protected from proteolysis by the large subunit . The mechanism for glutamine hydrolysis on the small subunit requires the participation of an essential sulfhydryl group for the formation of a thioester intermediate . Translation initiation at the UUG start codon has been confirmed experimentally . CarA: "carbamoyl phosphate" cap: (do not use as name/synonym; name has been labeled "misleading" by the original author )

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

FUNCTION: Small subunit of the glutamine-dependent carbamoyl phosphate synthetase (CPSase). CPSase catalyzes the formation of carbamoyl phosphate from the ammonia moiety of glutamine, carbonate, and phosphate donated by ATP, constituting the first step of 2 biosynthetic pathways, one leading to arginine and/or urea and the other to pyrimidine nucleotides. The small subunit (glutamine amidotransferase) binds and cleaves glutamine to supply the large subunit with the substrate ammonia. {ECO:0000255|HAMAP-Rule:MF_01209, ECO:0000269|PubMed:2658488, ECO:0000269|PubMed:2868386, ECO:0000269|PubMed:4944634, ECO:0000269|Ref.10}.

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

- `encodes` <-- [[gene.b0032|gene.b0032]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P0A6F1`
- `KEGG:ecj:JW0030;eco:b0032;ecoc:C3026_00165;`
- `GeneID:93777404;949025;`
- `GO:GO:0004088; GO:0004359; GO:0005524; GO:0005737; GO:0005829; GO:0005951; GO:0006207; GO:0006526; GO:0006541; GO:0019856; GO:0044205; GO:0046982`
- `EC:6.3.5.5`

## Notes

Carbamoyl phosphate synthase small chain (EC 6.3.5.5) (Carbamoyl phosphate synthetase glutamine chain)
