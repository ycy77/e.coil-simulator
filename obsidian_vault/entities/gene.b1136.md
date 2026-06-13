---
entity_id: "gene.b1136"
entity_type: "gene"
name: "icd"
source_database: "NCBI RefSeq"
source_id: "gene-b1136"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b1136"
  - "icd"
---

# icd

`gene.b1136`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b1136`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

icd (gene.b1136) is a gene entity. It encodes icd (protein.P08200). Encoded protein function: FUNCTION: Catalyzes the oxidative decarboxylation of isocitrate to 2-oxoglutarate and carbon dioxide with the concomitant reduction of NADP(+). {ECO:0000269|PubMed:21151122, ECO:0000269|PubMed:3112144, ECO:0000269|PubMed:4400493, ECO:0000269|PubMed:7761851, ECO:0000269|PubMed:7819221}. EcoCyc product frame: ISOCITDEH-SUBUNIT. EcoCyc synonyms: icdE, icdA. Genomic coordinates: 1195123-1196373.

## Biological Role

Repressed by DNA-binding transcriptional dual regulator IHF (complex.ecocyc.PC00027), arcA (protein.P0A9Q1). Activated by rpoD (protein.P00579), cra (protein.P0ACP1), nac (protein.Q47005).

## Enriched Pathways

- `eco00020` Citrate cycle (TCA cycle) (KEGG)
- `eco00480` Glutathione metabolism (KEGG)
- `eco00720` Other carbon fixation pathways (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01110` Biosynthesis of secondary metabolites (KEGG)
- `eco01120` Microbial metabolism in diverse environments (KEGG)
- `eco01200` Carbon metabolism (KEGG)
- `eco01210` 2-Oxocarboxylic acid metabolism (KEGG)
- `eco01230` Biosynthesis of amino acids (KEGG)
- `eco04146` Peroxisome (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P08200|protein.P08200]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (5)

- `activates` <-- [[protein.P00579|protein.P00579]] `RegulonDB` `S` - sigma=sigma70; target=icd; function=+
- `activates` <-- [[protein.P0ACP1|protein.P0ACP1]] `RegulonDB` `S` - regulator=Cra; target=icd; function=+
- `activates` <-- [[protein.Q47005|protein.Q47005]] `RegulonDB|EcoCyc` `S` - regulator=Nac; target=icd; function=+ | EcoCyc regulation TYPES=Transcription-Factor-Binding
- `represses` <-- [[complex.ecocyc.PC00027|complex.ecocyc.PC00027]] `EcoCyc` `database` - EcoCyc regulation TYPES=Transcription-Factor-Binding
- `represses` <-- [[protein.P0A9Q1|protein.P0A9Q1]] `RegulonDB` `C` - regulator=ArcA; target=icd; function=-

## External IDs

- `Dbxref:ASAP:ABE-0003823,ECOCYC:EG10489,GeneID:945702`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:1195123-1196373:+; feature_type=gene
