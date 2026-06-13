---
entity_id: "complex.ecocyc.ACETOLACTSYNI-CPLX"
entity_type: "complex"
name: "acetohydroxybutanoate synthase / acetolactate synthase"
source_database: "EcoCyc"
source_id: "ACETOLACTSYNI-CPLX"
default_state: "active"
allowed_states: "active|impaired|disrupted|assembled|disassembled|inhibited"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/complex
  - source/EcoCyc
aliases:
  - "acetohydroxybutanoate synthase I"
  - "acetohydroxy-acid synthase I"
  - "acetolactate synthase I"
  - "AHASI"
---

# acetohydroxybutanoate synthase / acetolactate synthase

`complex.ecocyc.ACETOLACTSYNI-CPLX`

## Static

- Type: `complex`
- Source: `EcoCyc:ACETOLACTSYNI-CPLX`
- Default state: `active`
- Allowed states: `active|impaired|disrupted|assembled|disassembled|inhibited`
- Complex type: `structural`
- Components: [[protein.P08142|protein.P08142]], [[protein.P0ADF8|protein.P0ADF8]]

## Enriched Summary

The bifunctional acetohydroxybutanoate synthase/acetolactate synthase (AHAS I, IlvBN) carries out both the first step in valine biosynthesis and the second step in isoleucine biosynthesis. AHAS I catalyzes the conversion of pyruvate and oxobutanoate into 2-aceto-2-hydroxy-butyrate and the conversion of pyruvate into 2-acetolactate. Both reactions generate carbon dioxide as a product . This enzyme has a wide substrate range in vitro . This bifunctional enzyme is a tetramer comprising two IlvB subunits and two IlvN subunits. Its apparent molecular weight rises above the expected weight for this configuration when pyruvate is added in vitro . The IlvB large subunit can catalyze the reaction in isolation and is not inhibited by valine in the manner of the holoenzyme. However, the Vmax for the reaction as catalyzed by only IlvB is sharply reduced, as is the enzyme's affinity for the required FAD cofactor . Both activities are catalyzed by the same active site on IlvB . The enzyme works normally if the IlvB and IlvN subunits are covalently connected via a flexible linker . Wild type cells are sensitive to exogenous valine due to inhibition of the enzymatic activity of AHAS I . ilvN mutants, however, while still able to grow in the absence of valine and isoleucine, are no longer sensitive in this manner to exogenous valine...

## Biological Role

Catalyzes ACETOLACTSYN-RXN (reaction.ecocyc.ACETOLACTSYN-RXN), 2-aceto-2-hydroxy-butyrate synthase (reaction.ecocyc.ACETOOHBUTSYN-RXN). Bound by FAD (molecule.C00016), Thiamin diphosphate (molecule.C00068), Magnesium cation (molecule.C00305).

## Annotation

The bifunctional acetohydroxybutanoate synthase/acetolactate synthase (AHAS I, IlvBN) carries out both the first step in valine biosynthesis and the second step in isoleucine biosynthesis. AHAS I catalyzes the conversion of pyruvate and oxobutanoate into 2-aceto-2-hydroxy-butyrate and the conversion of pyruvate into 2-acetolactate. Both reactions generate carbon dioxide as a product . This enzyme has a wide substrate range in vitro . This bifunctional enzyme is a tetramer comprising two IlvB subunits and two IlvN subunits. Its apparent molecular weight rises above the expected weight for this configuration when pyruvate is added in vitro . The IlvB large subunit can catalyze the reaction in isolation and is not inhibited by valine in the manner of the holoenzyme. However, the Vmax for the reaction as catalyzed by only IlvB is sharply reduced, as is the enzyme's affinity for the required FAD cofactor . Both activities are catalyzed by the same active site on IlvB . The enzyme works normally if the IlvB and IlvN subunits are covalently connected via a flexible linker . Wild type cells are sensitive to exogenous valine due to inhibition of the enzymatic activity of AHAS I . ilvN mutants, however, while still able to grow in the absence of valine and isoleucine, are no longer sensitive in this manner to exogenous valine . Mutants lacking AHAS I function are unable to grow on acetate or oleate . A number of herbicides have been identified as inhibitors of AHAS I . Interactions between the large and small subunits of the three AHAS isozymes have been studied . Review:

## Outgoing Edges (2)

- `catalyzes` --> [[reaction.ecocyc.ACETOLACTSYN-RXN|reaction.ecocyc.ACETOLACTSYN-RXN]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` --> [[reaction.ecocyc.ACETOOHBUTSYN-RXN|reaction.ecocyc.ACETOOHBUTSYN-RXN]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (5)

- `binds` <-- [[molecule.C00016|molecule.C00016]] `EcoCyc` `database` - EcoCyc enzymatic reaction cofactor
- `binds` <-- [[molecule.C00068|molecule.C00068]] `EcoCyc` `database` - EcoCyc enzymatic reaction cofactor
- `binds` <-- [[molecule.C00305|molecule.C00305]] `EcoCyc` `database` - EcoCyc enzymatic reaction cofactor
- `is_component_of` <-- [[protein.P08142|protein.P08142]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2
- `is_component_of` <-- [[protein.P0ADF8|protein.P0ADF8]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2

## External IDs

- `EcoCyc:ACETOLACTSYNI-CPLX`
- `PDB:6LPI`
- `QSPROTEOME:QS00049342`

## Notes

2*protein.P08142|2*protein.P0ADF8
