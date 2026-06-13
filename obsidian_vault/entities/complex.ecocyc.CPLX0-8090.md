---
entity_id: "complex.ecocyc.CPLX0-8090"
entity_type: "complex"
name: "diguanylate cyclase DgcM"
source_database: "EcoCyc"
source_id: "CPLX0-8090"
default_state: "active"
allowed_states: "active|impaired|disrupted|assembled|disassembled|inhibited"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/complex
  - source/EcoCyc
aliases:
---

# diguanylate cyclase DgcM

`complex.ecocyc.CPLX0-8090`

## Static

- Type: `complex`
- Source: `EcoCyc:CPLX0-8090`
- Default state: `active`
- Allowed states: `active|impaired|disrupted|assembled|disassembled|inhibited`
- Complex type: `regulatory`
- Components: [[protein.P77302|protein.P77302]]

## Enriched Summary

Curli amyloid fibers are thin, coiled surface structures composed of a polymer of a single type of subunit, EG11489-MONOMER, encoded by the EG11489 gene . Curli are the key component of the extracellular matrix produced during biofilm formation by Escherichia coli and related Enterobacteriaceae and are involved in inert surface colonization, biofilm formation, and bacterial binding to a variety of extracellular matrix and serum proteins . Curli production is controlled by a complex signaling cascade, with the EG12396 DgcE/EG12252 PdeH diguanylate cyclase (DGC)/phosphodiesterase (PDE) pair acting upstream of G6639 PdeR, which itself is upstream of the DGC G6673 DgcM, and all acting upstream of the EG12008 "MlrA transcription factor". MlrA controls expression of G6546 "CsgD transcriptional regulator", which controls the transcription of the TU00390 operon, encoding curli production . The G6639-MONOMER PdeR phosphodiesterase inhibits DgcM; this inhibition is relieved when PdeR binds and hydrolyzes C-DI-GMP (c-di-GMP), allowing DgcM to activate the transcription factor EG12008-MONOMER MlrA. Production of c-di-GMP by DgcM contributes to, but is not essential for MlrA activation by DgcM . Curli expression is heterogeneous - it does not occur within all cells that occupy the same position within a biofilm...

## Biological Role

Catalyzes RXN0-5359 (reaction.ecocyc.RXN0-5359).

## Annotation

Curli amyloid fibers are thin, coiled surface structures composed of a polymer of a single type of subunit, EG11489-MONOMER, encoded by the EG11489 gene . Curli are the key component of the extracellular matrix produced during biofilm formation by Escherichia coli and related Enterobacteriaceae and are involved in inert surface colonization, biofilm formation, and bacterial binding to a variety of extracellular matrix and serum proteins . Curli production is controlled by a complex signaling cascade, with the EG12396 DgcE/EG12252 PdeH diguanylate cyclase (DGC)/phosphodiesterase (PDE) pair acting upstream of G6639 PdeR, which itself is upstream of the DGC G6673 DgcM, and all acting upstream of the EG12008 "MlrA transcription factor". MlrA controls expression of G6546 "CsgD transcriptional regulator", which controls the transcription of the TU00390 operon, encoding curli production . The G6639-MONOMER PdeR phosphodiesterase inhibits DgcM; this inhibition is relieved when PdeR binds and hydrolyzes C-DI-GMP (c-di-GMP), allowing DgcM to activate the transcription factor EG12008-MONOMER MlrA. Production of c-di-GMP by DgcM contributes to, but is not essential for MlrA activation by DgcM . Curli expression is heterogeneous - it does not occur within all cells that occupy the same position within a biofilm . This bimodal expression was also observed in a well-stirred planktonic culture, indicating that it is not due to microenvironmental gradients . Removal of the regulatory network does not abolish the bimodality of curli gene expression . DgcM does not play a global regulatory role; csgD transcription may be its only target. PdeR acts antagonistically to DgcM . Genetic analysis using epistasis experiments elucidated the presence of a signaling cascade, with the EG12396 DgcE/E

## Outgoing Edges (1)

- `catalyzes` --> [[reaction.ecocyc.RXN0-5359|reaction.ecocyc.RXN0-5359]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (1)

- `is_component_of` <-- [[protein.P77302|protein.P77302]] `EcoCyc` `database` - EcoCyc component coefficient=4 | EcoCyc protcplxs.col coefficient=4

## External IDs

- `EcoCyc:CPLX0-8090`
- `QSPROTEOME:QS00195647`

## Notes

4*protein.P77302
