---
entity_id: "gene.b3197"
entity_type: "gene"
name: "kdsD"
source_database: "NCBI RefSeq"
source_id: "gene-b3197"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b3197"
  - "kdsD"
---

# kdsD

`gene.b3197`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b3197`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

kdsD (gene.b3197) is a gene entity. It encodes kdsD (protein.P45395). Encoded protein function: FUNCTION: Involved in the biosynthesis of 3-deoxy-D-manno-octulosonate (KDO), a unique 8-carbon sugar component of lipopolysaccharides (LPSs). KdsD is not essential in the KDO biosynthesis and can be substituted by GutQ. Catalyzes the reversible aldol-ketol isomerization between D-ribulose 5-phosphate (Ru5P) and D-arabinose 5-phosphate (A5P). {ECO:0000269|PubMed:12805358, ECO:0000269|PubMed:16199563, ECO:0000269|PubMed:16765569, ECO:0000269|PubMed:20039350}. EcoCyc product frame: G7662-MONOMER. EcoCyc synonyms: yrbH. Genomic coordinates: 3341266-3342252. EcoCyc protein note: D-arabinose-5-phosphate is a precursor for KDO (2-keto-3-deoxy-octulosonate), a constituent of the cell envelope lipopolysaccharide. Arabinose-5-phosphate isomerase is responsible for the interconversion of D-ribulose-5-phosphate and D-arabinose-5-phosphate, the first committed step in the biosynthesis of KDO. The enzyme was originally isolated and partially characterized from E. coli strain B . KdsD is a tetramer in solution. The reaction kinetics, specificity, and optimal conditions have been characterized, and the physical characteristics of the active site are discussed . Substrate specificity was investigated by saturation transfer difference NMR spectroscopy...

## Biological Role

Activated by rpoD (protein.P00579).

## Enriched Pathways

- `eco00541` Biosynthesis of various nucleotide sugars (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01250` Biosynthesis of nucleotide sugars (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P45395|protein.P45395]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (1)

- `activates` <-- [[protein.P00579|protein.P00579]] `RegulonDB` `S` - sigma=sigma70; target=kdsD; function=+

## External IDs

- `Dbxref:ASAP:ABE-0010504,ECOCYC:G7662,GeneID:947734`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:3341266-3342252:+; feature_type=gene
