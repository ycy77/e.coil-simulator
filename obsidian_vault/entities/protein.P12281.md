---
entity_id: "protein.P12281"
entity_type: "protein"
name: "moeA"
source_database: "UniProt"
source_id: "P12281"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "moeA bisB chlE narE b0827 JW0811"
---

# moeA

`protein.P12281`

## Static

- Type: `protein`
- Source: `UniProt:P12281`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`

## Enriched Summary

FUNCTION: Catalyzes the insertion of molybdate into adenylated molybdopterin with the concomitant release of AMP. {ECO:0000269|PubMed:15632135}.

## Biological Role

Component of molybdopterin molybdotransferase (complex.ecocyc.CPLX0-8045).

## Enriched Pathways

- `eco00790` Folate biosynthesis (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01240` Biosynthesis of cofactors (KEGG)

## Annotation

FUNCTION: Catalyzes the insertion of molybdate into adenylated molybdopterin with the concomitant release of AMP. {ECO:0000269|PubMed:15632135}.

## Pathways

- `eco00790` Folate biosynthesis (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01240` Biosynthesis of cofactors (KEGG)

## Outgoing Edges (1)

- `is_component_of` --> [[complex.ecocyc.CPLX0-8045|complex.ecocyc.CPLX0-8045]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2

## Incoming Edges (1)

- `encodes` <-- [[gene.b0827|gene.b0827]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P12281`
- `KEGG:ecj:JW0811;eco:b0827;ecoc:C3026_05190;`
- `GeneID:945454;`
- `GO:GO:0005737; GO:0005829; GO:0006777; GO:0042802; GO:0042803; GO:0046872; GO:0061599`
- `EC:2.10.1.1`

## Notes

Molybdopterin molybdenumtransferase (MPT Mo-transferase) (EC 2.10.1.1)
