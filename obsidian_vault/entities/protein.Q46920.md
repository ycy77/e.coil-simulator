---
entity_id: "protein.Q46920"
entity_type: "protein"
name: "queF"
source_database: "UniProt"
source_id: "Q46920"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cytoplasm {ECO:0000305}."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "queF yqcD b2794 JW2765"
---

# queF

`protein.Q46920`

## Static

- Type: `protein`
- Source: `UniProt:Q46920`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cytoplasm {ECO:0000305}.

## Enriched Summary

FUNCTION: Catalyzes the NADPH-dependent reduction of 7-cyano-7-deazaguanine (preQ0) to 7-aminomethyl-7-deazaguanine (preQ1), a late step in the queuosine pathway. Is highly specific for its natural substrate preQ0, since it cannot use various aliphatic, aromatic, benzylic and heterocyclic nitriles, such as acetonitrile, benzonitrile, benzylcyanide and 2-cyanopyrrole, although it can reduce the substrate analog 5-cyanopyrrolo[2,3-d]pyrimidin-4-one with lesser efficiency. {ECO:0000269|PubMed:15767583, ECO:0000269|PubMed:23410922, ECO:0000269|PubMed:23595998}.

## Biological Role

Component of 7-cyano-7-deazaguanine reductase (complex.ecocyc.CPLX0-3501).

## Enriched Pathways

- `eco00790` Folate biosynthesis (KEGG)
- `eco01100` Metabolic pathways (KEGG)

## Annotation

FUNCTION: Catalyzes the NADPH-dependent reduction of 7-cyano-7-deazaguanine (preQ0) to 7-aminomethyl-7-deazaguanine (preQ1), a late step in the queuosine pathway. Is highly specific for its natural substrate preQ0, since it cannot use various aliphatic, aromatic, benzylic and heterocyclic nitriles, such as acetonitrile, benzonitrile, benzylcyanide and 2-cyanopyrrole, although it can reduce the substrate analog 5-cyanopyrrolo[2,3-d]pyrimidin-4-one with lesser efficiency. {ECO:0000269|PubMed:15767583, ECO:0000269|PubMed:23410922, ECO:0000269|PubMed:23595998}.

## Pathways

- `eco00790` Folate biosynthesis (KEGG)
- `eco01100` Metabolic pathways (KEGG)

## Outgoing Edges (1)

- `is_component_of` --> [[complex.ecocyc.CPLX0-3501|complex.ecocyc.CPLX0-3501]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2

## Incoming Edges (1)

- `encodes` <-- [[gene.b2794|gene.b2794]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:Q46920`
- `KEGG:ecj:JW2765;eco:b2794;ecoc:C3026_15365;`
- `GeneID:947270;`
- `GO:GO:0005829; GO:0008616; GO:0033739`
- `EC:1.7.1.13`

## Notes

NADPH-dependent 7-cyano-7-deazaguanine reductase (EC 1.7.1.13) (7-cyano-7-carbaguanine reductase) (NADPH-dependent nitrile oxidoreductase) (PreQ(0) reductase)
