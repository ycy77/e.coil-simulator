---
entity_id: "protein.P15977"
entity_type: "protein"
name: "malQ"
source_database: "UniProt"
source_id: "P15977"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cytoplasm."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "malQ malA b3416 JW3379"
---

# malQ

`protein.P15977`

## Static

- Type: `protein`
- Source: `UniProt:P15977`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cytoplasm.

## Enriched Summary

4-alpha-glucanotransferase (EC 2.4.1.25) (Amylomaltase) (Disproportionating enzyme) (D-enzyme) Amylomaltase (MalQ) was first described as a maltose-inducible enzyme that catalyzes a reversible transglycosidase reaction . The enzyme belongs to the glycoside hydrolase family GH77 of 4-α-glucanotransferases that catalyzes transglycosylation of maltose and maltodextrins. MalQ does not have maltase activity, i.e. it does not hydrolyze maltose to form two molecules of glucose . The specificity of MalQ for donor and acceptor molecules of the transglycosylation reaction has been difficult to ascertain. It was initially reported that maltose serves as an acceptor substrate of the enzyme . Further experiments using more highly purified maltose suggested that maltose is a poor acceptor . Later, it was demonstrated that the enzyme can utilize purified 14C-maltose to produce labeled maltodextrins and glucose . Maltotetraose appears to be the most efficient substrate . Kinetic data of the utilization of maltose and higher oligomers alone or with the addition of glucose have been measured . MalQ transfers glycosyl chains of 1-9 glucosyl units from the nonreducing end of donor molecules onto the nonreducing end of maltodextrin acceptors, including maltose and glucose . Glucose feedback-inhibits the reaction at concentrations above 0.1 mM...

## Biological Role

Catalyzes AMYLOMALT-RXN (reaction.ecocyc.AMYLOMALT-RXN), MALTODEG-RXN (reaction.ecocyc.MALTODEG-RXN), RXN-14260 (reaction.ecocyc.RXN-14260), RXN-14261 (reaction.ecocyc.RXN-14261), RXN0-7347 (reaction.ecocyc.RXN0-7347).

## Enriched Pathways

- `eco00500` Starch and sucrose metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01110` Biosynthesis of secondary metabolites (KEGG)

## Annotation

4-alpha-glucanotransferase (EC 2.4.1.25) (Amylomaltase) (Disproportionating enzyme) (D-enzyme)

## Pathways

- `eco00500` Starch and sucrose metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01110` Biosynthesis of secondary metabolites (KEGG)

## Outgoing Edges (5)

- `catalyzes` --> [[reaction.ecocyc.AMYLOMALT-RXN|reaction.ecocyc.AMYLOMALT-RXN]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` --> [[reaction.ecocyc.MALTODEG-RXN|reaction.ecocyc.MALTODEG-RXN]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` --> [[reaction.ecocyc.RXN-14260|reaction.ecocyc.RXN-14260]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` --> [[reaction.ecocyc.RXN-14261|reaction.ecocyc.RXN-14261]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` --> [[reaction.ecocyc.RXN0-7347|reaction.ecocyc.RXN0-7347]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (1)

- `encodes` <-- [[gene.b3416|gene.b3416]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P15977`
- `KEGG:ecj:JW3379;eco:b3416;ecoc:C3026_18530;`
- `GeneID:947923;`
- `GO:GO:0000025; GO:0000272; GO:0004134; GO:0005829; GO:0005978; GO:0005980`
- `EC:2.4.1.25`

## Notes

4-alpha-glucanotransferase (EC 2.4.1.25) (Amylomaltase) (Disproportionating enzyme) (D-enzyme)
