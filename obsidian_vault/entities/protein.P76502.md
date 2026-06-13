---
entity_id: "protein.P76502"
entity_type: "protein"
name: "sixA"
source_database: "UniProt"
source_id: "P76502"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "sixA yfcW b2340 JW2337"
---

# sixA

`protein.P76502`

## Static

- Type: `protein`
- Source: `UniProt:P76502`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`

## Enriched Summary

FUNCTION: Exhibits phosphohistidine phosphatase activity towards the HPt domain of the ArcB sensor involved in the multistep His-Asp phosphorelay. SixA is a phosphohistidine phosphatase. Genetic evidence suggested that MONOMER0-4292 NPr-P is a target for dephosphorylation by SixA ; the activity has now been confirmed in vitro . Dephosphorylation of NPr-P by SixA involves formation of a transient phosphohistidine intermediate . SixA was shown to remove the phosphoryl group from the His717 residue of PHOSPHO-ARCB717 ArcB in vitro . Initial results showed that under anaerobic growth conditions, dephosphorylation of ArcB accelerates the derepression of the sdh operon via the ArcB/ArcA phosphorelay in the presence of anaerobic electron acceptors . However, a later report shows no evidence that SixA affects ArcB/ArcA signaling to icdA expression under anaerobic conditions in vivo . SixA dephosphorylates the inactive, phosphorylated 6PFK-1-MONOMER reversing its inhibition . Crystal structures of the free and tungstate-bound forms of SixA have been solved at 2.06 and 1.9 Å resolution . A His8Arg mutant of SixA lacks phosphohistidine phosphatase activity both in vivo and in vitro ; a His8Ala mutant is unable to dephosphorylate NPr-P in vivo...

## Biological Role

Catalyzes RXN0-312 (reaction.ecocyc.RXN0-312), RXN0-7395 (reaction.ecocyc.RXN0-7395).

## Annotation

FUNCTION: Exhibits phosphohistidine phosphatase activity towards the HPt domain of the ArcB sensor involved in the multistep His-Asp phosphorelay.

## Outgoing Edges (2)

- `catalyzes` --> [[reaction.ecocyc.RXN0-312|reaction.ecocyc.RXN0-312]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` --> [[reaction.ecocyc.RXN0-7395|reaction.ecocyc.RXN0-7395]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (1)

- `encodes` <-- [[gene.b2340|gene.b2340]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P76502`
- `KEGG:ecj:JW2337;eco:b2340;ecoc:C3026_13025;`
- `GeneID:93774836;946815;`
- `GO:GO:0005737; GO:0070297; GO:0101006`
- `EC:3.1.3.-`

## Notes

Phosphohistidine phosphatase SixA (EC 3.1.3.-) (RX6)
