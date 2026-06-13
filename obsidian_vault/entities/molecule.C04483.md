---
entity_id: "molecule.C04483"
entity_type: "small_molecule"
name: "Deoxycholic acid"
source_database: "KEGG"
source_id: "C04483"
default_state: "low"
allowed_states: "absent|low|medium|high"
subcellular_location: ""
enriched_summary_quality: "placeholder"
tags:
  - entity/small_molecule
  - source/KEGG
aliases:
  - "Deoxycholic acid"
  - "Deoxycholate"
  - "3alpha,12alpha-Dihydroxy-5beta-cholanate"
  - "3alpha,12alpha-Dihydroxy-5beta-cholanic acid"
---

# Deoxycholic acid

`molecule.C04483`

## Static

- Type: `small_molecule`
- Source: `KEGG:C04483`
- Default state: `low`
- Allowed states: `absent|low|medium|high`

## Enriched Summary

KEGG compound: Deoxycholic acid; Deoxycholate; 3alpha,12alpha-Dihydroxy-5beta-cholanate; 3alpha,12alpha-Dihydroxy-5beta-cholanic acid EcoCyc common name: deoxycholate. DEOXYCHOLATE Deoxycholate and CPD-7235 are secondary bile acids, derived from the primary bile acids by bacterial degradation in the gut. They are the most abundant bile acids in the healthy human gut, with mean concentrations of approximately 200 and 150 μM, respectively .

## Biological Role

Consumed as substrate in 5 reaction(s). Produced in 5 reaction(s).

## Enriched Pathways

- `eco00121` Secondary bile acid biosynthesis (KEGG)

## Annotation

KEGG compound: Deoxycholic acid; Deoxycholate; 3alpha,12alpha-Dihydroxy-5beta-cholanate; 3alpha,12alpha-Dihydroxy-5beta-cholanic acid

## Pathways

- `eco00121` Secondary bile acid biosynthesis (KEGG)

## Outgoing Edges (11)

- `is_product_of` --> [[reaction.ecocyc.TRANS-RXN-349|reaction.ecocyc.TRANS-RXN-349]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.TRANS-RXN-352|reaction.ecocyc.TRANS-RXN-352]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.TRANS-RXN-365|reaction.ecocyc.TRANS-RXN-365]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.TRANS-RXN0-589|reaction.ecocyc.TRANS-RXN0-589]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.TRANS-RXN0-590|reaction.ecocyc.TRANS-RXN0-590]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` --> [[reaction.ecocyc.TRANS-RXN-349|reaction.ecocyc.TRANS-RXN-349]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.TRANS-RXN-352|reaction.ecocyc.TRANS-RXN-352]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.TRANS-RXN-365|reaction.ecocyc.TRANS-RXN-365]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.TRANS-RXN0-589|reaction.ecocyc.TRANS-RXN0-589]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.TRANS-RXN0-590|reaction.ecocyc.TRANS-RXN0-590]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `represses` --> [[reaction.ecocyc.4OHBENZOATE-OCTAPRENYLTRANSFER-RXN|reaction.ecocyc.4OHBENZOATE-OCTAPRENYLTRANSFER-RXN]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity

## Incoming Edges (4)

- `transports` <-- [[complex.ecocyc.CPLX0-2141|complex.ecocyc.CPLX0-2141]] `EcoCyc` `database` - EcoCyc transporters.col equation
- `transports` <-- [[complex.ecocyc.CPLX0-2161|complex.ecocyc.CPLX0-2161]] `EcoCyc` `database` - EcoCyc transporters.col equation
- `transports` <-- [[protein.P25744|protein.P25744]] `EcoCyc` `database` - EcoCyc transporters.col equation
- `transports` <-- [[protein.P37340|protein.P37340]] `EcoCyc` `database` - EcoCyc transporters.col equation

## External IDs

- `KEGG:C04483`

## Notes

Included because it appears in at least one E. coli KEGG pathway.
