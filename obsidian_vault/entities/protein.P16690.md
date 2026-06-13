---
entity_id: "protein.P16690"
entity_type: "protein"
name: "phnN"
source_database: "UniProt"
source_id: "P16690"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "phnN b4094 JW4055"
---

# phnN

`protein.P16690`

## Static

- Type: `protein`
- Source: `UniProt:P16690`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`

## Enriched Summary

FUNCTION: Catalyzes the phosphorylation of ribose 1,5-bisphosphate to 5-phospho-D-ribosyl alpha-1-diphosphate (PRPP). Accepts ATP but not GTP as a phosphoryl donor, and uses ribose 1,5-bisphosphate but not ribose, ribose 1-phosphate, or ribose 5-phosphate as a phosphoryl acceptor. {ECO:0000269|PubMed:12700258, ECO:0000269|PubMed:19733071}. PhnN was found to catalyze the ribose 1,5-bisphosphokinase reaction in the PWY-7805 pathway. phnN is part of a phosphate starvation-inducible operon that is required for use of phosphonate and phosphite as phosphorous sources . It was initially suggested that PhnN might be a subunit or an accessory factor of a C-P lyase. phnN insertion mutants show reduced growth on phosphite and methylphosphonate as a source of phosphorous . Derepression of phnN expression suppresses the NAD requirement of a Δprs mutant . The authors proposed a PRPP biosynthesis pathway involving phosphoribomutase (DeoB), a hypothesized ribose-1-phosphokinase, and PhnN. Overexpression of phnN increases the tolerance of E. coli to n-butanol . Reviews:

## Biological Role

Catalyzes RXN0-1401 (reaction.ecocyc.RXN0-1401).

## Enriched Pathways

- `eco00030` Pentose phosphate pathway (KEGG)
- `eco01100` Metabolic pathways (KEGG)

## Annotation

FUNCTION: Catalyzes the phosphorylation of ribose 1,5-bisphosphate to 5-phospho-D-ribosyl alpha-1-diphosphate (PRPP). Accepts ATP but not GTP as a phosphoryl donor, and uses ribose 1,5-bisphosphate but not ribose, ribose 1-phosphate, or ribose 5-phosphate as a phosphoryl acceptor. {ECO:0000269|PubMed:12700258, ECO:0000269|PubMed:19733071}.

## Pathways

- `eco00030` Pentose phosphate pathway (KEGG)
- `eco01100` Metabolic pathways (KEGG)

## Outgoing Edges (1)

- `catalyzes` --> [[reaction.ecocyc.RXN0-1401|reaction.ecocyc.RXN0-1401]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (1)

- `encodes` <-- [[gene.b4094|gene.b4094]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P16690`
- `KEGG:ecj:JW4055;eco:b4094;ecoc:C3026_22130;`
- `GeneID:93777740;948608;`
- `GO:GO:0005524; GO:0005829; GO:0006015; GO:0009435; GO:0019634; GO:0033863`
- `EC:2.7.4.23`

## Notes

Ribose 1,5-bisphosphate phosphokinase PhnN (EC 2.7.4.23) (Ribose 1,5-bisphosphokinase)
