---
entity_id: "gene.b2041"
entity_type: "gene"
name: "rfbB"
source_database: "NCBI RefSeq"
source_id: "gene-b2041"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b2041"
  - "rfbB"
---

# rfbB

`gene.b2041`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b2041`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

rfbB (gene.b2041) is a gene entity. It encodes rfbB (protein.P37759). Encoded protein function: FUNCTION: Catalyzes the dehydration of dTDP-D-glucose to form dTDP-6-deoxy-D-xylo-4-hexulose via a three-step process involving oxidation, dehydration and reduction. {ECO:0000250|UniProtKB:P27830}. EcoCyc product frame: DTDPGLUCDEHYDRAT-MONOMER. EcoCyc synonyms: som, rmlB. Genomic coordinates: 2111976-2113061. EcoCyc protein note: dTDP-glucose 4,6-dehydratase (RfbB) is involved in the dTDP-rhamnose biosynthesis pathway, which is important for the synthesis of O-specific LPS. This enzyme catalyzes the conversion of dTDP-α-D-glucose into dTDP-4-keto-6-deoxyglucose. This reaction occurs in three steps: dehydrogenation, dehydration, and rereduction. The coenzyme NAD+ mediates the dehydrogenation and rereduction steps of the reaction . The reduction of enzyme-bound NAD+ to NADH results in a conformational change in the protein such that the substrate cannot be released at a significant rate from this form of the enzyme, thus the intermediates in the normal catalytic process remain tightly bound to the enzyme . The genes encoding the enzymes involved in the biosynthesis of O-specific polysaccharides are clustered in the rfb region. E. coli K-12 does not normally express O-specific LPS due to mutations in the rfb region. However, genes in the rfb cluster have been identified...

## Biological Role

Repressed by nac (protein.Q47005). Activated by glaR (protein.P37338).

## Enriched Pathways

- `eco00521` Streptomycin biosynthesis (KEGG)
- `eco00523` Polyketide sugar unit biosynthesis (KEGG)
- `eco00525` Acarbose and validamycin biosynthesis (KEGG)
- `eco00541` Biosynthesis of various nucleotide sugars (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01110` Biosynthesis of secondary metabolites (KEGG)
- `eco01250` Biosynthesis of nucleotide sugars (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P37759|protein.P37759]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (2)

- `activates` <-- [[protein.P37338|protein.P37338]] `RegulonDB|EcoCyc` `S` - regulator=GlaR; target=rfbB; function=+ | EcoCyc regulation TYPES=Transcription-Factor-Binding
- `represses` <-- [[protein.Q47005|protein.Q47005]] `RegulonDB|EcoCyc` `S` - regulator=Nac; target=rfbB; function=- | EcoCyc regulation TYPES=Transcription-Factor-Binding

## External IDs

- `Dbxref:ASAP:ABE-0006766,ECOCYC:EG12412,GeneID:945276`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:2111976-2113061:-; feature_type=gene
