---
entity_id: "gene.b2038"
entity_type: "gene"
name: "rfbC"
source_database: "NCBI RefSeq"
source_id: "gene-b2038"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b2038"
  - "rfbC"
---

# rfbC

`gene.b2038`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b2038`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

rfbC (gene.b2038) is a gene entity. It encodes rfbC (protein.P37745). Encoded protein function: FUNCTION: Catalyzes the epimerization of the C3' and C5'positions of dTDP-6-deoxy-D-xylo-4-hexulose, forming dTDP-6-deoxy-L-lyxo-4-hexulose. {ECO:0000250|UniProtKB:P26394}. EcoCyc product frame: DTDPDEHYDRHAMEPIM-MONOMER. EcoCyc synonyms: rfbD, rmlC. Genomic coordinates: 2109581-2110138. EcoCyc protein note: dTDP-4-dehydrorhamnose 3,5-epimerase is involved in the dTDP-rhamnose biosynthesis pathway, which is important for the synthesis of O-specific LPS. dTDP-4-dehydrorhamnose 3,5-epimerase forms a complex with dTDP-4-dehydrorhamnose reductase, which is known as dTDP-L-rhamnose synthetase. The epimerase catalyzes inversion at C-3 and C-5 via corresponding enediols, but these molecules cannot be released from the enzyme. The reductase then catalyzes the stereospecific reduction of the 4-keto group of dTDP-4-dehydro-6-deoxy-L-mannose. dTDP-4-dehydrorhamnose 3,5-epimerase is coded for by the rfbC gene. rfbC was identified in a screen for genes that reduce the lethal effects of stress. An rfbC insertion mutant is more sensitive than wild type to mitomycin C and other stresses . The genes encoding the enzymes involved in the biosynthesis of O-specific polysaccharides are clustered in the rfb region. E...

## Biological Role

Activated by nac (protein.Q47005).

## Enriched Pathways

- `eco00521` Streptomycin biosynthesis (KEGG)
- `eco00523` Polyketide sugar unit biosynthesis (KEGG)
- `eco00541` Biosynthesis of various nucleotide sugars (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01110` Biosynthesis of secondary metabolites (KEGG)
- `eco01250` Biosynthesis of nucleotide sugars (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P37745|protein.P37745]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (1)

- `activates` <-- [[protein.Q47005|protein.Q47005]] `RegulonDB|EcoCyc` `S` - regulator=Nac; target=rfbC; function=+ | EcoCyc regulation TYPES=Transcription-Factor-Binding

## External IDs

- `Dbxref:ASAP:ABE-0006759,ECOCYC:EG11979,GeneID:947482`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:2109581-2110138:-; feature_type=gene
