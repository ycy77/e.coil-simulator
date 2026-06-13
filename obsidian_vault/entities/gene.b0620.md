---
entity_id: "gene.b0620"
entity_type: "gene"
name: "dpiA"
source_database: "NCBI RefSeq"
source_id: "gene-b0620"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b0620"
  - "dpiA"
---

# dpiA

`gene.b0620`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b0620`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

dpiA (gene.b0620) is a gene entity. It encodes dpiA (protein.P0AEF4). Encoded protein function: FUNCTION: Member of the two-component regulatory system DpiA/DpiB, which is essential for expression of citrate-specific fermentation genes and genes involved in plasmid inheritance. Could be involved in response to both the presence of citrate and external redox conditions. Regulates the transcription of citCDEFXGT, dpiAB, mdh and exuT. Binds specifically to the dpiB-citC intergenic region. {ECO:0000269|PubMed:18997424, ECO:0000269|PubMed:19202292}. EcoCyc product frame: PHOSPHO-DPIA. EcoCyc synonyms: citB, criR, mpdA. Genomic coordinates: 653862-654542. EcoCyc protein note: CitB/DpiA is a dual transcriptional regulator involved in anaerobic citrate catabolism. In the presence of citrate and under anaerobic conditions it activates genes for citrate fermentation, the citCDEFXGT operon, the citAB operon, and mdh, as well as the exuTR operon for dissimilation of hexuronate . Due to the ability of CitB/DpiA to bind to A/T-rich sequences, multiple other roles have been assigned to CitB. When overexpressed in E. coli, it destabilizes plasmid inheritance, represses transcription of appY, encoding a regulator of anaerobic metabolism, and induces the SOS response by competing with DnaA and DnaB in binding to A/T-rich sequences at the replication origin...

## Biological Role

Repressed by chiX (gene.b4585). Activated by dcuR (protein.P0AD01), dpiA (protein.P0AEF4).

## Enriched Pathways

- `eco02020` Two-component system (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0AEF4|protein.P0AEF4]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (3)

- `activates` <-- [[protein.P0AD01|protein.P0AD01]] `RegulonDB` `S` - regulator=DcuR; target=dpiA; function=+
- `activates` <-- [[protein.P0AEF4|protein.P0AEF4]] `RegulonDB` `S` - regulator=DpiA; target=dpiA; function=+
- `represses` <-- [[gene.b4585|gene.b4585]] `RegulonDB` `S` - regulator=ChiX; target=dpiA; function=-

## External IDs

- `Dbxref:ASAP:ABE-0002131,ECOCYC:G6346,GeneID:947008`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:653862-654542:+; feature_type=gene
