---
entity_id: "molecule.C01847"
entity_type: "small_molecule"
name: "Reduced FMN"
source_database: "KEGG"
source_id: "C01847"
default_state: "low"
allowed_states: "absent|low|medium|high"
subcellular_location: ""
enriched_summary_quality: "placeholder"
tags:
  - entity/small_molecule
  - source/KEGG
aliases:
  - "Reduced FMN"
  - "FMNH2"
---

# Reduced FMN

`molecule.C01847`

## Static

- Type: `small_molecule`
- Source: `KEGG:C01847`
- Default state: `low`
- Allowed states: `absent|low|medium|high`

## Enriched Summary

KEGG compound: Reduced FMN; FMNH2 EcoCyc common name: FMNH2. FMNH2 is the fully reduced form of FMN. FMN is the principal form in which RIBOFLAVIN (vitamin B2) is found in cells and tissues. While it takes more energy to produce than the non-phosphorylated form of RIBOFLAVIN, it is more soluble. FMN is produced from riboflavin by the enzyme riboflavin kinase, and functions as prosthetic group of various oxidoreductases including NADH dehydrogenase. During the catalytic cycle, FMN cycles between the oxidized (FMN), semiquinone (FMNH) and reduced (FMNH2) forms, enabling it to take part in both one and two electron transfers. FMN is a stronger oxidizing agent than NAD.

## Biological Role

Consumed as substrate in 11 reaction(s). Binds chorismate synthase (complex.ecocyc.AROC-CPLX).

## Enriched Pathways

- `eco00740` Riboflavin metabolism (KEGG)

## Annotation

KEGG compound: Reduced FMN; FMNH2

## Pathways

- `eco00740` Riboflavin metabolism (KEGG)

## Outgoing Edges (12)

- `binds` --> [[complex.ecocyc.AROC-CPLX|complex.ecocyc.AROC-CPLX]] `EcoCyc` `database` - EcoCyc enzymatic reaction cofactor
- `is_substrate_of` --> [[reaction.ecocyc.FMNREDUCT-RXN|reaction.ecocyc.FMNREDUCT-RXN]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.RXN-12444|reaction.ecocyc.RXN-12444]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.RXN-12886|reaction.ecocyc.RXN-12886]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.RXN-13418|reaction.ecocyc.RXN-13418]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.RXN-15341|reaction.ecocyc.RXN-15341]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.RXN-16937|reaction.ecocyc.RXN-16937]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.RXN-22443|reaction.ecocyc.RXN-22443]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.RXN-9510|reaction.ecocyc.RXN-9510]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.RXN0-280|reaction.ecocyc.RXN0-280]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.RXN0-6444|reaction.ecocyc.RXN0-6444]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.RXN0-6973|reaction.ecocyc.RXN0-6973]] `EcoCyc` `database` - EcoCyc reaction LEFT

## Incoming Edges (0)

_None._

## External IDs

- `KEGG:C01847`

## Notes

Included because it appears in at least one E. coli KEGG pathway.
