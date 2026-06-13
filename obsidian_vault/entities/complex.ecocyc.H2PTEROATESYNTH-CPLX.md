---
entity_id: "complex.ecocyc.H2PTEROATESYNTH-CPLX"
entity_type: "complex"
name: "dihydropteroate synthase"
source_database: "EcoCyc"
source_id: "H2PTEROATESYNTH-CPLX"
default_state: "active"
allowed_states: "active|impaired|disrupted|assembled|disassembled|inhibited"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/complex
  - source/EcoCyc
aliases:
---

# dihydropteroate synthase

`complex.ecocyc.H2PTEROATESYNTH-CPLX`

## Static

- Type: `complex`
- Source: `EcoCyc:H2PTEROATESYNTH-CPLX`
- Default state: `active`
- Allowed states: `active|impaired|disrupted|assembled|disassembled|inhibited`
- Complex type: `structural`
- Components: [[protein.P0AC13|protein.P0AC13]]

## Enriched Summary

Dihydropteroate synthase catalyzes the condensation of 4-aminobenzoate (p-aminobenzoate) with 6-hydroxymethyl-dihydropterin diphosphate. This reaction forms a C-N bond that joins the pterin ring moiety of 6-hydroxymethyl-dihydropterin diphosphate to 4-aminobenzoate to produce 7,8-dihydropteroate (dihydropteroate) . Dihydropteroate is an intermediary metabolite that is subsequently converted to tetrahydrofolate (tetrahydrofolic acid), which is essential for the syntheses of purines, thymidylate, glycine, methionine, pantothenic acid, and N-formyl-L-methionyl-tRNAfmet. Sulfonamide derivatives (sulfa drugs) are structural analogs of 4-aminobenzoate that compete with this substrate for the enzyme. Several mechanisms of sulfonamide resistance can develop, including mutations in folP . The soluble, native enzyme was purified and characterized and the folP gene was cloned and expressed . The crystal structure of this enzyme has been determined at 2.0 Å resolution . Review: Dihydropteroate synthase catalyzes the condensation of 4-aminobenzoate (p-aminobenzoate) with 6-hydroxymethyl-dihydropterin diphosphate. This reaction forms a C-N bond that joins the pterin ring moiety of 6-hydroxymethyl-dihydropterin diphosphate to 4-aminobenzoate to produce 7,8-dihydropteroate (dihydropteroate)...

## Biological Role

Catalyzes H2PTEROATESYNTH-RXN (reaction.ecocyc.H2PTEROATESYNTH-RXN). Bound by Magnesium cation (molecule.C00305).

## Annotation

Dihydropteroate synthase catalyzes the condensation of 4-aminobenzoate (p-aminobenzoate) with 6-hydroxymethyl-dihydropterin diphosphate. This reaction forms a C-N bond that joins the pterin ring moiety of 6-hydroxymethyl-dihydropterin diphosphate to 4-aminobenzoate to produce 7,8-dihydropteroate (dihydropteroate) . Dihydropteroate is an intermediary metabolite that is subsequently converted to tetrahydrofolate (tetrahydrofolic acid), which is essential for the syntheses of purines, thymidylate, glycine, methionine, pantothenic acid, and N-formyl-L-methionyl-tRNAfmet. Sulfonamide derivatives (sulfa drugs) are structural analogs of 4-aminobenzoate that compete with this substrate for the enzyme. Several mechanisms of sulfonamide resistance can develop, including mutations in folP . The soluble, native enzyme was purified and characterized and the folP gene was cloned and expressed . The crystal structure of this enzyme has been determined at 2.0 Å resolution . Review:

## Outgoing Edges (1)

- `catalyzes` --> [[reaction.ecocyc.H2PTEROATESYNTH-RXN|reaction.ecocyc.H2PTEROATESYNTH-RXN]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (2)

- `binds` <-- [[molecule.C00305|molecule.C00305]] `EcoCyc` `database` - EcoCyc enzymatic reaction cofactor
- `is_component_of` <-- [[protein.P0AC13|protein.P0AC13]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2

## External IDs

- `EcoCyc:H2PTEROATESYNTH-CPLX`
- `QSPROTEOME:QS00196209`

## Notes

2*protein.P0AC13
