---
entity_id: "protein.P61320"
entity_type: "protein"
name: "lolB"
source_database: "UniProt"
source_id: "P61320"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cell outer membrane; Lipid-anchor."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "lolB hemM ychC b1209 JW1200"
---

# lolB

`protein.P61320`

## Static

- Type: `protein`
- Source: `UniProt:P61320`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cell outer membrane; Lipid-anchor.

## Enriched Summary

FUNCTION: Plays a critical role in the incorporation of lipoproteins in the outer membrane after they are released by the LolA protein. Essential for E.coli viability. LolB is an outer membrane lipoprotein which is part of the 5 protein LolABCDE lipoprotein trafficking pathway; LolB interacts with G6465-MONOMER "LolA"-lipoprotein complexes and catalyses lipoprotein insertion into the outer membrane. The major outer membrane lipoprotein Lpp, is incorporated into proteoliposomes reconstituted from purified LolB and phospholipids in vitro; Lpp is transferred from Lpp-LolA to a water-soluble LolB (mLolB) in vitro . Lipoproteins (Lpp, Pal and NlpB) released from spheroplasts in the presence of LolA are subsequently incorporated into LolB-containing membranes in vitro . LolB specifically interacts with liganded LolA and the interaction between free LolA and LolB is negligible . LolB (itself a lipoprotein) released from spheroplasts forms LolA-LolB and larger heterogeneous complexes; in vitro incorporation of LolB into outer membranes containing normal levels of LolB is inefficient but is enhanced in outer membranes prepared from LolB-overproducing cells; LolB localization in vivo probably takes place in a LolB-dependent manner . LolB is essential for growth...

## Biological Role

Catalyzes RXN-22553 (reaction.ecocyc.RXN-22553).

## Annotation

FUNCTION: Plays a critical role in the incorporation of lipoproteins in the outer membrane after they are released by the LolA protein. Essential for E.coli viability.

## Outgoing Edges (1)

- `catalyzes` --> [[reaction.ecocyc.RXN-22553|reaction.ecocyc.RXN-22553]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (1)

- `encodes` <-- [[gene.b1209|gene.b1209]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P61320`
- `KEGG:ecj:JW1200;eco:b1209;ecoc:C3026_07105;`
- `GeneID:86946691;93775274;945775;`
- `GO:GO:0009279; GO:0015031; GO:0030288; GO:0042157; GO:0044874`

## Notes

Outer-membrane lipoprotein LolB
