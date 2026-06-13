---
entity_id: "complex.ecocyc.NITRITREDUCT-CPLX"
entity_type: "complex"
name: "nitrite reductase - NADH dependent"
source_database: "EcoCyc"
source_id: "NITRITREDUCT-CPLX"
default_state: "active"
allowed_states: "active|impaired|disrupted|assembled|disassembled|inhibited"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/complex
  - source/EcoCyc
aliases:
  - "Nir"
---

# nitrite reductase - NADH dependent

`complex.ecocyc.NITRITREDUCT-CPLX`

## Static

- Type: `complex`
- Source: `EcoCyc:NITRITREDUCT-CPLX`
- Default state: `active`
- Allowed states: `active|impaired|disrupted|assembled|disassembled|inhibited`
- Complex type: `structural`
- Components: [[protein.P0A9I8|protein.P0A9I8]], [[protein.P08201|protein.P08201]]

## Enriched Summary

The cytoplasmic NADH-dependent nitrite reductase (Nir) catalyzes the six-electron reduction of nitrite to ammonia. Nir activity does not generate a proton gradient; its metabolic role was proposed to be detoxification of nitrite . However, a recent study showed that the ammonium produced by Nir is utilized for cell growth; excess nitrite produced when cells are grown at high levels of nitrate is excreted. Thus, Nir does not appear to play a role in nitrite detoxification . Another possible role is the recycling of NADH in the presence of excess reducing equivalents inside the cell . The presence of Nir leads to higher anaerobic growth on low-to-medium concentrations of glucose and nitrate compared to a Δnir mutant. Utilization of Nir for the reoxidation of NADH to maintain redox balance enables the energetically favorable fermentation of glucose to formate and acetate rather than the less favorable ethanol fermentation . E. coli strains lacking either NirB or NirD contain no detectable NADH-dependent nitrite reductase activity. In vitro reconstitution of nitrite reductase activity from cell extracts required stoichiometric quantities of NirB and NirD. The NirD protein appears to be present in partially purified nitrite reductase . Nitrite reductase contains FAD, a [2Fe-2S] iron-sulfur cluster and siroheme as cofactors. E...

## Biological Role

Catalyzes RXN-13854 (reaction.ecocyc.RXN-13854). Bound by FAD (molecule.C00016), Siroheme (molecule.C00748), a [2Fe-2S] iron-sulfur cluster (molecule.ecocyc.CPD-6).

## Annotation

The cytoplasmic NADH-dependent nitrite reductase (Nir) catalyzes the six-electron reduction of nitrite to ammonia. Nir activity does not generate a proton gradient; its metabolic role was proposed to be detoxification of nitrite . However, a recent study showed that the ammonium produced by Nir is utilized for cell growth; excess nitrite produced when cells are grown at high levels of nitrate is excreted. Thus, Nir does not appear to play a role in nitrite detoxification . Another possible role is the recycling of NADH in the presence of excess reducing equivalents inside the cell . The presence of Nir leads to higher anaerobic growth on low-to-medium concentrations of glucose and nitrate compared to a Δnir mutant. Utilization of Nir for the reoxidation of NADH to maintain redox balance enables the energetically favorable fermentation of glucose to formate and acetate rather than the less favorable ethanol fermentation . E. coli strains lacking either NirB or NirD contain no detectable NADH-dependent nitrite reductase activity. In vitro reconstitution of nitrite reductase activity from cell extracts required stoichiometric quantities of NirB and NirD. The NirD protein appears to be present in partially purified nitrite reductase . Nitrite reductase contains FAD, a [2Fe-2S] iron-sulfur cluster and siroheme as cofactors. E. coli encodes two distinct nitrite reductases that reduce nitrite to ammonia. Their expression is complementary — with low concentrations of nitrate in the environment, CYTOCHROMEC552-MONOMER (NrfA) is made; with high concentrations of nitrate, the NADH-dependent nitrite reductase is made almost exclusively. At intermediate concentrations of nitrate, both enzymes are made. Nitrite also induces the formation of both enzymes, but it is a less effective in

## Outgoing Edges (1)

- `catalyzes` --> [[reaction.ecocyc.RXN-13854|reaction.ecocyc.RXN-13854]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (5)

- `binds` <-- [[molecule.C00016|molecule.C00016]] `EcoCyc` `database` - EcoCyc enzymatic reaction cofactor
- `binds` <-- [[molecule.C00748|molecule.C00748]] `EcoCyc` `database` - EcoCyc enzymatic reaction cofactor
- `binds` <-- [[molecule.ecocyc.CPD-6|molecule.ecocyc.CPD-6]] `EcoCyc` `database` - EcoCyc enzymatic reaction cofactor
- `is_component_of` <-- [[protein.P08201|protein.P08201]] `EcoCyc` `database` - EcoCyc component coefficient= | EcoCyc protcplxs.col coefficient=1
- `is_component_of` <-- [[protein.P0A9I8|protein.P0A9I8]] `EcoCyc` `database` - EcoCyc component coefficient= | EcoCyc protcplxs.col coefficient=1

## External IDs

- `EcoCyc:NITRITREDUCT-CPLX`
- `QSPROTEOME:QS00049510`

## Notes

protein.P0A9I8|protein.P08201
