---
entity_id: "protein.P00811"
entity_type: "protein"
name: "ampC"
source_database: "UniProt"
source_id: "P00811"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Periplasm {ECO:0000303|PubMed:6795623}."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "ampC ampA b4150 JW4111"
---

# ampC

`protein.P00811`

## Static

- Type: `protein`
- Source: `UniProt:P00811`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Periplasm {ECO:0000303|PubMed:6795623}.

## Enriched Summary

FUNCTION: Class C beta-lactamase which confers resistance to penicillins and cephalosporins (PubMed:12323371, PubMed:17956081, PubMed:23043117, PubMed:33199391, PubMed:6998377). Has benzylpenicillin- and cephaloridine-hydrolyzing activity (PubMed:3264154, PubMed:3264155, PubMed:6998377). Has weak cefuroxime, cefotaxime, cefoxitin and oxacillin-hydrolyzing activities (PubMed:19913034, PubMed:3264154, PubMed:3264155). {ECO:0000269|PubMed:12323371, ECO:0000269|PubMed:17956081, ECO:0000269|PubMed:19913034, ECO:0000269|PubMed:23043117, ECO:0000269|PubMed:3264154, ECO:0000269|PubMed:3264155, ECO:0000269|PubMed:33199391, ECO:0000269|PubMed:6998377}. The ampC β-lactamase gene encodes a serine cephalosporinase . AmpC was shown to be active against penicillin G with a Km of 12 μM, D-ampicillin with a Km of 6 μM, and cephalosporin C with a Km of 217 μM . AmpC has been shown to bind 125I-penicillin-X and aztreonam . AmpC is also believed to have an additional function as a peptidoglycan hydrolyzing enzyme . The ampA1 mutation, located in the promoter or operator region for ampC, causes increased expression of the ampC gene resulting in increased β-lactam resistance . ampC mutants exhibit aberrant cell morphology in a mrcA dacA background . Overexpression of bolA increases ampC expression in addition to dacA and dacC expression...

## Biological Role

Catalyzes beta-lactamhydrolase (reaction.R03743), BETA-LACTAMASE-RXN (reaction.ecocyc.BETA-LACTAMASE-RXN).

## Enriched Pathways

- `eco01501` beta-Lactam resistance (KEGG)
- `eco02020` Two-component system (KEGG)

## Annotation

FUNCTION: Class C beta-lactamase which confers resistance to penicillins and cephalosporins (PubMed:12323371, PubMed:17956081, PubMed:23043117, PubMed:33199391, PubMed:6998377). Has benzylpenicillin- and cephaloridine-hydrolyzing activity (PubMed:3264154, PubMed:3264155, PubMed:6998377). Has weak cefuroxime, cefotaxime, cefoxitin and oxacillin-hydrolyzing activities (PubMed:19913034, PubMed:3264154, PubMed:3264155). {ECO:0000269|PubMed:12323371, ECO:0000269|PubMed:17956081, ECO:0000269|PubMed:19913034, ECO:0000269|PubMed:23043117, ECO:0000269|PubMed:3264154, ECO:0000269|PubMed:3264155, ECO:0000269|PubMed:33199391, ECO:0000269|PubMed:6998377}.

## Pathways

- `eco01501` beta-Lactam resistance (KEGG)
- `eco02020` Two-component system (KEGG)

## Outgoing Edges (2)

- `catalyzes` --> [[reaction.R03743|reaction.R03743]] `KEGG` `database` - via EC:3.5.2.6
- `catalyzes` --> [[reaction.ecocyc.BETA-LACTAMASE-RXN|reaction.ecocyc.BETA-LACTAMASE-RXN]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (1)

- `encodes` <-- [[gene.b4150|gene.b4150]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P00811`
- `KEGG:ecj:JW4111;eco:b4150;ecoc:C3026_22435;`
- `GeneID:948669;`
- `GO:GO:0008800; GO:0017001; GO:0030288; GO:0046677`
- `EC:3.5.2.6`

## Notes

Beta-lactamase (EC 3.5.2.6) (Cephalosporinase) (CSase)
