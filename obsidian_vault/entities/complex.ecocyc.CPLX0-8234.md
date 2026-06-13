---
entity_id: "complex.ecocyc.CPLX0-8234"
entity_type: "complex"
name: "DNA-binding transcriptional repressor FrmR"
source_database: "EcoCyc"
source_id: "CPLX0-8234"
default_state: "active"
allowed_states: "active|impaired|disrupted|assembled|disassembled|inhibited"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/complex
  - source/EcoCyc
aliases:
  - "FrmR"
---

# DNA-binding transcriptional repressor FrmR

`complex.ecocyc.CPLX0-8234`

## Static

- Type: `complex`
- Source: `EcoCyc:CPLX0-8234`
- Default state: `active`
- Allowed states: `active|impaired|disrupted|assembled|disassembled|inhibited`
- Complex type: `regulatory`
- Components: [[protein.P0AAP3|protein.P0AAP3]]

## Enriched Summary

FrmR is a formaldehyde sensor and a member of the CsoR/RcnR family of transcriptional repressors . It was first identified by Herring and Blattner (2004) as a negative regulator of the frmRAB operon; its function can be inactivated by suppression of its amber stop codon . FrmR appears to also regulate genes involved in the IncP1-type plasmid conjugation mechanism . frmR expression is induced by formaldehyde, but not by S-nitrosoglutathione . Expression of frmR is induced 41-fold upon exposure of cells to the biocide polyhexamethylene biguanide. Overexpression of frmR has no effect on the MIC of polyhexamethylene biguanide . Based on in vivo and in vitro experiments, it was shown that FrmR senses the toxic chemical formaldehyde directly, with no metal dependence, via the formation of intersubunit methylene bridges between adjacent Pro2 and Cys35 residues . The X-ray structure of the formaldehyde-treated FrmR tetramer has been identified at 2.7-Å resolution . FrmR is conserved among the Proteobacteria . FrmR: "formaldehyde-induced regulator" . FrmR is a formaldehyde sensor and a member of the CsoR/RcnR family of transcriptional repressors . It was first identified by Herring and Blattner (2004) as a negative regulator of the frmRAB operon; its function can be inactivated by suppression of its amber stop codon...

## Biological Role

Component of FrmR-formaldehyde (complex.ecocyc.CPLX0-8235).

## Annotation

FrmR is a formaldehyde sensor and a member of the CsoR/RcnR family of transcriptional repressors . It was first identified by Herring and Blattner (2004) as a negative regulator of the frmRAB operon; its function can be inactivated by suppression of its amber stop codon . FrmR appears to also regulate genes involved in the IncP1-type plasmid conjugation mechanism . frmR expression is induced by formaldehyde, but not by S-nitrosoglutathione . Expression of frmR is induced 41-fold upon exposure of cells to the biocide polyhexamethylene biguanide. Overexpression of frmR has no effect on the MIC of polyhexamethylene biguanide . Based on in vivo and in vitro experiments, it was shown that FrmR senses the toxic chemical formaldehyde directly, with no metal dependence, via the formation of intersubunit methylene bridges between adjacent Pro2 and Cys35 residues . The X-ray structure of the formaldehyde-treated FrmR tetramer has been identified at 2.7-Å resolution . FrmR is conserved among the Proteobacteria . FrmR: "formaldehyde-induced regulator" .

## Outgoing Edges (1)

- `is_component_of` --> [[complex.ecocyc.CPLX0-8235|complex.ecocyc.CPLX0-8235]] `EcoCyc` `database` - EcoCyc component coefficient=

## Incoming Edges (1)

- `is_component_of` <-- [[protein.P0AAP3|protein.P0AAP3]] `EcoCyc` `database` - EcoCyc component coefficient=4 | EcoCyc protcplxs.col coefficient=4

## External IDs

- `EcoCyc:CPLX0-8234`
- `QSPROTEOME:QS00195545`

## Notes

4*protein.P0AAP3
