---
entity_id: "gene.b1584"
entity_type: "gene"
name: "speG"
source_database: "NCBI RefSeq"
source_id: "gene-b1584"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b1584"
  - "speG"
---

# speG

`gene.b1584`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b1584`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

speG (gene.b1584) is a gene entity. It encodes speG (protein.P0A951). Encoded protein function: FUNCTION: Involved in the protection against polyamine toxicity by regulating their concentration (PubMed:10986239, PubMed:7642535). Catalyzes the transfer of an acetyl group from acetyl coenzyme A (AcCoA) to the primary amino groups of spermidine to yield N(1)- and N(8)-acetylspermidine (PubMed:6297970, PubMed:7052085, PubMed:8077207). It can also use spermine, but not putrescine (PubMed:7052085). {ECO:0000269|PubMed:10986239, ECO:0000269|PubMed:6297970, ECO:0000269|PubMed:7052085, ECO:0000269|PubMed:7642535, ECO:0000269|PubMed:8077207}.; FUNCTION: In addition, may act as a modulator of transcription through its ability to interact with the two-component response regulator RcsB. Inhibits transcription of the small RNA regulator rprA in an acetylation-independent manner. Interaction with the DNA-binding domain of RcsB might be responsible for SpeG-dependent inhibition of RcsB-dependent rprA transcription (PubMed:30562360). SpeG does not acetylate RcsB in vitro (PubMed:30562360). {ECO:0000269|PubMed:30562360}. EcoCyc product frame: SPERMACTRAN-MONOMER. Genomic coordinates: 1656184-1656744.

## Biological Role

Repressed by gadX (protein.P37639).

## Enriched Pathways

- `eco00330` Arginine and proline metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0A951|protein.P0A951]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (1)

- `represses` <-- [[protein.P37639|protein.P37639]] `RegulonDB` `S` - regulator=GadX; target=speG; function=-

## External IDs

- `Dbxref:ASAP:ABE-0005286,ECOCYC:G6842,GeneID:946117`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:1656184-1656744:+; feature_type=gene
