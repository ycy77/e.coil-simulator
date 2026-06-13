---
entity_id: "complex.ecocyc.E1P-CPLX"
entity_type: "complex"
name: "pyruvate dehydrogenase"
source_database: "EcoCyc"
source_id: "E1P-CPLX"
default_state: "active"
allowed_states: "active|impaired|disrupted|assembled|disassembled|inhibited"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/complex
  - source/EcoCyc
aliases:
---

# pyruvate dehydrogenase

`complex.ecocyc.E1P-CPLX`

## Static

- Type: `complex`
- Source: `EcoCyc:E1P-CPLX`
- Default state: `active`
- Allowed states: `active|impaired|disrupted|assembled|disassembled|inhibited`
- Complex type: `regulatory`
- Components: [[protein.P0AFG8|protein.P0AFG8]]

## Enriched Summary

It is sometimes confusing that this component and the PYRUVATEDEH-CPLX "multi-enzyme complex" both carry the same name. AceE has many lysine residues that are acetylated (see Protein Features tab for details). Mutation studies reveal acetyl phosphate and PHOSACETYLTRANS-MONOMER play a role in acetylation and results in decreased pyruvate dehydrogenase activity, while ACETATEKINA-MONOMER and G6577-MONOMER play a role in deacetylation and results in increased AceE activity and pyruvate accumulation relative to wild-type. Multiple residues in AceE were affected . AceE was identified as a putative phosphohistidine acceptor by using chemoproteomics analysis with a stable analogue of 3-pHis . The mRNA of aceE appears to interact with the small regulatory RNA GlnZ and the expression of transcripts corresponding to the 5 UTR of aceE decreases when GlnZ is overexpressed . Several metabolic genes, including aceE, were found upregulated in two MG1655 lysogens carrying closely related Stx2a phages O104 and PA8 . Certain mutations in aceE rescue growth of DXS-MONOMER Dxs-defective mutants by enabling the production of sufficient DXP in vivo . It is sometimes confusing that this component and the PYRUVATEDEH-CPLX "multi-enzyme complex" both carry the same name. AceE has many lysine residues that are acetylated (see Protein Features tab for details)...

## Biological Role

Catalyzes RXN0-1134 (reaction.ecocyc.RXN0-1134). Component of pyruvate dehydrogenase (complex.ecocyc.PYRUVATEDEH-CPLX).

## Annotation

It is sometimes confusing that this component and the PYRUVATEDEH-CPLX "multi-enzyme complex" both carry the same name. AceE has many lysine residues that are acetylated (see Protein Features tab for details). Mutation studies reveal acetyl phosphate and PHOSACETYLTRANS-MONOMER play a role in acetylation and results in decreased pyruvate dehydrogenase activity, while ACETATEKINA-MONOMER and G6577-MONOMER play a role in deacetylation and results in increased AceE activity and pyruvate accumulation relative to wild-type. Multiple residues in AceE were affected . AceE was identified as a putative phosphohistidine acceptor by using chemoproteomics analysis with a stable analogue of 3-pHis . The mRNA of aceE appears to interact with the small regulatory RNA GlnZ and the expression of transcripts corresponding to the 5 UTR of aceE decreases when GlnZ is overexpressed . Several metabolic genes, including aceE, were found upregulated in two MG1655 lysogens carrying closely related Stx2a phages O104 and PA8 . Certain mutations in aceE rescue growth of DXS-MONOMER Dxs-defective mutants by enabling the production of sufficient DXP in vivo .

## Outgoing Edges (2)

- `catalyzes` --> [[reaction.ecocyc.RXN0-1134|reaction.ecocyc.RXN0-1134]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_component_of` --> [[complex.ecocyc.PYRUVATEDEH-CPLX|complex.ecocyc.PYRUVATEDEH-CPLX]] `EcoCyc` `database` - EcoCyc component coefficient=12

## Incoming Edges (1)

- `is_component_of` <-- [[protein.P0AFG8|protein.P0AFG8]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2

## External IDs

- `EcoCyc:E1P-CPLX`
- `QSPROTEOME:QS00154921`
- `PDB:1RP7`

## Notes

2*protein.P0AFG8
