---
entity_id: "complex.ecocyc.CPLX0-8583"
entity_type: "complex"
name: "phosphoglucosamine mutase"
source_database: "EcoCyc"
source_id: "CPLX0-8583"
default_state: "active"
allowed_states: "active|impaired|disrupted|assembled|disassembled|inhibited"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/complex
  - source/EcoCyc
aliases:
---

# phosphoglucosamine mutase

`complex.ecocyc.CPLX0-8583`

## Static

- Type: `complex`
- Source: `EcoCyc:CPLX0-8583`
- Default state: `active`
- Allowed states: `active|impaired|disrupted|assembled|disassembled|inhibited`
- Complex type: `structural`
- Components: [[protein.P31120|protein.P31120]]

## Enriched Summary

Phosphoglucosamine mutase catalyzes the interconversion of the glucosamine-6-phosphate (GlcN-6-P) and glucosamine-1-phosphate (GlcN-1-P) isomers. The enzyme is active only in phosphorylated form ; it can autophosphorylate in vitro in the presence of ATP to a low level . The modified amino acid is the serine residue S102 . Only approximately 5% of GlmM protein purified from wild-type cells is phosphorylated, but this may be an artifact of the purification procedure . The in vivo mechanism of activation/phosphorylation of the enzyme is still unclear. Using a method that distinguishes N-phosphorylation from O-phosphorylation, His103 residue was also found to be phosphorylated . Using chemoproteomics analysis with a stable analogue of 3-pHis, this protein was identified as a putative phosphohistidine acceptor at 2 amino acids . The phosphoglucosamine mutase reaction follows a ping-pong bi-bi mechanism, where glucosamine-1,6-diphosphate acts as both the first product and the second substrate. Once the enzyme is phosphorylated, it no longer requires glucosamine-1,6-diphosphate as a cofactor . When analyzed by gel filtration, the protein behaves as a trimer at pH 8.4; the degree of aggregation increases at pH 7.4 . However, phosphoglucosamine mutases from other organisms, e.g. Staphylococcus aureus, form homodimers...

## Biological Role

Catalyzes 5.4.2.10-RXN (reaction.ecocyc.5.4.2.10-RXN). Bound by glucosamine 1,6-diphosphate (molecule.ecocyc.CPD0-1096).

## Annotation

Phosphoglucosamine mutase catalyzes the interconversion of the glucosamine-6-phosphate (GlcN-6-P) and glucosamine-1-phosphate (GlcN-1-P) isomers. The enzyme is active only in phosphorylated form ; it can autophosphorylate in vitro in the presence of ATP to a low level . The modified amino acid is the serine residue S102 . Only approximately 5% of GlmM protein purified from wild-type cells is phosphorylated, but this may be an artifact of the purification procedure . The in vivo mechanism of activation/phosphorylation of the enzyme is still unclear. Using a method that distinguishes N-phosphorylation from O-phosphorylation, His103 residue was also found to be phosphorylated . Using chemoproteomics analysis with a stable analogue of 3-pHis, this protein was identified as a putative phosphohistidine acceptor at 2 amino acids . The phosphoglucosamine mutase reaction follows a ping-pong bi-bi mechanism, where glucosamine-1,6-diphosphate acts as both the first product and the second substrate. Once the enzyme is phosphorylated, it no longer requires glucosamine-1,6-diphosphate as a cofactor . When analyzed by gel filtration, the protein behaves as a trimer at pH 8.4; the degree of aggregation increases at pH 7.4 . However, phosphoglucosamine mutases from other organisms, e.g. Staphylococcus aureus, form homodimers . Unlike GlmM from the Gram-positive bacterium Staphylococcus aureus, E. coli GlmM does not inhibit the function of S. aureus DacA . When shifted to the restrictive temperature, conditional glmM mutant cells lose their rod shape and stop growth . GlmM: "glucosamine mutase" Review:

## Outgoing Edges (1)

- `catalyzes` --> [[reaction.ecocyc.5.4.2.10-RXN|reaction.ecocyc.5.4.2.10-RXN]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (2)

- `binds` <-- [[molecule.ecocyc.CPD0-1096|molecule.ecocyc.CPD0-1096]] `EcoCyc` `database` - EcoCyc enzymatic reaction cofactor
- `is_component_of` <-- [[protein.P31120|protein.P31120]] `EcoCyc` `database` - EcoCyc component coefficient=3 | EcoCyc protcplxs.col coefficient=3

## External IDs

- `EcoCyc:CPLX0-8583`
- `QSPROTEOME:QS00196595`

## Notes

3*protein.P31120
