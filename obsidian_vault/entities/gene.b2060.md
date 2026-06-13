---
entity_id: "gene.b2060"
entity_type: "gene"
name: "wzc"
source_database: "NCBI RefSeq"
source_id: "gene-b2060"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b2060"
  - "wzc"
---

# wzc

`gene.b2060`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b2060`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

wzc (gene.b2060) is a gene entity. It encodes wzc (protein.P76387). Encoded protein function: FUNCTION: Required for the extracellular polysaccharide colanic acid synthesis. The autophosphorylated form is inactive. Probably involved in the export of colanic acid from the cell to medium. Phosphorylates udg. {ECO:0000269|PubMed:12851388}. EcoCyc product frame: G7105-MONOMER. Genomic coordinates: 2133490-2135652. EcoCyc protein note: The G7105 gene encodes a bacterial tyrosine (BY) kinase that regulates production of the extracellular polysaccharide CPD-21504 "colanic acid" (CA). Purified Wzc, incubated in the presence of ATP, autophosphorylates on a tyrosine residue; phosphorylated Wzc is dephosphorylated by G7106-MONOMER Wzb . Wzc-autophosphorylation negatively regulates colanic acid biosynthesis, and Wzb phosphatase activity counteracts this negative regulation . Both the phosphorylated and nonphosphorylated forms of Wzc are required for wild-type synthesis of CA in a CA-producing K-12 strain; Wzc phosphorylation influences the size distribution of CA; Wzc has an ATPase activity in addition to its kinase activity . Wzc also catalyzes tyrosine phosphorylation of UGD-MONOMER (Ugd) and this phosphorylation stimulates Ugd activity...

## Biological Role

Repressed by nac (protein.Q47005). Activated by rpoD (protein.P00579), rpoE (protein.P0AGB6).

## Enriched Pathways

- `eco02020` Two-component system (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P76387|protein.P76387]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (3)

- `activates` <-- [[protein.P00579|protein.P00579]] `RegulonDB` `S` - sigma=sigma70; target=wzc; function=+
- `activates` <-- [[protein.P0AGB6|protein.P0AGB6]] `RegulonDB` `S` - sigma=sigma24; target=wzc; function=+
- `represses` <-- [[protein.Q47005|protein.Q47005]] `RegulonDB|EcoCyc` `S` - regulator=Nac; target=wzc; function=- | EcoCyc regulation TYPES=Transcription-Factor-Binding

## External IDs

- `Dbxref:ASAP:ABE-0006819,ECOCYC:G7105,GeneID:946567`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:2133490-2135652:-; feature_type=gene
