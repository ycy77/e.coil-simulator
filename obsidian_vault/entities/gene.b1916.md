---
entity_id: "gene.b1916"
entity_type: "gene"
name: "sdiA"
source_database: "NCBI RefSeq"
source_id: "gene-b1916"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b1916"
  - "sdiA"
---

# sdiA

`gene.b1916`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b1916`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

sdiA (gene.b1916) is a gene entity. It encodes sdiA (protein.P07026). Encoded protein function: FUNCTION: Activates cell division by specifically increasing transcription from one of the two promoters that lie immediately upstream of the ftsQAZ gene cluster. Activates ydiV expression in response to extracellular autoinducer AI-1 (Vibrio fischeri autoinducer oxoC6). {ECO:0000269|PubMed:18560382, ECO:0000269|PubMed:1915297}. EcoCyc product frame: PD02198. Genomic coordinates: 1996110-1996832. EcoCyc protein note: The transcription factor SdiA, for "Suppressor of the cell division inhibitor," is possibly positively autoregulated and controls the transcription of the genes involved in cell division and acid tolerance . SdiA has been shown to increase transcription from the P2 promoter of the ftsQAZ operon by facilitating RNA polymerase binding to the promoter region . SdiA activates the expression of ydiV, which is involved in the interaction between two quorum-sensing systems. An sdiA ydiV double mutant reduces cAMP levels, which inhibits quorum-sensing system 2 . Expression of sdiA itself is regulated by a mechanism similar to quorum sensing: exposure to conditioned medium results in a 50-80% decrease in sdiA expression . The transcriptional activity of SdiA is affected not only by quorum signaling but also by other environmental factors, such as oxidation...

## Biological Role

Repressed by carbon storage regulator CsrA (complex.ecocyc.CPLX0-7956), csrA (protein.P69913), nac (protein.Q47005). Activated by [2Fe-2S] cluster DNA-binding transcriptional dual regulator (complex.ecocyc.CPLX0-7639), ATP-dependent RNA helicase DeaD (complex.ecocyc.CPLX0-8557), rpoD (protein.P00579), fur (protein.P0A9A9).

## Enriched Pathways

- `eco02020` Two-component system (KEGG)
- `eco02024` Quorum sensing (KEGG)
- `eco02026` Biofilm formation - Escherichia coli (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P07026|protein.P07026]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (7)

- `activates` <-- [[complex.ecocyc.CPLX0-7639|complex.ecocyc.CPLX0-7639]] `EcoCyc` `database` - EcoCyc regulation TYPES=Transcription-Factor-Binding
- `activates` <-- [[complex.ecocyc.CPLX0-8557|complex.ecocyc.CPLX0-8557]] `EcoCyc` `database` - EcoCyc regulation TYPES=Protein-Mediated-Translation-Regulation
- `activates` <-- [[protein.P00579|protein.P00579]] `RegulonDB` `S` - sigma=sigma70; target=sdiA; function=+
- `activates` <-- [[protein.P0A9A9|protein.P0A9A9]] `RegulonDB` `S` - regulator=Fur; target=sdiA; function=+
- `represses` <-- [[complex.ecocyc.CPLX0-7956|complex.ecocyc.CPLX0-7956]] `EcoCyc` `database` - EcoCyc regulation TYPES=Protein-Mediated-Translation-Regulation
- `represses` <-- [[protein.P69913|protein.P69913]] `RegulonDB` `C` - regulator=carbon storage regulator CsrA; target=sdiA; function=-
- `represses` <-- [[protein.Q47005|protein.Q47005]] `RegulonDB` `S` - regulator=Nac; target=sdiA; function=-

## External IDs

- `Dbxref:ASAP:ABE-0006381,ECOCYC:EG10935,GeneID:946421`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:1996110-1996832:-; feature_type=gene
