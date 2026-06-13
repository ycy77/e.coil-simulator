---
entity_id: "complex.ecocyc.F16B-CPLX"
entity_type: "complex"
name: "fructose-1,6-bisphosphatase 1"
source_database: "EcoCyc"
source_id: "F16B-CPLX"
default_state: "active"
allowed_states: "active|impaired|disrupted|assembled|disassembled|inhibited"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/complex
  - source/EcoCyc
aliases:
---

# fructose-1,6-bisphosphatase 1

`complex.ecocyc.F16B-CPLX`

## Static

- Type: `complex`
- Source: `EcoCyc:F16B-CPLX`
- Default state: `active`
- Allowed states: `active|impaired|disrupted|assembled|disassembled|inhibited`
- Complex type: `regulatory`
- Components: [[protein.P0A993|protein.P0A993]]

## Enriched Summary

Fructose-1,6-bisphosphatase catalyzes the conversion of fructose-1,6-bisphosphate to fructose-6-phosphate in the gluconeogenesis pathway. The enzyme is required for growth on glycerol, succinate and acetate as the carbon source, but not for growth on hexoses and pentoses . To avoid futile cycling with phosphofructokinases, the activity of fructose-1,6-bisphosphatase must be regulated. Like the mammalian enzymes, E. coli fructose-1,6-bisphosphatase is inhibited by fructose-2,6-bisphosphate; however, this compound is not present in vivo . AMP is a noncompetitive inhibitor of the enzyme. The low Ki of the enzyme for AMP suggests that under physiological conditions the enzyme would be inhibited to a great extent . A mutant enzyme that is insensitive to AMP inhibition has been isolated . Phosphoenolpyruvate (PEP) was initially reported to partially inhibit fructose-1,6-bisphosphatase activity at high concentrations, but was able to block inhibition by AMP . A later report showed that PEP at low concentrations (2 mM) activates the enzyme; PEP may thus be the physiological regulator under gluconeogenic growth conditions . Under nondenaturing conditions, the enzyme is present in several aggregated forms in which the tetramer seems to predominate at low enzyme concentrations . A crystal structure of this enzyme has been solved at 1.45 Å resolution...

## Biological Role

Catalyzes F16BDEPHOS-RXN (reaction.ecocyc.F16BDEPHOS-RXN). Bound by Magnesium cation (molecule.C00305).

## Annotation

Fructose-1,6-bisphosphatase catalyzes the conversion of fructose-1,6-bisphosphate to fructose-6-phosphate in the gluconeogenesis pathway. The enzyme is required for growth on glycerol, succinate and acetate as the carbon source, but not for growth on hexoses and pentoses . To avoid futile cycling with phosphofructokinases, the activity of fructose-1,6-bisphosphatase must be regulated. Like the mammalian enzymes, E. coli fructose-1,6-bisphosphatase is inhibited by fructose-2,6-bisphosphate; however, this compound is not present in vivo . AMP is a noncompetitive inhibitor of the enzyme. The low Ki of the enzyme for AMP suggests that under physiological conditions the enzyme would be inhibited to a great extent . A mutant enzyme that is insensitive to AMP inhibition has been isolated . Phosphoenolpyruvate (PEP) was initially reported to partially inhibit fructose-1,6-bisphosphatase activity at high concentrations, but was able to block inhibition by AMP . A later report showed that PEP at low concentrations (2 mM) activates the enzyme; PEP may thus be the physiological regulator under gluconeogenic growth conditions . Under nondenaturing conditions, the enzyme is present in several aggregated forms in which the tetramer seems to predominate at low enzyme concentrations . A crystal structure of this enzyme has been solved at 1.45 Å resolution . Crystal structures have also been solved with several bound ligands at 2.05 Å resolution and 2.18 Å resolution . In addition to PEP, citrate is also an activator. Tetramers with bound PEP or citrate are in the active allosteric R state conformation. PEP, citrate, 3-phosphoglycerate, cis-aconitate, isocitrate, oxaloacetate, and α-ketoglutarate are activators at concentrations of up to 5 mM, although PEP is the most potent activator. L

## Outgoing Edges (1)

- `catalyzes` --> [[reaction.ecocyc.F16BDEPHOS-RXN|reaction.ecocyc.F16BDEPHOS-RXN]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (2)

- `binds` <-- [[molecule.C00305|molecule.C00305]] `EcoCyc` `database` - EcoCyc enzymatic reaction cofactor
- `is_component_of` <-- [[protein.P0A993|protein.P0A993]] `EcoCyc` `database` - EcoCyc component coefficient=4 | EcoCyc protcplxs.col coefficient=4

## External IDs

- `EcoCyc:F16B-CPLX`
- `QSPROTEOME:QS00183135`

## Notes

4*protein.P0A993
