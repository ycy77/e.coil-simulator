---
entity_id: "molecule.C00170"
entity_type: "small_molecule"
name: "5'-Methylthioadenosine"
source_database: "KEGG"
source_id: "C00170"
default_state: "low"
allowed_states: "absent|low|medium|high"
subcellular_location: ""
enriched_summary_quality: "placeholder"
tags:
  - entity/small_molecule
  - source/KEGG
aliases:
  - "5'-Methylthioadenosine"
  - "Methylthioadenosine"
  - "S-Methyl-5'-thioadenosine"
  - "5-Methylthioadenosine"
  - "5'-Deoxy-5'-(methylthio)adenosine"
  - "Thiomethyladenosine"
  - "MTA"
  - "5'-Deoxy-5'-(methylsulfanyl)adenosine"
---

# 5'-Methylthioadenosine

`molecule.C00170`

## Static

- Type: `small_molecule`
- Source: `KEGG:C00170`
- Default state: `low`
- Allowed states: `absent|low|medium|high`

## Enriched Summary

KEGG compound: 5'-Methylthioadenosine; Methylthioadenosine; S-Methyl-5'-thioadenosine; 5-Methylthioadenosine; 5'-Deoxy-5'-(methylthio)adenosine; Thiomethyladenosine; MTA; 5'-Deoxy-5'-(methylsulfanyl)adenosine EcoCyc common name: S-methyl-5'-thioadenosine.

## Biological Role

Consumed as substrate in 3 reaction(s). Produced in 4 reaction(s).

## Enriched Pathways

- `eco00270` Cysteine and methionine metabolism (KEGG)

## Annotation

KEGG compound: 5'-Methylthioadenosine; Methylthioadenosine; S-Methyl-5'-thioadenosine; 5-Methylthioadenosine; 5'-Deoxy-5'-(methylthio)adenosine; Thiomethyladenosine; MTA; 5'-Deoxy-5'-(methylsulfanyl)adenosine

## Pathways

- `eco00270` Cysteine and methionine metabolism (KEGG)

## Outgoing Edges (8)

- `is_component_of` --> [[complex.ecocyc.CPLX0-8026|complex.ecocyc.CPLX0-8026]] `EcoCyc` `database` - EcoCyc component coefficient=
- `is_product_of` --> [[reaction.ecocyc.2.5.1.25-RXN|reaction.ecocyc.2.5.1.25-RXN]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.RXN-21179|reaction.ecocyc.RXN-21179]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.RXN0-5217|reaction.ecocyc.RXN0-5217]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.SPERMIDINESYN-RXN|reaction.ecocyc.SPERMIDINESYN-RXN]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` --> [[reaction.ecocyc.5-METHYLTHIOADENOSINE-PHOSPHORYLASE-RXN|reaction.ecocyc.5-METHYLTHIOADENOSINE-PHOSPHORYLASE-RXN]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.METHYLTHIOADENOSINE-NUCLEOSIDASE-RXN|reaction.ecocyc.METHYLTHIOADENOSINE-NUCLEOSIDASE-RXN]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.RXN0-7069|reaction.ecocyc.RXN0-7069]] `EcoCyc` `database` - EcoCyc reaction LEFT

## Incoming Edges (0)

_None._

## External IDs

- `KEGG:C00170`

## Notes

Included because it appears in at least one E. coli KEGG pathway.
