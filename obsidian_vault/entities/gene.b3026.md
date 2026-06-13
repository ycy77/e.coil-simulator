---
entity_id: "gene.b3026"
entity_type: "gene"
name: "qseC"
source_database: "NCBI RefSeq"
source_id: "gene-b3026"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b3026"
  - "qseC"
---

# qseC

`gene.b3026`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b3026`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

qseC (gene.b3026) is a gene entity. It encodes qseC (protein.P40719). Encoded protein function: FUNCTION: Member of a two-component regulatory system QseB/QseC. Activates the flagella regulon by activating transcription of FlhDC. May activate QseB by phosphorylation. {ECO:0000269|PubMed:11929534}. EcoCyc product frame: MONOMER0-4171. EcoCyc synonyms: ygiY. Genomic coordinates: 3170484-3171833. EcoCyc protein note: This is the His-246 phosphorylated form of EG12658-MONOMER "QseC" - the sensor histidine kinase of the QseBC two-component signal transduction system. EcoCyc protein note: QseC is the sensor kinase component of the QseB-QseC two-component system which is involved in the activation of flagella and motility genes; QseBC modulates transcription of flhDC, the master regulator for flagella and motility genes . QseC contains two predicted transmembrane helices, a dimerization domain which contains the predicted site (His-246) of autophosphorylation and an 'orthodox-type' ATP-binding kinase domain (see ). QseC is predicted to have both histidine autokinase and phosphotransferase activity; the QseBC system has been well studied in enterohemorrhagic (EHEC) and uropathogenic (UPAC) E...

## Biological Role

Activated by basR (protein.P30843), qseB (protein.P52076).

## Enriched Pathways

- `eco02020` Two-component system (KEGG)
- `eco02024` Quorum sensing (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P40719|protein.P40719]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (2)

- `activates` <-- [[protein.P30843|protein.P30843]] `RegulonDB` `S` - regulator=BasR; target=qseC; function=+
- `activates` <-- [[protein.P52076|protein.P52076]] `RegulonDB` `S` - regulator=QseB; target=qseC; function=+

## External IDs

- `Dbxref:ASAP:ABE-0009938,ECOCYC:EG12658,GeneID:947174`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:3170484-3171833:+; feature_type=gene
