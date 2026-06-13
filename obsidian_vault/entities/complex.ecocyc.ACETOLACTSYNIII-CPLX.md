---
entity_id: "complex.ecocyc.ACETOLACTSYNIII-CPLX"
entity_type: "complex"
name: "acetolactate synthase / acetohydroxybutanoate synthase"
source_database: "EcoCyc"
source_id: "ACETOLACTSYNIII-CPLX"
default_state: "active"
allowed_states: "active|impaired|disrupted|assembled|disassembled|inhibited"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/complex
  - source/EcoCyc
aliases:
  - "acetolactate synthase III"
  - "acetohydroxy acid synthase III"
  - "AHAS III"
  - "acetohydroxybutanoate synthase III"
---

# acetolactate synthase / acetohydroxybutanoate synthase

`complex.ecocyc.ACETOLACTSYNIII-CPLX`

## Static

- Type: `complex`
- Source: `EcoCyc:ACETOLACTSYNIII-CPLX`
- Default state: `active`
- Allowed states: `active|impaired|disrupted|assembled|disassembled|inhibited`
- Complex type: `structural`
- Components: [[protein.P00893|protein.P00893]], [[protein.P00894|protein.P00894]]

## Enriched Summary

Acetohydroxy acid synthase III (AHAS III) is one of two functional isozymes catalyzing the decarboxylation of pyruvate and transfer of the resulting acetaldehyde group to either pyruvate or α-ketobutyrate, producing α-acetolactate for the valine pathway and α-aceto-α-hydroxybutyrate for the isoleucine pathway. This is the first common step in the biosynthesis of the branched-chain amino acids isoleucine, leucine, and valine. A third isozyme, AHAS II, is not functional in E. coli K-12 due to the presence of a frame shift mutation in the gene encoding the large subunit, ilvG. In the presence of both pyruvate and α-ketobutyrate, AHAS III produces approximately 40-fold more acetohydroxybutyrate than acetolactate, while AHAS I shows no product preference . The differential regulation of enzymatic activity and expression of the isozymes has direct physiological consequences and has been under intense study. The end products of the branched-chain amino acid biosynthesis pathways all inhibit AHAS III activity, although inhibition by valine is most significant . Both AHAS I and III are inhibited by valine . Activity of AHAS III is only partially inhibited by leucine, while AHAS I activity can be almost completely inhibited . Interactions between the large and small subunits of the three AHAS isozymes have been studied...

## Biological Role

Catalyzes ACETOLACTSYN-RXN (reaction.ecocyc.ACETOLACTSYN-RXN), 2-aceto-2-hydroxy-butyrate synthase (reaction.ecocyc.ACETOOHBUTSYN-RXN). Bound by FAD (molecule.C00016), Thiamin diphosphate (molecule.C00068), Magnesium cation (molecule.C00305).

## Annotation

Acetohydroxy acid synthase III (AHAS III) is one of two functional isozymes catalyzing the decarboxylation of pyruvate and transfer of the resulting acetaldehyde group to either pyruvate or α-ketobutyrate, producing α-acetolactate for the valine pathway and α-aceto-α-hydroxybutyrate for the isoleucine pathway. This is the first common step in the biosynthesis of the branched-chain amino acids isoleucine, leucine, and valine. A third isozyme, AHAS II, is not functional in E. coli K-12 due to the presence of a frame shift mutation in the gene encoding the large subunit, ilvG. In the presence of both pyruvate and α-ketobutyrate, AHAS III produces approximately 40-fold more acetohydroxybutyrate than acetolactate, while AHAS I shows no product preference . The differential regulation of enzymatic activity and expression of the isozymes has direct physiological consequences and has been under intense study. The end products of the branched-chain amino acid biosynthesis pathways all inhibit AHAS III activity, although inhibition by valine is most significant . Both AHAS I and III are inhibited by valine . Activity of AHAS III is only partially inhibited by leucine, while AHAS I activity can be almost completely inhibited . Interactions between the large and small subunits of the three AHAS isozymes have been studied . Review:

## Outgoing Edges (2)

- `catalyzes` --> [[reaction.ecocyc.ACETOLACTSYN-RXN|reaction.ecocyc.ACETOLACTSYN-RXN]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` --> [[reaction.ecocyc.ACETOOHBUTSYN-RXN|reaction.ecocyc.ACETOOHBUTSYN-RXN]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (5)

- `binds` <-- [[molecule.C00016|molecule.C00016]] `EcoCyc` `database` - EcoCyc enzymatic reaction cofactor
- `binds` <-- [[molecule.C00068|molecule.C00068]] `EcoCyc` `database` - EcoCyc enzymatic reaction cofactor
- `binds` <-- [[molecule.C00305|molecule.C00305]] `EcoCyc` `database` - EcoCyc enzymatic reaction cofactor
- `is_component_of` <-- [[protein.P00893|protein.P00893]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2
- `is_component_of` <-- [[protein.P00894|protein.P00894]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2

## External IDs

- `EcoCyc:ACETOLACTSYNIII-CPLX`
- `QSPROTEOME:QS00049344`

## Notes

2*protein.P00893|2*protein.P00894
