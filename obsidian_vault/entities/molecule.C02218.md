---
entity_id: "molecule.C02218"
entity_type: "small_molecule"
name: "Dehydroalanine"
source_database: "KEGG"
source_id: "C02218"
default_state: "low"
allowed_states: "absent|low|medium|high"
subcellular_location: ""
enriched_summary_quality: "placeholder"
tags:
  - entity/small_molecule
  - source/KEGG
aliases:
  - "Dehydroalanine"
  - "2-Aminoacrylate"
  - "2-Aminoprop-2-enoate"
---

# Dehydroalanine

`molecule.C02218`

## Static

- Type: `small_molecule`
- Source: `KEGG:C02218`
- Default state: `low`
- Allowed states: `absent|low|medium|high`

## Enriched Summary

KEGG compound: Dehydroalanine; 2-Aminoacrylate; 2-Aminoprop-2-enoate EcoCyc common name: 2-aminoprop-2-enoate.

## Biological Role

Consumed as substrate in 2 reaction(s). Produced in 7 reaction(s).

## Enriched Pathways

- `eco00270` Cysteine and methionine metabolism (KEGG)

## Annotation

KEGG compound: Dehydroalanine; 2-Aminoacrylate; 2-Aminoprop-2-enoate

## Pathways

- `eco00270` Cysteine and methionine metabolism (KEGG)

## Outgoing Edges (9)

- `is_product_of` --> [[reaction.R00590|reaction.R00590]] `KEGG` `database` - C00065 <=> C02218 + C00001
- `is_product_of` --> [[reaction.ecocyc.RXN-15125|reaction.ecocyc.RXN-15125]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.RXN-15129|reaction.ecocyc.RXN-15129]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.RXN-15131|reaction.ecocyc.RXN-15131]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.RXN-15578|reaction.ecocyc.RXN-15578]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.RXN-15581|reaction.ecocyc.RXN-15581]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.RXN-19381|reaction.ecocyc.RXN-19381]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` --> [[reaction.ecocyc.RXN-15124|reaction.ecocyc.RXN-15124]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.RXN-8899|reaction.ecocyc.RXN-8899]] `EcoCyc` `database` - EcoCyc reaction LEFT

## Incoming Edges (0)

_None._

## External IDs

- `KEGG:C02218`

## Notes

Included because it appears in at least one E. coli KEGG pathway.
