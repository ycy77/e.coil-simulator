---
entity_id: "complex.ecocyc.CPLX0-8180"
entity_type: "complex"
name: "protein disaggregase"
source_database: "EcoCyc"
source_id: "CPLX0-8180"
default_state: "active"
allowed_states: "active|impaired|disrupted|assembled|disassembled|inhibited"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/complex
  - source/EcoCyc
aliases:
  - "ClpB95"
  - "ClpB93"
  - "Hsp100"
---

# protein disaggregase

`complex.ecocyc.CPLX0-8180`

## Static

- Type: `complex`
- Source: `EcoCyc:CPLX0-8180`
- Default state: `active`
- Allowed states: `active|impaired|disrupted|assembled|disassembled|inhibited`
- Complex type: `regulatory`
- Components: [[protein.P63284|protein.P63284]]

## Enriched Summary

ClpB belongs to the superfamily of AAA+ ("ATPase associated with a variety of cellular activities") proteins. ClpB is a member of the heat-shock induced chaperone network; ClpB together with the EG10241-MONOMER "DnaK chaperone system" (DnaK/DnaJ/GrpE) solubilizes and reactivates aggregated proteins. A ΔclpB::Kmr strain has a slower growth rate at 44°C and dies faster at 50°C compared to wild type . Purified ClpB has both basal and protein (casein, insulin) activated ATPase activity . ClpB has no disaggregating activity on its own; ClpB together with the DnaK system suppresses or reverses aggregation of denatured proteins in vitro and in vivo (see further ). CPLX0-8108 "IbpA/CPLX0-8107 "IbpB", ClpB and the DnaK system form a functional triad of chaperones; the small heat shock proteins IbpA and IbpB cooperate with the ClpB/DnaK system to reverse heat-induced protein aggregation in vivo and in vitro . The ClpB/DnaK/DnaJ disaggregating chaperones relocalize and associate dynamically with misfolded proteins deposited at the cell poles after heat stress in an energy dependent process . The disaggregating chaperones exhibit a binding hierachy to protein aggregates; DnaJ mediated association of DnaK with aggregated protein is a prerequisite for the recruitment of ClpB...

## Biological Role

Catalyzes RXN185E-10 (reaction.ecocyc.RXN185E-10).

## Annotation

ClpB belongs to the superfamily of AAA+ ("ATPase associated with a variety of cellular activities") proteins. ClpB is a member of the heat-shock induced chaperone network; ClpB together with the EG10241-MONOMER "DnaK chaperone system" (DnaK/DnaJ/GrpE) solubilizes and reactivates aggregated proteins. A ΔclpB::Kmr strain has a slower growth rate at 44°C and dies faster at 50°C compared to wild type . Purified ClpB has both basal and protein (casein, insulin) activated ATPase activity . ClpB has no disaggregating activity on its own; ClpB together with the DnaK system suppresses or reverses aggregation of denatured proteins in vitro and in vivo (see further ). CPLX0-8108 "IbpA/CPLX0-8107 "IbpB", ClpB and the DnaK system form a functional triad of chaperones; the small heat shock proteins IbpA and IbpB cooperate with the ClpB/DnaK system to reverse heat-induced protein aggregation in vivo and in vitro . The ClpB/DnaK/DnaJ disaggregating chaperones relocalize and associate dynamically with misfolded proteins deposited at the cell poles after heat stress in an energy dependent process . The disaggregating chaperones exhibit a binding hierachy to protein aggregates; DnaJ mediated association of DnaK with aggregated protein is a prerequisite for the recruitment of ClpB . ClpB is a multidomain protein consisting of two nucleotide-binding domains (NBD1/ATP1 and NBD2/ATP2) separated by a linker or middle domain and enclosed by N and C-terminal regions (see ). A number of studies have examined the contribution of various domains to oligomerization, ATPase, and chaperone activity . The middle or M domain forms a coiled-coil structure which wraps around the outer edge of the complex and acts as a molecular switch or toggle to control ClpB ATPase activity (see further ). In the presen

## Outgoing Edges (1)

- `catalyzes` --> [[reaction.ecocyc.RXN185E-10|reaction.ecocyc.RXN185E-10]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (1)

- `is_component_of` <-- [[protein.P63284|protein.P63284]] `EcoCyc` `database` - EcoCyc component coefficient=6 | EcoCyc protcplxs.col coefficient=6

## External IDs

- `EcoCyc:CPLX0-8180`
- `PDB:6OG3`
- `PDB:6OG2`
- `PDB:6OG1`
- `PDB:6OAY`
- `PDB:6OAX`

## Notes

6*protein.P63284
