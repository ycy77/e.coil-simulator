---
entity_id: "gene.b0619"
entity_type: "gene"
name: "dpiB"
source_database: "NCBI RefSeq"
source_id: "gene-b0619"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b0619"
  - "dpiB"
---

# dpiB

`gene.b0619`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b0619`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

dpiB (gene.b0619) is a gene entity. It encodes dpiB (protein.P77510). Encoded protein function: FUNCTION: Member of the two-component regulatory system DpiA/DpiB, which is essential for expression of citrate-specific fermentation genes and genes involved in plasmid inheritance. Could be involved in response to both the presence of citrate and external redox conditions. Functions as a sensor kinase that phosphorylates DpiA in the presence of citrate. {ECO:0000269|PubMed:11889485, ECO:0000269|PubMed:19202292}. EcoCyc product frame: PHOSPHO-DPIB. EcoCyc synonyms: ybeP, mpdB, citA. Genomic coordinates: 652235-653893. EcoCyc protein note: Represents the His-347 phosphorylated form of G6345-MONOMER "DpiB" - the sensor histidine kinase of the DpiBA two-component signal transduction system. EcoCyc protein note: DpiB is the membrane associated sensor kinase of the DpiAB two component system which regulates the expression of genes involved in co-substrate dependent anaerobic citrate fermentation. Sequence analysis suggests that DpiB contains a periplasmic sensing domain surrounded by two transmembrane segments plus a cytoplasmic effector domain . The purified periplasmic domain of DpiB has a high affinity for citrate in vitro; it also binds isocitrate and tricarballylate...

## Biological Role

Repressed by chiX (gene.b4585). Activated by dcuR (protein.P0AD01), dpiA (protein.P0AEF4).

## Enriched Pathways

- `eco02020` Two-component system (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P77510|protein.P77510]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (3)

- `activates` <-- [[protein.P0AD01|protein.P0AD01]] `RegulonDB` `S` - regulator=DcuR; target=dpiB; function=+
- `activates` <-- [[protein.P0AEF4|protein.P0AEF4]] `RegulonDB` `S` - regulator=DpiA; target=dpiB; function=+
- `represses` <-- [[gene.b4585|gene.b4585]] `RegulonDB` `S` - regulator=ChiX; target=dpiB; function=-

## External IDs

- `Dbxref:ASAP:ABE-0002129,ECOCYC:G6345,GeneID:945233`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:652235-653893:+; feature_type=gene
