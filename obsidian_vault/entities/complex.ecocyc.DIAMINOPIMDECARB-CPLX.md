---
entity_id: "complex.ecocyc.DIAMINOPIMDECARB-CPLX"
entity_type: "complex"
name: "diaminopimelate decarboxylase"
source_database: "EcoCyc"
source_id: "DIAMINOPIMDECARB-CPLX"
default_state: "active"
allowed_states: "active|impaired|disrupted|assembled|disassembled|inhibited"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/complex
  - source/EcoCyc
aliases:
---

# diaminopimelate decarboxylase

`complex.ecocyc.DIAMINOPIMDECARB-CPLX`

## Static

- Type: `complex`
- Source: `EcoCyc:DIAMINOPIMDECARB-CPLX`
- Default state: `active`
- Allowed states: `active|impaired|disrupted|assembled|disassembled|inhibited`
- Complex type: `structural`
- Components: [[protein.P00861|protein.P00861]]

## Enriched Summary

Diaminopimelate decarboxylase (LysA) catalyzes the last step in lysine biosynthesis, the decarboxylation of meso-diaminopimelate to produce lysine . first isolated a 200 kDa protein complex, indicating that LysA functions as a homotetramer, while , using a His-tagged protein, identified the monomer as the active form. Using analytical ultracentrifugation and small angle X-ray scattering, the active form has now been identified as the homodimer . lysA mutants require L-lysine for growth and are unable to grow with diaminopimelate . Growth phenotypes of different lysA mutants were characterized using phenotype microarrays . The lysA27 mutant, which encodes a Ser384Phe substitution, requires glycine betaine for protein folding . Expression of lysA is activated by LysR and ArgP and may be controlled by RpoS during growth in minimal medium . lysA promoter activity during activation of the lysine biosynthesis pathway has been measured . Compared to other promoters of genes in the lysine biosynthesis pathway, the lysA promoter has a significantly slower transition rate between its active and inactive states . A temperature-sensitive mutation in this gene was identified that showed potential as a growth-switch for genetic engineering...

## Biological Role

Catalyzes DIAMINOPIMDECARB-RXN (reaction.ecocyc.DIAMINOPIMDECARB-RXN). Bound by Pyridoxal phosphate (molecule.C00018).

## Annotation

Diaminopimelate decarboxylase (LysA) catalyzes the last step in lysine biosynthesis, the decarboxylation of meso-diaminopimelate to produce lysine . first isolated a 200 kDa protein complex, indicating that LysA functions as a homotetramer, while , using a His-tagged protein, identified the monomer as the active form. Using analytical ultracentrifugation and small angle X-ray scattering, the active form has now been identified as the homodimer . lysA mutants require L-lysine for growth and are unable to grow with diaminopimelate . Growth phenotypes of different lysA mutants were characterized using phenotype microarrays . The lysA27 mutant, which encodes a Ser384Phe substitution, requires glycine betaine for protein folding . Expression of lysA is activated by LysR and ArgP and may be controlled by RpoS during growth in minimal medium . lysA promoter activity during activation of the lysine biosynthesis pathway has been measured . Compared to other promoters of genes in the lysine biosynthesis pathway, the lysA promoter has a significantly slower transition rate between its active and inactive states . A temperature-sensitive mutation in this gene was identified that showed potential as a growth-switch for genetic engineering . Review:

## Outgoing Edges (1)

- `catalyzes` --> [[reaction.ecocyc.DIAMINOPIMDECARB-RXN|reaction.ecocyc.DIAMINOPIMDECARB-RXN]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (2)

- `binds` <-- [[molecule.C00018|molecule.C00018]] `EcoCyc` `database` - EcoCyc enzymatic reaction cofactor
- `is_component_of` <-- [[protein.P00861|protein.P00861]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2

## External IDs

- `EcoCyc:DIAMINOPIMDECARB-CPLX`
- `QSPROTEOME:QS00188577`

## Notes

2*protein.P00861
