---
entity_id: "protein.P67603"
entity_type: "protein"
name: "yqfB"
source_database: "UniProt"
source_id: "P67603"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "yqfB b2900 JW2868"
---

# yqfB

`protein.P67603`

## Static

- Type: `protein`
- Source: `UniProt:P67603`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`

## Enriched Summary

FUNCTION: Catalyzes the hydrolysis of N(4)-acetylcytidine (ac4C). Can also hydrolyze N(4)-acetyl-2'-deoxycytidine and N(4)-acetylcytosine with lower efficiency. Has weaker activity towards a wide range of structurally different N(4)-acylated cytosines and cytidines. {ECO:0000269|PubMed:31964920}. YqfB hydrolyzes a variety of N4-modified cytosine/cytidine compounds, including N4-acetylcytidine (ac4C), its likely physiological substrate . Amino acid residues conserved between closely related proteins were identified and mutagenized; the Arg26Ala, Thr24Ala and Lys21Ala mutants lacked catalytic activity. A catalytic mechanism has been proposed . A solution structure of YqfB has been determined . However, this structure may differ significantly from the native structure of the protein .

## Biological Role

Catalyzes N4-acetylcytidine amidohydrolase (reaction.R12635), RXN-21270 (reaction.ecocyc.RXN-21270).

## Annotation

FUNCTION: Catalyzes the hydrolysis of N(4)-acetylcytidine (ac4C). Can also hydrolyze N(4)-acetyl-2'-deoxycytidine and N(4)-acetylcytosine with lower efficiency. Has weaker activity towards a wide range of structurally different N(4)-acylated cytosines and cytidines. {ECO:0000269|PubMed:31964920}.

## Outgoing Edges (2)

- `catalyzes` --> [[reaction.R12635|reaction.R12635]] `KEGG` `database` - via EC:3.5.1.135
- `catalyzes` --> [[reaction.ecocyc.RXN-21270|reaction.ecocyc.RXN-21270]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (1)

- `encodes` <-- [[gene.b2900|gene.b2900]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P67603`
- `KEGG:ecj:JW2868;eco:b2900;ecoc:C3026_15900;`
- `GeneID:75173001;947380;`
- `GO:GO:0005829; GO:0016813; GO:0046135; GO:0106251`
- `EC:3.5.1.135`

## Notes

N(4)-acetylcytidine amidohydrolase (ac4C amidohydrolase) (EC 3.5.1.135)
