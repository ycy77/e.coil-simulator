---
entity_id: "protein.P77374"
entity_type: "protein"
name: "ynfE"
source_database: "UniProt"
source_id: "P77374"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cell membrane {ECO:0000250}; Peripheral membrane protein {ECO:0000250}; Cytoplasmic side {ECO:0000250}."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "ynfE b1587 JW1579"
---

# ynfE

`protein.P77374`

## Static

- Type: `protein`
- Source: `UniProt:P77374`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cell membrane {ECO:0000250}; Peripheral membrane protein {ECO:0000250}; Cytoplasmic side {ECO:0000250}.

## Enriched Summary

FUNCTION: Terminal reductase during anaerobic growth on various sulfoxide and N-oxide compounds. {ECO:0000250}. YnfE has been implicated as a Tat-dependent selenate reductase enzyme in E. coli. A ynfEF double null mutant is unable to reduce selenate to elemental selenium . The disruption is specific to the initial selenate reduction process since selenium production is restored when selenite is added to the growth medium . Production of either YnfE or YnfF from a plasmid restored the ability of the E. coli ynfEF double mutant to reduce selenate to selenium in vivo . YnfE is highly similar to DmsA, the catalytic subunit of the dimethyl sulfoxide reductase heterotrimer, and cross-reacts with an anti-DmsA antibody. The protein is poorly expressed. In a plasmid expression system, expression of YnfE appears to inhibit expression of YnfFGH . In a ΔtusA strain, expression of ynfE is decreased in mid-exponential phase and under aerobic conditions .

## Biological Role

Component of selenate reductase (complex.ecocyc.CPLX0-1601).

## Enriched Pathways

- `eco00450` Selenocompound metabolism (KEGG)

## Annotation

FUNCTION: Terminal reductase during anaerobic growth on various sulfoxide and N-oxide compounds. {ECO:0000250}.

## Pathways

- `eco00450` Selenocompound metabolism (KEGG)

## Outgoing Edges (1)

- `is_component_of` --> [[complex.ecocyc.CPLX0-1601|complex.ecocyc.CPLX0-1601]] `EcoCyc` `database` - EcoCyc component coefficient=1 | EcoCyc protcplxs.col coefficient=1

## Incoming Edges (1)

- `encodes` <-- [[gene.b1587|gene.b1587]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P77374`
- `KEGG:ecj:JW1579;eco:b1587;ecoc:C3026_09145;`
- `GeneID:946135;`
- `GO:GO:0005886; GO:0009055; GO:0009061; GO:0009389; GO:0030151; GO:0030288; GO:0033797; GO:0043546; GO:0051539`
- `EC:1.8.99.-`

## Notes

Putative dimethyl sulfoxide reductase chain YnfE (DMSO reductase) (EC 1.8.99.-)
