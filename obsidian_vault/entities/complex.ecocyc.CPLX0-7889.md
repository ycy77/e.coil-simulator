---
entity_id: "complex.ecocyc.CPLX0-7889"
entity_type: "complex"
name: "EF-P-lysine lysyltransferase"
source_database: "EcoCyc"
source_id: "CPLX0-7889"
default_state: "active"
allowed_states: "active|impaired|disrupted|assembled|disassembled|inhibited"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/complex
  - source/EcoCyc
aliases:
---

# EF-P-lysine lysyltransferase

`complex.ecocyc.CPLX0-7889`

## Static

- Type: `complex`
- Source: `EcoCyc:CPLX0-7889`
- Default state: `active`
- Allowed states: `active|impaired|disrupted|assembled|disassembled|inhibited`
- Complex type: `structural`
- Components: [[protein.P0A8N7|protein.P0A8N7]]

## Enriched Summary

EpmA specifically aminoacylates the EG12099-MONOMER at the ε-amino group of Lys34 with lysine . EF-P is a structural mimic of tRNA; it appears to be the only cellular target for lysylation by EpmA . Site-directed mutagenesis identified residues within EpmA that are critical for activity, and residues within EF-P that are critical for its ability to be modified. Co-expression of EpmB enhances the lysylation of EF-P by EpmA in vivo . EpmA has sequence similarity to the class II LysRS tRNA aminoacyltransferase, but lacks the anticodon binding domain. The enzyme is able to catalyze ATP-dependent activation of lysine and lysine analogs by formation of a lysine adenylate ; (R)-β-lysine is the most efficient substrate . EpmA was originally suggested to regulate pyruvate oxidase and named PoxA. The pyruvate oxidase activity of a epmA mutant is severalfold decreased compared to wild type . An epmA mutant shows pleiotropic phenotypes (including drug sensitivities) distinct from the phenotypes of a poxB mutant, which lacks pyruvate oxidase . A structural alignment and crystal structure shows that EpmA has similarity to the catalytic core of the class II lysyl-tRNA synthetase, but lacking the tRNA anticodon binding domain. Physical clustering and phylogenetic analysis have implicated EpmA in a pathway for the modification of a lysine residue in EG12099-MONOMER...

## Biological Role

Catalyzes RXN0-6999 (reaction.ecocyc.RXN0-6999).

## Annotation

EpmA specifically aminoacylates the EG12099-MONOMER at the ε-amino group of Lys34 with lysine . EF-P is a structural mimic of tRNA; it appears to be the only cellular target for lysylation by EpmA . Site-directed mutagenesis identified residues within EpmA that are critical for activity, and residues within EF-P that are critical for its ability to be modified. Co-expression of EpmB enhances the lysylation of EF-P by EpmA in vivo . EpmA has sequence similarity to the class II LysRS tRNA aminoacyltransferase, but lacks the anticodon binding domain. The enzyme is able to catalyze ATP-dependent activation of lysine and lysine analogs by formation of a lysine adenylate ; (R)-β-lysine is the most efficient substrate . EpmA was originally suggested to regulate pyruvate oxidase and named PoxA. The pyruvate oxidase activity of a epmA mutant is severalfold decreased compared to wild type . An epmA mutant shows pleiotropic phenotypes (including drug sensitivities) distinct from the phenotypes of a poxB mutant, which lacks pyruvate oxidase . A structural alignment and crystal structure shows that EpmA has similarity to the catalytic core of the class II lysyl-tRNA synthetase, but lacking the tRNA anticodon binding domain. Physical clustering and phylogenetic analysis have implicated EpmA in a pathway for the modification of a lysine residue in EG12099-MONOMER . epmA plays a role for growth in LB at moderately low pH . EpmA: "EF-P post-translational modification A"

## Outgoing Edges (1)

- `catalyzes` --> [[reaction.ecocyc.RXN0-6999|reaction.ecocyc.RXN0-6999]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (1)

- `is_component_of` <-- [[protein.P0A8N7|protein.P0A8N7]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2

## External IDs

- `EcoCyc:CPLX0-7889`
- `QSPROTEOME:QS00167031`

## Notes

2*protein.P0A8N7
