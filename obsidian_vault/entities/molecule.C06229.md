---
entity_id: "molecule.C06229"
entity_type: "small_molecule"
name: "Fe(III)dicitrate"
source_database: "KEGG"
source_id: "C06229"
default_state: "low"
allowed_states: "absent|low|medium|high"
subcellular_location: ""
enriched_summary_quality: "placeholder"
tags:
  - entity/small_molecule
  - source/KEGG
aliases:
  - "Fe(III)dicitrate"
  - "Iron(III)dicitrate"
---

# Fe(III)dicitrate

`molecule.C06229`

## Static

- Type: `small_molecule`
- Source: `KEGG:C06229`
- Default state: `low`
- Allowed states: `absent|low|medium|high`

## Enriched Summary

KEGG compound: Fe(III)dicitrate; Iron(III)dicitrate EcoCyc common name: iron(III) dicitrate. This compound represents the complex between iron(III) and citrate. The coordination chemistry of iron(III) citrate appears complex and is the topic of continued investigation (see for example ). The structure shown here is a mononuclear dicitrate complex, also known as ferric dicitrate, which is thought to be important under physiological conditions. The complex has been crystallized . Dinuclear complexes (containing 2 Fe atoms) and polynuclear complexes (>2 Fe atoms) have also been described (see and references within).

## Biological Role

Consumed as substrate in 2 reaction(s). Produced in 2 reaction(s).

## Enriched Pathways

- `eco02010` ABC transporters (KEGG)

## Annotation

KEGG compound: Fe(III)dicitrate; Iron(III)dicitrate

## Pathways

- `eco02010` ABC transporters (KEGG)

## Outgoing Edges (4)

- `is_product_of` --> [[reaction.ecocyc.ABC-9-RXN|reaction.ecocyc.ABC-9-RXN]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.RXN0-1684|reaction.ecocyc.RXN0-1684]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` --> [[reaction.ecocyc.ABC-9-RXN|reaction.ecocyc.ABC-9-RXN]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.RXN0-1684|reaction.ecocyc.RXN0-1684]] `EcoCyc` `database` - EcoCyc reaction LEFT

## Incoming Edges (2)

- `transports` <-- [[complex.ecocyc.ABC-9-CPLX|complex.ecocyc.ABC-9-CPLX]] `EcoCyc` `database` - EcoCyc transporters.col equation
- `transports` <-- [[complex.ecocyc.CPLX0-1943|complex.ecocyc.CPLX0-1943]] `EcoCyc` `database` - EcoCyc transporters.col equation

## External IDs

- `KEGG:C06229`

## Notes

Included because it appears in at least one E. coli KEGG pathway.
