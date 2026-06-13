---
entity_id: "complex.ecocyc.CPLX0-8005"
entity_type: "complex"
name: "3-oxoacyl-[acyl-carrier-protein] reductase FabG"
source_database: "EcoCyc"
source_id: "CPLX0-8005"
default_state: "active"
allowed_states: "active|impaired|disrupted|assembled|disassembled|inhibited"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/complex
  - source/EcoCyc
aliases:
  - "3-oxoacyl-[acyl-carrier-protein] reductase"
---

# 3-oxoacyl-[acyl-carrier-protein] reductase FabG

`complex.ecocyc.CPLX0-8005`

## Static

- Type: `complex`
- Source: `EcoCyc:CPLX0-8005`
- Default state: `active`
- Allowed states: `active|impaired|disrupted|assembled|disassembled|inhibited`
- Complex type: `structural`
- Components: [[protein.P0AEK2|protein.P0AEK2]]

## Enriched Summary

3-Oxoacyl-[ACP] reductase catalyzes the NADPH-dependent reduction of 3-oxoacyl-[ACP] intermediates (β-ketoacyl-[ACP] intermediates) to (3R)-3-hydroxyacyl-[ACP] intermediates in the prokaryotic fatty acid biosynthesis pathway. It functions in every cycle of fatty acid elongation (see pathway FASYN-ELONG-PWY) and in the synthesis of unsaturated fatty acids (see PWY0-881). It is also involved in the biotin biosynthesis pathway (see pathway BIOTIN-BIOSYNTHESIS-PWY) . The enzyme is a member of the short-chain dehydrogenase/reductase (SDR) family . In early work, the enzyme was purified from E. coli extracts (although the strain used was not reported). It showed a marked preference for ACP derivatives over CoA derivatives as substrates and produced the D(-) isomer of the 3-hydroxyacyl-[ACP] product. It was specific for NADPH, but was nonspecific for the carbon chain length of the β-ketoacyl group. It utilized both saturated and unsaturated substrates . FabG has also been shown to function in an in vitro reconstruction of fatty acid biosynthesis using purified components and a steady state kinetic analysis of a reconstituted system has been performed . Site-directed mutagenesis studies and enzymatic analysis probed the residues on FabG required for high affinity binding to the ACP...

## Biological Role

Catalyzes 3-OXOACYL-ACP-REDUCT-RXN (reaction.ecocyc.3-OXOACYL-ACP-REDUCT-RXN), RXN-10655 (reaction.ecocyc.RXN-10655), RXN-10659 (reaction.ecocyc.RXN-10659), 3-oxo-glutaryl-[acp] methyl ester reductase (reaction.ecocyc.RXN-11476), RXN-11480 (reaction.ecocyc.RXN-11480), acetoacetyl-[acyl-carrier protein] reductase (reaction.ecocyc.RXN-9514), 3-oxo-cis-vaccenoyl-[acyl-carrier protein] reductase (reaction.ecocyc.RXN-9556), RXN0-2142 (reaction.ecocyc.RXN0-2142).

## Annotation

3-Oxoacyl-[ACP] reductase catalyzes the NADPH-dependent reduction of 3-oxoacyl-[ACP] intermediates (β-ketoacyl-[ACP] intermediates) to (3R)-3-hydroxyacyl-[ACP] intermediates in the prokaryotic fatty acid biosynthesis pathway. It functions in every cycle of fatty acid elongation (see pathway FASYN-ELONG-PWY) and in the synthesis of unsaturated fatty acids (see PWY0-881). It is also involved in the biotin biosynthesis pathway (see pathway BIOTIN-BIOSYNTHESIS-PWY) . The enzyme is a member of the short-chain dehydrogenase/reductase (SDR) family . In early work, the enzyme was purified from E. coli extracts (although the strain used was not reported). It showed a marked preference for ACP derivatives over CoA derivatives as substrates and produced the D(-) isomer of the 3-hydroxyacyl-[ACP] product. It was specific for NADPH, but was nonspecific for the carbon chain length of the β-ketoacyl group. It utilized both saturated and unsaturated substrates . FabG has also been shown to function in an in vitro reconstruction of fatty acid biosynthesis using purified components and a steady state kinetic analysis of a reconstituted system has been performed . Site-directed mutagenesis studies and enzymatic analysis probed the residues on FabG required for high affinity binding to the ACP. NMR spectroscopy was also used to identify the ACP residues contributing to formation of the FabG-[ACP] complex . The crystal structure of wild-type, uncomplexed FabG has been determined at 2.60 Å resolution. The enzyme was shown to be a homotetramer . The crystal structures of wild-type FabG and a Y151F mutant, both complexed with NADP(H), have been determined at 2.05 Å resolution. Each monomer in the complex bound one molecule of NADP+ and the asymmetric unit contained eight Ca2+. The data suggest

## Outgoing Edges (8)

- `catalyzes` --> [[reaction.ecocyc.3-OXOACYL-ACP-REDUCT-RXN|reaction.ecocyc.3-OXOACYL-ACP-REDUCT-RXN]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` --> [[reaction.ecocyc.RXN-10655|reaction.ecocyc.RXN-10655]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` --> [[reaction.ecocyc.RXN-10659|reaction.ecocyc.RXN-10659]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` --> [[reaction.ecocyc.RXN-11476|reaction.ecocyc.RXN-11476]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` --> [[reaction.ecocyc.RXN-11480|reaction.ecocyc.RXN-11480]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` --> [[reaction.ecocyc.RXN-9514|reaction.ecocyc.RXN-9514]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` --> [[reaction.ecocyc.RXN-9556|reaction.ecocyc.RXN-9556]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` --> [[reaction.ecocyc.RXN0-2142|reaction.ecocyc.RXN0-2142]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (1)

- `is_component_of` <-- [[protein.P0AEK2|protein.P0AEK2]] `EcoCyc` `database` - EcoCyc component coefficient=4 | EcoCyc protcplxs.col coefficient=4

## External IDs

- `EcoCyc:CPLX0-8005`
- `QSPROTEOME:QS00182735`

## Notes

4*protein.P0AEK2
