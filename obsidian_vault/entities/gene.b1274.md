---
entity_id: "gene.b1274"
entity_type: "gene"
name: "topA"
source_database: "NCBI RefSeq"
source_id: "gene-b1274"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b1274"
  - "topA"
---

# topA

`gene.b1274`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b1274`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

topA (gene.b1274) is a gene entity. It encodes topA (protein.P06612). Encoded protein function: FUNCTION: Releases the supercoiling and torsional tension of DNA, which is introduced during the DNA replication and transcription, by transiently cleaving and rejoining one strand of the DNA duplex. Introduces a single-strand break via transesterification at a target site in duplex DNA. The scissile phosphodiester is attacked by the catalytic tyrosine of the enzyme, resulting in the formation of a DNA-(5'-phosphotyrosyl)-enzyme intermediate and the expulsion of a 3'-OH DNA strand. The free DNA strand then undergoes passage around the unbroken strand, thus removing DNA supercoils. Finally, in the religation step, the DNA 3'-OH attacks the covalent intermediate to expel the active-site tyrosine and restore the DNA phosphodiester backbone. {ECO:0000255|HAMAP-Rule:MF_00952, ECO:0000269|PubMed:10681504, ECO:0000269|PubMed:21482796, ECO:0000269|PubMed:9497321}. EcoCyc product frame: EG11013-MONOMER. EcoCyc synonyms: supX. Genomic coordinates: 1331048-1333645. EcoCyc protein note: E. coli possess multiple DNA topoisomerases which coordinate, as well as compete, in order to maintain chromosomes in the appropriate topological state commensurate with their need for replication and transcription...

## Biological Role

Repressed by fis (protein.P0A6R3), lrp (protein.P0ACJ0). Activated by rpoD (protein.P00579), fis (protein.P0A6R3), rpoH (protein.P0AGB3), rpoS (protein.P13445).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P06612|protein.P06612]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (6)

- `activates` <-- [[protein.P00579|protein.P00579]] `RegulonDB` `S` - sigma=sigma70; target=topA; function=+
- `activates` <-- [[protein.P0A6R3|protein.P0A6R3]] `RegulonDB` `C` - regulator=Fis; target=topA; function=-+
- `activates` <-- [[protein.P0AGB3|protein.P0AGB3]] `RegulonDB` `S` - sigma=sigma32; target=topA; function=+
- `activates` <-- [[protein.P13445|protein.P13445]] `RegulonDB` `S` - sigma=sigma38; target=topA; function=+
- `represses` <-- [[protein.P0A6R3|protein.P0A6R3]] `RegulonDB` `C` - regulator=Fis; target=topA; function=-+
- `represses` <-- [[protein.P0ACJ0|protein.P0ACJ0]] `EcoCyc` `database` - EcoCyc regulation TYPES=Transcription-Factor-Binding

## External IDs

- `Dbxref:ASAP:ABE-0004275,ECOCYC:EG11013,GeneID:945862`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:1331048-1333645:+; feature_type=gene
