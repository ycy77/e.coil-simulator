---
entity_id: "complex.ecocyc.CPLX0-8549"
entity_type: "complex"
name: "NADPH-dependent aldehyde reductase Ahr"
source_database: "EcoCyc"
source_id: "CPLX0-8549"
default_state: "active"
allowed_states: "active|impaired|disrupted|assembled|disassembled|inhibited"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/complex
  - source/EcoCyc
aliases:
---

# NADPH-dependent aldehyde reductase Ahr

`complex.ecocyc.CPLX0-8549`

## Static

- Type: `complex`
- Source: `EcoCyc:CPLX0-8549`
- Default state: `active`
- Allowed states: `active|impaired|disrupted|assembled|disassembled|inhibited`
- Complex type: `structural`
- Components: [[protein.P27250|protein.P27250]]

## Enriched Summary

Ahr is a member of the zinc-containing medium-chain dehydrogenase/reductase family. The enzyme is a source of NADPH-dependent aldehyde reductase activity in the cell. Catalytic activity of the purified enzyme was measured with a variety of aldehyde substrates . Unpurified Ahr was previously shown to have acetaldehyde and isobutyraldehyde reductase activity, with a preference for the NADPH co-substrate. This activity contributes to the conversion of isobutyraldehyde to isobutanol in an engineered strain . In a metabolically engineered strain, phenylacetaldehyde and 4-hydroxyphenylacetaldehyde are reduced to 2-phenylethanol and 2-(4-hydroxyphenyl)ethanol by the endogenous aldehyde reductases YqhD, Ahr, and YahK . Crystal structures of the enzyme alone and in a complex with NADP have been determined, and a model to explain the broad substrate specificity of the enzyme was proposed . Mutants that change the preference of the enzyme for the NADPH cosubstrate towards NADH have been constructed . The yjgB gene of Salmonella enterica serovar Typhimurium is part of the RpoS regulon . Ahr: "aldehyde reductase" Ahr is a member of the zinc-containing medium-chain dehydrogenase/reductase family. The enzyme is a source of NADPH-dependent aldehyde reductase activity in the cell. Catalytic activity of the purified enzyme was measured with a variety of aldehyde substrates...

## Biological Role

Catalyzes ALCOHOL-DEHYDROGENASE-NADPORNOP+-RXN (reaction.ecocyc.ALCOHOL-DEHYDROGENASE-NADPORNOP_-RXN). Bound by Zinc cation (molecule.C00038).

## Annotation

Ahr is a member of the zinc-containing medium-chain dehydrogenase/reductase family. The enzyme is a source of NADPH-dependent aldehyde reductase activity in the cell. Catalytic activity of the purified enzyme was measured with a variety of aldehyde substrates . Unpurified Ahr was previously shown to have acetaldehyde and isobutyraldehyde reductase activity, with a preference for the NADPH co-substrate. This activity contributes to the conversion of isobutyraldehyde to isobutanol in an engineered strain . In a metabolically engineered strain, phenylacetaldehyde and 4-hydroxyphenylacetaldehyde are reduced to 2-phenylethanol and 2-(4-hydroxyphenyl)ethanol by the endogenous aldehyde reductases YqhD, Ahr, and YahK . Crystal structures of the enzyme alone and in a complex with NADP have been determined, and a model to explain the broad substrate specificity of the enzyme was proposed . Mutants that change the preference of the enzyme for the NADPH cosubstrate towards NADH have been constructed . The yjgB gene of Salmonella enterica serovar Typhimurium is part of the RpoS regulon . Ahr: "aldehyde reductase"

## Outgoing Edges (1)

- `catalyzes` --> [[reaction.ecocyc.ALCOHOL-DEHYDROGENASE-NADPORNOP_-RXN|reaction.ecocyc.ALCOHOL-DEHYDROGENASE-NADPORNOP_-RXN]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (2)

- `binds` <-- [[molecule.C00038|molecule.C00038]] `EcoCyc` `database` - EcoCyc enzymatic reaction cofactor
- `is_component_of` <-- [[protein.P27250|protein.P27250]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2

## External IDs

- `EcoCyc:CPLX0-8549`
- `QSPROTEOME:QS00188903`

## Notes

2*protein.P27250
