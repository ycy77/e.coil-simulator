---
entity_id: "protein.P27837"
entity_type: "protein"
name: "thrP"
source_database: "UniProt"
source_id: "P27837"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cell inner membrane {ECO:0000269|PubMed:15919996}; Multi-pass membrane protein {ECO:0000255}."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "thrP yifK b3795 JW5595"
---

# thrP

`protein.P27837`

## Static

- Type: `protein`
- Source: `UniProt:P27837`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cell inner membrane {ECO:0000269|PubMed:15919996}; Multi-pass membrane protein {ECO:0000255}.

## Enriched Summary

FUNCTION: Permease that mediates the proton-dependent threonine and serine uptake (PubMed:37025642). Shows higher specificity for threonine (PubMed:37025642). Cannot transport homoserine (PubMed:37025642). {ECO:0000269|PubMed:37025642}. ThrP (formerly YifK) is a proton-dependent, serine/threonine symporter - one of multiple known systems that mediate serine and threonine uptake . ThrP contributes to threonine uptake in a threonine auxotrophic strain that lacks the threonine transporters YGJU-MONOMER SstT and TDCC-MONOMER TdcC; growth of an engineered MG1655-derived strain which contains ThrP as the single threonine carrier is inhibited by an excess of serine . ThrP is a member of the Amino Acid Transporter (AAT) Family within the Amino Acid-Polyamine-Organocation (APC) Superfamily .

## Biological Role

Catalyzes L-serine:proton symport (reaction.ecocyc.TRANS-RXN-71), L-threonine:proton symport (reaction.ecocyc.TRANS-RXN-72).

## Annotation

FUNCTION: Permease that mediates the proton-dependent threonine and serine uptake (PubMed:37025642). Shows higher specificity for threonine (PubMed:37025642). Cannot transport homoserine (PubMed:37025642). {ECO:0000269|PubMed:37025642}.

## Outgoing Edges (2)

- `catalyzes` --> [[reaction.ecocyc.TRANS-RXN-71|reaction.ecocyc.TRANS-RXN-71]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` --> [[reaction.ecocyc.TRANS-RXN-72|reaction.ecocyc.TRANS-RXN-72]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (1)

- `encodes` <-- [[gene.b3795|gene.b3795]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P27837`
- `KEGG:ecj:JW5595;eco:b3795;ecoc:C3026_20550;`
- `GeneID:93778148;945400;`
- `GO:GO:0005886; GO:0015194; GO:0015195; GO:0015825; GO:0015826; GO:0022857`

## Notes

Threonine/serine transporter ThrP (Threonine/serine:H(+) symporter ThrP)
