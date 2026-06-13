---
entity_id: "complex.ecocyc.ATPA-CPLX"
entity_type: "complex"
name: "ATP synthase F1 complex subunit α"
source_database: "EcoCyc"
source_id: "ATPA-CPLX"
default_state: "active"
allowed_states: "active|impaired|disrupted|assembled|disassembled|inhibited"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/complex
  - source/EcoCyc
aliases:
  - "ATP synthase F<sub>1</sub> complex - alpha subunit"
---

# ATP synthase F1 complex subunit α

`complex.ecocyc.ATPA-CPLX`

## Static

- Type: `complex`
- Source: `EcoCyc:ATPA-CPLX`
- Default state: `active`
- Allowed states: `active|impaired|disrupted|assembled|disassembled|inhibited`
- Complex type: `regulatory`
- Components: [[protein.P0ABB0|protein.P0ABB0]]

## Enriched Summary

The α-subunit plays an essential role in the catalytic mechanism of the enzyme and in the binding and coupling between the F1 and Fo complexes. The α-subunit also contains an adenine-specific binding site which is noncatalytic, nonregulatory and not essential for enzyme assembly in vitro. Its function has not yet been determined. The α-subunit complex is a homotrimer . A hydrogen-bonding network is formed at the closed α/β-subunit interface of F1 . Elimination of this network results in a severely impaired enzyme. A possible role for the hydrogen-bonding network in coupling of ATP synthesis/hydrolysis and rotation has been proposed . The role of conserved residues surrounding the catalytic site has been studied . ΔatpA cells have a dissimilar growth profile to wild type in nutrient rich media but no difference is observed in nutrient-poor media; ΔatpA cells may upregulate respiration and glycolysis to compensate for the reduced efficiency of ATP synthase The α-subunit plays an essential role in the catalytic mechanism of the enzyme and in the binding and coupling between the F1 and Fo complexes. The α-subunit also contains an adenine-specific binding site which is noncatalytic, nonregulatory and not essential for enzyme assembly in vitro. Its function has not yet been determined. The α-subunit complex is a homotrimer...

## Biological Role

Component of ATP synthase F1 complex (complex.ecocyc.F-1-CPLX).

## Annotation

The α-subunit plays an essential role in the catalytic mechanism of the enzyme and in the binding and coupling between the F1 and Fo complexes. The α-subunit also contains an adenine-specific binding site which is noncatalytic, nonregulatory and not essential for enzyme assembly in vitro. Its function has not yet been determined. The α-subunit complex is a homotrimer . A hydrogen-bonding network is formed at the closed α/β-subunit interface of F1 . Elimination of this network results in a severely impaired enzyme. A possible role for the hydrogen-bonding network in coupling of ATP synthesis/hydrolysis and rotation has been proposed . The role of conserved residues surrounding the catalytic site has been studied . ΔatpA cells have a dissimilar growth profile to wild type in nutrient rich media but no difference is observed in nutrient-poor media; ΔatpA cells may upregulate respiration and glycolysis to compensate for the reduced efficiency of ATP synthase

## Outgoing Edges (1)

- `is_component_of` --> [[complex.ecocyc.F-1-CPLX|complex.ecocyc.F-1-CPLX]] `EcoCyc` `database` - EcoCyc component coefficient=1

## Incoming Edges (1)

- `is_component_of` <-- [[protein.P0ABB0|protein.P0ABB0]] `EcoCyc` `database` - EcoCyc component coefficient=3 | EcoCyc protcplxs.col coefficient=3

## External IDs

- `EcoCyc:ATPA-CPLX`
- `QSPROTEOME:QS00049351`

## Notes

3*protein.P0ABB0
