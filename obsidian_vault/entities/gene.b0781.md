---
entity_id: "gene.b0781"
entity_type: "gene"
name: "moaA"
source_database: "NCBI RefSeq"
source_id: "gene-b0781"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b0781"
  - "moaA"
---

# moaA

`gene.b0781`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b0781`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

moaA (gene.b0781) is a gene entity. It encodes moaA (protein.P30745). Encoded protein function: FUNCTION: Catalyzes, together with MoaC, the conversion of 5'-GTP to cyclic pyranopterin monophosphate (cPMP or molybdopterin precursor Z).; FUNCTION: Catalyzes the cyclization of GTP to (8S)-3',8-cyclo-7,8-dihydroguanosine 5'-triphosphate. {ECO:0000255|HAMAP-Rule:MF_01225}. EcoCyc product frame: EG11595-MONOMER. EcoCyc synonyms: bisA, chlA, chlA1, narA. Genomic coordinates: 817044-818033. EcoCyc protein note: MoaA, a member of the radical SAM superfamily of enzymes , participates in the PWY-6823 pathway. Biochemical characterization of the enzyme and its reaction mechanism have been performed with the Staphylococcus aureus enzyme, which was shown to catalyze a complex rearrangement reaction that involves the insertion of the C8 carbon of the purine moiety of GTP into the C2'-C3' bond of its ribose moiety . Under anaerobic conditions, the A-type Fe-S cluster carrier proteins CPLX0-7617 and CPLX0-7908 are involved in insertion of [4Fe-4S] clusters into MoaA . Using an E. coli strain overproducing MoaA and EG11666-MONOMER MoaC, PRECURSOR-Z (precursor Z) was produced, purified, and chemically characterized . In earlier work, expression of genes moaABC in a EG10153 mutant resulted in the production of "compound Z", an oxidized product of precursor Z...

## Biological Role

Repressed by [2Fe-2S] cluster DNA-binding transcriptional dual regulator (complex.ecocyc.CPLX0-7639), fur (protein.P0A9A9). Activated by fnr (protein.P0A9E5), modE (protein.P0A9G8), csrA (protein.P69913).

## Enriched Pathways

- `eco00790` Folate biosynthesis (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01240` Biosynthesis of cofactors (KEGG)
- `eco04122` Sulfur relay system (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P30745|protein.P30745]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (5)

- `activates` <-- [[protein.P0A9E5|protein.P0A9E5]] `RegulonDB` `S` - regulator=FNR; target=moaA; function=+
- `activates` <-- [[protein.P0A9G8|protein.P0A9G8]] `RegulonDB` `S` - regulator=ModE; target=moaA; function=+
- `activates` <-- [[protein.P69913|protein.P69913]] `RegulonDB` `C` - regulator=CsrA; target=moaA; function=+
- `represses` <-- [[complex.ecocyc.CPLX0-7639|complex.ecocyc.CPLX0-7639]] `EcoCyc` `database` - EcoCyc regulation TYPES=Transcription-Factor-Binding
- `represses` <-- [[protein.P0A9A9|protein.P0A9A9]] `RegulonDB` `S` - regulator=Fur; target=moaA; function=-

## External IDs

- `Dbxref:ASAP:ABE-0002669,ECOCYC:EG11595,GeneID:945392`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:817044-818033:+; feature_type=gene
