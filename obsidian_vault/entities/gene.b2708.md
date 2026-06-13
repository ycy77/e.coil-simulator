---
entity_id: "gene.b2708"
entity_type: "gene"
name: "gutQ"
source_database: "NCBI RefSeq"
source_id: "gene-b2708"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b2708"
  - "gutQ"
---

# gutQ

`gene.b2708`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b2708`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

gutQ (gene.b2708) is a gene entity. It encodes gutQ (protein.P17115). Encoded protein function: FUNCTION: Catalyzes the reversible aldol-ketol isomerization between D-ribulose 5-phosphate (Ru5P) and D-arabinose 5-phosphate (A5P). It appears that the physiological function of G-API may be to synthesize the regulatory molecule A5P, which in turn participates in the induction of the gut operon through an unknown mechanism. It is also able of sustaining the biosynthetic pathway of 3-deoxy-D-manno-octulosonate (KDO), a unique 8-carbon sugar component of lipopolysaccharides (LPSs). {ECO:0000269|PubMed:16199563}. EcoCyc product frame: EG10973-MONOMER. EcoCyc synonyms: srlQ. Genomic coordinates: 2829813-2830778. EcoCyc protein note: D-arabinose-5-phosphate is a precursor for 2-keto-3-deoxy-octulosonate (KDO), a constituent of the cell envelope lipopolysaccharide. Arabinose-5-phosphate isomerase is responsible for the interconversion of D-ribulose-5-phosphate and D-arabinose-5-phosphate, the first committed step in the biosynthesis of KDO. The enzyme was originally isolated and partially characterized from E. coli strain B . gutQ encodes the second of two D-arabinose 5-phosphate isomerases (API) in E. coli. Its biochemical properties are very similar to those of CPLX0-1262 KdsD, the first identified D-arabinose 5-phosphate isomerase...

## Biological Role

Activated by rpoD (protein.P00579).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P17115|protein.P17115]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (1)

- `activates` <-- [[protein.P00579|protein.P00579]] `RegulonDB` `S` - sigma=sigma70; target=gutQ; function=+

## External IDs

- `Dbxref:ASAP:ABE-0008902,ECOCYC:EG10973,GeneID:947587`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:2829813-2830778:+; feature_type=gene
