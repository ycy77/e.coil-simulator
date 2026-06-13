---
entity_id: "protein.P10908"
entity_type: "protein"
name: "ugpQ"
source_database: "UniProt"
source_id: "P10908"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cytoplasm {ECO:0000269|PubMed:18083802}."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "ugpQ b3449 JW3414"
---

# ugpQ

`protein.P10908`

## Static

- Type: `protein`
- Source: `UniProt:P10908`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cytoplasm {ECO:0000269|PubMed:18083802}.

## Enriched Summary

FUNCTION: Glycerophosphodiester phosphodiesterase hydrolyzes glycerophosphodiesters into glycerol-3-phosphate (G3P) and the corresponding alcohol. {ECO:0000269|PubMed:18083802}. UgpQ is a cytosolic glycerophosphodiester phosphodiesterase with broad substrate specificity . Initial experiments suggested that cytoplasmic glycerophosphodiesters are not substrates of UgpQ, and that they are hydrolyzed only when transported by the Ugp system . However, recent purification and characterization of the enzyme contradicts those results . Moreover, purified UgpQ does not affect the activity of the UgpB-EAC2 transporter complex in vitro . Expression of UgpQ is induced by phosphate starvation . The ugp operon is induced by carbon starvation during the late logarithmic growth phase . UgpQ: "uptake of glycerol phosphate"

## Biological Role

Catalyzes GLYCPDIESTER-RXN (reaction.ecocyc.GLYCPDIESTER-RXN), RXN-14073 (reaction.ecocyc.RXN-14073), RXN-14136 (reaction.ecocyc.RXN-14136), glycerophosphorylethanolamine phosphodiesterase (reaction.ecocyc.RXN-14160). Bound by Magnesium cation (molecule.C00305).

## Enriched Pathways

- `eco00564` Glycerophospholipid metabolism (KEGG)

## Annotation

FUNCTION: Glycerophosphodiester phosphodiesterase hydrolyzes glycerophosphodiesters into glycerol-3-phosphate (G3P) and the corresponding alcohol. {ECO:0000269|PubMed:18083802}.

## Pathways

- `eco00564` Glycerophospholipid metabolism (KEGG)

## Outgoing Edges (4)

- `catalyzes` --> [[reaction.ecocyc.GLYCPDIESTER-RXN|reaction.ecocyc.GLYCPDIESTER-RXN]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` --> [[reaction.ecocyc.RXN-14073|reaction.ecocyc.RXN-14073]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` --> [[reaction.ecocyc.RXN-14136|reaction.ecocyc.RXN-14136]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` --> [[reaction.ecocyc.RXN-14160|reaction.ecocyc.RXN-14160]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (2)

- `binds` <-- [[molecule.C00305|molecule.C00305]] `EcoCyc` `database` - EcoCyc enzymatic reaction cofactor
- `encodes` <-- [[gene.b3449|gene.b3449]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P10908`
- `KEGG:ecj:JW3414;eco:b3449;ecoc:C3026_18680;`
- `GeneID:947955;`
- `GO:GO:0000287; GO:0005737; GO:0006071; GO:0006629; GO:0008889; GO:0047389; GO:0047395`
- `EC:3.1.4.46`

## Notes

Glycerophosphodiester phosphodiesterase, cytoplasmic (Glycerophosphoryl diester phosphodiesterase, cytoplasmic) (EC 3.1.4.46)
