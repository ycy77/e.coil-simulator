---
entity_id: "protein.P0A853"
entity_type: "protein"
name: "tnaA"
source_database: "UniProt"
source_id: "P0A853"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cytoplasm {ECO:0000305|PubMed:22380631}. Note=Almost exclusively localized in foci near 1 cell pole in mid-to-late exponential phase, fewer cells have foci at stationary phase; polar localization depends on the minCDE operon."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "tnaA ind b3708 JW3686"
---

# tnaA

`protein.P0A853`

## Static

- Type: `protein`
- Source: `UniProt:P0A853`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cytoplasm {ECO:0000305|PubMed:22380631}. Note=Almost exclusively localized in foci near 1 cell pole in mid-to-late exponential phase, fewer cells have foci at stationary phase; polar localization depends on the minCDE operon.

## Enriched Summary

Tryptophanase (EC 4.1.99.1) (L-tryptophan indole-lyase) (TNase) Tryptophanase or tryptophan indole-lyase (TnaA) is an extremely well-studied pyridoxal phosphate (PLP)-dependent enzyme that catalyzes the cleavage of L-tryptophan to indole, pyruvate and NH4+. Together with the tryptophan transporter TnaB, it enables utilization of L-tryptophan as sole source of nitrogen or carbon for growth. In recent years, it has become clear that one of the reaction products, indole, plays a significant role as an extracellular and intracellular signal, even acting as a cell cycle regulator . Indole production by TnaA depends directly on the amount of exogenous tryptophan, and the enzyme does not appear to degrade internal anabolic tryptophan . Tryptophanase is a major contributor towards the cellular L-cysteine desulfhydrase (CD) activity . In vitro, tryptophanase also catalyzes α,β elimination, β replacement, and α hydrogen exchange reactions with a variety of L-amino acids . Tryptophanase is one of the most S-sulfhydrated proteins in E. coli; at least six of its seven Cys residues can be S-sulfhydrated. S-sulfhydration reduces the enzymatic activity of tryptophanase. In a mouse model, a diet high in sulfur-containing amino acids reduces indole levels in the gut and mitigates kidney damage...

## Biological Role

Catalyzes L-tryptophan indole-lyase (deaminating; pyruvate-forming) (reaction.R00673). Component of tryptophanase / L-cysteine desulfhydrase (complex.ecocyc.TRYPTOPHAN-CPLX).

## Enriched Pathways

- `eco00380` Tryptophan metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)

## Annotation

Tryptophanase (EC 4.1.99.1) (L-tryptophan indole-lyase) (TNase)

## Pathways

- `eco00380` Tryptophan metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)

## Outgoing Edges (2)

- `catalyzes` --> [[reaction.R00673|reaction.R00673]] `KEGG` `database` - via EC:4.1.99.1
- `is_component_of` --> [[complex.ecocyc.TRYPTOPHAN-CPLX|complex.ecocyc.TRYPTOPHAN-CPLX]] `EcoCyc` `database` - EcoCyc component coefficient=4 | EcoCyc protcplxs.col coefficient=4

## Incoming Edges (1)

- `encodes` <-- [[gene.b3708|gene.b3708]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P0A853`
- `KEGG:ecj:JW3686;eco:b3708;ecoc:C3026_20105;`
- `GeneID:75173927;75205423;948221;`
- `GO:GO:0005829; GO:0006569; GO:0009034; GO:0016020; GO:0016829; GO:0030170; GO:0030955; GO:0032991; GO:0042431; GO:0042802; GO:0060187; GO:0080146`
- `EC:4.1.99.1`

## Notes

Tryptophanase (EC 4.1.99.1) (L-tryptophan indole-lyase) (TNase)
