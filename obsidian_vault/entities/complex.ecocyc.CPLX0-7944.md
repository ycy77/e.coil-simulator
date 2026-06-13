---
entity_id: "complex.ecocyc.CPLX0-7944"
entity_type: "complex"
name: "outer membrane phospholipase A"
source_database: "EcoCyc"
source_id: "CPLX0-7944"
default_state: "active"
allowed_states: "active|impaired|disrupted|assembled|disassembled|inhibited"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/complex
  - source/EcoCyc
aliases:
  - "detergent resistant (DR) phospholipase A"
---

# outer membrane phospholipase A

`complex.ecocyc.CPLX0-7944`

## Static

- Type: `complex`
- Source: `EcoCyc:CPLX0-7944`
- Default state: `active`
- Allowed states: `active|impaired|disrupted|assembled|disassembled|inhibited`
- Complex type: `structural`
- Components: [[protein.P0A921|protein.P0A921]]

## Enriched Summary

pldA encodes outer membrane phospholipase A (OMPLA) . Purified OMPLA displays multiple lipolytic activities and is active on phospholipids, lysophosphospholipids, diglycerides and monoglycerides however in vivo the expected substrates are the phospholipids of the cell envelope . OMPLA activity is proposed to remove mislocalized phospholipids from the outer leaflet of the OM in response to disruptions in OM lipid asymmetry (see ); PldA acts a sensor for OM asymmetry; PldA degrades mislocalized phospholipids and generates fatty acids which act as second messengers in a proposed trans-envelope signaling pathway that restores OM homeostasis via modulation of the LPS biosynthetic enzyme UDPACYLGLCNACDEACETYL-MONOMER "LpxC" . Purified OMPLA requires Ca2+ for activity; with 1-palmitoyl-2-myristoyl-sn-glycero-3-phosphocholine as substrate, purified OMPLA displays phospholipase A1 activity, phospholipase A2 actiivty, lysophospholipase L1 activty and lysophospholipase L2 activity; the enzyme has a preference for lipids containing long (>=12 carbon) acyl chains and for hydrolyzing the primary acyl chain; enzyme binding appears to depend on the hydrocarbon chain . Dimerization of OMPLA is necessary for phospholipase activity; calcium binding and substrate binding modulate dimerization and enzyme activity in vitro . The enzyme binds two Ca2+ ions per monomer...

## Biological Role

Catalyzes RXN-19311 (reaction.ecocyc.RXN-19311), RXN-19312 (reaction.ecocyc.RXN-19312), RXN0-6725 (reaction.ecocyc.RXN0-6725), RXN0-6952 (reaction.ecocyc.RXN0-6952). Bound by Ca2+ (molecule.ecocyc.CA_2).

## Annotation

pldA encodes outer membrane phospholipase A (OMPLA) . Purified OMPLA displays multiple lipolytic activities and is active on phospholipids, lysophosphospholipids, diglycerides and monoglycerides however in vivo the expected substrates are the phospholipids of the cell envelope . OMPLA activity is proposed to remove mislocalized phospholipids from the outer leaflet of the OM in response to disruptions in OM lipid asymmetry (see ); PldA acts a sensor for OM asymmetry; PldA degrades mislocalized phospholipids and generates fatty acids which act as second messengers in a proposed trans-envelope signaling pathway that restores OM homeostasis via modulation of the LPS biosynthetic enzyme UDPACYLGLCNACDEACETYL-MONOMER "LpxC" . Purified OMPLA requires Ca2+ for activity; with 1-palmitoyl-2-myristoyl-sn-glycero-3-phosphocholine as substrate, purified OMPLA displays phospholipase A1 activity, phospholipase A2 actiivty, lysophospholipase L1 activty and lysophospholipase L2 activity; the enzyme has a preference for lipids containing long (>=12 carbon) acyl chains and for hydrolyzing the primary acyl chain; enzyme binding appears to depend on the hydrocarbon chain . Dimerization of OMPLA is necessary for phospholipase activity; calcium binding and substrate binding modulate dimerization and enzyme activity in vitro . The enzyme binds two Ca2+ ions per monomer . Substrate binding is a more significant driving force for OMPLA dimerization than is calcium binding . Although pldA is constitutively expressed, OMPLA activity is not detected under normal conditions but is induced by conditions which disturb outer membrane integrity (reviewed in ). Purifed OMPLA, reconstituted into giant lipid vesicles displays dual function; it forms nanapores through which ions and small molecules can pass

## Outgoing Edges (4)

- `catalyzes` --> [[reaction.ecocyc.RXN-19311|reaction.ecocyc.RXN-19311]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` --> [[reaction.ecocyc.RXN-19312|reaction.ecocyc.RXN-19312]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` --> [[reaction.ecocyc.RXN0-6725|reaction.ecocyc.RXN0-6725]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` --> [[reaction.ecocyc.RXN0-6952|reaction.ecocyc.RXN0-6952]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (2)

- `binds` <-- [[molecule.ecocyc.CA_2|molecule.ecocyc.CA_2]] `EcoCyc` `database` - EcoCyc enzymatic reaction cofactor
- `is_component_of` <-- [[protein.P0A921|protein.P0A921]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2

## External IDs

- `EcoCyc:CPLX0-7944`
- `QSPROTEOME:QS00049681`

## Notes

2*protein.P0A921
