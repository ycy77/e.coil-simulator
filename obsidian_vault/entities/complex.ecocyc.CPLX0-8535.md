---
entity_id: "complex.ecocyc.CPLX0-8535"
entity_type: "complex"
name: "diguanylate cyclase DgcE"
source_database: "EcoCyc"
source_id: "CPLX0-8535"
default_state: "active"
allowed_states: "active|impaired|disrupted|assembled|disassembled|inhibited"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/complex
  - source/EcoCyc
aliases:
---

# diguanylate cyclase DgcE

`complex.ecocyc.CPLX0-8535`

## Static

- Type: `complex`
- Source: `EcoCyc:CPLX0-8535`
- Default state: `active`
- Allowed states: `active|impaired|disrupted|assembled|disassembled|inhibited`
- Complex type: `regulatory`
- Components: [[protein.P38097|protein.P38097]]

## Enriched Summary

Curli amyloid fibers are thin, coiled surface structures composed of a polymer of a single type of subunit, EG11489-MONOMER, encoded by the EG11489 gene . Curli are the key component of the extracellular matrix produced during biofilm formation by Escherichia coli and related Enterobacteriaceae and are involved in inert surface colonization, biofilm formation, and bacterial binding to a variety of extracellular matrix and serum proteins . DgcE is an EC-2.7.7.65, that is involved in regulation of the switch from flagellar motility to sessile behavior and curli expression . The C-DI-GMP (c-di-GMP) produced by DgcE is hydrolyzed by the phosphodiesterase EG12252 PdeH. The EG12396 DgcE/EG12252 PdeH signalling module acts through a second diguanylate cyclase/phosphodiesterase module, G6673 DgcM/G6639 PdeR, which forms a ternary complex with the transcription factor EG12008 MlrA. MlrA modulates the expression of G6546 CsgD, a transcriptional regulator that controls expression of the TU00390 operon that encodes the proteins involved in curli production . Curli expression is heterogeneous - it does not occur within all cells that occupy the same position within a biofilm . This bimodal expression was also observed in a well-stirred planktonic culture, indicating that it is not due to microenvironmental gradients...

## Biological Role

Catalyzes RXN0-5359 (reaction.ecocyc.RXN0-5359).

## Annotation

Curli amyloid fibers are thin, coiled surface structures composed of a polymer of a single type of subunit, EG11489-MONOMER, encoded by the EG11489 gene . Curli are the key component of the extracellular matrix produced during biofilm formation by Escherichia coli and related Enterobacteriaceae and are involved in inert surface colonization, biofilm formation, and bacterial binding to a variety of extracellular matrix and serum proteins . DgcE is an EC-2.7.7.65, that is involved in regulation of the switch from flagellar motility to sessile behavior and curli expression . The C-DI-GMP (c-di-GMP) produced by DgcE is hydrolyzed by the phosphodiesterase EG12252 PdeH. The EG12396 DgcE/EG12252 PdeH signalling module acts through a second diguanylate cyclase/phosphodiesterase module, G6673 DgcM/G6639 PdeR, which forms a ternary complex with the transcription factor EG12008 MlrA. MlrA modulates the expression of G6546 CsgD, a transcriptional regulator that controls expression of the TU00390 operon that encodes the proteins involved in curli production . Curli expression is heterogeneous - it does not occur within all cells that occupy the same position within a biofilm . This bimodal expression was also observed in a well-stirred planktonic culture, indicating that it is not due to microenvironmental gradients . Removal of the regulatory network does not abolish the bimodality of curli gene expression . DgcE consists of an N-terminal MASE1 (Membrane-Associated SEnsor) domain, which includes ten putative membrane segments and is found in proteins associated with signal transduction ; three cytoplasmic PAS/PAC domains; the GGDEF domain associated with diguanylate cyclase activity; and a degenerate EAL domain . The MASE1, PAS and GGDEF domains are required for function, while the

## Outgoing Edges (1)

- `catalyzes` --> [[reaction.ecocyc.RXN0-5359|reaction.ecocyc.RXN0-5359]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (1)

- `is_component_of` <-- [[protein.P38097|protein.P38097]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2

## External IDs

- `EcoCyc:CPLX0-8535`
- `QSPROTEOME:QS00196897`

## Notes

2*protein.P38097
