---
entity_id: "gene.b3911"
entity_type: "gene"
name: "cpxA"
source_database: "NCBI RefSeq"
source_id: "gene-b3911"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b3911"
  - "cpxA"
---

# cpxA

`gene.b3911`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b3911`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

cpxA (gene.b3911) is a gene entity. It encodes cpxA (protein.P0AE82). Encoded protein function: FUNCTION: Histidine kinase member of the two-component regulatory system CpxA/CpxR which responds to envelope stress response by activating expression of downstream genes including cpxP, degP, dsbA and ppiA (PubMed:7883164, PubMed:9401031, PubMed:9473036). Activates CpxR by phosphorylation; has autokinase, phosphotransferase and (in the presence of Mg(2+) and/or ATP or ADP) phosphatase activity (PubMed:17259177, PubMed:24492262, PubMed:9401031). The kinase activity is inhibited by periplasmic accessory protein CpxP; proteolysis of CpxP relieves inhibition (PubMed:16166523, PubMed:17259177, PubMed:25207645). Involved in several diverse cellular processes, including the functioning of acetohydroxyacid synthetase I, the biosynthesis of isoleucine and valine, the TraJ protein activation activity for tra gene expression in F plasmid (PubMed:8432716), and the synthesis, translocation, or stability of cell envelope proteins (PubMed:7883164). Activates transcription of periplasmic protease degP, probably by phosphorylating the cognate response protein CpxR; overexpression of an outer membrane lipoprotein NlpE also leads to transcription of degP via CpxRA (PubMed:7883164)...

## Biological Role

Activated by cpxR (protein.P0AE88).

## Enriched Pathways

- `eco01503` Cationic antimicrobial peptide (CAMP) resistance (KEGG)
- `eco02020` Two-component system (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0AE82|protein.P0AE82]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (1)

- `activates` <-- [[protein.P0AE88|protein.P0AE88]] `RegulonDB` `S` - regulator=CpxR; target=cpxA; function=+

## External IDs

- `Dbxref:ASAP:ABE-0012772,ECOCYC:EG10163,GeneID:948405`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:4103602-4104975:-; feature_type=gene
