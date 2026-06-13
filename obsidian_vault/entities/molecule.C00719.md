---
entity_id: "molecule.C00719"
entity_type: "small_molecule"
name: "Betaine"
source_database: "KEGG"
source_id: "C00719"
default_state: "low"
allowed_states: "absent|low|medium|high"
subcellular_location: ""
enriched_summary_quality: "placeholder"
tags:
  - entity/small_molecule
  - source/KEGG
aliases:
  - "Betaine"
  - "Trimethylaminoacetate"
  - "Glycine betaine"
  - "N,N,N-Trimethylglycine"
  - "Trimethylammonioacetate"
---

# Betaine

`molecule.C00719`

## Static

- Type: `small_molecule`
- Source: `KEGG:C00719`
- Default state: `low`
- Allowed states: `absent|low|medium|high`

## Enriched Summary

KEGG compound: Betaine; Trimethylaminoacetate; Glycine betaine; N,N,N-Trimethylglycine; Trimethylammonioacetate EcoCyc common name: glycine betaine. Glycine betaine (N,N,N-trimethylglycine) is a very efficient osmolyte found in a wide range of bacteria and plants, where it is accumulated at high cytoplasmic concentrations in response to osmotic stress, to act as an osmoprotectant .

## Biological Role

Consumed as substrate in 5 reaction(s). Produced in 6 reaction(s).

## Enriched Pathways

- `eco00260` Glycine, serine and threonine metabolism (KEGG)
- `eco00670` One carbon pool by folate (KEGG)
- `eco02010` ABC transporters (KEGG)
- `eco04981` Folate transport and metabolism (KEGG)

## Annotation

KEGG compound: Betaine; Trimethylaminoacetate; Glycine betaine; N,N,N-Trimethylglycine; Trimethylammonioacetate

## Pathways

- `eco00260` Glycine, serine and threonine metabolism (KEGG)
- `eco00670` One carbon pool by folate (KEGG)
- `eco02010` ABC transporters (KEGG)
- `eco04981` Folate transport and metabolism (KEGG)

## Outgoing Edges (11)

- `is_product_of` --> [[reaction.ecocyc.BADH-RXN|reaction.ecocyc.BADH-RXN]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.RXN0-7231|reaction.ecocyc.RXN0-7231]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.TRANS-RXN-283|reaction.ecocyc.TRANS-RXN-283]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.TRANS-RXN-29A|reaction.ecocyc.TRANS-RXN-29A]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.TRANS-RXN0-490|reaction.ecocyc.TRANS-RXN0-490]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.TRANS-RXN0-532|reaction.ecocyc.TRANS-RXN0-532]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` --> [[reaction.ecocyc.RXN-17759|reaction.ecocyc.RXN-17759]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.TRANS-RXN-283|reaction.ecocyc.TRANS-RXN-283]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.TRANS-RXN-29A|reaction.ecocyc.TRANS-RXN-29A]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.TRANS-RXN0-490|reaction.ecocyc.TRANS-RXN0-490]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.TRANS-RXN0-532|reaction.ecocyc.TRANS-RXN0-532]] `EcoCyc` `database` - EcoCyc reaction LEFT

## Incoming Edges (3)

- `transports` <-- [[complex.ecocyc.ABC-40-CPLX|complex.ecocyc.ABC-40-CPLX]] `EcoCyc` `database` - EcoCyc transporters.col equation
- `transports` <-- [[complex.ecocyc.CPLX0-7642|complex.ecocyc.CPLX0-7642]] `EcoCyc` `database` - EcoCyc transporters.col equation
- `transports` <-- [[complex.ecocyc.CPLX0-7963|complex.ecocyc.CPLX0-7963]] `EcoCyc` `database` - EcoCyc transporters.col equation

## External IDs

- `KEGG:C00719`

## Notes

Included because it appears in at least one E. coli KEGG pathway.
