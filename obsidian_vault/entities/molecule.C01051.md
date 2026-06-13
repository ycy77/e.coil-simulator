---
entity_id: "molecule.C01051"
entity_type: "small_molecule"
name: "Uroporphyrinogen III"
source_database: "KEGG"
source_id: "C01051"
default_state: "low"
allowed_states: "absent|low|medium|high"
subcellular_location: ""
enriched_summary_quality: "placeholder"
tags:
  - entity/small_molecule
  - source/KEGG
aliases:
  - "Uroporphyrinogen III"
---

# Uroporphyrinogen III

`molecule.C01051`

## Static

- Type: `small_molecule`
- Source: `KEGG:C01051`
- Default state: `low`
- Allowed states: `absent|low|medium|high`

## Enriched Summary

KEGG compound: Uroporphyrinogen III EcoCyc common name: uroporphyrinogen-III. CPD-11444 "Uroporphyrinogen-I" and UROPORPHYRINOGEN-III are both naturally occurring isomers. The difference between the two is the relative positions of the acetyl and propanoyl side chains on only one of the rings. Where in CPD-11444 the side chains of all four rings have the same relative positions, in UROPORPHYRINOGEN-III the order is reversed on one of the rings. While CPD-11444 can be formed spontaneously from HYDROXYMETHYLBILANE, the formation of UROPORPHYRINOGEN-III requires a dedicated enzyme - EC-4.2.1.75 "EC 4.2.1.75, uroporphyrinogen-III synthase". Both isomers are substrates for EC-4.1.1.37 "EC 4.1.1.37, uroporphyrinogen decarboxylase", although UROPORPHYRINOGEN-III is a better substrate .

## Biological Role

Consumed as substrate in 4 reaction(s). Produced in 2 reaction(s).

## Enriched Pathways

- `eco00860` Porphyrin metabolism (KEGG)

## Annotation

KEGG compound: Uroporphyrinogen III

## Pathways

- `eco00860` Porphyrin metabolism (KEGG)

## Outgoing Edges (6)

- `is_product_of` --> [[reaction.R03165|reaction.R03165]] `KEGG` `database` - C01024 <=> C01051 + C00001
- `is_product_of` --> [[reaction.ecocyc.UROGENIIISYN-RXN|reaction.ecocyc.UROGENIIISYN-RXN]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` --> [[reaction.R03194|reaction.R03194]] `KEGG` `database` - 2 C00019 + C01051 <=> 2 C00021 + C02463
- `is_substrate_of` --> [[reaction.ecocyc.RXN-13403|reaction.ecocyc.RXN-13403]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.UROGENDECARBOX-RXN|reaction.ecocyc.UROGENDECARBOX-RXN]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.UROPORIIIMETHYLTRANSA-RXN|reaction.ecocyc.UROPORIIIMETHYLTRANSA-RXN]] `EcoCyc` `database` - EcoCyc reaction LEFT

## Incoming Edges (0)

_None._

## External IDs

- `KEGG:C01051`

## Notes

Included because it appears in at least one E. coli KEGG pathway.
