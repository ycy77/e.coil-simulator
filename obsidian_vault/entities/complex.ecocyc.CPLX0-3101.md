---
entity_id: "complex.ecocyc.CPLX0-3101"
entity_type: "complex"
name: "ClpP serine protease"
source_database: "EcoCyc"
source_id: "CPLX0-3101"
default_state: "active"
allowed_states: "active|impaired|disrupted|assembled|disassembled|inhibited"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/complex
  - source/EcoCyc
aliases:
---

# ClpP serine protease

`complex.ecocyc.CPLX0-3101`

## Static

- Type: `complex`
- Source: `EcoCyc:CPLX0-3101`
- Default state: `active`
- Allowed states: `active|impaired|disrupted|assembled|disassembled|inhibited`
- Complex type: `regulatory`
- Components: [[protein.P0A6G7|protein.P0A6G7]]

## Enriched Summary

ClpP is a serine protease with a chymotrypsin-like activity that is a part of the ClpAP, ClpAPX and ClpXP protease complexes . The ClpP protease is a tetradecamer, consisting of two heptamers of ClpP subunits stacked head-to-head . ClpP has an axial pore large enough to accept unfolded polypeptide chains, leading into a central cavity that contains fourteen serine protease active sites . This ring structure is required for proper protease function . The active site serine-111 and histidine-136 are also required for protease function . The interface between the two heptameric rings can switch between two different conformations; limiting this switching via crosslinking slows substrate release . Without the ClpA or ClpX ATPase chaperone components only short peptides can enter the ClpP cavity, thus ClpP alone cannot degrade folded proteins . However, acyldepsipeptides and other small molecule activators can activate ClpP to cleave folded proteins. Translocation of polypeptide substrates into ClpP is directional, with the carboxy-terminus going first . ClpP degrades the antitoxin proteins Phd and MazE from the toxin/antitoxin pairs phd-doc (from plasmid prophage P1) and mazEF (from the rel plasmid). The lysogenically expressed lambda protein lambdarexB inhibits this proteolysis . Lambda protein gpW mutants with hydrophobic tails are degraded in a ClpP-dependent manner...

## Biological Role

Catalyzes 3.4.21.92-RXN (reaction.ecocyc.3.4.21.92-RXN). Component of ClpAP (complex.ecocyc.CPLX0-3104), ClpXP (complex.ecocyc.CPLX0-3107), ClpAXP (complex.ecocyc.CPLX0-3108).

## Annotation

ClpP is a serine protease with a chymotrypsin-like activity that is a part of the ClpAP, ClpAPX and ClpXP protease complexes . The ClpP protease is a tetradecamer, consisting of two heptamers of ClpP subunits stacked head-to-head . ClpP has an axial pore large enough to accept unfolded polypeptide chains, leading into a central cavity that contains fourteen serine protease active sites . This ring structure is required for proper protease function . The active site serine-111 and histidine-136 are also required for protease function . The interface between the two heptameric rings can switch between two different conformations; limiting this switching via crosslinking slows substrate release . Without the ClpA or ClpX ATPase chaperone components only short peptides can enter the ClpP cavity, thus ClpP alone cannot degrade folded proteins . However, acyldepsipeptides and other small molecule activators can activate ClpP to cleave folded proteins. Translocation of polypeptide substrates into ClpP is directional, with the carboxy-terminus going first . ClpP degrades the antitoxin proteins Phd and MazE from the toxin/antitoxin pairs phd-doc (from plasmid prophage P1) and mazEF (from the rel plasmid). The lysogenically expressed lambda protein lambdarexB inhibits this proteolysis . Lambda protein gpW mutants with hydrophobic tails are degraded in a ClpP-dependent manner . ClpP is required for normal adaptation to and extended viability in stationary phase, and for growth in SDS . ClpP is a heat shock protein expressed in a sigma 32-dependent manner . It has a 14-amino acid leader peptide which is cleaved intermolecularly by another ClpP without any requirement for associated ClpA . Crystal structures of the ClpP tetradecamer have been solved at resolutions of 2.30 Å , 1.90 Å

## Outgoing Edges (4)

- `catalyzes` --> [[reaction.ecocyc.3.4.21.92-RXN|reaction.ecocyc.3.4.21.92-RXN]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_component_of` --> [[complex.ecocyc.CPLX0-3104|complex.ecocyc.CPLX0-3104]] `EcoCyc` `database` - EcoCyc component coefficient=1
- `is_component_of` --> [[complex.ecocyc.CPLX0-3107|complex.ecocyc.CPLX0-3107]] `EcoCyc` `database` - EcoCyc component coefficient=1
- `is_component_of` --> [[complex.ecocyc.CPLX0-3108|complex.ecocyc.CPLX0-3108]] `EcoCyc` `database` - EcoCyc component coefficient=1

## Incoming Edges (1)

- `is_component_of` <-- [[protein.P0A6G7|protein.P0A6G7]] `EcoCyc` `database` - EcoCyc component coefficient=14 | EcoCyc protcplxs.col coefficient=14

## External IDs

- `EcoCyc:CPLX0-3101`
- `QSPROTEOME:QS00246664`

## Notes

14*protein.P0A6G7
