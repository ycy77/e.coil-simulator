---
entity_id: "molecule.C00194"
entity_type: "small_molecule"
name: "Cobamide coenzyme"
source_database: "KEGG"
source_id: "C00194"
default_state: "low"
allowed_states: "absent|low|medium|high"
subcellular_location: ""
enriched_summary_quality: "placeholder"
tags:
  - entity/small_molecule
  - source/KEGG
aliases:
  - "Cobamide coenzyme"
  - "Adenosylcobalamin"
  - "Adenosylcob(III)alamin"
  - "Deoxyadenosylcobalamin"
  - "Cobamamide"
  - "Vitamin B12 coenzyme"
  - "5,6-Dimethylbenzimidazolyl-5-deoxyadenosyl-cobamide"
  - "(5'-Deoxy-5'-adenosyl)cobamide coenzyme"
  - "(5,6-Dimethylbenzimidazolyl)cobamide coenzyme"
  - "alpha-(5,6-Dimethylbenzimidazolyl)cobamide coenzyme"
  - "5'-Deoxy-5'-adenosylcobalamin"
  - "5'-Deoxy-5'-adenosyl vitamin B12"
  - "5'-Deoxy-5'-adenosyl-5,6-dimethylbenzimidazolylcobamide"
  - "5,6-Dimethylbenzimidazolyl-Co-5'-deoxy-5'-adenosylcobamide"
  - "Calomide"
  - "Cobalamin coenzyme"
  - "Coenzyme B12"
  - "DMBC coenzyme"
  - "Dibencozide"
  - "Funacomide"
---

# Cobamide coenzyme

`molecule.C00194`

## Static

- Type: `small_molecule`
- Source: `KEGG:C00194`
- Default state: `low`
- Allowed states: `absent|low|medium|high`

## Enriched Summary

KEGG compound: Cobamide coenzyme; Adenosylcobalamin; Adenosylcob(III)alamin; Deoxyadenosylcobalamin; Cobamamide; Vitamin B12 coenzyme; 5,6-Dimethylbenzimidazolyl-5-deoxyadenosyl-cobamide; (5'-Deoxy-5'-adenosyl)cobamide coenzyme; (5,6-Dimethylbenzimidazolyl)cobamide coenzyme; alpha-(5,6-Dimethylbenzimidazolyl)cobamide coenzyme; 5'-Deoxy-5'-adenosylcobalamin; 5'-Deoxy-5'-adenosyl vitamin B12; 5'-Deoxy-5'-adenosyl-5,6-dimethylbenzimidazolylcobamide; 5,6-Dimethylbenzimidazolyl-Co-5'-deoxy-5'-adenosylcobamide; Calomide; Cobalamin coenzyme; Coenzyme B12; DMBC coenzyme; Dibencozide; Funacomide EcoCyc common name: adenosylcobalamin.

## Biological Role

Consumed as substrate in 2 reaction(s). Produced in 4 reaction(s). Binds methylmalonyl-CoA mutase (complex.ecocyc.CPLX0-7741), ethanolamine ammonia-lyase (complex.ecocyc.ETHAMLY-CPLX).

## Enriched Pathways

- `eco00860` Porphyrin metabolism (KEGG)
- `eco04980` Cobalamin transport and metabolism (KEGG)

## Annotation

KEGG compound: Cobamide coenzyme; Adenosylcobalamin; Adenosylcob(III)alamin; Deoxyadenosylcobalamin; Cobamamide; Vitamin B12 coenzyme; 5,6-Dimethylbenzimidazolyl-5-deoxyadenosyl-cobamide; (5'-Deoxy-5'-adenosyl)cobamide coenzyme; (5,6-Dimethylbenzimidazolyl)cobamide coenzyme; alpha-(5,6-Dimethylbenzimidazolyl)cobamide coenzyme; 5'-Deoxy-5'-adenosylcobalamin; 5'-Deoxy-5'-adenosyl vitamin B12; 5'-Deoxy-5'-adenosyl-5,6-dimethylbenzimidazolylcobamide; 5,6-Dimethylbenzimidazolyl-Co-5'-deoxy-5'-adenosylcobamide; Calomide; Cobalamin coenzyme; Coenzyme B12; DMBC coenzyme; Dibencozide; Funacomide

## Pathways

- `eco00860` Porphyrin metabolism (KEGG)
- `eco04980` Cobalamin transport and metabolism (KEGG)

## Outgoing Edges (8)

- `binds` --> [[complex.ecocyc.CPLX0-7741|complex.ecocyc.CPLX0-7741]] `EcoCyc` `database` - EcoCyc enzymatic reaction cofactor
- `binds` --> [[complex.ecocyc.ETHAMLY-CPLX|complex.ecocyc.ETHAMLY-CPLX]] `EcoCyc` `database` - EcoCyc enzymatic reaction cofactor
- `is_product_of` --> [[reaction.R12183|reaction.R12183]] `KEGG` `database` - 2 C00002 + 2 C00541 + C03024 <=> 2 C00536 + 2 C00194 + C03161
- `is_product_of` --> [[reaction.ecocyc.RXN-19366|reaction.ecocyc.RXN-19366]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.RXN-8770|reaction.ecocyc.RXN-8770]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.TRANS-RXN-1592|reaction.ecocyc.TRANS-RXN-1592]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` --> [[reaction.R05223|reaction.R05223]] `KEGG` `database` - C00194 + C00144 <=> C06510 + C05775
- `is_substrate_of` --> [[reaction.ecocyc.TRANS-RXN-1592|reaction.ecocyc.TRANS-RXN-1592]] `EcoCyc` `database` - EcoCyc reaction LEFT

## Incoming Edges (1)

- `transports` <-- [[complex.ecocyc.CPLX0-1924|complex.ecocyc.CPLX0-1924]] `EcoCyc` `database` - EcoCyc transporters.col equation

## External IDs

- `KEGG:C00194`

## Notes

Included because it appears in at least one E. coli KEGG pathway.
