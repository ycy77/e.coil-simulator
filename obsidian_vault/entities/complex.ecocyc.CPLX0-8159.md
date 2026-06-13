---
entity_id: "complex.ecocyc.CPLX0-8159"
entity_type: "complex"
name: "putrescine aminotransferase"
source_database: "EcoCyc"
source_id: "CPLX0-8159"
default_state: "active"
allowed_states: "active|impaired|disrupted|assembled|disassembled|inhibited"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/complex
  - source/EcoCyc
aliases:
---

# putrescine aminotransferase

`complex.ecocyc.CPLX0-8159`

## Static

- Type: `complex`
- Source: `EcoCyc:CPLX0-8159`
- Default state: `active`
- Allowed states: `active|impaired|disrupted|assembled|disassembled|inhibited`
- Complex type: `regulatory`
- Components: [[protein.P42588|protein.P42588]]

## Enriched Summary

Putrescine aminotransferase (PATase, PatA) catalyzes the first step in one of two pathways for putrescine degradation (PUTDEG-PWY), where putrescine is converted into 4-aminobutyrate via 4-aminobutyraldehyde . PatA also functions as a cadaverine aminotransferase during degradation of L-lysine . Crystal structures of the free and putrescine-bound enzyme have been solved. PATase is dimeric in solution and in the crystal structure and adopts a class III PLP-dependent aminotransferase fold . PATase is a natural N-end rule protein degradation substrate of ClpS . Endogenous PATase is post-translationally modified by the addition of the destabilizing amino acids Leu or Phe to the N terminus. The modification requires EG11112-MONOMER and is required for conversion to a ClpS substrate . Repression of clpS transcription by PhoP under low Mg2+ growth conditions results in increased levels of PatA . Expression of putrescine aminotransferase activity is most highly induced by putrescine and is under catabolite repression . Nitrogen limitation results in a 3- to 5-fold increase in patA levels . RNA polymerase containing σS or σ54 appear to compete for binding to the patA promoter . A mutant lacking both patA and either puuA, puuB or puuC can not utilize putrescine as the sole source of nitrogen . A patA mutant has very little remaining putrescine aminotransferase activity...

## Biological Role

Catalyzes DIAMTRANSAM-RXN (reaction.ecocyc.DIAMTRANSAM-RXN), PUTTRANSAM-RXN (reaction.ecocyc.PUTTRANSAM-RXN), RXN0-7317 (reaction.ecocyc.RXN0-7317). Bound by Pyridoxal phosphate (molecule.C00018).

## Annotation

Putrescine aminotransferase (PATase, PatA) catalyzes the first step in one of two pathways for putrescine degradation (PUTDEG-PWY), where putrescine is converted into 4-aminobutyrate via 4-aminobutyraldehyde . PatA also functions as a cadaverine aminotransferase during degradation of L-lysine . Crystal structures of the free and putrescine-bound enzyme have been solved. PATase is dimeric in solution and in the crystal structure and adopts a class III PLP-dependent aminotransferase fold . PATase is a natural N-end rule protein degradation substrate of ClpS . Endogenous PATase is post-translationally modified by the addition of the destabilizing amino acids Leu or Phe to the N terminus. The modification requires EG11112-MONOMER and is required for conversion to a ClpS substrate . Repression of clpS transcription by PhoP under low Mg2+ growth conditions results in increased levels of PatA . Expression of putrescine aminotransferase activity is most highly induced by putrescine and is under catabolite repression . Nitrogen limitation results in a 3- to 5-fold increase in patA levels . RNA polymerase containing σS or σ54 appear to compete for binding to the patA promoter . A mutant lacking both patA and either puuA, puuB or puuC can not utilize putrescine as the sole source of nitrogen . A patA mutant has very little remaining putrescine aminotransferase activity . In earlier work, a mutant lacking putrescine aminotransferase activity was mapped to 89 min on the E. coli chromosome ; it is thus unlikely that this mutation resided in the patA gene. PatA: "putrescine aminotransferase pathway"

## Outgoing Edges (3)

- `catalyzes` --> [[reaction.ecocyc.DIAMTRANSAM-RXN|reaction.ecocyc.DIAMTRANSAM-RXN]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` --> [[reaction.ecocyc.PUTTRANSAM-RXN|reaction.ecocyc.PUTTRANSAM-RXN]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` --> [[reaction.ecocyc.RXN0-7317|reaction.ecocyc.RXN0-7317]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (2)

- `binds` <-- [[molecule.C00018|molecule.C00018]] `EcoCyc` `database` - EcoCyc enzymatic reaction cofactor
- `is_component_of` <-- [[protein.P42588|protein.P42588]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2

## External IDs

- `EcoCyc:CPLX0-8159`
- `QSPROTEOME:QS00196543`

## Notes

2*protein.P42588
