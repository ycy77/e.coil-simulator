---
entity_id: "complex.ecocyc.ANGLYC3PDEHYDROG-CPLX"
entity_type: "complex"
name: "anaerobic glycerol-3-phosphate dehydrogenase"
source_database: "EcoCyc"
source_id: "ANGLYC3PDEHYDROG-CPLX"
default_state: "active"
allowed_states: "active|impaired|disrupted|assembled|disassembled|inhibited"
subcellular_location: "CCI-CYTOSOL-GN"
enriched_summary_quality: "informative"
tags:
  - entity/complex
  - source/EcoCyc
aliases:
  - "G3P dehydrogenase"
  - "sn-glycerol-3-phosphate:(acceptor) 2-oxidoreductase"
  - "glycerol-3-phosphate:menaquinone oxidoreductase"
---

# anaerobic glycerol-3-phosphate dehydrogenase

`complex.ecocyc.ANGLYC3PDEHYDROG-CPLX`

## Static

- Type: `complex`
- Source: `EcoCyc:ANGLYC3PDEHYDROG-CPLX`
- Default state: `active`
- Allowed states: `active|impaired|disrupted|assembled|disassembled|inhibited`
- Location: CCI-CYTOSOL-GN
- Complex type: `regulatory`
- Components: [[protein.P0A9C0|protein.P0A9C0]], [[protein.P13033|protein.P13033]], [[protein.P0A996|protein.P0A996]]

## Enriched Summary

glpABC encodes anaerobic glycerol-3-phosphate dehydrogenase which catalyses the oxidation of glycerol-3-phosphate to dihyroxyacetone phosphate. GlpABC is a respiratory enzyme; anaerobic growth of E. coli with glycerol and fumarate induces expression of an anaerobic glycerol-3-phosphate dehydrogenase and fumarate reductase and is associated with proton translocation and the generation of a proton motive force . The GlpABC enzyme is loosely associated with the cell membrane. A functional two subunit form, GlpAB, has been isolated and characterised; it is assumed that the third subunit (GlpC) is responsible for membrane anchoring. The GlpAB complex contains contains 1 molecule of FAD and 2 non-haem irons per dimer; the GlpB subunit is thought to bind flavin mononucleotide . The GlpC subunit contains two iron-sulfur binding sites; it does not contain any transmembrane helices, so the mechanism by which it acts as the membrane anchor for the complex is not clear . Overexpressed GlpC associates with the inner membrane. GlpC is a participant in the electron transport path ( - note that this paper uses the name GlpB for the protein encoded by the third gene in the glp operon). glpABC is subject to complex transcriptional regulation...

## Biological Role

Catalyzes RXN-15740 (reaction.ecocyc.RXN-15740). Bound by FAD (molecule.C00016), FMN (molecule.C00061), an iron-sulfur cluster (molecule.ecocyc.FeS-Centers).

## Annotation

glpABC encodes anaerobic glycerol-3-phosphate dehydrogenase which catalyses the oxidation of glycerol-3-phosphate to dihyroxyacetone phosphate. GlpABC is a respiratory enzyme; anaerobic growth of E. coli with glycerol and fumarate induces expression of an anaerobic glycerol-3-phosphate dehydrogenase and fumarate reductase and is associated with proton translocation and the generation of a proton motive force . The GlpABC enzyme is loosely associated with the cell membrane. A functional two subunit form, GlpAB, has been isolated and characterised; it is assumed that the third subunit (GlpC) is responsible for membrane anchoring. The GlpAB complex contains contains 1 molecule of FAD and 2 non-haem irons per dimer; the GlpB subunit is thought to bind flavin mononucleotide . The GlpC subunit contains two iron-sulfur binding sites; it does not contain any transmembrane helices, so the mechanism by which it acts as the membrane anchor for the complex is not clear . Overexpressed GlpC associates with the inner membrane. GlpC is a participant in the electron transport path ( - note that this paper uses the name GlpB for the protein encoded by the third gene in the glp operon). glpABC is subject to complex transcriptional regulation. Expression of glpABC (along with other members of the glp regulon) is repressed by GlpR and induced by glycerol-3-phosphate; the glp regulon is subject to catabolite repression during growth in the presence of glucose (reviewed in , ). Expression of glpABC is positively regulated by the the Fnr transcription regulator . E. coli K-12 contains two glycerol-3-phosphate dehydrogenases encoded by the glpABC and glpD genes. GlpABC is required for anaerobic growth with glycerol or glycerol-3-phosphate and fumarate as the terminal electron acceptor while AE

## Outgoing Edges (1)

- `catalyzes` --> [[reaction.ecocyc.RXN-15740|reaction.ecocyc.RXN-15740]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (6)

- `binds` <-- [[molecule.C00016|molecule.C00016]] `EcoCyc` `database` - EcoCyc enzymatic reaction cofactor
- `binds` <-- [[molecule.C00061|molecule.C00061]] `EcoCyc` `database` - EcoCyc enzymatic reaction cofactor
- `binds` <-- [[molecule.ecocyc.FeS-Centers|molecule.ecocyc.FeS-Centers]] `EcoCyc` `database` - EcoCyc enzymatic reaction cofactor
- `is_component_of` <-- [[protein.P0A996|protein.P0A996]] `EcoCyc` `database` - EcoCyc component coefficient=1 | EcoCyc protcplxs.col coefficient=1
- `is_component_of` <-- [[protein.P0A9C0|protein.P0A9C0]] `EcoCyc` `database` - EcoCyc component coefficient=1 | EcoCyc protcplxs.col coefficient=1
- `is_component_of` <-- [[protein.P13033|protein.P13033]] `EcoCyc` `database` - EcoCyc component coefficient=1 | EcoCyc protcplxs.col coefficient=1

## External IDs

- `EcoCyc:ANGLYC3PDEHYDROG-CPLX`
- `QSPROTEOME:QS00049348`

## Notes

1*protein.P0A9C0|1*protein.P13033|1*protein.P0A996
