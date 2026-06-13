---
entity_id: "molecule.C03089"
entity_type: "small_molecule"
name: "5-Methylthio-D-ribose"
source_database: "KEGG"
source_id: "C03089"
default_state: "low"
allowed_states: "absent|low|medium|high"
subcellular_location: ""
enriched_summary_quality: "placeholder"
tags:
  - entity/small_molecule
  - source/KEGG
aliases:
  - "5-Methylthio-D-ribose"
  - "S-Methyl-5-thio-D-ribose"
  - "5-(Methylsulfanyl)-D-ribose"
---

# 5-Methylthio-D-ribose

`molecule.C03089`

## Static

- Type: `small_molecule`
- Source: `KEGG:C03089`
- Default state: `low`
- Allowed states: `absent|low|medium|high`

## Enriched Summary

KEGG compound: 5-Methylthio-D-ribose; S-Methyl-5-thio-D-ribose; 5-(Methylsulfanyl)-D-ribose EcoCyc common name: 5-(methylsulfanyl)-D-ribose.

## Biological Role

Consumed as substrate in 2 reaction(s). Produced in 3 reaction(s).

## Enriched Pathways

- `eco00270` Cysteine and methionine metabolism (KEGG)

## Annotation

KEGG compound: 5-Methylthio-D-ribose; S-Methyl-5-thio-D-ribose; 5-(Methylsulfanyl)-D-ribose

## Pathways

- `eco00270` Cysteine and methionine metabolism (KEGG)

## Outgoing Edges (5)

- `is_product_of` --> [[reaction.ecocyc.METHYLTHIOADENOSINE-NUCLEOSIDASE-RXN|reaction.ecocyc.METHYLTHIOADENOSINE-NUCLEOSIDASE-RXN]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.TRANS-RXN0-461|reaction.ecocyc.TRANS-RXN0-461]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.TRANS-RXN0-615|reaction.ecocyc.TRANS-RXN0-615]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` --> [[reaction.ecocyc.TRANS-RXN0-461|reaction.ecocyc.TRANS-RXN0-461]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.TRANS-RXN0-615|reaction.ecocyc.TRANS-RXN0-615]] `EcoCyc` `database` - EcoCyc reaction LEFT

## Incoming Edges (0)

_None._

## External IDs

- `KEGG:C03089`

## Notes

Included because it appears in at least one E. coli KEGG pathway.
