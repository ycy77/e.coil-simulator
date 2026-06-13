---
entity_id: "gene.b2023"
entity_type: "gene"
name: "hisH"
source_database: "NCBI RefSeq"
source_id: "gene-b2023"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b2023"
  - "hisH"
---

# hisH

`gene.b2023`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b2023`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

hisH (gene.b2023) is a gene entity. It encodes hisH (protein.P60595). Encoded protein function: FUNCTION: IGPS catalyzes the conversion of PRFAR and glutamine to IGP, AICAR and glutamate. The HisH subunit catalyzes the hydrolysis of glutamine to glutamate and ammonia as part of the synthesis of IGP and AICAR. The resulting ammonia molecule is channeled to the active site of HisF. {ECO:0000269|PubMed:8494895}. EcoCyc product frame: GLUTAMIDOTRANS-MONOMER. Genomic coordinates: 2094535-2095125. EcoCyc protein note: HisH is the glutamine amidotransferase subunit of imidazole glycerol phosphate synthase (HisFH). HisFH catalyzes the fifth step of histidine biosynthesis, as well as generates aminoimidazole carboxamide ribonucleotide, an intermediate in purine nucleotide biosynthesis. The two components of the HisFH dimer work together to catalyze the addition of nitrogen from glutamine to the imidazole ring of phosphoribulosylformimino-AICAR-phosphate to generate aminoimidazole carboxamide ribonucleotide, D-erythro-imidazole-glycerol-phosphate, and glutamate . Although isolated HisH has no activity, isolated HisF catalyzes an ammonia-dependent reaction that uses ammonia as a nitrogen donor in the place of the physiological donor glutamine . The kinetics of HisFH have been modeled . HisFH is a 1:1 dimer of HisF and HisH...

## Biological Role

Activated by rpoD (protein.P00579).

## Enriched Pathways

- `eco00340` Histidine metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01110` Biosynthesis of secondary metabolites (KEGG)
- `eco01230` Biosynthesis of amino acids (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P60595|protein.P60595]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (1)

- `activates` <-- [[protein.P00579|protein.P00579]] `RegulonDB` `S` - sigma=sigma70; target=hisH; function=+

## External IDs

- `Dbxref:ASAP:ABE-0006722,ECOCYC:EG10450,GeneID:946544`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:2094535-2095125:+; feature_type=gene
