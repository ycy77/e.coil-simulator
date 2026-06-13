---
entity_id: "gene.b3025"
entity_type: "gene"
name: "qseB"
source_database: "NCBI RefSeq"
source_id: "gene-b3025"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b3025"
  - "qseB"
---

# qseB

`gene.b3025`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b3025`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

qseB (gene.b3025) is a gene entity. It encodes qseB (protein.P52076). Encoded protein function: FUNCTION: Member of a two-component regulatory system QseB/QseC. Activates the flagella regulon by activating transcription of FlhDC. Currently it is not known whether this effect is direct or not. {ECO:0000269|PubMed:11929534}. EcoCyc product frame: MONOMER0-2741. EcoCyc synonyms: ygiX. Genomic coordinates: 3169828-3170487. EcoCyc protein note: QseB, "quorum-sensing E. coli regulator B", is the response regulator component of the QseB-QseC two-component system, which is one component of the quorum-sensing regulatory cascade involved in the regulation of biofilm formation, motility and flagella genes by activating transcription of flhDC, an operon that encodes the master regulator of these genes .QseB also regulates replication initiation by regulating DnaA expression . This protein also may have an undetermined role in metal metabolism, because qseBC deletion mutants show hypersensitivity to several toxic cations . QseB forms complexes with the chaperone DnaK and with the cell division protein FtsZ . QseB and QseC of enterohemorrhagic E. coli (EHEC) and of E. coli K-12 are almost identical; there are only three amino acid differences in QseB and only eight amino acid differences in QseC between these strains...

## Biological Role

Repressed by lrp (protein.P0ACJ0). Activated by basR (protein.P30843), qseB (protein.P52076).

## Enriched Pathways

- `eco02020` Two-component system (KEGG)
- `eco02024` Quorum sensing (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P52076|protein.P52076]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (3)

- `activates` <-- [[protein.P30843|protein.P30843]] `RegulonDB` `S` - regulator=BasR; target=qseB; function=+
- `activates` <-- [[protein.P52076|protein.P52076]] `RegulonDB` `S` - regulator=QseB; target=qseB; function=+
- `represses` <-- [[protein.P0ACJ0|protein.P0ACJ0]] `EcoCyc` `database` - EcoCyc regulation TYPES=Transcription-Factor-Binding

## External IDs

- `Dbxref:ASAP:ABE-0009936,ECOCYC:G7575,GeneID:945369`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:3169828-3170487:+; feature_type=gene
