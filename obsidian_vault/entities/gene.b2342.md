---
entity_id: "gene.b2342"
entity_type: "gene"
name: "fadI"
source_database: "NCBI RefSeq"
source_id: "gene-b2342"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b2342"
  - "fadI"
---

# fadI

`gene.b2342`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b2342`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

fadI (gene.b2342) is a gene entity. It encodes fadI (protein.P76503). Encoded protein function: FUNCTION: Catalyzes the final step of fatty acid oxidation in which acetyl-CoA is released and the CoA ester of a fatty acid two carbons shorter is formed. Strongly involved in the anaerobic degradation of long and medium-chain fatty acids in the presence of nitrate and weakly involved in the aerobic degradation of long-chain fatty acids. {ECO:0000269|PubMed:12270828, ECO:0000269|PubMed:12535077}. EcoCyc product frame: G7213-MONOMER. EcoCyc synonyms: yfcY. Genomic coordinates: 2459159-2460469. EcoCyc protein note: During anaerobic β-oxidation of fatty acids, G7213 FadI, G7212 FadJ, and EG12357 FadK serve functions parallel to those of EG10278 FadA, EG10279 FadB, and EG11530 FadD in the aerobic pathway . FadI and FadJ also exhibit partial functional redundancy with FadA and FadB under aerobic conditions; the two complexes are proposed to increase efficiency of β-oxidation by favoring substrates of different chain length . A strain producing FadI and FadJ from a plasmid exhibits thiolase activity with β-ketoacyl-CoAs of 6 to 12 carbon units, but not with acetoacetyl-CoA . It has been shown that the β-oxidation enzymes can be induced to work in the reverse direction, a phenomenon that is being utilized for metabolic engineering...

## Biological Role

Repressed by DNA-binding transcriptional dual regulator CpxR-phosphorylated (complex.ecocyc.CPLX0-7748), fadR (protein.P0A8V6), arcA (protein.P0A9Q1), lrp (protein.P0ACJ0). Activated by lrp (protein.P0ACJ0).

## Enriched Pathways

- `eco00071` Fatty acid degradation (KEGG)
- `eco00280` Valine, leucine and isoleucine degradation (KEGG)
- `eco00362` Benzoate degradation (KEGG)
- `eco00592` alpha-Linolenic acid metabolism (KEGG)
- `eco00907` Pinene, camphor and geraniol degradation (KEGG)
- `eco00984` Steroid degradation (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01110` Biosynthesis of secondary metabolites (KEGG)
- `eco01120` Microbial metabolism in diverse environments (KEGG)
- `eco01212` Fatty acid metabolism (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P76503|protein.P76503]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (5)

- `activates` <-- [[protein.P0ACJ0|protein.P0ACJ0]] `EcoCyc` `database` - EcoCyc regulation TYPES=Transcription-Factor-Binding
- `represses` <-- [[complex.ecocyc.CPLX0-7748|complex.ecocyc.CPLX0-7748]] `EcoCyc` `database` - EcoCyc regulation TYPES=Transcription-Factor-Binding
- `represses` <-- [[protein.P0A8V6|protein.P0A8V6]] `RegulonDB` `S` - regulator=FadR; target=fadI; function=-
- `represses` <-- [[protein.P0A9Q1|protein.P0A9Q1]] `RegulonDB` `S` - regulator=ArcA; target=fadI; function=-
- `represses` <-- [[protein.P0ACJ0|protein.P0ACJ0]] `EcoCyc` `database` - EcoCyc regulation TYPES=Transcription-Factor-Binding

## External IDs

- `Dbxref:ASAP:ABE-0007725,ECOCYC:G7213,GeneID:948823`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:2459159-2460469:-; feature_type=gene
