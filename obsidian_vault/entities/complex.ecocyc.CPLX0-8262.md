---
entity_id: "complex.ecocyc.CPLX0-8262"
entity_type: "complex"
name: "nucleotide 5'-monophosphate nucleosidase"
source_database: "EcoCyc"
source_id: "CPLX0-8262"
default_state: "active"
allowed_states: "active|impaired|disrupted|assembled|disassembled|inhibited"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/complex
  - source/EcoCyc
aliases:
---

# nucleotide 5'-monophosphate nucleosidase

`complex.ecocyc.CPLX0-8262`

## Static

- Type: `complex`
- Source: `EcoCyc:CPLX0-8262`
- Default state: `active`
- Allowed states: `active|impaired|disrupted|assembled|disassembled|inhibited`
- Complex type: `structural`
- Components: [[protein.P0ADR8|protein.P0ADR8]]

## Enriched Summary

The pyrimidine/purine nucleotide 5'-monophosphate nucleosidase activity of PpnN was discovered in a large-scale metabolomics screen for enzymatic activities of uncharacterized proteins in E. coli . PpnN was idientified as a (p)ppGpp-binding protein; Mg2+ inhibits binding with an IC50 of 5.4 ± 2.0 mM . (p)ppGpp increases the activity of PpnN in vitro; induction of the stringent response in vivo results in a transient increase of nucleobase levels in wild-type cells which does not occur in a ΔppnN mutant . Crystal structures of apo- and pppGpp-bound PpnN have been solved. A putative active site was identified based on the presence of a nucleotide-binding fold and a sequence motif that is highly conserved among enzymes with nucleosidase-like activities. The pppGpp-binding pocket is located at the interface between two subunits; pppGpp binding results in large-scale rearrangements that lead to opening of the putative active site. Site-directed mutagenesis of residues involved in pppGpp binding supported their importance for (p)ppGpp binding and stimulation of catalytic activity, as well as for tetramerization . A ΔppnN mutant has a slight growth defect when grown on M9 glucose . Wild-type cells have a growth advantage over a ΔppnN mutant when subjected to feast-or-famine cycles. A ΔppnN mutant produces more persister cells upon ofloxacin exposure...

## Biological Role

Catalyzes 3.2.2.10-RXN (reaction.ecocyc.3.2.2.10-RXN), AMP-NUCLEOSID-RXN (reaction.ecocyc.AMP-NUCLEOSID-RXN), INOSINATE-NUCLEOSIDASE-RXN (reaction.ecocyc.INOSINATE-NUCLEOSIDASE-RXN), RXN0-7352 (reaction.ecocyc.RXN0-7352).

## Annotation

The pyrimidine/purine nucleotide 5'-monophosphate nucleosidase activity of PpnN was discovered in a large-scale metabolomics screen for enzymatic activities of uncharacterized proteins in E. coli . PpnN was idientified as a (p)ppGpp-binding protein; Mg2+ inhibits binding with an IC50 of 5.4 ± 2.0 mM . (p)ppGpp increases the activity of PpnN in vitro; induction of the stringent response in vivo results in a transient increase of nucleobase levels in wild-type cells which does not occur in a ΔppnN mutant . Crystal structures of apo- and pppGpp-bound PpnN have been solved. A putative active site was identified based on the presence of a nucleotide-binding fold and a sequence motif that is highly conserved among enzymes with nucleosidase-like activities. The pppGpp-binding pocket is located at the interface between two subunits; pppGpp binding results in large-scale rearrangements that lead to opening of the putative active site. Site-directed mutagenesis of residues involved in pppGpp binding supported their importance for (p)ppGpp binding and stimulation of catalytic activity, as well as for tetramerization . A ΔppnN mutant has a slight growth defect when grown on M9 glucose . Wild-type cells have a growth advantage over a ΔppnN mutant when subjected to feast-or-famine cycles. A ΔppnN mutant produces more persister cells upon ofloxacin exposure . PpnN: "pyrimidine and purine nucleotide 5'-monophosphate nucleosidase" Review:

## Outgoing Edges (4)

- `catalyzes` --> [[reaction.ecocyc.3.2.2.10-RXN|reaction.ecocyc.3.2.2.10-RXN]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` --> [[reaction.ecocyc.AMP-NUCLEOSID-RXN|reaction.ecocyc.AMP-NUCLEOSID-RXN]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` --> [[reaction.ecocyc.INOSINATE-NUCLEOSIDASE-RXN|reaction.ecocyc.INOSINATE-NUCLEOSIDASE-RXN]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` --> [[reaction.ecocyc.RXN0-7352|reaction.ecocyc.RXN0-7352]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (1)

- `is_component_of` <-- [[protein.P0ADR8|protein.P0ADR8]] `EcoCyc` `database` - EcoCyc component coefficient=4 | EcoCyc protcplxs.col coefficient=4

## External IDs

- `EcoCyc:CPLX0-8262`
- `QSPROTEOME:QS00195411`

## Notes

4*protein.P0ADR8
