---
entity_id: "protein.P76016"
entity_type: "protein"
name: "dhaR"
source_database: "UniProt"
source_id: "P76016"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "dhaR ycgU b1201 JW5188"
---

# dhaR

`protein.P76016`

## Static

- Type: `protein`
- Source: `UniProt:P76016`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`

## Enriched Summary

FUNCTION: Positively regulates the dhaKLM operon from a sigma-70 promoter. Represses its own expression. {ECO:0000269|PubMed:15616579, ECO:0000269|PubMed:24440518}. "Dihydroxyacetone Regulator," DhaR, is negatively autoregulated and coordinately activates transcription of the divergent dha operon (dhaKLM), which encodes three subunits of the dihydroxyacetone (DHA) kinase . DhaR is inactivated when DnaK binds to the sensing domain of this regulator, in the absence of DHA . Dephosphorylated DhaL (DhaL::ADP) is an antagonist of DhaK and also is able to form complexes with the sensing domain of DhaR. In the presence of DHA, DhaL::ADP displaces DhaK or blocks the association of the DhaK/DhaR complex and DhaR activates the transcription of the dha operon . DhaR belongs to the family of bacterial enhancer-binding proteins which contain three domains: the sensing domain located in the N terminus, the central AAA+ domain, and the C-terminal domain, which contains a helix-turn-helix motif involved in the interaction with DNA. Although the C-terminal domain and the N-terminal domain from DhaR are similar to those of other members of this group, its central domain is not . The central AAA+ domain does not contain the two conserved submotifs in this family (ESELF and GAFTGA) responsible for interaction with σ54...

## Annotation

FUNCTION: Positively regulates the dhaKLM operon from a sigma-70 promoter. Represses its own expression. {ECO:0000269|PubMed:15616579, ECO:0000269|PubMed:24440518}.

## Outgoing Edges (0)

_None._

## Incoming Edges (1)

- `encodes` <-- [[gene.b1201|gene.b1201]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P76016`
- `KEGG:ecj:JW5188;eco:b1201;ecoc:C3026_07060;`
- `GeneID:945743;`
- `GO:GO:0000987; GO:0001216; GO:0005524; GO:0006071; GO:0006351; GO:0006355; GO:0032993; GO:0045893`

## Notes

PTS-dependent dihydroxyacetone kinase operon regulatory protein
