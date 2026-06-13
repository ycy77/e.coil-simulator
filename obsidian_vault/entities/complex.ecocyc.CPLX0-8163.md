---
entity_id: "complex.ecocyc.CPLX0-8163"
entity_type: "complex"
name: "molybdopterin adenylyltransferase"
source_database: "EcoCyc"
source_id: "CPLX0-8163"
default_state: "active"
allowed_states: "active|impaired|disrupted|assembled|disassembled|inhibited"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/complex
  - source/EcoCyc
aliases:
---

# molybdopterin adenylyltransferase

`complex.ecocyc.CPLX0-8163`

## Static

- Type: `complex`
- Source: `EcoCyc:CPLX0-8163`
- Default state: `active`
- Allowed states: `active|impaired|disrupted|assembled|disassembled|inhibited`
- Complex type: `structural`
- Components: [[protein.P0AF03|protein.P0AF03]]

## Enriched Summary

Molybdenum and tungsten cofactors of all enzymes (except nitrogenase) that require one or the other for activity are present in an oxidized state as molybdate or tungstate ions that are chelated by the cis-dithiolene moiety of a molybdenum cofactor. The cofactor that predominates in E. coli is molybdopterin guanine dinucleotide. Although much progress has been made in elucidating the biosynthetic pathways for molybdenum cofactors (see the review), some details remain to be determined. In the last step molybdenum is inserted to become chelated by the cis-dithiolene moiety of molybdopterin and a guanyl group is added yielding molybdopterin guanine dinucleotide, the active cofactor of E. coli. MogA, along with MoeA, is implicated in the step involving the chelation of molybdenum. Crystal structures of MogA have been solved at 1.6 Å and 1.45 Å resolution, and a putative active site has been identified. In two crystal forms studied the MogA monomers formed a trimeric arrangement. Analytical ultracentrifugation data showed a native molecular mass of 59,675 Da, consistent with a trimeric structure in solution . Studies using a bacterial two-hybrid system showed that MogA directly interacts with MoeA and MobB in vivo . In the presence of the enzyme-specific chaperone NarJ and the mature molybdenum cofactor, MobA, MobB, MoeA and MogA interact with apo-NarG . In E...

## Biological Role

Catalyzes RXN-8344 (reaction.ecocyc.RXN-8344). Bound by Magnesium cation (molecule.C00305).

## Annotation

Molybdenum and tungsten cofactors of all enzymes (except nitrogenase) that require one or the other for activity are present in an oxidized state as molybdate or tungstate ions that are chelated by the cis-dithiolene moiety of a molybdenum cofactor. The cofactor that predominates in E. coli is molybdopterin guanine dinucleotide. Although much progress has been made in elucidating the biosynthetic pathways for molybdenum cofactors (see the review), some details remain to be determined. In the last step molybdenum is inserted to become chelated by the cis-dithiolene moiety of molybdopterin and a guanyl group is added yielding molybdopterin guanine dinucleotide, the active cofactor of E. coli. MogA, along with MoeA, is implicated in the step involving the chelation of molybdenum. Crystal structures of MogA have been solved at 1.6 Å and 1.45 Å resolution, and a putative active site has been identified. In two crystal forms studied the MogA monomers formed a trimeric arrangement. Analytical ultracentrifugation data showed a native molecular mass of 59,675 Da, consistent with a trimeric structure in solution . Studies using a bacterial two-hybrid system showed that MogA directly interacts with MoeA and MobB in vivo . In the presence of the enzyme-specific chaperone NarJ and the mature molybdenum cofactor, MobA, MobB, MoeA and MogA interact with apo-NarG . In E. coli K-12, mog (mogA), moaA, moaB, moaE, modB, or modC deletion mutants lose the ability to reduce CPD-4544 (tellurate), which can be restored by complementation. Although the E. coli tellurate reductase gene and its product remain uncharacterized, these data suggest that it involves a molybdoenzyme . Data suggest that in the presence of physiological concentrations of molybdate, both MogA and MoeA are required to form

## Outgoing Edges (1)

- `catalyzes` --> [[reaction.ecocyc.RXN-8344|reaction.ecocyc.RXN-8344]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (2)

- `binds` <-- [[molecule.C00305|molecule.C00305]] `EcoCyc` `database` - EcoCyc enzymatic reaction cofactor
- `is_component_of` <-- [[protein.P0AF03|protein.P0AF03]] `EcoCyc` `database` - EcoCyc component coefficient=3 | EcoCyc protcplxs.col coefficient=3

## External IDs

- `EcoCyc:CPLX0-8163`
- `QSPROTEOME:QS00196473`

## Notes

3*protein.P0AF03
