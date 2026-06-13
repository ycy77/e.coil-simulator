---
entity_id: "gene.b0110"
entity_type: "gene"
name: "ampD"
source_database: "NCBI RefSeq"
source_id: "gene-b0110"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b0110"
  - "ampD"
---

# ampD

`gene.b0110`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b0110`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

ampD (gene.b0110) is a gene entity. It encodes ampD (protein.P13016). Encoded protein function: FUNCTION: Involved in cell wall peptidoglycan recycling (PubMed:19309146). Specifically cleaves the amide bond between the lactyl group of N-acetylmuramic acid and the alpha-amino group of the L-alanine in degradation products containing an anhydro N-acetylmuramyl moiety (PubMed:19309146). Is also involved in beta-lactamase induction (PubMed:2607970, PubMed:2691840). {ECO:0000269|PubMed:19309146, ECO:0000269|PubMed:2607970, ECO:0000269|PubMed:2691840}. EcoCyc product frame: EG10041-MONOMER. Genomic coordinates: 118733-119284. EcoCyc protein note: AmpD is a cytosolic N-acetylmuramyl-L-alanine amidase responsible for breakdown of anhMurNAc-linked peptides, releasing the peptides for recycling . Unlike in Citrobacter freundii or Enterobacter cloacae, the native EG10040-MONOMER AmpC β-lactamase of E. coli is not inducible by β-lactam antibiotics due to lack of the AmpR regulator. In Enterobacter cloacae, the signal molecule for AmpR-dependent induction of ampC expression is anhMurNAc-pentapeptide . In an ampD mutant, 1,6-anhydro-N-acetylmuramyl-L-alanyl-D-glutamyl-meso-diaminopimelic acid (anhMurNAc-tripeptide) accumulates in the cytoplasm and, after export, in the periplasm . ampD is a member of the ampDE operon . Reviews:

## Biological Role

Repressed by nac (protein.Q47005).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P13016|protein.P13016]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (1)

- `represses` <-- [[protein.Q47005|protein.Q47005]] `RegulonDB|EcoCyc` `S` - regulator=Nac; target=ampD; function=- | EcoCyc regulation TYPES=Transcription-Factor-Binding

## External IDs

- `Dbxref:ASAP:ABE-0000380,ECOCYC:EG10041,GeneID:948877`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:118733-119284:+; feature_type=gene
