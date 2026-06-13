---
entity_id: "molecule.C05684"
entity_type: "small_molecule"
name: "Selenite"
source_database: "KEGG"
source_id: "C05684"
default_state: "low"
allowed_states: "absent|low|medium|high"
subcellular_location: ""
enriched_summary_quality: "placeholder"
tags:
  - entity/small_molecule
  - source/KEGG
aliases:
  - "Selenite"
---

# Selenite

`molecule.C05684`

## Static

- Type: `small_molecule`
- Source: `KEGG:C05684`
- Default state: `low`
- Allowed states: `absent|low|medium|high`

## Enriched Summary

KEGG compound: Selenite Selenium is an essential trace element that is crucial for the normal development of bacteria and animals. High concentrations of selenium are however toxic, largely because transporters and enzymes involved in sulfur and sulfo-compound metabolism can often erroneously substitute Elemental-selenium for sulfur and can misincorporate seleno-amino acids into proteins . In humans the safety threshold between acute selenium poisoning (>400 μg/day) and selenium deficiency (<40 μg/day) is very narrow. The natural forms of selenium include SELENATE [Se(VI)], SELENITE [Se(IV)], Elemental-selenium [Se(0)], and SE-2 [Se(-II)]. Selenite is the most toxic, while elemental selenium is insoluble and is generally considered to be non-toxic . However, selenium rarely occurs in its elemental state in nature. Elemental selenium can be formed by certain organisms, usually by reduction of the oxidized forms SELENATE and SELENITE. Some bacterial species are known to form selenium nanoparticles that consist of elemental selenium coated by a mixture of proteins, lipids, and carbohydrates .

## Biological Role

Consumed as substrate in 3 reaction(s). Produced in 1 reaction(s).

## Enriched Pathways

- `eco00450` Selenocompound metabolism (KEGG)

## Annotation

KEGG compound: Selenite

## Pathways

- `eco00450` Selenocompound metabolism (KEGG)

## Outgoing Edges (4)

- `is_product_of` --> [[reaction.ecocyc.TRANS-RXN0-479|reaction.ecocyc.TRANS-RXN0-479]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` --> [[reaction.ecocyc.RXN-12864|reaction.ecocyc.RXN-12864]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.RXN-24479|reaction.ecocyc.RXN-24479]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.TRANS-RXN0-479|reaction.ecocyc.TRANS-RXN0-479]] `EcoCyc` `database` - EcoCyc reaction LEFT

## Incoming Edges (1)

- `transports` <-- [[complex.ecocyc.ABC-7-CPLX|complex.ecocyc.ABC-7-CPLX]] `EcoCyc` `database` - EcoCyc transporters.col equation

## External IDs

- `KEGG:C05684`

## Notes

Included because it appears in at least one E. coli KEGG pathway.
