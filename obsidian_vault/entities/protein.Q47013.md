---
entity_id: "protein.Q47013"
entity_type: "protein"
name: "elaD"
source_database: "UniProt"
source_id: "Q47013"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "elaD b2269 JW5840"
---

# elaD

`protein.Q47013`

## Static

- Type: `protein`
- Source: `UniProt:Q47013`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`

## Enriched Summary

FUNCTION: Protease that can act as an efficient and specific deubiquitinating enzyme in vitro. Does not possess desumoylating and deneddylating activities. The physiological substrate is unknown. {ECO:0000269|PubMed:17440617}. ElaD is a moderately active deubiquitinating protease. The C313 residue may be required for activity .

## Biological Role

Catalyzes 3.4.19.12-RXN (reaction.ecocyc.3.4.19.12-RXN).

## Annotation

FUNCTION: Protease that can act as an efficient and specific deubiquitinating enzyme in vitro. Does not possess desumoylating and deneddylating activities. The physiological substrate is unknown. {ECO:0000269|PubMed:17440617}.

## Outgoing Edges (1)

- `catalyzes` --> [[reaction.ecocyc.3.4.19.12-RXN|reaction.ecocyc.3.4.19.12-RXN]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (1)

- `encodes` <-- [[gene.b2269|gene.b2269]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:Q47013`
- `KEGG:ecj:JW5840;eco:b2269;`
- `GeneID:946742;`
- `GO:GO:0006508; GO:0008234; GO:0016579; GO:0016926; GO:0016929`
- `EC:3.4.22.-`

## Notes

Protease ElaD (EC 3.4.22.-) (Deubiquitinase) (Deubiquitinating enzyme) (DUB) (Deubiquitinating protease)
