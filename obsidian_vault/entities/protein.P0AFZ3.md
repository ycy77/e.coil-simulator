---
entity_id: "protein.P0AFZ3"
entity_type: "protein"
name: "sspB"
source_database: "UniProt"
source_id: "P0AFZ3"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "sspB b3228 JW3197"
---

# sspB

`protein.P0AFZ3`

## Static

- Type: `protein`
- Source: `UniProt:P0AFZ3`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`

## Enriched Summary

FUNCTION: Enhances recognition of ssrA-tagged proteins by the ClpX-ClpP protease; the ssrA degradation tag (AANDENYALAA) is added trans-translationally to proteins that are stalled on the ribosome, freeing the ribosome and targeting stalled peptides for degradation. SspB activates the ATPase activity of ClpX. Seems to act in concert with SspA in the regulation of several proteins during exponential and stationary-phase growth.; FUNCTION: Also stimulates degradation of the N-terminus of RseA (residues 1-108, alone or in complex with sigma-E) by ClpX-ClpP in a non-ssrA-mediated fashion. The SspB protein is a specificity-enhancing factor for the ClpXP protease . When protein synthesis is stalled, incomplete proteins that are produced are tagged with the small SsrA peptide. The ribosome-associated SspB protein binds to the SsrA tag and enhances degradation of the tagged peptide by the ClpXP protease . The SspB protein forms a homodimer with two independent binding sites for SsrA-tagged proteins . It also binds to ClpX and stimulates its ATPase activity . The dimerization and SsrA binding domain resides in the amino terminal 110-120 residues of SspB, while the C-terminal 40-50 residues are required for association with ClpXP and stimulation of its ATPase activity . Efficient ClpX hexamer binding and substrate delivery requires both C-terminal domains of the SspB dimer...

## Biological Role

Component of ClpXP protease specificity-enhancing factor (complex.ecocyc.CPLX0-2681).

## Annotation

FUNCTION: Enhances recognition of ssrA-tagged proteins by the ClpX-ClpP protease; the ssrA degradation tag (AANDENYALAA) is added trans-translationally to proteins that are stalled on the ribosome, freeing the ribosome and targeting stalled peptides for degradation. SspB activates the ATPase activity of ClpX. Seems to act in concert with SspA in the regulation of several proteins during exponential and stationary-phase growth.; FUNCTION: Also stimulates degradation of the N-terminus of RseA (residues 1-108, alone or in complex with sigma-E) by ClpX-ClpP in a non-ssrA-mediated fashion.

## Outgoing Edges (1)

- `is_component_of` --> [[complex.ecocyc.CPLX0-2681|complex.ecocyc.CPLX0-2681]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2

## Incoming Edges (1)

- `encodes` <-- [[gene.b3228|gene.b3228]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P0AFZ3`
- `KEGG:ecj:JW3197;eco:b3228;ecoc:C3026_17565;`
- `GeneID:93778758;944774;`
- `GO:GO:0003723; GO:0005829; GO:0005840; GO:0009376; GO:0030163; GO:0042803; GO:0045732; GO:0051117; GO:0060090; GO:1903052`

## Notes

Stringent starvation protein B (Adapter protein SspB) (Specificity-enhancing factor SspB)
