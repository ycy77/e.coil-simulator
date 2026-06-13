---
entity_id: "gene.b1201"
entity_type: "gene"
name: "dhaR"
source_database: "NCBI RefSeq"
source_id: "gene-b1201"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b1201"
  - "dhaR"
---

# dhaR

`gene.b1201`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b1201`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

dhaR (gene.b1201) is a gene entity. It encodes dhaR (protein.P76016). Encoded protein function: FUNCTION: Positively regulates the dhaKLM operon from a sigma-70 promoter. Represses its own expression. {ECO:0000269|PubMed:15616579, ECO:0000269|PubMed:24440518}. EcoCyc product frame: G6628-MONOMER. EcoCyc synonyms: ycgU. Genomic coordinates: 1251066-1252985. EcoCyc protein note: "Dihydroxyacetone Regulator," DhaR, is negatively autoregulated and coordinately activates transcription of the divergent dha operon (dhaKLM), which encodes three subunits of the dihydroxyacetone (DHA) kinase . DhaR is inactivated when DnaK binds to the sensing domain of this regulator, in the absence of DHA . Dephosphorylated DhaL (DhaL::ADP) is an antagonist of DhaK and also is able to form complexes with the sensing domain of DhaR. In the presence of DHA, DhaL::ADP displaces DhaK or blocks the association of the DhaK/DhaR complex and DhaR activates the transcription of the dha operon . DhaR belongs to the family of bacterial enhancer-binding proteins which contain three domains: the sensing domain located in the N terminus, the central AAA+ domain, and the C-terminal domain, which contains a helix-turn-helix motif involved in the interaction with DNA. Although the C-terminal domain and the N-terminal domain from DhaR are similar to those of other members of this group, its central domain is not...

## Biological Role

Activated by nac (protein.Q47005).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P76016|protein.P76016]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (1)

- `activates` <-- [[protein.Q47005|protein.Q47005]] `RegulonDB|EcoCyc` `S` - regulator=Nac; target=dhaR; function=+ | EcoCyc regulation TYPES=Transcription-Factor-Binding

## External IDs

- `Dbxref:ASAP:ABE-0004033,ECOCYC:G6628,GeneID:945743`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:1251066-1252985:+; feature_type=gene
