---
entity_id: "gene.b2074"
entity_type: "gene"
name: "mdtA"
source_database: "NCBI RefSeq"
source_id: "gene-b2074"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b2074"
  - "mdtA"
---

# mdtA

`gene.b2074`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b2074`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

mdtA (gene.b2074) is a gene entity. It encodes mdtA (protein.P76397). Encoded protein function: FUNCTION: The MdtABC tripartite complex confers resistance against novobiocin and deoxycholate. MdtABC requires TolC for its function. {ECO:0000269|PubMed:12107133, ECO:0000269|PubMed:12107134}. EcoCyc product frame: MDTA. EcoCyc synonyms: yegM. Genomic coordinates: 2154016-2155263. EcoCyc protein note: MdtA is the membrane fusion protein (MFP) of a tripartite efflux pump that is implicated in resistance to antibiotics, bile salt derivatives and SDS. MdtA exhibits 47% similarity and 28% identity to the AcrA membrane fusion protein .

## Biological Role

Activated by DNA-binding transcriptional dual regulator Cra (complex.ecocyc.PC00061), cpxR (protein.P0AE88), baeR (protein.P69228).

## Enriched Pathways

- `eco02020` Two-component system (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P76397|protein.P76397]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (3)

- `activates` <-- [[complex.ecocyc.PC00061|complex.ecocyc.PC00061]] `EcoCyc` `database` - EcoCyc regulation TYPES=Transcription-Factor-Binding
- `activates` <-- [[protein.P0AE88|protein.P0AE88]] `RegulonDB` `S` - regulator=CpxR; target=mdtA; function=+
- `activates` <-- [[protein.P69228|protein.P69228]] `RegulonDB` `S` - regulator=BaeR; target=mdtA; function=+

## External IDs

- `Dbxref:ASAP:ABE-0006872,ECOCYC:G7113,GeneID:946604`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:2154016-2155263:+; feature_type=gene
