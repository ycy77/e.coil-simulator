---
entity_id: "gene.b2557"
entity_type: "gene"
name: "purL"
source_database: "NCBI RefSeq"
source_id: "gene-b2557"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b2557"
  - "purL"
---

# purL

`gene.b2557`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b2557`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

purL (gene.b2557) is a gene entity. It encodes purL (protein.P15254). Encoded protein function: FUNCTION: Phosphoribosylformylglycinamidine synthase involved in the purines biosynthetic pathway. Catalyzes the ATP-dependent conversion of formylglycinamide ribonucleotide (FGAR) and glutamine to yield formylglycinamidine ribonucleotide (FGAM) and glutamate. {ECO:0000255|HAMAP-Rule:MF_00419, ECO:0000269|PubMed:2659070}. EcoCyc product frame: FGAMSYN-MONOMER. EcoCyc synonyms: purI. Genomic coordinates: 2691656-2695543. EcoCyc protein note: PurL catalyzes the fourth step in the E. coli purine de novo biosynthesis pathway. It converts 5'-phosphoribosyl-N-formylglycineamide (FGAR) to 5-phosphoribosyl-N-formylglycineamidine (FGAM) in the presence of glutamine and ATP. It is the second glutamine amidotransferase in the pathway, the other being PurF. PurL is a large, 141 kDa polypeptide that was shown by genetic complementation tests to contain three different domains. The N-terminal Domain I contains a potential ATP binding motif, the C-terminal Domain III is similar to several glutamine amidotransferases, and Domain II contains elements observed in the triosephosphate isomerase family. Thus, PurL may have arisen from the fusion of at least three different gene families . The enzyme mechanism was studied using initial velocity, dead-end inhibition, and substrate/product exchange studies...

## Biological Role

Repressed by [2Fe-2S] cluster DNA-binding transcriptional dual regulator (complex.ecocyc.CPLX0-7639), purR (protein.P0ACP7). Activated by rpoD (protein.P00579).

## Enriched Pathways

- `eco00230` Purine metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01110` Biosynthesis of secondary metabolites (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P15254|protein.P15254]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (3)

- `activates` <-- [[protein.P00579|protein.P00579]] `RegulonDB` `S` - sigma=sigma70; target=purL; function=+
- `represses` <-- [[complex.ecocyc.CPLX0-7639|complex.ecocyc.CPLX0-7639]] `EcoCyc` `database` - EcoCyc regulation TYPES=Transcription-Factor-Binding
- `represses` <-- [[protein.P0ACP7|protein.P0ACP7]] `RegulonDB` `S` - regulator=PurR; target=purL; function=-

## External IDs

- `Dbxref:ASAP:ABE-0008412,ECOCYC:EG10797,GeneID:947032`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:2691656-2695543:-; feature_type=gene
