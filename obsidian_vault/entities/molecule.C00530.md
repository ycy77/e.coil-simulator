---
entity_id: "molecule.C00530"
entity_type: "small_molecule"
name: "Hydroquinone"
source_database: "KEGG"
source_id: "C00530"
default_state: "low"
allowed_states: "absent|low|medium|high"
subcellular_location: ""
enriched_summary_quality: "placeholder"
tags:
  - entity/small_molecule
  - source/KEGG
aliases:
  - "Hydroquinone"
  - "p-Benzenediol"
  - "1,4-Benzenediol"
  - "1,4-Dihydroxybenzene"
  - "Benzene-1,4-diol"
  - "Quinol"
  - "4-Hydroxyphenol"
---

# Hydroquinone

`molecule.C00530`

## Static

- Type: `small_molecule`
- Source: `KEGG:C00530`
- Default state: `low`
- Allowed states: `absent|low|medium|high`

## Enriched Summary

KEGG compound: Hydroquinone; p-Benzenediol; 1,4-Benzenediol; 1,4-Dihydroxybenzene; Benzene-1,4-diol; Quinol; 4-Hydroxyphenol HYDROQUINONE Hydroquinone is the para isomer of the three isomeric Benzenediols benzenediols: CATECHOL (benzene-1,2-diol), CPD-623 (benzene-1,3-diol), and HYDROQUINONE (benzene-1,4-diol). The name "hydroquinone" was coined by Friedrich Wohler in 1843.

## Biological Role

Consumed as substrate in 2 reaction(s). Produced in 3 reaction(s).

## Enriched Pathways

- `eco00350` Tyrosine metabolism (KEGG)
- `eco00361` Chlorocyclohexane and chlorobenzene degradation (KEGG)
- `eco00362` Benzoate degradation (KEGG)
- `eco00627` Aminobenzoate degradation (KEGG)

## Annotation

KEGG compound: Hydroquinone; p-Benzenediol; 1,4-Benzenediol; 1,4-Dihydroxybenzene; Benzene-1,4-diol; Quinol; 4-Hydroxyphenol

## Pathways

- `eco00350` Tyrosine metabolism (KEGG)
- `eco00361` Chlorocyclohexane and chlorobenzene degradation (KEGG)
- `eco00362` Benzoate degradation (KEGG)
- `eco00627` Aminobenzoate degradation (KEGG)

## Outgoing Edges (5)

- `is_product_of` --> [[reaction.R06893|reaction.R06893]] `KEGG` `database` - C13636 + C00001 <=> C00530 + C00033
- `is_product_of` --> [[reaction.ecocyc.RXN0-5295|reaction.ecocyc.RXN0-5295]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.TRANS-RXN0-529|reaction.ecocyc.TRANS-RXN0-529]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` --> [[reaction.ecocyc.RXN-19775|reaction.ecocyc.RXN-19775]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.TRANS-RXN0-529|reaction.ecocyc.TRANS-RXN0-529]] `EcoCyc` `database` - EcoCyc reaction LEFT

## Incoming Edges (0)

_None._

## External IDs

- `KEGG:C00530`

## Notes

Included because it appears in at least one E. coli KEGG pathway.
