---
entity_id: "gene.b2844"
entity_type: "gene"
name: "yqeF"
source_database: "NCBI RefSeq"
source_id: "gene-b2844"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b2844"
  - "yqeF"
---

# yqeF

`gene.b2844`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b2844`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

yqeF (gene.b2844) is a gene entity. It encodes yqeF (protein.Q46939). Encoded protein function: Probable acetyl-CoA acetyltransferase (EC 2.3.1.9) (Acetoacetyl-CoA thiolase) EcoCyc product frame: G7464-MONOMER. Genomic coordinates: 2984411-2985592. EcoCyc protein note: yqeF encodes a predicted acetyl-CoA acetyltransferase . Expression of YqeF together with FucO enables engineered reversal of the fatty acid β-oxidation cycle for production of butanol . yqeF is induced during a second phase of growth on mucus when genes for anaerobic respiration, ethanolamine and fucose degradation, and the TCA cycle are induced . yqeF was shown to be upregulated in glucose-limited chemostat cultures . Mutation of the three PhoB binding sites in the yqeF-yqeG intergenic region resulted in five-fold decreased expression of yqeF .

## Biological Role

Activated by lrp (protein.P0ACJ0), crp (protein.P0ACJ8).

## Enriched Pathways

- `eco00071` Fatty acid degradation (KEGG)
- `eco00280` Valine, leucine and isoleucine degradation (KEGG)
- `eco00310` Lysine degradation (KEGG)
- `eco00362` Benzoate degradation (KEGG)
- `eco00380` Tryptophan metabolism (KEGG)
- `eco00620` Pyruvate metabolism (KEGG)
- `eco00630` Glyoxylate and dicarboxylate metabolism (KEGG)
- `eco00650` Butanoate metabolism (KEGG)
- `eco00720` Other carbon fixation pathways (KEGG)
- `eco00900` Terpenoid backbone biosynthesis (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01110` Biosynthesis of secondary metabolites (KEGG)
- `eco01120` Microbial metabolism in diverse environments (KEGG)
- `eco01200` Carbon metabolism (KEGG)
- `eco01212` Fatty acid metabolism (KEGG)
- `eco02020` Two-component system (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.Q46939|protein.Q46939]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (2)

- `activates` <-- [[protein.P0ACJ0|protein.P0ACJ0]] `RegulonDB|EcoCyc` `S` - regulator=Lrp; target=yqeF; function=+ | EcoCyc regulation TYPES=Transcription-Factor-Binding
- `activates` <-- [[protein.P0ACJ8|protein.P0ACJ8]] `RegulonDB` `S` - regulator=CRP; target=yqeF; function=+

## External IDs

- `Dbxref:ASAP:ABE-0009335,ECOCYC:G7464,GeneID:947324`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:2984411-2985592:-; feature_type=gene
