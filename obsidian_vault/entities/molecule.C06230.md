---
entity_id: "molecule.C06230"
entity_type: "small_molecule"
name: "Fe-enterobactin"
source_database: "KEGG"
source_id: "C06230"
default_state: "low"
allowed_states: "absent|low|medium|high"
subcellular_location: ""
enriched_summary_quality: "placeholder"
tags:
  - entity/small_molecule
  - source/KEGG
aliases:
  - "Fe-enterobactin"
  - "Fe-enterochlin"
---

# Fe-enterobactin

`molecule.C06230`

## Static

- Type: `small_molecule`
- Source: `KEGG:C06230`
- Default state: `low`
- Allowed states: `absent|low|medium|high`

## Enriched Summary

KEGG compound: Fe-enterobactin; Fe-enterochlin EcoCyc common name: iron(III)-enterobactin complex. ENTEROBACTIN Enterobactin is a catecholate siderophore produced almost exclusively by enterobacteria , although it has been reported in some Streptomyces species . It is a cyclic compound made of three units of 2,3-dihydroxybenzoylserine joined in a cyclic structure by lactone linkages (only the δ-cis isomer of the ferric chelate is biologically active). ENTEROBACTIN Enterobactin binds Fe3+ with a estimated Kd of 10-49 M (10-35 M at physiological pH) . ENTEROBACTIN Enterobactin not only is used by the organisms that produce it but also serves as an exosiderophore for many bacteria that are unable to synthesize it, such as TAX-287, in a strategy of siderophore piracy .

## Biological Role

Consumed as substrate in 4 reaction(s). Produced in 3 reaction(s).

## Enriched Pathways

- `eco02010` ABC transporters (KEGG)
- `eco02020` Two-component system (KEGG)

## Annotation

KEGG compound: Fe-enterobactin; Fe-enterochlin

## Pathways

- `eco02010` ABC transporters (KEGG)
- `eco02020` Two-component system (KEGG)

## Outgoing Edges (7)

- `is_product_of` --> [[reaction.ecocyc.ABC-10-RXN|reaction.ecocyc.ABC-10-RXN]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.RXN-20002|reaction.ecocyc.RXN-20002]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.RXN0-1682|reaction.ecocyc.RXN0-1682]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` --> [[reaction.ecocyc.ABC-10-RXN|reaction.ecocyc.ABC-10-RXN]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.RXN-20025|reaction.ecocyc.RXN-20025]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.RXN0-1682|reaction.ecocyc.RXN0-1682]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.RXN0-6938|reaction.ecocyc.RXN0-6938]] `EcoCyc` `database` - EcoCyc reaction LEFT

## Incoming Edges (2)

- `transports` <-- [[complex.ecocyc.ABC-10-CPLX|complex.ecocyc.ABC-10-CPLX]] `EcoCyc` `database` - EcoCyc transporters.col equation
- `transports` <-- [[complex.ecocyc.CPLX0-1941|complex.ecocyc.CPLX0-1941]] `EcoCyc` `database` - EcoCyc transporters.col equation

## External IDs

- `KEGG:C06230`

## Notes

Included because it appears in at least one E. coli KEGG pathway.
