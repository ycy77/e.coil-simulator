---
entity_id: "protein.P37197"
entity_type: "protein"
name: "ccp"
source_database: "UniProt"
source_id: "P37197"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cell inner membrane {ECO:0000305|PubMed:29550214, ECO:0000305|PubMed:37375153}; Single-pass membrane protein {ECO:0000255}; Periplasmic side {ECO:0000305|PubMed:28696311, ECO:0000305|PubMed:29550214, ECO:0000305|PubMed:37375153}."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "ccp yhjA b3518 JW3486"
---

# ccp

`protein.P37197`

## Static

- Type: `protein`
- Source: `UniProt:P37197`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cell inner membrane {ECO:0000305|PubMed:29550214, ECO:0000305|PubMed:37375153}; Single-pass membrane protein {ECO:0000255}; Periplasmic side {ECO:0000305|PubMed:28696311, ECO:0000305|PubMed:29550214, ECO:0000305|PubMed:37375153}.

## Enriched Summary

FUNCTION: Cytochrome peroxidase that enables anaerobic respiration with H(2)O(2) as a terminal electron acceptor (PubMed:28696311). It receives electrons from the quinol pool (PubMed:28696311, PubMed:29550214). Menaquinol is probably the electron donor in vivo (PubMed:28696311, PubMed:29550214). It can use menadiol (a menaquinol analog), hydroquinone, duroquinol and the artificial electron donor ABTS(2-) in vitro, but only menadiol and hydroquinone can efficiently transfer electrons to Ccp, maintaining the catalytic activity of the enzyme (PubMed:29550214). It enables E.coli to grow on a nonfermentable carbon source when H(2)O(2) is supplied (PubMed:28696311). Plays a role in the peroxide stress response under anaerobic conditions (PubMed:17464064). However, it does not degrade H(2)O(2) quickly enough to lower the periplasmic H(2)O(2) level below that of the surrounding medium and protect the cell from its toxic effects (PubMed:28696311). {ECO:0000269|PubMed:17464064, ECO:0000269|PubMed:28696311, ECO:0000269|PubMed:29550214}. ccp encodes a periplasmic cytochrome c peroxidase (CCP) that enables E...

## Biological Role

Catalyzes ferrocytochrome-c:hydrogen-peroxide oxidoreductase (reaction.R00017), RXN-19020 (reaction.ecocyc.RXN-19020), RXN-19775 (reaction.ecocyc.RXN-19775), RXN-19776 (reaction.ecocyc.RXN-19776). Bound by heme c (molecule.ecocyc.HEME_C).

## Annotation

FUNCTION: Cytochrome peroxidase that enables anaerobic respiration with H(2)O(2) as a terminal electron acceptor (PubMed:28696311). It receives electrons from the quinol pool (PubMed:28696311, PubMed:29550214). Menaquinol is probably the electron donor in vivo (PubMed:28696311, PubMed:29550214). It can use menadiol (a menaquinol analog), hydroquinone, duroquinol and the artificial electron donor ABTS(2-) in vitro, but only menadiol and hydroquinone can efficiently transfer electrons to Ccp, maintaining the catalytic activity of the enzyme (PubMed:29550214). It enables E.coli to grow on a nonfermentable carbon source when H(2)O(2) is supplied (PubMed:28696311). Plays a role in the peroxide stress response under anaerobic conditions (PubMed:17464064). However, it does not degrade H(2)O(2) quickly enough to lower the periplasmic H(2)O(2) level below that of the surrounding medium and protect the cell from its toxic effects (PubMed:28696311). {ECO:0000269|PubMed:17464064, ECO:0000269|PubMed:28696311, ECO:0000269|PubMed:29550214}.

## Outgoing Edges (4)

- `catalyzes` --> [[reaction.R00017|reaction.R00017]] `KEGG` `database` - via EC:1.11.1.5
- `catalyzes` --> [[reaction.ecocyc.RXN-19020|reaction.ecocyc.RXN-19020]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` --> [[reaction.ecocyc.RXN-19775|reaction.ecocyc.RXN-19775]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` --> [[reaction.ecocyc.RXN-19776|reaction.ecocyc.RXN-19776]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (2)

- `binds` <-- [[molecule.ecocyc.HEME_C|molecule.ecocyc.HEME_C]] `EcoCyc` `database` - EcoCyc enzymatic reaction cofactor
- `encodes` <-- [[gene.b3518|gene.b3518]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P37197`
- `KEGG:ecj:JW3486;eco:b3518;ecoc:C3026_19060;`
- `GeneID:948038;`
- `GO:GO:0004130; GO:0005886; GO:0009055; GO:0019645; GO:0020037; GO:0042542; GO:0042743; GO:0046872`
- `EC:1.11.1.-`

## Notes

Cytochrome c peroxidase Ccp (EC 1.11.1.-) (Quinol peroxidase)
