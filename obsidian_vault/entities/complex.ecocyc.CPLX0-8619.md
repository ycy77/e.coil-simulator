---
entity_id: "complex.ecocyc.CPLX0-8619"
entity_type: "complex"
name: "nucleoside phosphorylase PpnP"
source_database: "EcoCyc"
source_id: "CPLX0-8619"
default_state: "active"
allowed_states: "active|impaired|disrupted|assembled|disassembled|inhibited"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/complex
  - source/EcoCyc
aliases:
---

# nucleoside phosphorylase PpnP

`complex.ecocyc.CPLX0-8619`

## Static

- Type: `complex`
- Source: `EcoCyc:CPLX0-8619`
- Default state: `active`
- Allowed states: `active|impaired|disrupted|assembled|disassembled|inhibited`
- Complex type: `structural`
- Components: [[protein.P0C037|protein.P0C037]]

## Enriched Summary

The nucleoside phosphorylase activity of PpnP was discovered in a large-scale metabolomics screen for enzymatic activities of uncharacterized proteins in E. coli . Crystal structures of PpnP show an RlmC-like Cupin fold . Research focused on optimizing production of modified nucleosides has been carried out on PpnP . PpnP: "pyrimidine and purine nucleoside phosphorylase" The nucleoside phosphorylase activity of PpnP was discovered in a large-scale metabolomics screen for enzymatic activities of uncharacterized proteins in E. coli . Crystal structures of PpnP show an RlmC-like Cupin fold . Research focused on optimizing production of modified nucleosides has been carried out on PpnP . PpnP: "pyrimidine and purine nucleoside phosphorylase"

## Biological Role

Catalyzes ADENPHOSPHOR-RXN (reaction.ecocyc.ADENPHOSPHOR-RXN), INOPHOSPHOR-RXN (reaction.ecocyc.INOPHOSPHOR-RXN), RXN0-5199 (reaction.ecocyc.RXN0-5199), THYM-PHOSPH-RXN (reaction.ecocyc.THYM-PHOSPH-RXN), URPHOS-RXN (reaction.ecocyc.URPHOS-RXN), XANTHOSINEPHOSPHORY-RXN (reaction.ecocyc.XANTHOSINEPHOSPHORY-RXN).

## Annotation

The nucleoside phosphorylase activity of PpnP was discovered in a large-scale metabolomics screen for enzymatic activities of uncharacterized proteins in E. coli . Crystal structures of PpnP show an RlmC-like Cupin fold . Research focused on optimizing production of modified nucleosides has been carried out on PpnP . PpnP: "pyrimidine and purine nucleoside phosphorylase"

## Outgoing Edges (6)

- `catalyzes` --> [[reaction.ecocyc.ADENPHOSPHOR-RXN|reaction.ecocyc.ADENPHOSPHOR-RXN]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` --> [[reaction.ecocyc.INOPHOSPHOR-RXN|reaction.ecocyc.INOPHOSPHOR-RXN]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` --> [[reaction.ecocyc.RXN0-5199|reaction.ecocyc.RXN0-5199]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` --> [[reaction.ecocyc.THYM-PHOSPH-RXN|reaction.ecocyc.THYM-PHOSPH-RXN]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` --> [[reaction.ecocyc.URPHOS-RXN|reaction.ecocyc.URPHOS-RXN]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` --> [[reaction.ecocyc.XANTHOSINEPHOSPHORY-RXN|reaction.ecocyc.XANTHOSINEPHOSPHORY-RXN]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (1)

- `is_component_of` <-- [[protein.P0C037|protein.P0C037]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2

## External IDs

- `EcoCyc:CPLX0-8619`
- `QSPROTEOME:QS00159531`

## Notes

2*protein.P0C037
