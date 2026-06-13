---
entity_id: "complex.ecocyc.UDPNACETYLGLUCOSAMACYLTRANS-CPLX"
entity_type: "complex"
name: "acyl-[acyl-carrier-protein]—UDP-N-acetylglucosamine O-acyltransferase"
source_database: "EcoCyc"
source_id: "UDPNACETYLGLUCOSAMACYLTRANS-CPLX"
default_state: "active"
allowed_states: "active|impaired|disrupted|assembled|disassembled|inhibited"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/complex
  - source/EcoCyc
aliases:
  - "LpxA"
---

# acyl-[acyl-carrier-protein]—UDP-N-acetylglucosamine O-acyltransferase

`complex.ecocyc.UDPNACETYLGLUCOSAMACYLTRANS-CPLX`

## Static

- Type: `complex`
- Source: `EcoCyc:UDPNACETYLGLUCOSAMACYLTRANS-CPLX`
- Default state: `active`
- Allowed states: `active|impaired|disrupted|assembled|disassembled|inhibited`
- Complex type: `structural`
- Components: [[protein.P0A722|protein.P0A722]]

## Enriched Summary

UDP-N-acetylglucosamine acyltransferase (LpxA) catalyzes the first reaction of lipid A biosynthesis . Its substrates are situated at important biosynthetic branchpoints leading to several major cell envelope components. UDP-N-acetylglucosamine can be used in the synthesis of lipid A or incorporated into peptidoglycan. (R)-3-hydroxymyristoyl-ACP can act as the initial acyl donor for lipid A biosynthesis or it can be elongated by the fatty acid synthesis enzymes to palmitate, which is a major component of membrane glycerophospholipids. Although LpxA catalyzes the first step in lipid A biosynthesis, the reaction catalyzed by LpxA has a very unfavorable equilibrium constant. Therefore, the following reaction catalyzed by LpxC is the actual first committed step in lipid A biosynthesis . LpxA is highly selective for proper length of its acyl donor, preferring a myristoyl chain by a wide margin over similar donors of different lengths . Crystal structures of trimeric LpxA have been determined to 2.5 and 2.6 Å, revealing an LβH motif . A structural model of LpxA complexed with ACP-MONOMER has been developed based on these crystal structures and NMR-derived orientational constraints . A 1.8 Å-resolution structure of LpxA complexed with an antibacterial peptide show that one peptide binds per LpxA subunit...

## Biological Role

Catalyzes UDPNACETYLGLUCOSAMACYLTRANS-RXN (reaction.ecocyc.UDPNACETYLGLUCOSAMACYLTRANS-RXN).

## Annotation

UDP-N-acetylglucosamine acyltransferase (LpxA) catalyzes the first reaction of lipid A biosynthesis . Its substrates are situated at important biosynthetic branchpoints leading to several major cell envelope components. UDP-N-acetylglucosamine can be used in the synthesis of lipid A or incorporated into peptidoglycan. (R)-3-hydroxymyristoyl-ACP can act as the initial acyl donor for lipid A biosynthesis or it can be elongated by the fatty acid synthesis enzymes to palmitate, which is a major component of membrane glycerophospholipids. Although LpxA catalyzes the first step in lipid A biosynthesis, the reaction catalyzed by LpxA has a very unfavorable equilibrium constant. Therefore, the following reaction catalyzed by LpxC is the actual first committed step in lipid A biosynthesis . LpxA is highly selective for proper length of its acyl donor, preferring a myristoyl chain by a wide margin over similar donors of different lengths . Crystal structures of trimeric LpxA have been determined to 2.5 and 2.6 Å, revealing an LβH motif . A structural model of LpxA complexed with ACP-MONOMER has been developed based on these crystal structures and NMR-derived orientational constraints . A 1.8 Å-resolution structure of LpxA complexed with an antibacterial peptide show that one peptide binds per LpxA subunit . Comparative crystal structures of LpxA bound to its product, UDP-3-O-(3-hydroxymyristoyl)-N-acetylglucosamine and to the shorter-chain equivalent compound UDP-3-O-(R-3-hydroxydecanoyl)-N-acetylglucosamine, have been resolved to 1.74 Å and 1.85 Å, respectively. Comparison of these two structures highlights binding elements within LpxA that are critical in determining its strong selectivity for the myristoyl chain over other possible acyl moieties . Crystal structure of LpxA in

## Outgoing Edges (1)

- `catalyzes` --> [[reaction.ecocyc.UDPNACETYLGLUCOSAMACYLTRANS-RXN|reaction.ecocyc.UDPNACETYLGLUCOSAMACYLTRANS-RXN]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (1)

- `is_component_of` <-- [[protein.P0A722|protein.P0A722]] `EcoCyc` `database` - EcoCyc component coefficient=3 | EcoCyc protcplxs.col coefficient=3

## External IDs

- `EcoCyc:UDPNACETYLGLUCOSAMACYLTRANS-CPLX`
- `QSPROTEOME:QS00181689`
- `PDB:2aq9`
- `PDB:2jf2`
- `PDB:2jf3`
- `PDB:2qia`
- `PDB:2qiv`

## Notes

3*protein.P0A722
