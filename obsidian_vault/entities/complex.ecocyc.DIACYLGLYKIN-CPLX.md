---
entity_id: "complex.ecocyc.DIACYLGLYKIN-CPLX"
entity_type: "complex"
name: "diacylglycerol kinase"
source_database: "EcoCyc"
source_id: "DIACYLGLYKIN-CPLX"
default_state: "active"
allowed_states: "active|impaired|disrupted|assembled|disassembled|inhibited"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/complex
  - source/EcoCyc
aliases:
---

# diacylglycerol kinase

`complex.ecocyc.DIACYLGLYKIN-CPLX`

## Static

- Type: `complex`
- Source: `EcoCyc:DIACYLGLYKIN-CPLX`
- Default state: `active`
- Allowed states: `active|impaired|disrupted|assembled|disassembled|inhibited`
- Complex type: `regulatory`
- Components: [[protein.P0ABN1|protein.P0ABN1]]

## Enriched Summary

The inner membrane protein diacylglycerol kinase (DgkA) is the smallest known kinase; it phosphorylates diacylglycerol substrates, yielding phosphatidic acids. Diacylglycerol kinase functions in the recycling of diacylglycerol produced as a by-product of membrane-derived oligosaccharides (MDO) biosynthesis . In addition to the MgATP substrate, the enzyme requires a second divalent metal cation and a lipid activator for activity . The lipid activator was thought to induce a conformational change in the enzyme, switching it from a catalytically inactive form susceptible to inactivation to a catalytically active form resistant to inactivation . Phosphoryl transfer appears to be direct, i.e. it does not involve a phosphorylated enzyme intermediate . Solid-state NMR has enabled a more detailed understanding of the reaction mechanism; ATP hydrolysis shows positive cooperativity , and nucleotide binding induces a conformational change in the enzyme prior to catalysis . Putative active site mutants , mutants in Trp residues that are thought to anchor transmembrane helices , and mutations in residues that affect oligomerization have been generated and tested. Experimental investigation of the membrane topology of DgkA shows three transmembrane domains and an N-terminal amphipathic helix located on the cytoplasmic surface...

## Biological Role

Catalyzes DIACYLGLYKIN-RXN (reaction.ecocyc.DIACYLGLYKIN-RXN). Bound by Magnesium cation (molecule.C00305), Mn2+ (molecule.ecocyc.MN_2).

## Annotation

The inner membrane protein diacylglycerol kinase (DgkA) is the smallest known kinase; it phosphorylates diacylglycerol substrates, yielding phosphatidic acids. Diacylglycerol kinase functions in the recycling of diacylglycerol produced as a by-product of membrane-derived oligosaccharides (MDO) biosynthesis . In addition to the MgATP substrate, the enzyme requires a second divalent metal cation and a lipid activator for activity . The lipid activator was thought to induce a conformational change in the enzyme, switching it from a catalytically inactive form susceptible to inactivation to a catalytically active form resistant to inactivation . Phosphoryl transfer appears to be direct, i.e. it does not involve a phosphorylated enzyme intermediate . Solid-state NMR has enabled a more detailed understanding of the reaction mechanism; ATP hydrolysis shows positive cooperativity , and nucleotide binding induces a conformational change in the enzyme prior to catalysis . Putative active site mutants , mutants in Trp residues that are thought to anchor transmembrane helices , and mutations in residues that affect oligomerization have been generated and tested. Experimental investigation of the membrane topology of DgkA shows three transmembrane domains and an N-terminal amphipathic helix located on the cytoplasmic surface . Folding, unfolding, and structural properties of the enzyme have been studied extensively . Crosslinking suggested a homotrimeric structure ; mixing different active site mutants and measuring the resulting activity supports a model where each active site is formed by multiple subunits . A peptide corresponding to the second transmembrane segment is able to inhibit enzymatic activity . Solution and solid state NMR structures as well as crystal structures of th

## Outgoing Edges (1)

- `catalyzes` --> [[reaction.ecocyc.DIACYLGLYKIN-RXN|reaction.ecocyc.DIACYLGLYKIN-RXN]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (3)

- `binds` <-- [[molecule.C00305|molecule.C00305]] `EcoCyc` `database` - EcoCyc enzymatic reaction cofactor
- `binds` <-- [[molecule.ecocyc.MN_2|molecule.ecocyc.MN_2]] `EcoCyc` `database` - EcoCyc enzymatic reaction cofactor
- `is_component_of` <-- [[protein.P0ABN1|protein.P0ABN1]] `EcoCyc` `database` - EcoCyc component coefficient=3 | EcoCyc protcplxs.col coefficient=3

## External IDs

- `EcoCyc:DIACYLGLYKIN-CPLX`
- `QSPROTEOME:QS00195279`

## Notes

3*protein.P0ABN1
