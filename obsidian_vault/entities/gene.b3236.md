---
entity_id: "gene.b3236"
entity_type: "gene"
name: "mdh"
source_database: "NCBI RefSeq"
source_id: "gene-b3236"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b3236"
  - "mdh"
---

# mdh

`gene.b3236`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b3236`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

mdh (gene.b3236) is a gene entity. It encodes mdh (protein.P61889). Encoded protein function: FUNCTION: Catalyzes the reversible oxidation of malate to oxaloacetate. {ECO:0000255|HAMAP-Rule:MF_01516, ECO:0000269|PubMed:2993232, ECO:0000269|PubMed:7028159}. EcoCyc product frame: MALATE-DEHASE-MONOMER. Genomic coordinates: 3383330-3384268.

## Biological Role

Repressed by [2Fe-2S] cluster DNA-binding transcriptional dual regulator (complex.ecocyc.CPLX0-7639), fur (protein.P0A9A9), arcA (protein.P0A9Q1), btsR (protein.P0AFT5). Activated by rpoD (protein.P00579), dpiA (protein.P0AEF4).

## Enriched Pathways

- `eco00020` Citrate cycle (TCA cycle) (KEGG)
- `eco00270` Cysteine and methionine metabolism (KEGG)
- `eco00566` Sulfoquinovose metabolism (KEGG)
- `eco00620` Pyruvate metabolism (KEGG)
- `eco00630` Glyoxylate and dicarboxylate metabolism (KEGG)
- `eco00680` Methane metabolism (KEGG)
- `eco00710` Carbon fixation by Calvin cycle (KEGG)
- `eco00720` Other carbon fixation pathways (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01110` Biosynthesis of secondary metabolites (KEGG)
- `eco01120` Microbial metabolism in diverse environments (KEGG)
- `eco01200` Carbon metabolism (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P61889|protein.P61889]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (6)

- `activates` <-- [[protein.P00579|protein.P00579]] `RegulonDB` `S` - sigma=sigma70; target=mdh; function=+
- `activates` <-- [[protein.P0AEF4|protein.P0AEF4]] `RegulonDB` `S` - regulator=DpiA; target=mdh; function=+
- `represses` <-- [[complex.ecocyc.CPLX0-7639|complex.ecocyc.CPLX0-7639]] `EcoCyc` `database` - EcoCyc regulation TYPES=Transcription-Factor-Binding
- `represses` <-- [[protein.P0A9A9|protein.P0A9A9]] `RegulonDB` `S` - regulator=Fur; target=mdh; function=-
- `represses` <-- [[protein.P0A9Q1|protein.P0A9Q1]] `EcoCyc` `database` - EcoCyc regulation TYPES=Transcription-Factor-Binding
- `represses` <-- [[protein.P0AFT5|protein.P0AFT5]] `RegulonDB` `S` - regulator=BtsR; target=mdh; function=-

## External IDs

- `Dbxref:ASAP:ABE-0010613,ECOCYC:EG10576,GeneID:947854`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:3383330-3384268:-; feature_type=gene
