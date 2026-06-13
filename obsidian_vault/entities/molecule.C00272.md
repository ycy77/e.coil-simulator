---
entity_id: "molecule.C00272"
entity_type: "small_molecule"
name: "Tetrahydrobiopterin"
source_database: "KEGG"
source_id: "C00272"
default_state: "low"
allowed_states: "absent|low|medium|high"
subcellular_location: ""
enriched_summary_quality: "placeholder"
tags:
  - entity/small_molecule
  - source/KEGG
aliases:
  - "Tetrahydrobiopterin"
  - "5,6,7,8-Tetrahydrobiopterin"
  - "2-Amino-6-(1,2-dihydroxypropyl)-5,6,7,8-tetrahydoro-4(1H)-pteridinone"
  - "L-erythro-Tetrahydrobiopterin"
---

# Tetrahydrobiopterin

`molecule.C00272`

## Static

- Type: `small_molecule`
- Source: `KEGG:C00272`
- Default state: `low`
- Allowed states: `absent|low|medium|high`

## Enriched Summary

KEGG compound: Tetrahydrobiopterin; 5,6,7,8-Tetrahydrobiopterin; 2-Amino-6-(1,2-dihydroxypropyl)-5,6,7,8-tetrahydoro-4(1H)-pteridinone; L-erythro-Tetrahydrobiopterin EcoCyc common name: 5,6,7,8-tetrahydrobiopterin. CPD-14053 serves as an electron donor for several enzymes, including the aromatic amino acid hydroxylases EC-1.14.16.4, EC-1.14.16.2, and EC-1.14.16.1 (which are essential for the formation of the neurotransmitters DOPAMINE, NOREPINEPHRINE, L-EPINEPHRINE and SEROTONIN - see PWY66-301), and the enzyme EC-1.14.16.5. It also serves as a cofactor for all three forms of mammalian EC-1.14.13.39 (NOS) - CPLX-6585, CPLX-6581, and CPLX-6582 (see PWY-4983). In addition, TETRA-H-BIOPTERIN has been proposed to be involved in proliferation of murine erythrocyte cells , promotion of neurotransmitter release in the brain and regulation of human melanogenesis . Deffciency causes severe neurological disorders characterized by hyperphenylalaninaemia and monoamine neurotransmitter deffciency, and is also implicated in Parkinson's disease, Alzheimer's disease and depression (. TETRA-H-BIOPTERIN Tetrahydrobiopterin is present in probably every cell or tissue of higher animals . On the other hand, most bacteria, fungi and plants do not synthesize tetrahydrobiopterin...

## Biological Role

Consumed as substrate in 1 reaction(s).

## Enriched Pathways

- `eco00790` Folate biosynthesis (KEGG)

## Annotation

KEGG compound: Tetrahydrobiopterin; 5,6,7,8-Tetrahydrobiopterin; 2-Amino-6-(1,2-dihydroxypropyl)-5,6,7,8-tetrahydoro-4(1H)-pteridinone; L-erythro-Tetrahydrobiopterin

## Pathways

- `eco00790` Folate biosynthesis (KEGG)

## Outgoing Edges (2)

- `is_substrate_of` --> [[reaction.ecocyc.1.5.1.34-RXN|reaction.ecocyc.1.5.1.34-RXN]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `represses` --> [[reaction.ecocyc.GTP-CYCLOHYDRO-I-RXN|reaction.ecocyc.GTP-CYCLOHYDRO-I-RXN]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity

## Incoming Edges (0)

_None._

## External IDs

- `KEGG:C00272`

## Notes

Included because it appears in at least one E. coli KEGG pathway.
