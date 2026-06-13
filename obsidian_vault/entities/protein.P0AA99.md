---
entity_id: "protein.P0AA99"
entity_type: "protein"
name: "dpaA"
source_database: "UniProt"
source_id: "P0AA99"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "dpaA ldtF yafK b0224 JW0214"
---

# dpaA

`protein.P0AA99`

## Static

- Type: `protein`
- Source: `UniProt:P0AA99`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`

## Enriched Summary

FUNCTION: Hydrolase that plays a role in the regulation of peptidoglycan-outer membrane linkages (PubMed:33941679, PubMed:33947763). It has two distinctive enzymatic functions, an L,D-endopeptidase activity and a carboxypeptidase activity (PubMed:33941679, PubMed:33947763). Acts as a murein L,D-endopeptidase that catalyzes the cleavage of the cross-link between the outer membrane-anchored Braun's lipoprotein (Lpp) and peptidoglycan, detaching Lpp from the peptidoglycan layer (PubMed:33941679, PubMed:33947763, PubMed:37830798). It also exhibits glycine-specific carboxypeptidase activity on muropeptides containing a terminal glycine residue (PubMed:33941679, PubMed:33947763). DpaA hydrolyzes the amide bond between the L-center of meso-diaminopimelate in peptidoglycan stem peptides and the C-terminal L-lysine of Lpp, and between the L-center of meso-diaminopimelate and a terminal glycine residue in tetrapeptides (PubMed:33941679, PubMed:33947763). The detachment of Lpp from peptidoglycan is beneficial for the cell under certain stress conditions, suggesting that DpaA may help the cell to cope with these stress conditions (PubMed:33947763). DpaA may also cleave Lpp bound to the inner membrane (PubMed:33941679). It does not show any L,D-transpeptidase or L,D-carboxypeptidase activity (PubMed:33947763)...

## Biological Role

Catalyzes RXN-22575 (reaction.ecocyc.RXN-22575), RXN-22576 (reaction.ecocyc.RXN-22576).

## Annotation

FUNCTION: Hydrolase that plays a role in the regulation of peptidoglycan-outer membrane linkages (PubMed:33941679, PubMed:33947763). It has two distinctive enzymatic functions, an L,D-endopeptidase activity and a carboxypeptidase activity (PubMed:33941679, PubMed:33947763). Acts as a murein L,D-endopeptidase that catalyzes the cleavage of the cross-link between the outer membrane-anchored Braun's lipoprotein (Lpp) and peptidoglycan, detaching Lpp from the peptidoglycan layer (PubMed:33941679, PubMed:33947763, PubMed:37830798). It also exhibits glycine-specific carboxypeptidase activity on muropeptides containing a terminal glycine residue (PubMed:33941679, PubMed:33947763). DpaA hydrolyzes the amide bond between the L-center of meso-diaminopimelate in peptidoglycan stem peptides and the C-terminal L-lysine of Lpp, and between the L-center of meso-diaminopimelate and a terminal glycine residue in tetrapeptides (PubMed:33941679, PubMed:33947763). The detachment of Lpp from peptidoglycan is beneficial for the cell under certain stress conditions, suggesting that DpaA may help the cell to cope with these stress conditions (PubMed:33947763). DpaA may also cleave Lpp bound to the inner membrane (PubMed:33941679). It does not show any L,D-transpeptidase or L,D-carboxypeptidase activity (PubMed:33947763). {ECO:0000269|PubMed:33941679, ECO:0000269|PubMed:33947763, ECO:0000269|PubMed:37830798}.

## Outgoing Edges (2)

- `catalyzes` --> [[reaction.ecocyc.RXN-22575|reaction.ecocyc.RXN-22575]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` --> [[reaction.ecocyc.RXN-22576|reaction.ecocyc.RXN-22576]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (1)

- `encodes` <-- [[gene.b0224|gene.b0224]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P0AA99`
- `KEGG:ecj:JW0214;eco:b0224;ecoc:C3026_01060;ecoc:C3026_23800;`
- `GeneID:93777171;944910;`
- `GO:GO:0000270; GO:0004175; GO:0004180; GO:0008360; GO:0009252; GO:0016757; GO:0071555`
- `EC:3.4.-.-`

## Notes

Peptidoglycan meso-diaminopimelic acid protein amidase A (EC 3.4.-.-) (Carboxypeptidase) (Murein L,D-endopeptidase) (Transpeptidase-like protein DpaA)
