---
entity_id: "molecule.C00748"
entity_type: "small_molecule"
name: "Siroheme"
source_database: "KEGG"
source_id: "C00748"
default_state: "low"
allowed_states: "absent|low|medium|high"
subcellular_location: ""
enriched_summary_quality: "placeholder"
tags:
  - entity/small_molecule
  - source/KEGG
aliases:
  - "Siroheme"
---

# Siroheme

`molecule.C00748`

## Static

- Type: `small_molecule`
- Source: `KEGG:C00748`
- Default state: `low`
- Allowed states: `absent|low|medium|high`

## Enriched Summary

KEGG compound: Siroheme SIROHEME Siroheme is an iron-containing isobacteriochlorin, a modified tetrapyrrole similar in structure to both heme and chlorophyll that was discovered in 1973 . Siroheme is covalently coupled to an iron-sulfur cluster ([FeS]) to form an electronically integrated metallo-cofactor for delivering electrons to substrate. Siroheme is found as a prosthetic group of several enzymes, including sulfite and nitrite reductases, which catalyze the six-electron reductions of sulfite to sulfide and nitrite to ammonia, respectively. Assimilatory sulfite reductases (see TAX-83333 SULFITE-REDUCT-ENZRXN) are found in bacteria, fungi and plants but not in animals, while dissimilatory sulfite reductases are found in diverse sulfate-reducing eubacteria (see TAX-879 CPLX-266) and some species of thermophilic archaebacteria (see TAX-2234 CPLX-7178) . Siroheme is also an intermediate in the biosynthesis of CPD-17059 in denitrifying bacteria, and in an alternative Heme-b biosynthesis pathway found in many archaea and sulfate reducing bacteria .

## Biological Role

Consumed as substrate in 1 reaction(s). Produced in 1 reaction(s). Binds nitrite reductase - NADH dependent (complex.ecocyc.NITRITREDUCT-CPLX), assimilatory sulfite reductase (NADPH) (complex.ecocyc.SULFITE-REDUCT-CPLX).

## Enriched Pathways

- `eco00860` Porphyrin metabolism (KEGG)

## Annotation

KEGG compound: Siroheme

## Pathways

- `eco00860` Porphyrin metabolism (KEGG)

## Outgoing Edges (4)

- `binds` --> [[complex.ecocyc.NITRITREDUCT-CPLX|complex.ecocyc.NITRITREDUCT-CPLX]] `EcoCyc` `database` - EcoCyc enzymatic reaction cofactor
- `binds` --> [[complex.ecocyc.SULFITE-REDUCT-CPLX|complex.ecocyc.SULFITE-REDUCT-CPLX]] `EcoCyc` `database` - EcoCyc enzymatic reaction cofactor
- `is_product_of` --> [[reaction.ecocyc.SIROHEME-FERROCHELAT-RXN|reaction.ecocyc.SIROHEME-FERROCHELAT-RXN]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` --> [[reaction.R02864|reaction.R02864]] `KEGG` `database` - C00748 + 2 C00080 <=> C14818 + C05778

## Incoming Edges (0)

_None._

## External IDs

- `KEGG:C00748`

## Notes

Included because it appears in at least one E. coli KEGG pathway.
