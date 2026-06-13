---
entity_id: "protein.P31675"
entity_type: "protein"
name: "setA"
source_database: "UniProt"
source_id: "P31675"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cell inner membrane; Multi-pass membrane protein."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "setA yabM b0070 JW0069"
---

# setA

`protein.P31675`

## Static

- Type: `protein`
- Source: `UniProt:P31675`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cell inner membrane; Multi-pass membrane protein.

## Enriched Summary

FUNCTION: Involved in the efflux of sugars. The physiological role may be the detoxification of non-metabolizable sugar analogs. Can transport IPTG, lactose and glucose. Has broad substrate specificity, with preferences for glucosides or galactosides with alkyl or aryl substituents. SetA is an efflux transporter capable of exporting a number of sugars and sugar analogues; the physiological role of SetA is not clear. Overexpression of setA decreases the amount of protein produced form IPTG-responsive promoters and suppresses the growth inhibition that is associated with over-expression of membrane proteins; inside-out membrane vesicles prepared from cells overexpressing setA accumulate significant amounts of lactose in a manner that is sensitive to the proton ionophore, carbonyl cyanide m-chlorophenylhydrazone (CCCP) . SetA can transport lactose and glucose; SetA also transports some glucosides and galactosides with alkyl or aryl substituents and overexpression of setA protects cells from the toxic sugar analog 2-nitrophenyl-beta-D-thiogalactopyranoside (ONPTG) . Under stress conditions induced by the presence of the non-metabolizable glucose analog CPD-3582 "α-methyl glucoside", setA is coexpressed with RNA0-241 "sgrS" in an EG12094-MONOMER "SgrR" dependent manner...

## Biological Role

Catalyzes lactose:proton antiport (reaction.ecocyc.TRANS-RXN-82).

## Annotation

FUNCTION: Involved in the efflux of sugars. The physiological role may be the detoxification of non-metabolizable sugar analogs. Can transport IPTG, lactose and glucose. Has broad substrate specificity, with preferences for glucosides or galactosides with alkyl or aryl substituents.

## Outgoing Edges (1)

- `catalyzes` --> [[reaction.ecocyc.TRANS-RXN-82|reaction.ecocyc.TRANS-RXN-82]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (1)

- `encodes` <-- [[gene.b0070|gene.b0070]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P31675`
- `KEGG:ecj:JW0069;eco:b0070;`
- `GeneID:944793;`
- `GO:GO:0005351; GO:0005886; GO:0015767; GO:0016020; GO:0034219; GO:0036448; GO:1904659`

## Notes

Sugar efflux transporter A
