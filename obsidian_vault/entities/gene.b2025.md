---
entity_id: "gene.b2025"
entity_type: "gene"
name: "hisF"
source_database: "NCBI RefSeq"
source_id: "gene-b2025"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b2025"
  - "hisF"
---

# hisF

`gene.b2025`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b2025`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

hisF (gene.b2025) is a gene entity. It encodes hisF (protein.P60664). Encoded protein function: FUNCTION: IGPS catalyzes the conversion of PRFAR and glutamine to IGP, AICAR and glutamate. The HisF subunit catalyzes the cyclization activity that produces IGP and AICAR from PRFAR using the ammonia provided by the HisH subunit. EcoCyc product frame: CYCLASE-MONOMER. Genomic coordinates: 2095844-2096620. EcoCyc protein note: HisF is the synthase subunit of imidazole glycerol phosphate synthase (HisFH). HisFH catalyzes the fifth step of histidine biosynthesis, as well as generates aminoimidazole carboxamide ribonucleotide, an intermediate in purine nucleotide biosynthesis. The two components of the HisFH dimer work together to catalyze the addition of nitrogen from glutamine to the imidazole ring of phosphoribulosylformimino-AICAR-phosphate to generate aminoimidazole carboxamide ribonucleotide, D-erythro-imidazole-glycerol-phosphate, and glutamate . Although isolated HisH has no activity, isolated HisF catalyzes an ammonia-dependent reaction that uses ammonia as a nitrogen donor in the place of the physiological donor glutamine . The kinetics of HisFH have been modeled . HisFH is a 1:1 dimer of HisF and HisH . The critical residues involved in subunit interaction in general and in the specific case of cooperation of the two active sites have been examined...

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

- `encodes` --> [[protein.P60664|protein.P60664]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (1)

- `activates` <-- [[protein.P00579|protein.P00579]] `RegulonDB` `S` - sigma=sigma70; target=hisF; function=+

## External IDs

- `Dbxref:ASAP:ABE-0006727,ECOCYC:EG10448,GeneID:946516`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:2095844-2096620:+; feature_type=gene
