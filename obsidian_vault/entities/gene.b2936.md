---
entity_id: "gene.b2936"
entity_type: "gene"
name: "loiP"
source_database: "NCBI RefSeq"
source_id: "gene-b2936"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b2936"
  - "loiP"
---

# loiP

`gene.b2936`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b2936`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

loiP (gene.b2936) is a gene entity. It encodes loiP (protein.P25894). Encoded protein function: FUNCTION: Metalloprotease that cleaves substrates preferentially between Phe-Phe residues. Plays a role in response to some stress conditions. Seems to regulate the expression of speB. {ECO:0000269|PubMed:1310091, ECO:0000269|PubMed:17651431, ECO:0000269|PubMed:17909889, ECO:0000269|PubMed:22491786}. EcoCyc product frame: EG11291-MONOMER. EcoCyc synonyms: yggG. Genomic coordinates: 3081913-3082671. EcoCyc protein note: LoiP is an outer membrane metalloprotease that preferentially cleaves between Phe/Phe residues . LoiP is predicted to be a lipoprotein with a type II signal peptide . The protein is associated with the membrane fraction . LoiP is an outer membrane lipoprotein . LoiP has one intramolecular S-S bond plus one additional cysteine that mediates lipid attachment . Expression of loiP is upregulated in response to stress (heat shock, UV irradiation) and in an era-1 mutant background . loiP is upregulated and increased amounts of LoiP are produced when cells are grown in low osmolarity media . Overexpression of full-length loiP inhibits growth . There is no significant difference in growth between wild-type and a loiP deletion strain when grown in low osmolarity media...

## Biological Role

Activated by rpoD (protein.P00579).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P25894|protein.P25894]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (1)

- `activates` <-- [[protein.P00579|protein.P00579]] `RegulonDB` `S` - sigma=sigma70; target=loiP; function=+

## External IDs

- `Dbxref:ASAP:ABE-0009629,ECOCYC:EG11291,GeneID:945173`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:3081913-3082671:+; feature_type=gene
