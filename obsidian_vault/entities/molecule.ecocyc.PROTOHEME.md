---
entity_id: "molecule.ecocyc.PROTOHEME"
entity_type: "small_molecule"
name: "protoheme"
source_database: "EcoCyc"
source_id: "PROTOHEME"
default_state: "low"
allowed_states: "absent|low|medium|high"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/small_molecule
  - source/EcoCyc
aliases:
  - "protoheme IX"
  - "ferroprotoporphyrin IX"
  - "ferroheme b"
---

# protoheme

`molecule.ecocyc.PROTOHEME`

## Static

- Type: `small_molecule`
- Source: `EcoCyc:PROTOHEME`
- Default state: `low`
- Allowed states: `absent|low|medium|high`

## Enriched Summary

'Heme' is usually understood as any tetrapyrrolic chelate of iron. The terms 'ferroheme' and 'ferriheme' refer to the Fe(II) and Fe(III) oxidation states in heme (even though Fe(IV) is found as a catalytic intermediate in some systems). Heme-b "Heme b", whose PROTOHEME "ferrous form" is known as protoheme IX, is the immediate product of the heme biosynthesis pathways (by ferro-chelation of PROTOPORPHYRIN_IX) and the most abundant heme form. It is found in common proteins such as hemoglobin and myoglobin. Heme b is part of Cytochromes-B "b-type cytochromes". 'Heme' is usually understood as any tetrapyrrolic chelate of iron. The terms 'ferroheme' and 'ferriheme' refer to the Fe(II) and Fe(III) oxidation states in heme (even though Fe(IV) is found as a catalytic intermediate in some systems). Heme-b "Heme b", whose PROTOHEME "ferrous form" is known as protoheme IX, is the immediate product of the heme biosynthesis pathways (by ferro-chelation of PROTOPORPHYRIN_IX) and the most abundant heme form. It is found in common proteins such as hemoglobin and myoglobin. Heme b is part of Cytochromes-B "b-type cytochromes".

## Biological Role

Consumed as substrate in 5 reaction(s). Produced in 2 reaction(s). Binds catalase/hydroperoxidase HPI (complex.ecocyc.HYDROPEROXIDI-CPLX), hmp (protein.P24232).

## Annotation

'Heme' is usually understood as any tetrapyrrolic chelate of iron. The terms 'ferroheme' and 'ferriheme' refer to the Fe(II) and Fe(III) oxidation states in heme (even though Fe(IV) is found as a catalytic intermediate in some systems). Heme-b "Heme b", whose PROTOHEME "ferrous form" is known as protoheme IX, is the immediate product of the heme biosynthesis pathways (by ferro-chelation of PROTOPORPHYRIN_IX) and the most abundant heme form. It is found in common proteins such as hemoglobin and myoglobin. Heme b is part of Cytochromes-B "b-type cytochromes".

## Outgoing Edges (9)

- `binds` --> [[complex.ecocyc.HYDROPEROXIDI-CPLX|complex.ecocyc.HYDROPEROXIDI-CPLX]] `EcoCyc` `database` - EcoCyc enzymatic reaction cofactor
- `binds` --> [[protein.P24232|protein.P24232]] `EcoCyc` `database` - EcoCyc enzymatic reaction cofactor
- `is_product_of` --> [[reaction.ecocyc.TRANS-RXN-1540|reaction.ecocyc.TRANS-RXN-1540]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.TRANS-RXN0-162|reaction.ecocyc.TRANS-RXN0-162]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` --> [[reaction.ecocyc.HEMEOSYN-RXN|reaction.ecocyc.HEMEOSYN-RXN]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.PROTOHEMEFERROCHELAT-RXN|reaction.ecocyc.PROTOHEMEFERROCHELAT-RXN]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.RXN-21407|reaction.ecocyc.RXN-21407]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.TRANS-RXN-1540|reaction.ecocyc.TRANS-RXN-1540]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.TRANS-RXN0-162|reaction.ecocyc.TRANS-RXN0-162]] `EcoCyc` `database` - EcoCyc reaction LEFT

## Incoming Edges (2)

- `transports` <-- [[complex.ecocyc.ABC-35-CPLX|complex.ecocyc.ABC-35-CPLX]] `EcoCyc` `database` - EcoCyc transporters.col equation
- `transports` <-- [[complex.ecocyc.ABC-6-CPLX|complex.ecocyc.ABC-6-CPLX]] `EcoCyc` `database` - EcoCyc transporters.col equation

## External IDs

- `EcoCyc:PROTOHEME`
- `HMDB:HMDB0003178`
- `METANETX:MNXM249`
- `REFMET:Heme`
- `BIGG:pheme`

## Notes

(C 34)
